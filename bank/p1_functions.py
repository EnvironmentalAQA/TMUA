"""Functions and transformations (MM1.7, MM8.2, MM8.3, MM8.4)."""
from gen.model import Q, ROMAN3

T = "functions"

QUESTIONS = [
    Q("FUN-01", T, "MM8.2", r"The graph of $y = x^2$ is translated by $3$ units in the positive $x$-direction and then stretched parallel to the $y$-axis with scale factor $2$. What is the equation of the resulting graph?",
      [r"$y = 2(x-3)^2$", r"$y = 2(x+3)^2$", r"$y = (2x-3)^2$", r"$y = 2x^2 - 3$", r"$y = (x-3)^2 + 2$", r"$y = \frac12 (x-3)^2$"], "A",
      r"Translation: $y = (x-3)^2$. Stretch by factor $2$ in the $y$-direction: $y = 2(x-3)^2$.", diff=1),

    Q("FUN-02", T, "MM8.2", r"$f(x) = x^2 - 4x$. The graph of $y = f(x + 2)$ has its minimum point at",
      [r"$(0, -4)$", r"$(4, -4)$", r"$(2, -4)$", r"$(0, 0)$", r"$(-2, -4)$", r"$(2, 0)$"], "A",
      r"$f(x) = (x-2)^2 - 4$ has minimum at $(2, -4)$. Replacing $x$ by $x + 2$ translates the graph $2$ units to the left: $(0, -4)$.", diff=1),

    Q("FUN-03", T, "MM8.2", r"Let $f(x) = 2x + 1$ and $g(x) = x^2 - 3$. Find $f(g(2)) - g(f(2))$.",
      ["$-19$", "$19$", "$-17$", "$3$", "$-3$", "$25$"], "A",
      r"$g(2) = 1$, $f(1) = 3$. $f(2) = 5$, $g(5) = 22$. So $3 - 22 = -19$.", diff=1),

    Q("FUN-04", T, "MM1.7", r"Which of the following functions, each with domain the set of all real numbers, is one-to-one?",
      [r"$f(x) = x^3 - x$", r"$f(x) = x^3 + x$", r"$f(x) = |x|$", r"$f(x) = x^2 + 2x$", r"$f(x) = \cos x$"], "B",
      r"$x^3 + x$ is strictly increasing (its derivative $3x^2 + 1 > 0$), so different inputs give different outputs. $x^3 - x$ takes the value $0$ at $x = -1, 0, 1$; the others are even or periodic.", diff=2),

    Q("FUN-05", T, "MM8.2", r"The graph of $y = f(x)$ passes through $(4, 6)$. Which point must lie on the graph of $y = 3f(2x) - 1$?",
      [r"$(2, 17)$", r"$(8, 17)$", r"$(2, 18)$", r"$(8, 18)$", r"$(2, 11)$", r"$(4, 17)$"], "A",
      r"$f(2x)$ halves $x$-coordinates: $(2, 6)$. Then $3f - 1$: $y = 18 - 1 = 17$. Point $(2, 17)$.", diff=1),

    Q("FUN-06", T, "MM8.2", r"The curve $y = x^2 - 6x + 5$ is reflected in the $y$-axis. Find the equation of the reflected curve.",
      [r"$y = x^2 + 6x + 5$", r"$y = -x^2 + 6x - 5$", r"$y = x^2 - 6x - 5$", r"$y = -x^2 - 6x + 5$", r"$y = x^2 + 6x - 5$"], "A",
      r"Reflecting in the $y$-axis replaces $x$ with $-x$: $y = x^2 + 6x + 5$.", diff=1),

    Q("FUN-07", T, "MM8.2", r"The function $f$ satisfies $f(x) = x^2$ for all $x$. Which of the following transformations maps $y = f(x)$ onto $y = 4x^2 - 8x + 4$?",
      [r"a translation of $1$ unit in the positive $x$-direction followed by a stretch parallel to the $y$-axis with factor $4$",
       r"a translation of $1$ unit in the negative $x$-direction followed by a stretch parallel to the $y$-axis with factor $4$",
       r"a stretch parallel to the $x$-axis with factor $2$ followed by a translation of $2$ units in the positive $x$-direction",
       r"a translation of $2$ units in the positive $x$-direction followed by a stretch parallel to the $y$-axis with factor $2$",
       r"a stretch parallel to the $y$-axis with factor $4$ followed by a translation of $4$ units in the positive $y$-direction"], "A",
      r"$4x^2 - 8x + 4 = 4(x-1)^2$, i.e. $y = 4f(x - 1)$: translate $1$ right, then stretch vertically by $4$. (Equivalently $y = f(2x - 2) = f(2(x-1))$: stretch parallel to the $x$-axis by factor $\frac12$ then translate 1 right - not offered.)", diff=2),

    Q("FUN-08", T, "MM1.7", r"For which values of $x$ is $\sqrt{x^2} = -x$?",
      [r"$x \leq 0$", r"$x \geq 0$", r"$x = 0$ only", r"all real $x$", r"no real $x$", r"$x < 0$ only"], "A",
      r"$\sqrt{x^2} = |x|$, and $|x| = -x$ exactly when $x \leq 0$.", diff=1),

    Q("FUN-09", T, "MM8.2", r"The graph of $y = \sin x$ is transformed to $y = 2\sin(3x) + 1$. What is the maximum value of the new function, and what is its period (in degrees)?",
      [r"maximum $3$, period $120^\circ$", r"maximum $3$, period $1080^\circ$", r"maximum $2$, period $120^\circ$", r"maximum $3$, period $360^\circ$", r"maximum $1$, period $120^\circ$", r"maximum $2$, period $180^\circ$"], "A",
      r"$\sin(3x)$ has period $360^\circ/3 = 120^\circ$. $2\sin(3x)$ ranges from $-2$ to $2$, so $2\sin(3x) + 1$ has maximum $3$.", diff=1),

    Q("FUN-10", T, "MM8.2", r"""$f(x) = x^2 + 1$. Which of the following statements is/are true?

I. $f(f(x)) = x^4 + 2x^2 + 2$ for all $x$
II. $f(x + 1) = f(x) + 1$ for all $x$
III. $f(2x) = 4f(x) - 3$ for all $x$""", ROMAN3, "F",
      r"I: $f(f(x)) = (x^2+1)^2 + 1 = x^4 + 2x^2 + 2$: true. II: $f(x+1) = x^2 + 2x + 2 \neq x^2 + 2$: false. III: $f(2x) = 4x^2 + 1$ and $4f(x) - 3 = 4x^2 + 1$: true.", paper=2, tags=("roman",)),

    Q("FUN-11", T, "MM8.2", r"The graph of $y = f(x)$ is transformed by the sequence: reflect in the $x$-axis, then translate $2$ units in the positive $y$-direction, then reflect in the $y$-axis. The resulting graph has equation",
      [r"$y = 2 - f(-x)$", r"$y = -f(-x) - 2$", r"$y = f(-x) - 2$", r"$y = -f(x - 2)$", r"$y = 2 - f(x)$", r"$y = -f(-x + 2)$"], "A",
      r"Reflect in $x$-axis: $y = -f(x)$. Translate up $2$: $y = -f(x) + 2$. Reflect in $y$-axis (replace $x$ by $-x$): $y = 2 - f(-x)$.", diff=1),

    Q("FUN-12", T, "MM1.7", r"""Let $f(x) = \sqrt{x - 3}$ for $x \geq 3$ and $g(x) = x^2 + 3$. Which of the following statements is/are true?

I. $g(f(x)) = x$ for all $x \geq 3$
II. $f(g(x)) = x$ for all real $x$
III. $f(g(x)) = |x|$ for all real $x$""", ROMAN3, "F",
      r"I: $g(f(x)) = (\sqrt{x-3})^2 + 3 = x$ for $x \geq 3$: true. $f(g(x)) = \sqrt{x^2} = |x|$, so II fails (e.g. $x = -1$) and III is true.", paper=2, tags=("roman",)),

    Q("FUN-13", T, "MM8.4", r"The graph of $y = a(x + b)^2 + c$ has vertex $(-2, 5)$ and passes through $(0, -3)$. Find $a$.",
      ["$-2$", "$2$", "$-1$", "$1$", r"$-\dfrac12$", "$-4$"], "A",
      r"$b = 2$, $c = 5$. At $x = 0$: $4a + 5 = -3$, so $a = -2$.", diff=1),

    Q("FUN-14", T, "MM8.2", r"The graph of $y = f(x)$ has a maximum point at $(3, 8)$. The graph of $y = f(x - a) + b$ has its maximum at $(1, 2)$. Find $a + b$.",
      ["$-8$", "$8$", "$-4$", "$4$", "$0$", "$-2$"], "A",
      r"The maximum moves from $(3, 8)$ to $(3 + a, 8 + b) = (1, 2)$, so $a = -2$, $b = -6$ and $a + b = -8$.", diff=1),

    Q("FUN-15", T, "MM8.2", r"Which of the following is the equation of the graph obtained by stretching $y = x^3 - 3x$ parallel to the $x$-axis with scale factor $\dfrac{1}{2}$?",
      [r"$y = 8x^3 - 6x$", r"$y = \dfrac{x^3}{8} - \dfrac{3x}{2}$", r"$y = 2x^3 - 6x$", r"$y = \dfrac{1}{2}x^3 - \dfrac{3}{2}x$", r"$y = 8x^3 - 3x$"], "A",
      r"A stretch parallel to the $x$-axis with factor $\frac12$ gives $y = f(2x) = (2x)^3 - 3(2x) = 8x^3 - 6x$.", diff=1),

    Q("FUN-16", T, "MM1.7", r"The function $f$ is defined by $f(x) = |x - 2| + |x + 2|$ for all real $x$. What is the minimum value of $f(x)$, and for how many values of $x$ is it attained?",
      [r"minimum $4$, attained for infinitely many $x$", r"minimum $4$, attained for exactly one $x$", r"minimum $0$, attained for exactly two $x$", r"minimum $2$, attained for exactly one $x$", r"minimum $4$, attained for exactly two $x$"], "A",
      r"For $-2 \leq x \leq 2$: $f(x) = (2 - x) + (x + 2) = 4$. Outside this interval $f(x) > 4$. So the minimum $4$ is attained on the whole interval $[-2, 2]$.", diff=2),

    Q("FUN-17", T, "MM8.3", r"The line $y = mx + c$ passes through $(2, 7)$. If $m$ is increased by $1$ and $c$ is decreased by $2$, the new line passes through $(2, k)$. Find $k$.",
      ["$7$", "$8$", "$6$", "$9$", "$5$", "$10$"], "A",
      r"New value at $x = 2$: $(m+1)\cdot 2 + (c - 2) = 2m + c = 7$. So $k = 7$.", diff=1),
]
