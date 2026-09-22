"""Extra Paper 2-style questions across the Section 1 topics: statements to test, necessary and
sufficient conditions, counterexamples and 'must be true' reasoning about calculus, algebra, graphs."""
from gen.model import Q, ROMAN3

NS = ["P is necessary and sufficient for Q.", "P is necessary but not sufficient for Q.", "P is sufficient but not necessary for Q.", "P is neither necessary nor sufficient for Q."]

QUESTIONS = [
    Q("X2-01", "quadratics", "MM1.3", r"""$p$ and $q$ are real numbers. Which of the following statements is/are true?

I. If $p^2 < 4q$ then $x^2 + px + q > 0$ for all real $x$.
II. If $x^2 + px + q > 0$ for all real $x$ then $q > 0$.
III. If $q < 0$ then $x^2 + px + q = 0$ has two real roots of opposite sign.""", ROMAN3, "H",
      r"I: negative discriminant and positive leading coefficient. II: put $x = 0$. III: the product of the roots is $q < 0$ (and the discriminant $p^2 - 4q > 0$), so the roots are real with opposite signs.", paper=2, tags=("roman",), diff=2),

    Q("X2-02", "differentiation", "MM6.3", r"Let $f$ be a polynomial. $P$: '$f'(x) > 0$ for all real $x$'. $Q$: '$f(x) = 0$ has exactly one real root'. Which one of the following is true?", NS, "C",
      r"If $f' > 0$ everywhere, $f$ is strictly increasing and (being an odd-degree polynomial) crosses the axis exactly once: $P$ is sufficient. But $f(x) = x^3$ has exactly one root and $f'(0) = 0$, so $P$ is not necessary.", paper=2, tags=("fixed",), diff=2),

    Q("X2-03", "integration", "MM7.1", r"""$f$ is a function defined for all real $x$ and $\displaystyle\int_{0}^{4} f(x)\,dx = 0$. Which of the following statements must be true?

I. $f(x) = 0$ for some $x$ with $0 \leq x \leq 4$.
II. The area between the curve and the $x$-axis from $0$ to $4$ is $0$.
III. $\displaystyle\int_{0}^{2} f(x)\,dx = -\int_{2}^{4} f(x)\,dx$""", ROMAN3, "D",
      r"III is just the rule for combining integrals over adjacent ranges. I fails for a function that jumps from $-1$ to $1$ without passing through $0$ (nothing says $f$ is continuous). II fails: $f(x) = x - 2$ has integral $0$ but area $4$.", paper=2, tags=("roman",), diff=3),

    Q("X2-04", "sequences-series", "MM2.3", r"A geometric series has first term $a \neq 0$ and common ratio $r$. $P$: '$-1 < r < 1$'. $Q$: 'the series has a sum to infinity'. Which one of the following is true?", NS, "A",
      r"A geometric series converges if and only if $|r| < 1$, which is exactly $-1 < r < 1$.", paper=2, tags=("fixed",), diff=1),

    Q("X2-05", "straight-lines", "MM3.1", r"""Two distinct lines have equations $y = m_1 x + c_1$ and $y = m_2 x + c_2$. Which of the following statements is/are true?

I. If $m_1 m_2 = -1$ then the lines meet at exactly one point.
II. If $m_1 = m_2$ then the lines do not meet.
III. If the lines meet on the $y$-axis then $c_1 = c_2$.""", ROMAN3, "H",
      r"I: perpendicular lines are not parallel, so they meet once. II: equal gradients and distinct lines means parallel and different, so no intersection. III: on the $y$-axis $x = 0$, so $y = c_1 = c_2$.", paper=2, tags=("roman",), diff=1),

    Q("X2-06", "exp-logs", "MM5.2", r"Which of the following is a counterexample to the claim **'for all positive $x$ and $y$, $\log_{10}(x + y) \leq \log_{10} x + \log_{10} y$'**?",
      [r"$x = y = 1$", r"$x = y = 2$", r"$x = 10$, $y = 100$", r"$x = 4$, $y = 4$", r"$x = 5$, $y = 5$"], "A",
      r"$x = y = 1$: $\log 2 > 0 = \log 1 + \log 1$, so the inequality fails. For the others $x + y \leq xy$ and the claim holds ($\log$ is increasing).", paper=2, diff=2),

    Q("X2-07", "trig-functions", "MM4.6", r"""Consider the equation $\sin x = k$ where $k$ is a real constant. Which of the following statements is/are true?

I. For every $k$ with $-1 < k < 1$ the equation has exactly two solutions in $0 \leq x < 2\pi$.
II. For $k = 1$ the equation has exactly one solution in $0 \leq x < 2\pi$.
III. For every real $k$ the equation has at least one solution.""", ROMAN3, "E",
      r"I and II are read from the graph of $\sin$ over one period. III is false: $\sin x = 2$ has no solutions.", paper=2, tags=("roman",), diff=1),

    Q("X2-08", "polynomials", "MM1.6", r"$p(x)$ is a polynomial. $P$: '$p(2) = 0$'. $Q$: '$(x - 2)^2$ is a factor of $p(x)$'. Which one of the following is true?", NS, "B",
      r"If $(x-2)^2$ divides $p$ then certainly $p(2) = 0$, so $P$ is necessary for $Q$. But $p(x) = x - 2$ has $p(2) = 0$ without a repeated factor, so $P$ is not sufficient.", paper=2, tags=("fixed",), diff=1),

    Q("X2-09", "graphs", "MM8.7", r"""The graphs of $y = f(x)$ and $y = g(x)$ meet at exactly three points. Which of the following statements must be true?

I. The equation $f(x) = g(x)$ has exactly three real solutions.
II. The graph of $y = f(x) - g(x)$ crosses the $x$-axis exactly three times.
III. $f(x) - g(x)$ is a polynomial of degree at least $3$.""", ROMAN3, "B",
      r"I is the definition of an intersection. II fails because the difference could touch the axis rather than cross it at one of the points. III fails because $f$ and $g$ need not be polynomials at all (e.g. $\sin x$ and a line).", paper=2, tags=("roman",), diff=2),

    Q("X2-10", "circles", "MM3.2", r"The circle $C$ has centre $(a, b)$ and radius $r$. $P$: '$r > |b|$'. $Q$: '$C$ crosses the $x$-axis at two distinct points'. Which one of the following is true?", NS, "A",
      r"The distance from the centre to the $x$-axis is $|b|$; the circle cuts the axis twice exactly when this is less than $r$.", paper=2, tags=("fixed",), diff=1),

    Q("X2-11", "functions", "MM8.2", r"""Let $f(x) = x^2$ for all real $x$, and let $g$ be the function whose graph is obtained by translating the graph of $y = f(x)$ by $2$ units in the positive $x$-direction and then reflecting in the $y$-axis. Which of the following statements is/are true?

I. $g(x) = (x + 2)^2$
II. $g(x) = (x - 2)^2$
III. The graph of $g$ has its vertex at $(-2, 0)$""", ROMAN3, "F",
      r"Translation gives $(x - 2)^2$; reflecting in the $y$-axis replaces $x$ by $-x$: $(-x - 2)^2 = (x + 2)^2$, with vertex at $(-2, 0)$.", paper=2, tags=("roman",), diff=2),

    Q("X2-12", "indices-surds", "MM1.1", r"""$a$ and $b$ are positive real numbers. Which of the following statements is/are true?

I. If $a^2 = b^2$ then $a = b$.
II. If $2^a = 2^b$ then $a = b$.
III. If $a^b = 1$ then $a = 1$.""", ROMAN3, "H",
      r"I holds because $a, b > 0$ rules out $a = -b$. II holds because $2^x$ is one-to-one. III: for positive $a$ and $b$, $a^b = 1$ gives $b\log a = 0$, so $\log a = 0$ and $a = 1$. All three are true.", paper=2, tags=("roman",), diff=2),

    Q("X2-13", "binomial", "MM2.4", r"""$n$ is a positive integer. Which of the following statements is/are true?

I. The coefficient of $x^n$ in $(1 + x)^{2n}$ is $\binom{2n}{n}$.
II. The sum of the coefficients in the expansion of $(1 - x)^n$ is $0$.
III. $(1 + x)^n \geq 1 + nx$ for all $x \geq 0$.""", ROMAN3, "H",
      r"I is the general term with $r = n$. II: put $x = 1$. III: expanding $(1 + x)^n$ gives $1 + nx$ plus non-negative terms when $x \geq 0$.", paper=2, tags=("roman",), diff=2),

    Q("X2-14", "simultaneous-inequalities", "MM1.5", r"$x$ is a real number. $P$: '$x^2 < 4$'. $Q$: '$x < 2$'. Which one of the following is true?", NS, "C",
      r"$x^2 < 4$ means $-2 < x < 2$, which implies $x < 2$ (sufficient); but $x = -5$ satisfies $Q$ and not $P$ (not necessary).", paper=2, tags=("fixed",), diff=1),

    Q("X2-15", "trig-triangles", "MM4.1", r"In triangle $ABC$, $P$: '$a^2 = b^2 + c^2$'. $Q$: 'angle $A = 90^\circ$'. Which one of the following is true?", NS, "A",
      r"Pythagoras and its converse: the cosine rule gives $\cos A = \frac{b^2 + c^2 - a^2}{2bc}$, which is $0$ exactly when $a^2 = b^2 + c^2$.", paper=2, tags=("fixed",), diff=1),

    Q("X2-16", "differentiation", "MM6.3", r"""The function $f$ has $f'(x) = (x - 1)(x - 3)^2$. Which of the following statements is/are true?

I. $f$ has a local minimum at $x = 1$.
II. $f$ has a local maximum at $x = 3$.
III. $f$ is increasing for all $x > 1$.""", ROMAN3, "F",
      r"$f'$ changes from negative to positive at $x = 1$ (minimum). At $x = 3$ the squared factor keeps $f' \geq 0$ on both sides, so no turning point: II is false, and $f' \geq 0$ for $x > 1$ (zero only at $3$) makes III true.", paper=2, tags=("roman",), diff=2),

    Q("X2-17", "integration", "MM7.5", r"The trapezium rule with $n$ strips is used to estimate $\displaystyle\int_{0}^{1} \sqrt{x}\,dx$. Which of the following is true for every $n$?",
      [r"The estimate is an underestimate.", r"The estimate is an overestimate.", r"The estimate is exact.", r"The estimate is an underestimate only when $n$ is even.", r"It cannot be decided without calculating."], "A",
      r"$y = \sqrt x$ is concave (bends downwards), so every chord lies below the curve and the trapezia underestimate the area.", paper=2, diff=1),

    Q("X2-18", "number", "M2.3", r"""$n$ is a positive integer greater than $1$. Which of the following statements is/are true?

I. If $n$ is not prime, then $n$ has a prime factor at most $\sqrt n$.
II. If $n$ has no prime factor at most $\sqrt n$, then $n$ is prime.
III. If $n$ is prime, then $n$ has no factor between $1$ and $n$ exclusive.""", ROMAN3, "H",
      r"If $n = ab$ with $1 < a \leq b$ then $a \leq \sqrt n$ and $a$ has a prime factor $\leq \sqrt n$ (I). II is the contrapositive of I. III is the definition of prime.", paper=2, tags=("roman",), diff=2),

    Q("X2-19", "probability", "M7.7", r"Events $A$ and $B$ have $P(A) > 0$ and $P(B) > 0$. $P$: '$A$ and $B$ are mutually exclusive'. $Q$: '$A$ and $B$ are not independent'. Which one of the following is true?", NS, "C",
      r"Mutually exclusive gives $P(A \text{ and } B) = 0 \neq P(A)P(B)$, so they cannot be independent: $P$ is sufficient. But two overlapping events can also fail to be independent, so $P$ is not necessary.", paper=2, tags=("fixed",), diff=2),

    Q("X2-20", "geometry", "M5.3", r"$ABCD$ is a quadrilateral. $P$: 'the diagonals of $ABCD$ bisect each other'. $Q$: '$ABCD$ is a rectangle'. Which one of the following is true?", NS, "B",
      r"Every rectangle is a parallelogram, and a parallelogram's diagonals bisect each other: $P$ is necessary. A non-rectangular parallelogram has bisecting diagonals without being a rectangle: not sufficient.", paper=2, tags=("fixed",), diff=1),

    Q("X2-21", "graphs", "MM8.6", r"""$p(x)$ is a polynomial of degree $4$ with real coefficients. Which of the following statements must be true?

I. $p(x) = 0$ has at least one real root.
II. $p(x) = 0$ has at most four real roots.
III. The graph of $y = p(x)$ has at least one turning point.""", ROMAN3, "G",
      r"I fails: $x^4 + 1$ has no real roots. II: a degree-4 polynomial has at most 4 roots. III: an even-degree polynomial tends to the same infinity at both ends, so it must turn at least once.", paper=2, tags=("roman",), diff=2),

    Q("X2-22", "exp-logs", "MM5.3", r"Consider the statement: **for all real $x$, $2^{x} > x^2$.** Which of the following is a counterexample?",
      [r"$x = 3$", r"$x = 1$", r"$x = 5$", r"$x = 0$", r"$x = 10$"], "A",
      r"$2^3 = 8 < 9 = 3^2$, so $x = 3$ breaks the claim. The other options satisfy it: $2 > 1$, $32 > 25$, $1 > 0$, $1024 > 100$.", paper=2, diff=2),

    Q("X2-23", "sequences-series", "MM2.2", r"""An arithmetic sequence has first term $a$ and common difference $d$, both non-zero. Which of the following statements is/are true?

I. If $d > 0$ then every term after some point is positive.
II. The sum of the first $n$ terms is a quadratic function of $n$.
III. If $a$ and $d$ are integers then $S_n$ is an integer for every $n$.""", ROMAN3, "H",
      r"I: terms $a + (n-1)d$ eventually exceed any bound. II: $S_n = \frac n2(2a + (n-1)d)$ is quadratic in $n$. III: $S_n$ is a sum of integers.", paper=2, tags=("roman",), diff=1),

    Q("X2-24", "logic", "Arg2", r"For a real number $x$, $P$: '$x > 0$'. $Q$: '$x^3 > 0$'. Which one of the following is true?", NS, "A",
      r"Cubing preserves sign, so $x > 0 \Leftrightarrow x^3 > 0$.", paper=2, tags=("fixed",), diff=1),

    Q("X2-25", "errors", "Err2", r"""A student solves $x^2 - 5x + 6 > 0$ as follows.

I. $x^2 - 5x + 6 = (x - 2)(x - 3)$.
II. So $(x - 2)(x - 3) > 0$.
III. So $x - 2 > 0$ and $x - 3 > 0$.
IV. So $x > 3$.

Which of the following is correct?""",
      ["The first error is on line III: a product is positive when both factors are positive **or** both are negative, so $x < 2$ is missed.", "The solution is completely correct.", "The first error is on line I.", "The first error is on line IV: it should be $x > 2$.", "The first error is on line II."], "A",
      r"The full solution set is $x < 2$ or $x > 3$.", paper=2, tags=("fixed",), diff=1),

    Q("X2-26", "reasoning", "Prf5", r"""The positive integers $a$, $b$ and $c$ satisfy $a < b < c$ and $a + b + c = 12$. Which of the following statements must be true?

I. $a \leq 3$
II. $c \geq 5$
III. $b = 4$""", ROMAN3, "E",
      r"Since $a < b < c$, $3a < 12$ so $a \leq 3$ (I); $3c > 12$ so $c \geq 5$ (II). III fails: $1 + 2 + 9 = 12$ has $b = 2$.", paper=2, tags=("roman",), diff=2),

    Q("X2-27", "proof", "Prf1", r"Consider the claim: **if $n$ is a positive integer then $n^2 + n + 1$ is odd.** Which of the following is a valid proof?",
      [r"$n^2 + n = n(n + 1)$ is even, being the product of consecutive integers, so $n^2 + n + 1$ is even plus one, which is odd.", r"For $n = 1, 2, 3$ the values are $3, 7, 13$, all odd, so the claim holds.", r"$n^2 + n + 1$ cannot be factorised, so it is odd.", r"If $n$ is odd then $n^2$ is odd and $n$ is odd, so $n^2 + n + 1$ is odd.", r"Suppose $n^2 + n + 1$ is even. Then $n$ is even, which is a contradiction."], "A",
      r"A is a direct general argument. B only checks cases; C is irrelevant; D is correct for odd $n$ but says nothing about even $n$; E does not reach a contradiction.", paper=2, diff=1),

    Q("X2-28", "statistics", "M6.3", r"""A set of five distinct positive integers has median $10$ and mean $10$. Which of the following statements must be true?

I. The largest value is at least $12$.
II. The smallest value is at most $8$.
III. The range is at least $4$.""", ROMAN3, "H",
      r"The two values above the median are distinct integers greater than $10$, so at least $11$ and $12$ (I); similarly the two below are at most $9$ and $8$ (II); hence the range is at least $12 - 8 = 4$ (III).", paper=2, tags=("roman",), diff=2),

    Q("X2-29", "mensuration", "M5.16", r"$P$: 'a solid cylinder and a solid cube have equal volumes'. $Q$: 'the cylinder and the cube have equal surface areas'. Which one of the following is true?", NS, "D",
      r"Equal volumes say nothing about surface areas (a long thin cylinder has a large surface area), and equal surface areas say nothing about volumes. Neither implies the other.", paper=2, tags=("fixed",), diff=1),

    Q("X2-30", "quadratics", "MM1.3", r"The equation $x^2 + bx + c = 0$ has real coefficients. Which of the following is a **sufficient** condition for it to have two distinct real roots?",
      [r"$c < 0$", r"$b \neq 0$", r"$b^2 \geq 4c$", r"$c > 0$", r"$b > 0$"], "A",
      r"$c < 0$ makes the discriminant $b^2 - 4c$ positive. $b^2 \geq 4c$ allows equality (a repeated root); the others do not control the discriminant.", paper=2, diff=1),
]

