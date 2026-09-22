"""The logic of arguments (Arg1-Arg4): if/then, converse, contrapositive, necessary and sufficient,
quantifiers and negation. All Paper 2."""
from gen.model import Q, ROMAN3

T = "logic"
NS = ["P is necessary and sufficient for Q.", "P is necessary but not sufficient for Q.", "P is sufficient but not necessary for Q.", "P is neither necessary nor sufficient for Q."]
TF = ["The statement is true and its converse is true.", "The statement is true and its converse is false.", "The statement is false and its converse is true.", "The statement is false and its converse is false."]

QUESTIONS = [
    Q("LGC-01", T, "Arg1", r"Consider the statement: **if $n$ is a multiple of $6$, then $n$ is a multiple of $3$.** Which of the following is its contrapositive?",
      [r"If $n$ is not a multiple of $3$, then $n$ is not a multiple of $6$.", r"If $n$ is a multiple of $3$, then $n$ is a multiple of $6$.", r"If $n$ is not a multiple of $6$, then $n$ is not a multiple of $3$.", r"$n$ is a multiple of $6$ if and only if $n$ is a multiple of $3$.", r"If $n$ is a multiple of $3$, then $n$ is not a multiple of $6$."], "A",
      r"The contrapositive of 'if $A$ then $B$' is 'if not $B$ then not $A$'. It is logically equivalent to the original; B is the converse and C is the inverse.", diff=1, tags=("fixed",)),

    Q("LGC-02", T, "Arg2", r"Let $P$ be the statement '$x > 2$' and $Q$ the statement '$x^2 > 4$', where $x$ is a real number. Which one of the following is true?", NS, "C",
      r"$x > 2 \Rightarrow x^2 > 4$, so $P$ is sufficient for $Q$. But $x = -3$ gives $x^2 > 4$ without $x > 2$, so $P$ is not necessary.", diff=1, tags=("fixed",)),

    Q("LGC-03", T, "Arg4", r"Which of the following is the negation of the statement **'every student in the class scored more than $50$'**?",
      [r"At least one student in the class scored $50$ or less.", r"Every student in the class scored $50$ or less.", r"No student in the class scored more than $50$.", r"At least one student in the class scored more than $50$.", r"Every student in the class scored less than $50$."], "A",
      r"The negation of 'for all $x$, $P(x)$' is 'there exists $x$ such that not $P(x)$'. 'Not more than $50$' means '$50$ or less'.", diff=1),

    Q("LGC-04", T, "Arg1", r"Consider the statement about a real number $x$: **if $x^2 = x$, then $x = 1$.** Which one of the following is true?", TF, "C",
      r"$x = 0$ satisfies $x^2 = x$ but not $x = 1$, so the statement is false. The converse, 'if $x = 1$ then $x^2 = x$', is true.", diff=1, tags=("fixed",)),

    Q("LGC-05", T, "Arg3", r"""Which of the following statements is/are true?

I. For every real number $x$, there exists a real number $y$ such that $y > x$.
II. There exists a real number $y$ such that for every real number $x$, $y > x$.
III. For every real number $x$, there exists a real number $y$ such that $xy = 1$.""", ROMAN3, "B",
      r"I is true (take $y = x + 1$). II claims a single largest real number exists: false. III fails for $x = 0$.", tags=("roman",), diff=2),

    Q("LGC-06", T, "Arg1", r"A teacher says: **'You will pass only if you revise.'** Which of the following statements means the same thing?",
      [r"If you pass, then you revised.", r"If you revise, then you will pass.", r"You will pass if you revise.", r"If you do not pass, then you did not revise.", r"You will pass if and only if you revise."], "A",
      r"'$A$ only if $B$' means '$A \Rightarrow B$': passing implies revising. It does not promise that revising guarantees a pass.", diff=2, tags=("fixed",)),

    Q("LGC-07", T, "Arg2", r"Let $P$: 'the quadrilateral $ABCD$ is a square' and $Q$: 'the quadrilateral $ABCD$ has four equal sides'. Which one of the following is true?", NS, "C",
      r"A square has four equal sides ($P \Rightarrow Q$, sufficient), but a rhombus that is not a square shows $Q$ does not imply $P$ (not necessary).", diff=1, tags=("fixed",)),

    Q("LGC-08", T, "Arg4", r"Which of the following is the negation of **'there exists a positive integer $n$ such that $n^2 + n + 41$ is not prime'**?",
      [r"For every positive integer $n$, $n^2 + n + 41$ is prime.", r"There exists a positive integer $n$ such that $n^2 + n + 41$ is prime.", r"For every positive integer $n$, $n^2 + n + 41$ is not prime.", r"There is no positive integer $n$ for which $n^2 + n + 41$ is prime.", r"For some positive integer $n$, $n^2 + n + 41$ is prime."], "A",
      r"Negating 'there exists $n$ with not $P(n)$' gives 'for all $n$, $P(n)$'.", diff=1),

    Q("LGC-09", T, "Arg1", r"""Consider the statement $S$: **for all real $x$, if $x > 0$ then $x + \dfrac{1}{x} \geq 2$.** Which of the following statements is/are true?

I. $S$ is true.
II. The converse of $S$ (for all real $x$, if $x + \frac1x \geq 2$ then $x > 0$) is true.
III. The contrapositive of $S$ is true.""", ROMAN3, "H",
      r"For $x > 0$, $x + \frac1x - 2 = \frac{(x-1)^2}{x} \geq 0$, so $S$ is true, and so is its contrapositive (III). For the converse: if $x < 0$ then $x + \frac1x < 0 < 2$, so $x + \frac1x \geq 2$ forces $x > 0$ (II true).", tags=("roman",), diff=3),

    Q("LGC-10", T, "Arg2", r"For real numbers $a$ and $b$, let $P$: '$a = b$' and $Q$: '$a^2 = b^2$'. Which one of the following is true?", NS, "C",
      r"$a = b \Rightarrow a^2 = b^2$ (sufficient), but $a = 1$, $b = -1$ gives $a^2 = b^2$ without $a = b$ (not necessary).", diff=1, tags=("fixed",)),

    Q("LGC-11", T, "Arg1", r"""The statement **'if a triangle is equilateral then it is isosceles'** is true. Which of the following must therefore also be true?

I. If a triangle is isosceles then it is equilateral.
II. If a triangle is not isosceles then it is not equilateral.
III. If a triangle is not equilateral then it is not isosceles.""", ROMAN3, "C",
      r"Only the contrapositive (II) is logically equivalent to the original. I is the converse and III is the inverse; both are in fact false here.", tags=("roman",), diff=1),

    Q("LGC-12", T, "Arg3", r"Consider the statement: **there exists a real number $k$ such that for all real $x$, $x^2 + kx + 1 > 0$.** Which of the following is true?",
      [r"The statement is true; for example $k = 0$ works.", r"The statement is false because $x^2 + kx + 1$ can be negative for large $x$.", r"The statement is true; every value of $k$ works.", r"The statement is false because for every $k$ there is an $x$ with $x^2 + kx + 1 \leq 0$.", r"The statement is true; for example $k = 2$ works."], "A",
      r"Need discriminant $k^2 - 4 < 0$, i.e. $-2 < k < 2$. So some (not all) values of $k$ work; $k = 0$ gives $x^2 + 1 > 0$. ($k = 2$ gives $(x+1)^2$, which is $0$ at $x = -1$.)", diff=2),

    Q("LGC-13", T, "Arg4", r"Which of the following is the negation of **'$x > 3$ and $y \leq 5$'**?",
      [r"$x \leq 3$ or $y > 5$", r"$x \leq 3$ and $y > 5$", r"$x < 3$ or $y \geq 5$", r"$x < 3$ and $y > 5$", r"$x \leq 3$ or $y \geq 5$"], "A",
      r"Not ($A$ and $B$) is (not $A$) or (not $B$). Not $x > 3$ is $x \leq 3$; not $y \leq 5$ is $y > 5$.", diff=1),

    Q("LGC-14", T, "Arg1", r"For a positive integer $n$, consider the statement: **if $n$ is prime, then $n$ is odd.** Which one of the following is true?", TF, "D",
      r"$n = 2$ is an even prime, so the statement is false. The converse, 'if $n$ is odd then $n$ is prime', fails for $n = 9$.", diff=1, tags=("fixed",)),

    Q("LGC-15", T, "Arg2", r"Let $P$: 'the integer $n$ is divisible by $4$' and $Q$: 'the integer $n^2$ is divisible by $8$'. Which one of the following is true?", NS, "A",
      r"If $4 \mid n$ then $16 \mid n^2$, so $8 \mid n^2$: $P$ is sufficient. Conversely, if $8 \mid n^2$ then $n$ is even, say $n = 2m$, and $8 \mid 4m^2$ forces $m$ to be even, so $4 \mid n$: $P$ is also necessary. (Tempting wrong answer: 'sufficient but not necessary' - but no counterexample exists.)", diff=3, tags=("fixed",)),

    Q("LGC-16", T, "Arg3", r"""Which of the following statements is/are true about real numbers?

I. For all $x$ and all $y$, if $x < y$ then $x^2 < y^2$.
II. For all $x$ there exists $y$ such that $x < y$ and $x^2 < y^2$.
III. There exist $x$ and $y$ with $x < y$ and $x^2 > y^2$.""", ROMAN3, "G",
      r"I fails for $x = -2$, $y = 1$. II: take $y = |x| + 1$. III: $x = -2$, $y = 1$ works.", tags=("roman",), diff=2),

    Q("LGC-17", T, "Arg1", r"Let $x$ be a real number. Which of the following statements is equivalent to **'$x \geq 2$ if and only if $x^3 \geq 8$'**?",
      [r"($x \geq 2 \Rightarrow x^3 \geq 8$) and ($x^3 \geq 8 \Rightarrow x \geq 2$)", r"$x \geq 2 \Rightarrow x^3 \geq 8$", r"$x^3 \geq 8 \Rightarrow x \geq 2$", r"($x < 2 \Rightarrow x^3 \geq 8$) or ($x^3 < 8 \Rightarrow x \geq 2$)", r"$x \geq 2$ or $x^3 \geq 8$"], "A",
      r"'If and only if' is the conjunction of the implication and its converse.", diff=1),

    Q("LGC-18", T, "Arg4", r"A statement reads: **for every positive integer $n$, there is a prime $p$ with $n < p < 2n$.** Which of the following is its negation?",
      [r"There is a positive integer $n$ such that no prime $p$ satisfies $n < p < 2n$.", r"For every positive integer $n$, no prime $p$ satisfies $n < p < 2n$.", r"There is a positive integer $n$ and a prime $p$ with $p \leq n$ or $p \geq 2n$.", r"For every positive integer $n$, there is a prime $p$ with $p \leq n$ or $p \geq 2n$.", r"There is a prime $p$ such that for every positive integer $n$, $n < p < 2n$ fails."], "A",
      r"Negate the quantifiers in turn: 'for every $n$, there exists $p$ with ...' becomes 'there exists $n$ such that for every prime $p$, not ...', i.e. no prime lies strictly between $n$ and $2n$.", diff=2),

    Q("LGC-19", T, "Arg2", r"Let $f$ be a function defined for all real numbers. $P$: '$f'(a) = 0$'; $Q$: '$f$ has a stationary point at $x = a$'. Which one of the following is true?", NS, "A",
      r"A stationary point is by definition a point where the derivative is zero, so $P$ and $Q$ are equivalent.", diff=1, tags=("fixed",)),

    Q("LGC-20", T, "Arg1", r"""Which of the following statements is/are logically equivalent to **'if it is raining, then the ground is wet'**?

I. It is not raining, or the ground is wet.
II. If the ground is not wet, then it is not raining.
III. If the ground is wet, then it is raining.""", ROMAN3, "E",
      r"'$A \Rightarrow B$' is equivalent to 'not $A$, or $B$' (I) and to its contrapositive (II). III is the converse, which is not equivalent.", tags=("roman",), diff=2),

    Q("LGC-21", T, "Arg3", r"Consider the statement $S$: **for all real $x$, $x^2 - 6x + 10 > 0$.** Which of the following is true?",
      [r"$S$ is true, because $x^2 - 6x + 10 = (x - 3)^2 + 1$.", r"$S$ is false, because $x = 3$ gives $x^2 - 6x + 10 = 0$.", r"$S$ is false, because a quadratic can be negative.", r"$S$ is true, because $x^2 - 6x + 10$ has two real roots.", r"$S$ cannot be decided without knowing $x$."], "A",
      r"Completing the square shows the expression is at least $1$ for every $x$.", diff=1),

    Q("LGC-22", T, "Arg2", r"For real numbers $a, b$: $P$: '$ab = 0$'; $Q$: '$a = 0$'. Which one of the following is true?", NS, "B",
      r"$a = 0 \Rightarrow ab = 0$, so $P$ is necessary for $Q$. But $ab = 0$ could be because $b = 0$ with $a \neq 0$, so $P$ is not sufficient.", diff=1, tags=("fixed",)),

    Q("LGC-23", T, "Arg1", r"Consider the statement: **if $a$ and $b$ are irrational, then $a + b$ is irrational.** Which of the following pairs is a counterexample?",
      [r"$a = \sqrt2$, $b = -\sqrt2$", r"$a = \sqrt2$, $b = \sqrt3$", r"$a = 1$, $b = -1$", r"$a = \sqrt2$, $b = 2\sqrt2$", r"$a = \pi$, $b = \sqrt2$"], "A",
      r"A counterexample needs the hypothesis true (both irrational) and the conclusion false ($a + b$ rational): $\sqrt2 + (-\sqrt2) = 0$.", diff=1),

    Q("LGC-24", T, "Arg4", r"Let $S$ be the statement: **every even number greater than $2$ can be written as the sum of two primes.** A single counterexample to $S$ would be",
      [r"an even number greater than $2$ that is not the sum of any two primes", r"an even number that is the sum of two primes", r"an odd number that is not the sum of two primes", r"two primes whose sum is odd", r"an even number greater than $2$ that can be written as the sum of two primes in two different ways"], "A",
      r"To refute 'for all $n$, $P(n)$' you exhibit one $n$ with $P(n)$ false.", diff=1),
]
