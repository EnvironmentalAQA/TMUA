"""Polynomials, factor and remainder theorems (MM1.6)."""
from gen.model import Q, ROMAN3

T = "polynomials"

QUESTIONS = [
    Q("POL-01", T, "MM1.6", r"When $x^3 - 4x^2 + kx + 6$ is divided by $(x - 3)$ the remainder is $-6$. Find $k$.",
      ["$-1$", "$1$", "$-3$", "$3$", "$-5$", "$5$"], "A",
      r"Remainder Theorem: $27 - 36 + 3k + 6 = -6 \Rightarrow 3k - 3 = -6 \Rightarrow k = -1$.", diff=1),

    Q("POL-02", T, "MM1.6", r"$(x + 2)$ is a factor of $2x^3 + ax^2 - 5x - 6$. Find the value of $a$.",
      ["$3$", "$-3$", "$2$", "$-2$", "$5$", "$1$"], "A",
      r"Factor Theorem: $f(-2) = -16 + 4a + 10 - 6 = 4a - 12 = 0$, so $a = 3$.", diff=1),

    Q("POL-03", T, "MM1.6", r"Fully factorise $x^3 - 7x + 6$.",
      [r"$(x-1)(x-2)(x+3)$", r"$(x+1)(x+2)(x-3)$", r"$(x-1)(x+2)(x-3)$", r"$(x+1)(x-2)(x+3)$", r"$(x-1)(x-2)(x-3)$", r"$(x-1)(x^2 + x + 6)$"], "A",
      r"$f(1) = 0$, so $(x-1)$ is a factor: $x^3 - 7x + 6 = (x-1)(x^2 + x - 6) = (x-1)(x+3)(x-2)$.", diff=1),

    Q("POL-04", T, "MM1.6", r"Find the remainder when $x^{4} + 2x^{3} - 3x + 1$ is divided by $(2x - 1)$.",
      [r"$-\dfrac{3}{16}$", r"$\dfrac{3}{16}$", r"$-\dfrac{1}{4}$", r"$\dfrac{13}{16}$", r"$1$", r"$-\dfrac{7}{16}$"], "A",
      r"$f\!\left(\frac12\right) = \frac1{16} + \frac{2}{8} - \frac32 + 1 = \frac{1}{16} + \frac{4}{16} - \frac{24}{16} + \frac{16}{16} = -\frac{3}{16}$.", diff=1),

    Q("POL-05", T, "MM1.6", r"The polynomial $p(x) = x^3 + ax^2 + bx + 4$ has $(x-1)$ and $(x+2)$ as factors. Find the third linear factor.",
      [r"$(x - 2)$", r"$(x + 2)$", r"$(x - 4)$", r"$(x + 1)$", r"$(x + 4)$", r"$(x - 1)$"], "A",
      r"Write $p(x) = (x-1)(x+2)(x-r)$. The constant term is $(-1)(2)(-r) = 2r = 4$, so $r = 2$: the third factor is $(x - 2)$.", diff=1),

    Q("POL-06", T, "MM1.6", r"When $p(x)$ is divided by $(x-1)$ the remainder is $3$, and when divided by $(x+1)$ the remainder is $-1$. Find the remainder when $p(x)$ is divided by $(x^2 - 1)$.",
      [r"$2x + 1$", r"$x + 2$", r"$2x - 1$", r"$-x + 2$", r"$3x - 1$", r"$2$"], "A",
      r"The remainder has degree $< 2$: $ax + b$ with $a + b = 3$ and $-a + b = -1$. So $b = 1$, $a = 2$: remainder $2x + 1$.", diff=2),

    Q("POL-07", T, "MM1.6", r"Find the quotient when $2x^3 - 3x^2 + 4x - 5$ is divided by $(x - 1)$.",
      [r"$2x^2 - x + 3$", r"$2x^2 + x + 3$", r"$2x^2 - x - 3$", r"$2x^2 - 5x + 9$", r"$2x^2 + x - 3$", r"$2x^2 - x + 5$"], "A",
      r"$2x^3 - 3x^2 + 4x - 5 = (x-1)(2x^2 - x + 3) - 2$: check the expansion $2x^3 - x^2 + 3x - 2x^2 + x - 3 = 2x^3 - 3x^2 + 4x - 3$, then subtract $2$ for the remainder.", diff=1),

    Q("POL-08", T, "MM1.6", r"""Which of the following statements about the polynomial $p(x) = x^3 - 6x^2 + 11x - 6$ is/are true?

I. $p(x)$ has three distinct real roots.
II. $(x - 4)$ is a factor of $p(x) - 6$.
III. $p(x) > 0$ for all $x > 3$.""", ROMAN3, "H",
      r"$p(x) = (x-1)(x-2)(x-3)$, so I is true. $p(4) - 6 = 3\cdot2\cdot1 - 6 = 0$, so II is true. For $x > 3$ all three factors are positive, so III is true.", paper=2, tags=("roman",)),

    Q("POL-09", T, "MM1.6", r"The expression $x^4 + 4$ can be factorised into two quadratics with integer coefficients. What is the sum of the coefficients of $x$ in these two quadratics?",
      ["$0$", "$2$", "$4$", "$-4$", "$1$", "It cannot be factorised."], "A",
      r"$x^4 + 4 = (x^2 + 2)^2 - 4x^2 = (x^2 + 2x + 2)(x^2 - 2x + 2)$. The $x$-coefficients are $2$ and $-2$, summing to $0$.", diff=2),

    Q("POL-10", T, "MM1.6", r"Given that $x^3 + px + q$ is divisible by $(x - 2)^2$, find the value of $q$.",
      ["$16$", "$-16$", "$8$", "$-8$", "$12$", "$-12$"], "A",
      r"$x^3 + px + q = (x-2)^2(x - r)$. Comparing $x^2$ coefficients: $-4 - r = 0 \Rightarrow r = -4$. Constant term: $(4)(4) = 16 = q$. (Also $p = 4 + 4r = -12$.)", diff=2),

    Q("POL-11", T, "MM1.6", r"Find the coefficient of $x^2$ in the expansion of $(x + 1)(x - 2)(2x + 3)$.",
      ["$1$", "$-1$", "$3$", "$-3$", "$2$", "$-2$"], "A",
      r"$(x+1)(x-2) = x^2 - x - 2$; multiply by $(2x + 3)$: the $x^2$ term is $3x^2 - 2x^2 = x^2$, coefficient $1$.", diff=1),

    Q("POL-12", T, "MM1.6", r"When $x^3 - 3x^2 + 2x + 7$ is divided by $x^2 + 1$, what is the remainder?",
      [r"$x + 10$", r"$x + 4$", r"$-x + 10$", r"$3x + 4$", r"$x + 7$", r"$10$"], "A",
      r"$x^3 - 3x^2 + 2x + 7 = (x^2 + 1)(x - 3) + (x + 10)$: expanding gives $x^3 - 3x^2 + x - 3 + x + 10$. Remainder $x + 10$.", diff=2),

    Q("POL-13", T, "MM1.6", r"Which of the following is a factor of $x^4 - 5x^2 + 4$?",
      [r"$x - 3$", r"$x + 4$", r"$x + 2$", r"$x - 4$", r"$x^2 + 1$", r"$x^2 + 4$"], "C",
      r"$x^4 - 5x^2 + 4 = (x^2 - 1)(x^2 - 4) = (x-1)(x+1)(x-2)(x+2)$.", diff=1),

    Q("POL-14", T, "MM1.6", r"$p(x)$ is a cubic polynomial with $p(1) = p(2) = p(3) = 0$ and $p(0) = 12$. Find $p(4)$.",
      ["$-12$", "$12$", "$24$", "$-24$", "$6$", "$0$"], "A",
      r"$p(x) = a(x-1)(x-2)(x-3)$; $p(0) = -6a = 12 \Rightarrow a = -2$. $p(4) = -2 \cdot 3\cdot2\cdot1 = -12$.", diff=1),

    Q("POL-15", T, "MM1.6", r"The polynomial $x^3 + ax^2 + bx + c$ has roots $2$, $-1$ and $3$. Find the value of $a + b + c$.",
      ["$3$", "$-3$", "$5$", "$-5$", "$7$", "$-7$"], "A",
      r"$p(1) = 1 + a + b + c$, and $p(1) = (1-2)(1+1)(1-3) = (-1)(2)(-2) = 4$. So $a + b + c = 3$. (Directly: $(x-2)(x+1)(x-3) = x^3 - 4x^2 + x + 6$.)", diff=1),

    Q("POL-16", T, "MM1.6", r"For which value of $k$ does $x^2 - x + k$ divide exactly into $x^3 - 2x^2 + 3x - 4$? (Assume such a value exists.)",
      ["$2$", "$-2$", "$4$", "$1$", "$3$", "no such value exists"], "F",
      r"Try $x^3 - 2x^2 + 3x - 4 = (x^2 - x + k)(x + m)$: comparing $x^2$: $m - 1 = -2 \Rightarrow m = -1$. Then $x$: $k - m = k + 1 = 3 \Rightarrow k = 2$. Constant: $km = -2 \neq -4$. No value of $k$ works.", diff=2),
]

