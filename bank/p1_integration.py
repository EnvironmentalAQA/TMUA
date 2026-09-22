"""Integration (MM7.1-MM7.6)."""
from gen.model import Q, ROMAN3

T = "integration"

QUESTIONS = [
    Q("INT-01", T, "MM7.2", r"Evaluate $\displaystyle\int_{1}^{4} \dfrac{3x^2 - 5}{\sqrt{x}}\,dx$.",
      [r"$\dfrac{136}{5}$", r"$\dfrac{186}{5}$", r"$\dfrac{86}{5}$", r"$28$", r"$\dfrac{126}{5}$", r"$\dfrac{146}{5}$"], "A",
      r"Integrand $= 3x^{3/2} - 5x^{-1/2}$; integral $= \left[\frac65 x^{5/2} - 10x^{1/2}\right]_1^4 = \left(\frac{6\cdot32}{5} - 20\right) - \left(\frac65 - 10\right) = \frac{192}{5} - 20 - \frac65 + 10 = \frac{186}{5} - 10 = \frac{136}{5}$.", diff=2),

    Q("INT-02", T, "MM7.1", r"Find the area enclosed between the curve $y = x^2 - 4x$ and the $x$-axis.",
      [r"$\dfrac{32}{3}$", r"$-\dfrac{32}{3}$", r"$\dfrac{16}{3}$", r"$\dfrac{64}{3}$", r"$8$", r"$\dfrac{8}{3}$"], "A",
      r"Roots $0$ and $4$; the curve is below the axis between them. $\int_0^4 (x^2 - 4x)\,dx = \frac{64}{3} - 32 = -\frac{32}{3}$, so the area is $\frac{32}{3}$.", diff=1),

    Q("INT-03", T, "MM7.3", r"Given that $\displaystyle\int_{1}^{5} f(x)\,dx = 7$ and $\displaystyle\int_{3}^{5} f(x)\,dx = 2$, find $\displaystyle\int_{1}^{3} \left(2f(x) - 1\right)dx$.",
      ["$8$", "$10$", "$12$", "$9$", "$3$", "$16$"], "A",
      r"$\int_1^3 f = 7 - 2 = 5$. So $2 \times 5 - (3 - 1) = 8$.", diff=1),

    Q("INT-04", T, "MM7.6", r"A curve has $\dfrac{dy}{dx} = 6x^2 - 4x + 1$ and passes through $(1, 3)$. Find its equation.",
      [r"$y = 2x^3 - 2x^2 + x + 2$", r"$y = 2x^3 - 2x^2 + x$", r"$y = 2x^3 - 4x^2 + x + 4$", r"$y = 12x - 4$", r"$y = 2x^3 - 2x^2 + x + 3$", r"$y = 2x^3 - 2x^2 + 2$"], "A",
      r"$y = 2x^3 - 2x^2 + x + c$; at $(1, 3)$: $2 - 2 + 1 + c = 3 \Rightarrow c = 2$.", diff=1),

    Q("INT-05", T, "MM7.1", r"Find the area of the finite region enclosed by the curve $y = x^2$ and the line $y = 2x + 3$.",
      [r"$\dfrac{32}{3}$", r"$\dfrac{16}{3}$", r"$\dfrac{64}{3}$", r"$12$", r"$\dfrac{20}{3}$", r"$\dfrac{28}{3}$"], "A",
      r"Intersections: $x^2 - 2x - 3 = (x - 3)(x + 1) = 0$. Area $= \int_{-1}^{3} (2x + 3 - x^2)\,dx = \left[x^2 + 3x - \frac{x^3}{3}\right]_{-1}^{3} = (9 + 9 - 9) - \left(1 - 3 + \frac13\right) = 9 + \frac53 = \frac{32}{3}$.", diff=2),

    Q("INT-06", T, "MM7.5", r"The trapezium rule with $2$ strips of equal width is used to estimate $\displaystyle\int_{0}^{2} x^2\,dx$. Which of the following is true?",
      [r"The estimate is $\dfrac{5}{2}$ and it is an overestimate.", r"The estimate is $\dfrac{5}{2}$ and it is an underestimate.", r"The estimate is $3$ and it is an overestimate.", r"The estimate is $\dfrac{8}{3}$ and it is exact.", r"The estimate is $3$ and it is an underestimate."], "C",
      r"$h = 1$: $\frac{h}{2}[y_0 + 2y_1 + y_2] = \frac12[0 + 2(1) + 4] = 3$. The true value is $\frac83$; the curve bends upwards (convex), so the chords lie above it and the rule overestimates.", diff=1),

    Q("INT-07", T, "MM7.3", r"Given that $\displaystyle\int_{0}^{a} (2x + 1)\,dx = 12$ where $a > 0$, find $a$.",
      ["$3$", "$4$", "$2$", "$6$", r"$\sqrt{12}$", "$12$"], "A",
      r"$a^2 + a = 12 \Rightarrow (a + 4)(a - 3) = 0 \Rightarrow a = 3$.", diff=1),

    Q("INT-08", T, "MM7.4", r"Let $F(x) = \displaystyle\int_{2}^{x} (t^2 - 3t)\,dt$. Find $F'(3)$.",
      ["$0$", "$9$", "$-3$", r"$\dfrac{9}{2}$", "$3$", r"$-\dfrac{7}{6}$"], "A",
      r"By the Fundamental Theorem of Calculus $F'(x) = x^2 - 3x$, so $F'(3) = 9 - 9 = 0$.", diff=1),

    Q("INT-09", T, "MM7.1", r"""Which of the following statements is/are true?

I. $\displaystyle\int_{-2}^{2} x^3\,dx = 0$
II. The area between $y = x^3$ and the $x$-axis from $x = -2$ to $x = 2$ is $0$.
III. $\displaystyle\int_{-2}^{2} x^2\,dx = 2\int_{0}^{2} x^2\,dx$""", ROMAN3, "F",
      r"I: odd function over a symmetric interval, so $0$. II is false: the area is $2\int_0^2 x^3\,dx = 8$; the integral is $0$ because the parts cancel. III: even function, true.", paper=2, tags=("roman",), diff=1),

    Q("INT-10", T, "MM7.2", r"Find $\displaystyle\int \left(x + \dfrac{1}{x}\right)^2 dx$.",
      [r"$\dfrac{x^3}{3} + 2x - \dfrac{1}{x} + c$", r"$\dfrac{x^3}{3} + 2x + \dfrac{1}{x} + c$", r"$\dfrac{x^3}{3} - \dfrac{1}{x} + c$", r"$\dfrac{x^3}{3} + 2x + c$", r"$\dfrac{1}{3}\left(x + \dfrac1x\right)^3 + c$", r"$x^3 + 2x - \dfrac1x + c$"], "A",
      r"$\left(x + \frac1x\right)^2 = x^2 + 2 + x^{-2}$, which integrates to $\frac{x^3}{3} + 2x - x^{-1} + c$. ($\frac13\left(x + \frac1x\right)^3 + c$ is a common error: you cannot integrate a power of a bracket that way.)", diff=1),

    Q("INT-11", T, "MM7.1", r"The region bounded by $y = 4 - x^2$, the $x$-axis and the lines $x = 0$ and $x = 3$ is shaded. Find the total shaded area.",
      [r"$\dfrac{23}{3}$", r"$3$", r"$\dfrac{16}{3}$", r"$\dfrac{7}{3}$", r"$9$", r"$\dfrac{25}{3}$"], "A",
      r"From $0$ to $2$ the curve is above the axis: $\int_0^2 (4 - x^2)\,dx = 8 - \frac83 = \frac{16}{3}$. From $2$ to $3$ it is below: $\left|\int_2^3 (4 - x^2)\,dx\right| = \left|(12 - 9) - \frac{16}{3}\right| = \frac73$. Total $\frac{23}{3}$.", diff=2),

    Q("INT-12", T, "MM7.2", r"Find the value of $\displaystyle\int_{1}^{8} x^{-\frac{2}{3}}\,dx$.",
      ["$3$", "$6$", r"$\dfrac{3}{2}$", "$9$", r"$\dfrac{21}{2}$", "$2$"], "A",
      r"$\left[3x^{1/3}\right]_1^8 = 3(2 - 1) = 3$.", diff=1),

    Q("INT-13", T, "MM7.3", r"$f(x) = ax + b$ satisfies $\displaystyle\int_{0}^{1} f(x)\,dx = 2$ and $\displaystyle\int_{0}^{2} f(x)\,dx = 6$. Find $f(1)$.",
      ["$2$", "$3$", "$1$", "$4$", "$0$", "$5$"], "B",
      r"$\frac a2 + b = 2$ and $2a + 2b = 6$, so $a + b = 3$; subtracting the first equation from this gives $\frac a2 = 1$, so $a = 2$, $b = 1$ and $f(1) = 3$.", diff=1),

    Q("INT-14", T, "MM7.5", r"The trapezium rule is used to estimate $\displaystyle\int_{a}^{b} f(x)\,dx$. For which of the following functions is the estimate guaranteed to be an underestimate for every choice of $a < b$?",
      [r"$f(x) = -x^2$", r"$f(x) = x^2$", r"$f(x) = 2x + 1$", r"$f(x) = x^3$", r"$f(x) = x^4$"], "A",
      r"The trapezium rule underestimates when the curve is concave (bends downwards) so that chords lie below the curve: $y = -x^2$ everywhere. $x^3$ changes concavity at $0$.", diff=2),

    Q("INT-15", T, "MM7.1", r"The area between the curve $y = x^2$ and the line $y = k$ (where $k > 0$) is $\dfrac{32}{3}$. Find $k$.",
      ["$4$", "$2$", "$8$", "$16$", "$3$", r"$\sqrt{8}$"], "A",
      r"Area $= \int_{-\sqrt k}^{\sqrt k}(k - x^2)\,dx = 2\left(k^{3/2} - \frac{k^{3/2}}{3}\right) = \frac43 k^{3/2} = \frac{32}{3} \Rightarrow k^{3/2} = 8 \Rightarrow k = 4$.", diff=2),

    Q("INT-16", T, "MM7.4", r"Given that $\displaystyle\int_{0}^{4} f(x)\,dx = 10$, find $\displaystyle\int_{0}^{4} \left(f(x) + 3x\right)dx - \int_{4}^{0} f(x)\,dx$.",
      ["$44$", "$24$", "$34$", "$0$", "$14$", "$20$"], "A",
      r"$10 + 24 - (-10) = 44$.", diff=1),

    Q("INT-17", T, "MM7.6", r"The gradient of a curve at $(x, y)$ is $3\sqrt{x}$ and the curve passes through $(4, 20)$. Find the $y$-intercept of the curve.",
      ["$4$", "$20$", "$12$", "$0$", "$8$", "$-4$"], "A",
      r"$y = 2x^{3/2} + c$; $20 = 16 + c \Rightarrow c = 4$. The $y$-intercept is $4$.", diff=1),

    Q("INT-18", T, "MM7.3", r"Let $I = \displaystyle\int_{0}^{1} (x^2 + 1)\,dx$ and $J = \displaystyle\int_{0}^{1} (x + 1)^2\,dx$. Which of the following is true?",
      [r"$I < J$ and $J - I = 1$", r"$I < J$ and $J - I = \dfrac{1}{2}$", r"$I = J$", r"$I > J$", r"$I < J$ and $J - I = \dfrac{4}{3}$"], "A",
      r"$I = \frac13 + 1 = \frac43$. $J = \int_0^1 (x^2 + 2x + 1)\,dx = \frac13 + 1 + 1 = \frac73$. $J - I = 1$.", diff=1),

    Q("INT-19", T, "MM7.1", r"The curve $y = x(x - 1)(x - 2)$ and the $x$-axis enclose two regions. What is the ratio of the area of the region for $0 \leq x \leq 1$ to the area for $1 \leq x \leq 2$?",
      [r"$1 : 1$", r"$1 : 2$", r"$2 : 1$", r"$1 : 3$", r"$3 : 1$", r"$1 : 4$"], "A",
      r"The cubic has rotational symmetry about $(1, 0)$ (it is $u^3 - u$ with $u = x - 1$, an odd function), so the two regions are congruent: ratio $1 : 1$.", diff=2),

    Q("INT-20", T, "MM7.2", r"Evaluate $\displaystyle\int_{-1}^{2} |x|\,dx$.",
      [r"$\dfrac{5}{2}$", r"$\dfrac{3}{2}$", r"$2$", r"$3$", r"$\dfrac{1}{2}$", r"$\dfrac{7}{2}$"], "A",
      r"Two triangles: $\frac12\cdot1\cdot1 + \frac12\cdot2\cdot2 = \frac12 + 2 = \frac52$.", diff=1),
]
