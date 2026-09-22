"""Data classes for the question bank.

A question's text, options and solution use a small markup:
  $...$          inline maths (LaTeX subset that both KaTeX and matplotlib mathtext accept:
                 \\frac \\dfrac \\sqrt[n]{} \\left( \\right) \\sum \\int \\binom \\leq \\geq \\neq \\pm \\times
                 \\Rightarrow \\Leftrightarrow \\log_{a} \\sin ^\\circ \\mathrm{} \\text{} \\ldots \\infty \\pi \\theta)
  $$...$$        display maths on its own line
  blank line     paragraph break
  I. / II. / III.  a line starting with a roman numeral and a dot is one numbered statement
  - text         a bullet point
  **bold**       bold
Avoid \\le \\ge \\implies \\displaystyle \\tfrac \\textbf \\big and matrices (mathtext cannot draw them);
write column vectors as \\binom{a}{b}.
"""
from dataclasses import dataclass, field

LETTERS = "ABCDEFGH"

# The standard option list for "which of the following statements is/are true" questions.
ROMAN3 = ["none of them", "I only", "II only", "III only", "I and II only", "I and III only", "II and III only", "I, II and III"]
ROMAN2 = ["neither of them", "I only", "II only", "both I and II"]


@dataclass
class Q:
    id: str                 # unique, e.g. "IND-03"
    topic: str              # slug from bank/topics.py
    spec: str               # spec reference(s), e.g. "MM1.1"
    text: str               # the question (markup above)
    options: list           # 4 to 8 option strings, in order A, B, C ...
    answer: str             # correct letter
    solution: str           # worked solution (markup above)
    paper: int = 1          # 1 = Paper 1 style, 2 = Paper 2 style (reasoning / Section 2)
    diff: int = 2           # 1 = quick, 2 = standard, 3 = hard
    fig: str = None         # figure key in gen/figures.py
    tags: tuple = ()        # e.g. ("roman", "counterexample", "proof-error")
    check: object = None    # optional zero-argument callable returning the expected letter (sympy verification)
    full: object = None     # Sol: the full teaching solution, attached at build time from bank/sol_*.py

    @property
    def n(self):
        return len(self.options)

    @property
    def letters(self):
        return LETTERS[: self.n]


@dataclass
class Sol:
    """A full teaching solution for one question: not just the working, but what the question is
    testing, the reason for every step, the wrong turns and the principle to carry forward.

    idea      1-2 sentences: what is really being tested and how to recognise the type.
    steps     list of (what you do, why you do it) pairs, in order.
    pitfalls  list of strings: the mistakes that are easy to make here and the answers they lead to.
    takeaway  one sentence: the general principle worth remembering.
    Same markup as questions ($...$ for maths).
    """
    idea: str
    steps: list
    pitfalls: list = field(default_factory=list)
    takeaway: str = ""


@dataclass
class Fact:
    """A fact / formula flashcard for the recall drill."""
    topic: str
    prompt: str
    answer: str
    spec: str = ""
