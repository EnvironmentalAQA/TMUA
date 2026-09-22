"""Dev helper: normalise multi-line r"..." strings to r\"\"\"...\"\"\" in bank/*.py, then import every
bank module and run the sanity checks (unique ids, answer letter in range, 4-8 options, no duplicate
options, maths parses in mathtext, optional `check` callables agree with the stated answer)."""
import glob, importlib, os, re, sys, traceback

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

for p in glob.glob(os.path.join(ROOT, "bank", "*.py")):
    s = open(p, encoding="utf-8").read()
    n = re.sub(r'(?<![A-Za-z0-9_])r"([^"\n]*\n[^"]*)"', lambda m: 'r"""' + m.group(1) + '"""', s)
    # plain "..." literals containing a backslash -> raw strings (avoids invalid-escape warnings)
    n = re.sub(r'(?<![rRbf"\w])"([^"\n\\]*\\[^"\n]*)"', lambda m: 'r"' + m.group(1) + '"', n)
    if n != s:
        open(p, "w", encoding="utf-8").write(n)
        print("normalised", os.path.basename(p))

from gen import mathtex
from bank.topics import ALL_SLUGS

only = sys.argv[1:]
seen = {}
errs = 0
total = 0
for p in sorted(glob.glob(os.path.join(ROOT, "bank", "*.py"))):
    name = os.path.basename(p)[:-3]
    if name in ("__init__", "topics") or name.startswith("notes_") or name.startswith("official") or name in ("facts",):
        continue
    if only and name not in only:
        continue
    try:
        mod = importlib.import_module("bank." + name)
    except Exception:
        print("IMPORT ERROR", name)
        traceback.print_exc()
        errs += 1
        continue
    qs = getattr(mod, "QUESTIONS", [])
    total += len(qs)
    for q in qs:
        problems = []
        if q.id in seen:
            problems.append(f"duplicate id (also in {seen[q.id]})")
        seen[q.id] = name
        if q.topic not in ALL_SLUGS:
            problems.append(f"unknown topic {q.topic}")
        if not (4 <= len(q.options) <= 8):
            problems.append(f"{len(q.options)} options")
        if q.answer not in "ABCDEFGH"[: len(q.options)]:
            problems.append(f"answer {q.answer} out of range")
        if len(set(q.options)) != len(q.options):
            problems.append("duplicate options")
        for field in (q.text, q.solution, *q.options):
            try:
                mathtex.check_math(field)
            except Exception as e:
                problems.append(f"maths error in {field[:50]!r}: {str(e).splitlines()[-1][:90]}")
        if q.check is not None:
            try:
                got = q.check()
                if got != q.answer:
                    problems.append(f"check() gives {got}, stated {q.answer}")
            except Exception as e:
                problems.append(f"check() raised {e!r}")
        if "Hmm" in q.solution or "Answer " in q.solution or "re-read" in q.solution.lower():
            problems.append("solution contains working-out chatter")
        if problems:
            errs += 1
            print(f"{q.id}: " + "; ".join(problems))
    print(f"{name}: {len(qs)} questions")
print(f"{total} questions, {errs} problems")
