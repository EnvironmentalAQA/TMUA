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

    @property
    def n(self):
        return len(self.options)

    @property
    def letters(self):
        return LETTERS[: self.n]


@dataclass
class Fact:
    """A fact / formula flashcard for the recall drill."""
    topic: str
    prompt: str
    answer: str
    spec: str = ""
