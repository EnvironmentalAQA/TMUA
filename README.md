# TMUA practice site

A self-contained revision site for the **Test of Mathematics for University Admission (TMUA)**:
an original multiple-choice question bank written to the UAT-UK Content Specification, generated
mock papers in the real format (HTML and PDF), every official past paper with online marking against
the real answer keys and grade conversions, revision notes for all 26 topics, a full teaching solution
for every one of the 489 questions, and practice modes.

**Open the site:** `site/index.html` (double-click) or serve `site/` with any static server.
Maths is rendered by KaTeX from a CDN, so an internet connection is needed for the formulas.

## Layout

```
build.py                rebuilds everything into site/ (site/ is output - never edit it by hand)
tools_check.py          normalises and validates the question bank; run after editing bank/*.py
bank/topics.py          the topic tree (26 slugs in three groups) taken from the specification
bank/p1_*.py            Section 1 Part 1 questions (AS pure): indices, quadratics, ... graphs
bank/p2_*.py            Section 1 Part 2 questions (Higher GCSE): number, ratio, algebra, geometry, ...
bank/s2_*.py            Section 2 questions (Paper 2 only): logic, proof, reasoning, errors in proofs
bank/x_paper2_mixed.py  Paper 2-style questions on the Section 1 topics
bank/sol_*.py           full teaching solutions, keyed by question id (one file per topic)
bank/notes_*.py         revision notes per topic
bank/facts.py           formula / fact flashcards
bank/official_keys.py   answer keys and score conversions for every published paper
bank/official_index.py  topic of every question in every published paper
gen/model.py            Q, Sol and Fact data classes + markup rules
gen/mathtex.py          markup -> HTML (KaTeX) and -> PDF (matplotlib mathtext images)
gen/papers.py           assembles 20-question mock papers
gen/pdf.py              TMUA-format PDFs (reportlab)
gen/site.py, gen/pages.py   static HTML generator
official-papers/        the official PDFs (TMUA-<series>-P1/P2/KEY.pdf) and the specification
site/                   OUTPUT
```

## Rebuild

```bash
python tools_check.py          # validate the bank (unique ids, answers in range, maths renders)
python build.py                # full build: HTML + all PDFs (about 5 minutes the first time)
python build.py --no-pdf       # HTML only (seconds)
python build.py --papers 20    # more mock papers per paper (default 12)
```

Requirements: Python 3.12 with `reportlab`, `matplotlib`, `pymupdf`, `numpy`, `pillow`
(`python -m pip install reportlab matplotlib pymupdf numpy pillow`). Rendered maths images are cached in
`build-cache/` (ignored by git).

## Adding questions

Add a `Q(...)` to the `QUESTIONS` list in the relevant `bank/*.py` (any module exporting `QUESTIONS` is
picked up automatically):

```python
Q("IND-23", "indices-surds", "MM1.1",
  r"Solve $4^{x+1} = 8^{2x-3}$.",                       # question text (LaTeX in $...$)
  [r"$x = \dfrac{5}{4}$", r"$x = \dfrac{11}{4}$", ...],  # 4-8 options, in order A, B, C ...
  "B",                                                   # correct letter
  r"Write both sides as powers of 2: ...",               # worked solution
  paper=1, diff=1)                                       # paper style (1/2), difficulty 1-3
```

Markup rules (see `gen/model.py`): `$...$` inline maths, `$$...$$` display maths, blank line between
paragraphs, lines `I. ...`, `II. ...` for statement lists (use `ROMAN3` as the options and
`tags=("roman",)`), `- ` bullets, `**bold**`. Use the LaTeX subset that both KaTeX and matplotlib
mathtext accept: `\frac`, `\dfrac`, `\sqrt[n]{}`, `\left( \right)`, `\sum`, `\int`, `\binom`, `\leq`,
`\geq`, `\neq`, `\Rightarrow`, `\Leftrightarrow`, `\log_{a}`, trig functions, `^\circ`, `\text{}`,
`\mathbf{}`, `\overrightarrow{}`. Avoid `\le`, `\ge`, `\implies`, `\displaystyle`, `\tfrac`, `\textbf`,
`\big`, matrices and `\cancel` (they are stripped or rejected for the PDFs). Write column vectors
as `\binom{a}{b}`.

Options are shuffled deterministically at build time so correct answers are spread over A-H; add
`tags=("fixed",)` to keep the authored order (e.g. "the first error is on line I/II/III").

`build.py` refuses to build if an id is duplicated, an answer letter is out of range, options repeat,
or a maths snippet does not parse.

## Adding a full solution

The `solution=` argument above is the short working shown when a question is marked. The **solution
bank** is separate: a `Sol` per question id in the matching `bank/sol_*.py`, holding the teaching
version - what the question tests, the reason for every step, the wrong turns and the principle.

```python
"IND-23": Sol(
    idea=r"...what is really being tested and how to recognise the type...",
    steps=[
        (r"what you do", r"why you do it"),      # one pair per step, in order
        ...
    ],
    pitfalls=[r"...the mistake, and the value it leads to..."],
    takeaway=r"one sentence worth remembering"),
```

Refer to **values** in `pitfalls`, never to option letters: options are shuffled at build time, so
"an offered option" is safe but "option C" is not. `build.py` prints how many questions have a full
solution and names any that do not; `tools_check.py` checks every `Sol` parses and has non-empty steps.

## Site features (all state lives in the browser's localStorage)

- **Questions by topic** (`topic/<slug>.html`): instant marking with worked solutions; a correct first
  attempt marks the question *secure*, a wrong one *needs work*; filter bar (keyword, paper style,
  difficulty, question type, status); print with or without solutions; PDF sets of 12 questions with
  separate solution booklets; the real past questions on the topic, newest first.
- **Mock papers** (`papers.html`, `paper/*.html`): 20 questions, 75-minute countdown that survives
  reloads, answer grid, submit for score, grade estimate (published conversion table), time used and
  a topic breakdown; PDFs in the format of the real paper (cover page, one question per page).
- **Official papers** (`official.html`, `real/<series>-P<n>.html`): the PDF alongside an answer grid and
  timer; marked against the real key with the official grade conversion and a topic breakdown linking to
  notes and practice.
- **Solution bank** (`solutions.html`, `solutions/<slug>.html`): every question with its answer, the
  quick working and the full method - the idea behind the question, each step paired with the reason
  for it, the pitfalls and what they would give you, and the takeaway. Printable, and included in the
  topic solution PDFs.
- **Real questions by topic** (`pastq.html`): all 360 published questions indexed by topic.
- **Revision notes** (`notes/<slug>.html`): summary, sections by spec reference, must-know formulas,
  classic traps, a worked example and the real questions on the topic.
- **Quick-fire** (`quickfire.html`): random questions filtered by paper / group / topic / difficulty,
  keyboard answers, per-question stopwatch, sprint mode (`?sprint=10`), needs-work weighting and
  spaced repetition (secure questions return after 1, 3, 7, 14, 30 days; `?due=1`).
- **Formula recall** (`facts.html`): flashcards with spaced repetition (no formula booklet in the test).
- **Skill drills** (`drills.html`): 24 generators with fresh numbers - indices, surds, quadratics, logs,
  series, binomial, calculus, exact trig values, percentages, HCF/LCM, converse/contrapositive, negation.
- **Planner** (`planner.html`): test-date countdown, accuracy by topic (weakest first), score history,
  suggested next steps. **Grades** (`grades.html`): every published conversion table and a calculator.
  **Exam technique** (`technique.html`). **Search** (`search.html`). Dark mode and print styles.

## Publishing on GitHub Pages

`.github/workflows/pages.yml` deploys the prebuilt `site/` folder on every push to `main`.
Workflow: edit `bank/*.py` -> `python tools_check.py` -> `python build.py` -> commit -> push.
In the repository settings choose *Pages -> Source: GitHub Actions* the first time.

The official papers are copyright Cambridge University Press & Assessment / UAT-UK and are included
for personal revision; the questions, notes and mock papers on this site are original.
