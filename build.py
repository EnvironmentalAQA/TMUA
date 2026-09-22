"""Build the whole site: validates the bank, shuffles options deterministically, writes topic pages,
notes, mock papers (HTML + PDF), official-paper pages and the practice pages into site/.

Usage:  python build.py               (defaults: 12 mock papers per paper, PDFs on)
        python build.py --papers 20
        python build.py --no-pdf      (HTML only, fast)
"""
import argparse, importlib, os, pkgutil, random, re, shutil, sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bank
from bank.topics import ALL_SLUGS, GROUPS, topic_index
from bank.official_keys import KEYS, GRADES, SERIES
from bank.official_index import OFFICIAL_INDEX
from gen import site, pages, papers as paper_gen, mathtex
from gen.model import ROMAN3

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
SET_SIZE = 12   # questions per topic-set PDF
KEEP_LAST = re.compile(r"^(none|no |no\b|all real|all values|infinitely|it cannot|neither|there (is|are) no|the (situation|statement)|nothing)", re.I)


def load_bank():
    questions, notes, facts = [], {}, []
    for m in pkgutil.iter_modules(bank.__path__):
        mod = importlib.import_module(f"bank.{m.name}")
        questions += getattr(mod, "QUESTIONS", [])
        notes.update(getattr(mod, "NOTES", {}))
        facts += getattr(mod, "FACTS", [])
    return questions, notes, facts


def validate(questions):
    ids = Counter(q.id for q in questions)
    errs = []
    for q in questions:
        if ids[q.id] > 1:
            errs.append(f"duplicate id {q.id}")
        if q.topic not in ALL_SLUGS:
            errs.append(f"{q.id}: unknown topic '{q.topic}'")
        if not 4 <= len(q.options) <= 8:
            errs.append(f"{q.id}: {len(q.options)} options")
        if q.answer not in q.letters:
            errs.append(f"{q.id}: answer {q.answer} not in A-{q.letters[-1]}")
        if len(set(q.options)) != len(q.options):
            errs.append(f"{q.id}: duplicate options")
        if q.paper not in (1, 2) or q.diff not in (1, 2, 3):
            errs.append(f"{q.id}: bad paper/diff")
        for field in (q.text, q.solution, *q.options):
            try:
                mathtex.check_math(field)
            except Exception as e:
                errs.append(f"{q.id}: maths does not render: {str(e).splitlines()[-1][:80]}")
    for sid in KEYS:
        for p in (1, 2):
            if len(KEYS[sid][p]) != 20 or not set(KEYS[sid][p]) <= set("ABCDEFGH"):
                errs.append(f"key {sid} P{p} malformed")
    for sid, g in GRADES.items():
        if len(g["p1"]) != 21 or len(g["p2"]) != 21 or len(g["overall"]) != 41:
            errs.append(f"grade table {sid} wrong length")
    for sid, ps in OFFICIAL_INDEX.items():
        for p, qs in ps.items():
            for n, (slug, desc) in qs.items():
                if slug not in ALL_SLUGS:
                    errs.append(f"official index {sid} P{p} Q{n}: unknown topic {slug}")
            if sorted(qs) != list(range(1, 21)):
                errs.append(f"official index {sid} P{p}: questions {sorted(qs)}")
    if errs:
        print("VALIDATION ERRORS:")
        for e in errs:
            print("  -", e)
        sys.exit(1)


def shuffle_options(q):
    """Deterministic per-question shuffle so correct letters are spread over A-H. Roman-numeral
    and 'fixed' questions keep their order; options like 'none of these' stay at the end."""
    if "roman" in q.tags or "fixed" in q.tags or q.options == ROMAN3:
        return
    rng = random.Random("shuffle-" + q.id)
    pairs = list(zip(q.letters, q.options))
    head = [p for p in pairs if not KEEP_LAST.match(p[1])]
    tail = [p for p in pairs if KEEP_LAST.match(p[1])]
    rng.shuffle(head)
    new = head + tail
    correct = q.options[q.letters.index(q.answer)]
    q.options = [o for _, o in new]
    q.answer = q.letters[q.options.index(correct)]


def official_files():
    out = []
    src = os.path.join(ROOT, "official-papers")
    for name in sorted(os.listdir(src)):
        m = re.match(r"TMUA-([A-Za-z0-9]+)-(P1|P2|KEY)\.pdf$", name)
        if m:
            out.append({"name": name, "series": m.group(1), "kind": m.group(2)})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--papers", type=int, default=12, help="mock papers per paper")
    ap.add_argument("--no-pdf", action="store_true")
    args = ap.parse_args()

    questions, notes, facts = load_bank()
    validate(questions)
    for q in questions:
        shuffle_options(q)
    idx = topic_index()
    print(f"Bank: {len(questions)} questions, {len(notes)} notes, {len(facts)} facts")
    print("Answer letters:", dict(sorted(Counter(q.answer for q in questions).items())))
    site.NOTES_ALL.update(notes)
    site.FACTS[:] = facts
    missing = [s for s in idx if s not in notes]
    if missing:
        print("  ! no notes for:", ", ".join(missing))

    for d in ("pdf/topic", "pdf/papers", "topic", "notes", "paper", "official", "real"):
        os.makedirs(os.path.join(SITE, d), exist_ok=True)

    by_topic = {}
    for q in questions:
        by_topic.setdefault(q.topic, []).append(q)
    for slug in by_topic:
        by_topic[slug].sort(key=lambda q: (q.diff, q.id))
    real = site.real_by_topic()
    real_counts = site.official_counts()

    # ---- topic pages + topic-set PDFs ----
    sets_by_topic = {}
    for slug in ALL_SLUGS:
        qs = by_topic.get(slug, [])
        sets = [qs[i:i + SET_SIZE] for i in range(0, len(qs), SET_SIZE)]
        sets_by_topic[slug] = sets
        info = idx[slug]
        for k, s in enumerate(sets, 1):
            base = os.path.join(SITE, "pdf", "topic", f"{slug}-set{k}")
            if not args.no_pdf:
                from gen import pdf
                pdf.build_topic_set(base + "-QP.pdf", f"{info['name']} - Set {k}", f"TMUA practice questions by topic. Specification {info['spec']}. {len(s)} questions.", s)
                pdf.build_solutions(base + "-SOL.pdf", f"{info['name']} - Set {k} - Solutions", f"Specification {info['spec']}.", s)
        with open(os.path.join(SITE, "topic", f"{slug}.html"), "w", encoding="utf-8") as f:
            f.write(site.topic_page(slug, qs, sets, real.get(slug, [])))
        if slug in notes:
            with open(os.path.join(SITE, "notes", f"{slug}.html"), "w", encoding="utf-8") as f:
                f.write(site.notes_page(slug, notes[slug], qs, real.get(slug, [])))
        print(f"  {slug}: {len(qs)} questions, {real_counts.get(slug, 0)} real")

    # ---- mock papers ----
    generated = []
    used = Counter()
    for pno in (1, 2):
        for n in range(1, args.papers + 1):
            qs = paper_gen.assemble(pno, n, questions, used)
            fname = f"P{pno}-Set{n:02d}"
            g = {"paper": pno, "set": n, "questions": qs, "file": fname}
            generated.append(g)
            if len(qs) < 20:
                print(f"  ! {fname}: only {len(qs)} questions")
            if not args.no_pdf:
                from gen import pdf
                base = os.path.join(SITE, "pdf", "papers", fname)
                pdf.build_question_paper(base + "-QP.pdf", pno, f"Set {n:02d}", qs)
                pdf.build_solutions(base + "-SOL.pdf", f"Paper {pno} - Set {n:02d} - Solutions", "Generated practice paper: answer key and worked solutions.", qs)
            with open(os.path.join(SITE, "paper", fname + ".html"), "w", encoding="utf-8") as f:
                f.write(site.paper_online_page(g))
        print(f"  Paper {pno}: {args.papers} mock papers")

    # ---- official papers ----
    files = official_files()
    for fl in files:
        shutil.copy2(os.path.join(ROOT, "official-papers", fl["name"]), os.path.join(SITE, "official", fl["name"]))
    shutil.copy2(os.path.join(ROOT, "official-papers", "TMUA-Specification.pdf"), os.path.join(SITE, "official", "TMUA-Specification.pdf"))
    site.OFFICIAL_FILES[:] = files
    for sid in KEYS:
        for pno in (1, 2):
            with open(os.path.join(SITE, "real", f"{sid}-P{pno}.html"), "w", encoding="utf-8") as f:
                f.write(site.real_paper_page(sid, pno))

    counts = {"questions": len(questions), "topics": len(ALL_SLUGS), "papers": len(generated), "official": sum(1 for f in files if f["kind"] != "KEY"),
              "facts": len(facts), "real": real_counts}
    out = {
        "index.html": site.index_page(by_topic, counts, generated),
        "topics.html": site.topics_page(by_topic, counts),
        "notes.html": site.notes_index_page(by_topic),
        "papers.html": site.papers_page(generated),
        "official.html": site.official_page(files),
        "pastq.html": site.pastq_page(),
        "practice.html": site.practice_page(counts),
        "quickfire.html": pages.quickfire_page(),
        "search.html": pages.search_page(),
        "facts.html": pages.facts_page(facts),
        "drills.html": pages.drills_page(),
        "planner.html": pages.planner_page(by_topic, real_counts),
        "technique.html": pages.technique_page(),
        "grades.html": pages.grades_page(),
        "qdata.js": site.qdata_js(questions),
    }
    for name, content in out.items():
        with open(os.path.join(SITE, name), "w", encoding="utf-8") as f:
            f.write(content)
    with open(os.path.join(SITE, ".nojekyll"), "w") as f:
        f.write("")
    print(f"Done -> {os.path.join(SITE, 'index.html')}")


if __name__ == "__main__":
    main()
