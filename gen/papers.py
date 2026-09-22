"""Assemble 20-question mock papers in the TMUA pattern.

Paper 1 (Applications): questions from Section 1 topics only, mostly the AS-level Part 1 topics with a
few Part 2 (GCSE) ones, at most two per topic, ordered roughly easy -> hard like the real papers.
Paper 2 (Reasoning): 2-3 quick Section 1 questions to open, then a mix of Section 2 questions
(logic / proof / reasoning / errors) and Section 1 questions written in the Paper 2 style
(statement I/II/III, necessary/sufficient, counterexamples), again at most two per topic.

Questions rotate across sets so every set is different and the whole bank gets used.
"""
import random
from collections import Counter
from bank.topics import GROUPS

PART1 = [t["slug"] for g in GROUPS if g["slug"] == "part1" for t in g["topics"]]
PART2 = [t["slug"] for g in GROUPS if g["slug"] == "part2" for t in g["topics"]]
SEC2 = [t["slug"] for g in GROUPS if g["slug"] == "section2" for t in g["topics"]]

N = 20


def _pick(pool, k, used, rng, max_per_topic=2, taken=None):
    """Pick k questions from pool, preferring least-used, at most max_per_topic per topic."""
    taken = taken if taken is not None else []
    per_topic = Counter(q.topic for q in taken)
    ids = {q.id for q in taken}
    cands = [q for q in pool if q.id not in ids]
    rng.shuffle(cands)
    cands.sort(key=lambda q: used[q.id])          # stable: random within equal usage
    out = []
    for q in cands:
        if len(out) >= k:
            break
        if per_topic[q.topic] >= max_per_topic:
            continue
        out.append(q)
        per_topic[q.topic] += 1
        ids.add(q.id)
    return out


def assemble(pno, n, questions, used):
    rng = random.Random(f"tmua-{pno}-{n}")
    if pno == 1:
        p1 = [q for q in questions if q.topic in PART1 and q.paper == 1]
        p2 = [q for q in questions if q.topic in PART2 and q.paper == 1]
        chosen = _pick(p1, 16, used, rng)
        chosen += _pick(p2, N - len(chosen), used, rng, taken=chosen)
        if len(chosen) < N:
            chosen += _pick(p1 + p2, N - len(chosen), used, rng, max_per_topic=3, taken=chosen)
    else:
        opener = [q for q in questions if q.topic in PART1 and q.paper == 1 and q.diff == 1]
        sec2 = [q for q in questions if q.topic in SEC2]
        style2 = [q for q in questions if q.topic not in SEC2 and q.paper == 2]
        chosen = _pick(opener, 3, used, rng, max_per_topic=1)
        chosen += _pick(sec2, 10, used, rng, max_per_topic=3, taken=chosen)
        chosen += _pick(style2, N - len(chosen), used, rng, taken=chosen)
        if len(chosen) < N:
            pool = [q for q in questions if q.topic in PART1 + PART2]
            chosen += _pick(pool, N - len(chosen), used, rng, max_per_topic=3, taken=chosen)
    for q in chosen:
        used[q.id] += 1
    # order: openers first for paper 2, otherwise by difficulty with a little shuffle inside bands
    if pno == 2:
        head, tail = chosen[:3], chosen[3:]
        tail.sort(key=lambda q: (q.diff, rng.random()))
        chosen = head + tail
    else:
        chosen.sort(key=lambda q: (q.diff, rng.random()))
    return chosen[:N]
