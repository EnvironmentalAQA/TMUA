"""Differentiation (MM6.1-MM6.3, MM8.5)."""
from gen.model import Q, ROMAN3

T = "differentiation"

QUESTIONS = [
    Q("DIF-01", T, "MM6.2", r"Find $\dfrac{dy}{dx}$ when $y = \dfrac{(3x - 2)^2}{x^2}$.",
      [r"$\dfrac{12}{x^2} - \dfrac{8}{x^3}$", r"$\dfrac{12}{x^2} + \dfrac{8}{x^3}$", r"$-\dfrac{12}{x^2} + \dfrac{8}{x^3}$", r"$\dfrac{6(3x-2)}{x^2}$", r"$\dfrac{6}{x} - \dfrac{12}{x^2}$", r"$9 - \dfrac{12}{x}$"], "A",
      r"$y = 9 - 12x^{-1} + 4x^{-2}$, so $y' = 12x^{-2} - 8x^{-3}$.", diff=1),

    Q("DIF-02", T, "MM6.3", r"Find the coordinates of the stationary points of $y = x^3 - 3x^2 - 9x + 5$ and state their nature.",
      [r"maximum at $(-1, 10)$, minimum at $(3, -22)$", r"minimum at $(-1, 10)$, maximum at $(3, -22)$", r"maximum at $(-1, 0)$, minimum at $(3, -32)$", r"maximum at $(1, -6)$, minimum at $(-3, -22)$", r"maximum at $(-1, 10)$ only"], "A",
      r"$y' = 3x^2 - 6x - 9 = 3(x - 3)(x + 1)$. $y'' = 6x - 6$: negative at $x = -1$ (max, $y = -1 - 3 + 9 + 5 = 10$), positive at $x = 3$ (min, $y = 27 - 27 - 27 + 5 = -22$).", diff=1),

    Q("DIF-03", T, "MM6.3", r"The tangent to $y = x^2 - 4x + 1$ at the point where $x = 3$ meets the $y$-axis at",
      [r"$(0, -8)$", r"$(0, -2)$", r"$(0, 1)$", r"$(0, 4)$", r"$(0, -5)$", r"$(0, 8)$"], "A",
      r"$y' = 2x - 4 = 2$ at $x = 3$; the point is $(3, -2)$. Tangent: $y + 2 = 2(x - 3)$, so at $x = 0$, $y = -8$.", diff=1),

    Q("DIF-04", T, "MM6.3", r"Find the equation of the normal to the curve $y = \sqrt{x}$ at the point $(4, 2)$.",
      [r"$y = -4x + 18$", r"$y = \dfrac14 x + 1$", r"$y = -4x + 16$", r"$y = 4x - 14$", r"$y = -\dfrac14 x + 3$", r"$y = -4x + 2$"], "A",
      r"$y' = \frac{1}{2\sqrt x} = \frac14$ at $x = 4$, so the normal has gradient $-4$: $y - 2 = -4(x - 4)$, i.e. $y = -4x + 18$.", diff=1),

    Q("DIF-05", T, "MM6.3", r"For what range of values of $x$ is $f(x) = 2x^3 - 15x^2 + 24x + 1$ decreasing?",
      [r"$1 < x < 4$", r"$x < 1$ or $x > 4$", r"$-4 < x < -1$", r"$x < 4$", r"$x > 1$", r"$2 < x < 3$"], "A",
      r"$f'(x) = 6x^2 - 30x + 24 = 6(x - 1)(x - 4) < 0$ for $1 < x < 4$.", diff=1),

    Q("DIF-06", T, "MM6.1", r"The displacement $s$ metres of a particle at time $t$ seconds is $s = t^3 - 6t^2 + 9t$. At what times is the particle momentarily at rest?",
      [r"$t = 1$ and $t = 3$", r"$t = 0$ and $t = 3$", r"$t = 2$ only", r"$t = 1$ only", r"$t = 3$ only", r"$t = 0$, $t = 1$ and $t = 3$"], "A",
      r"Velocity $= \frac{ds}{dt} = 3t^2 - 12t + 9 = 3(t - 1)(t - 3) = 0$ at $t = 1$ and $t = 3$.", diff=1),

    Q("DIF-07", T, "MM6.3", r"The curve $y = ax^2 + bx$ has a stationary point at $(2, -8)$. Find $a + b$.",
      ["$-6$", "$6$", "$-2$", "$2$", "$-10$", "$10$"], "A",
      r"$y' = 2ax + b = 0$ at $x = 2$: $b = -4a$. $y(2) = 4a + 2b = 4a - 8a = -4a = -8 \Rightarrow a = 2$, $b = -8$. $a + b = -6$.", diff=1),

    Q("DIF-08", T, "MM6.2", r"Given $f(x) = x^{\frac{3}{2}} - 6x^{\frac{1}{2}}$ for $x > 0$, find the value of $x$ at which $f$ has its minimum.",
      ["$2$", "$4$", "$1$", "$3$", "$6$", r"$\sqrt{2}$"], "A",
      r"$f'(x) = \frac32 x^{1/2} - 3x^{-1/2} = \frac{3}{2\sqrt x}(x - 2) = 0$ at $x = 2$; $f'$ changes from negative to positive there, so it is a minimum.", diff=2),

    Q("DIF-09", T, "MM6.3", r"A rectangle has perimeter $40$. What is its maximum possible area?",
      ["$100$", "$400$", "$80$", "$200$", "$50$", "$160$"], "A",
      r"Sides $x$ and $20 - x$: $A = 20x - x^2$, $A' = 20 - 2x = 0$ at $x = 10$, giving $A = 100$ (a square).", diff=1),

    Q("DIF-10", T, "MM6.3", r"The curve $y = x^3 + px^2 + qx$ has stationary points at $x = 1$ and $x = 3$. Find $q$.",
      ["$9$", "$-6$", "$6$", "$-9$", "$3$", "$12$"], "A",
      r"$y' = 3x^2 + 2px + q = 3(x - 1)(x - 3) = 3x^2 - 12x + 9$. So $q = 9$ (and $p = -6$).", diff=1),

    Q("DIF-11", T, "MM6.3", r"""Which of the following statements about $f(x) = x^3 - 3x$ is/are true?

I. $f$ is increasing for all $x > 1$.
II. $f$ has a local maximum at $x = -1$.
III. $f(x) \geq -2$ for all real $x$.""", ROMAN3, "E",
      r"$f'(x) = 3x^2 - 3 = 3(x-1)(x+1)$: positive for $x > 1$ (I true); $f'' = 6x < 0$ at $x = -1$ (II true). III false: the local minimum $f(1) = -2$ is not a global minimum since $f(x) \to -\infty$ as $x \to -\infty$ (e.g. $f(-3) = -18$).", paper=2, tags=("roman",)),

    Q("DIF-12", T, "MM6.3", r"The line $y = 4x + c$ is a tangent to $y = x^2 + 2x + 5$. Find $c$.",
      ["$4$", "$5$", "$1$", "$6$", "$-4$", "$3$"], "A",
      r"$2x + 2 = 4 \Rightarrow x = 1$, $y = 8$. $8 = 4 + c \Rightarrow c = 4$.", diff=1),

    Q("DIF-13", T, "MM6.1", r"$f(x)$ is a polynomial with $f'(x) = (x - 2)^2(x + 1)$. Which of the following is true?",
      [r"$f$ has a local minimum at $x = -1$ and no turning point at $x = 2$", r"$f$ has a local maximum at $x = -1$ and a local minimum at $x = 2$", r"$f$ has local minima at $x = -1$ and $x = 2$", r"$f$ has a local minimum at $x = -1$ and a local maximum at $x = 2$", r"$f$ has no turning points"], "A",
      r"$f'$ changes sign from negative to positive at $x = -1$ (local minimum). At $x = 2$ the factor $(x-2)^2$ does not change sign, so $f'$ stays positive: a stationary point but not a turning point (a point of inflexion).", diff=2),

    Q("DIF-14", T, "MM6.2", r"Find $\dfrac{d^2y}{dx^2}$ when $y = \dfrac{1}{x^2} + 4\sqrt{x}$.",
      [r"$\dfrac{6}{x^4} - x^{-\frac32}$", r"$\dfrac{6}{x^4} + x^{-\frac32}$", r"$-\dfrac{6}{x^4} - x^{-\frac32}$", r"$\dfrac{2}{x^3} + 2x^{-\frac12}$", r"$\dfrac{6}{x^4} - 2x^{-\frac32}$", r"$\dfrac{3}{x^4} - x^{-\frac32}$"], "A",
      r"$y' = -2x^{-3} + 2x^{-1/2}$; $y'' = 6x^{-4} - x^{-3/2}$.", diff=1),

    Q("DIF-15", T, "MM6.3", r"The volume of a cuboid with a square base of side $x$ is $V = 4x^2 - x^3$ for $0 < x < 4$. Find the maximum volume.",
      [r"$\dfrac{256}{27}$", r"$\dfrac{64}{27}$", r"$\dfrac{32}{3}$", r"$16$", r"$\dfrac{128}{27}$", r"$8$"], "A",
      r"$V' = 8x - 3x^2 = x(8 - 3x) = 0 \Rightarrow x = \frac83$. $V = \frac{64}{9}\cdot 4 - \frac{512}{27} = \frac{768 - 512}{27} = \frac{256}{27}$.", diff=2),

    Q("DIF-16", T, "MM6.3", r"The tangent to $y = x^3$ at the point $(a, a^3)$, where $a \neq 0$, meets the curve again at the point with $x$-coordinate",
      [r"$-2a$", r"$2a$", r"$-a$", r"$a/2$", r"$-a/2$", r"$0$"], "A",
      r"Tangent: $y = 3a^2 x - 2a^3$. Solve $x^3 - 3a^2 x + 2a^3 = 0$; $x = a$ is a double root, so $(x - a)^2(x + 2a) = 0$: the other intersection is $x = -2a$.", diff=2),

    Q("DIF-17", T, "MM6.3", r"The curve $y = x^2 + kx$ (with $k < 0$) crosses the $x$-axis at the origin and at one other point $P$. The gradient of the curve at $P$ is $6$. Find $k$.",
      ["$-6$", "$6$", "$-3$", "$3$", "$-12$", "$-2$"], "A",
      r"$P = (-k, 0)$. $y' = 2x + k = -2k + k = -k = 6$, so $k = -6$.", diff=1),

    Q("DIF-18", T, "MM6.3", r"Find the minimum value of $x + \dfrac{4}{x}$ for $x > 0$.",
      ["$4$", "$2$", "$8$", r"$2\sqrt2$", "$5$", "$0$"], "A",
      r"Derivative $1 - \frac{4}{x^2} = 0$ at $x = 2$; value $2 + 2 = 4$ (second derivative $\frac{8}{x^3} > 0$, so a minimum).", diff=1),

    Q("DIF-19", T, "MM6.1", r"""Which of the following statements is/are true for every function $f$ that has a derivative at every real number?

I. If $f'(a) = 0$ then $f$ has a maximum or a minimum at $x = a$.
II. If $f$ has a local minimum at $x = a$ then $f'(a) = 0$.
III. If $f'(x) > 0$ for all $x$, then $f(3) > f(2)$.""", ROMAN3, "G",
      r"I is false: $f(x) = x^3$ has $f'(0) = 0$ but no turning point. II is true (a stationary point is required at an interior local extremum of a differentiable function). III is true: a strictly increasing function has $f(3) > f(2)$.", paper=2, tags=("roman",), diff=2),

    Q("DIF-20", T, "MM6.3", r"Find the sum of the $y$-coordinates of the stationary points of the curve $y = 2x^3 - 9x^2 + 12x - 3$.",
      ["$3$", "$2$", "$1$", "$4$", "$0$", "$5$"], "A",
      r"$y' = 6x^2 - 18x + 12 = 6(x - 1)(x - 2)$: stationary points at $x = 1$ ($y = 2 - 9 + 12 - 3 = 2$) and $x = 2$ ($y = 16 - 36 + 24 - 3 = 1$). Sum $3$.", diff=1),
]
