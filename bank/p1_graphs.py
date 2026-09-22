"""Graphs of functions (MM8.1, MM8.5-MM8.7, M4.15)."""
from gen.model import Q, ROMAN3

T = "graphs"

QUESTIONS = [
    Q("GRA-01", T, "MM8.6", r"How many times does the graph of $y = x^3 - x^2 - 6x$ cross or touch the $x$-axis?",
      ["$3$", "$2$", "$1$", "$0$", "$4$"], "A",
      r"$x(x^2 - x - 6) = x(x - 3)(x + 2)$: three distinct real roots, so three crossings.", diff=1),

    Q("GRA-02", T, "MM8.7", r"The graphs of $y = x^2 - 2x$ and $y = k$ meet at exactly two points. Find the complete set of values of $k$.",
      [r"$k > -1$", r"$k \geq -1$", r"$k < -1$", r"$k > 0$", r"$k = -1$", r"all real $k$"], "A",
      r"$y = (x-1)^2 - 1$ has minimum $-1$; a horizontal line above the minimum meets the parabola twice.", diff=1),

    Q("GRA-03", T, "MM8.1", r"Which of the following could be the equation of a cubic curve that touches the $x$-axis at $x = 2$ and crosses it at $x = -1$, and has a negative $y$-intercept?",
      [r"$y = -(x - 2)^2(x + 1)$", r"$y = (x - 2)^2(x + 1)$", r"$y = (x + 2)^2(x - 1)$", r"$y = -(x + 2)^2(x - 1)$", r"$y = (x - 2)(x + 1)^2$"], "A",
      r"Touching at $2$ needs the factor $(x - 2)^2$ and crossing at $-1$ the factor $(x + 1)$. $y = (x-2)^2(x+1)$ has $y$-intercept $4 > 0$, so the sign is reversed: $y = -(x-2)^2(x+1)$ with intercept $-4$.", diff=1),

    Q("GRA-04", T, "MM8.7", r"The line $y = x + c$ and the curve $y = \dfrac{1}{x}$ have no points of intersection. Find the complete set of values of $c$.",
      [r"$-2 < c < 2$", r"$c < -2$ or $c > 2$", r"$c > 2$", r"$c < 2$", r"$-1 < c < 1$", r"no such values"], "F",
      r"$x^2 + cx - 1 = 0$ always has discriminant $c^2 + 4 > 0$: two intersections for every $c$. So there are no values of $c$ with no intersection.", diff=2),

    Q("GRA-05", T, "MM8.1", r"""Which of the following statements about the graph of $y = |2x - 4|$ is/are true?

I. It meets the $x$-axis at exactly one point.
II. It is symmetric about the line $x = 2$.
III. It lies entirely on or above the line $y = 0$.""", ROMAN3, "H",
      r"$|2x - 4| = 0$ only at $x = 2$ (I). $|2x - 4| = 2|x - 2|$ is symmetric about $x = 2$ (II). A modulus is never negative (III).", paper=2, tags=("roman",), diff=1),

    Q("GRA-06", T, "MM8.6", r"The curve $y = x^4 - 5x^2 + 4$ meets the coordinate axes at how many points in total?",
      ["$5$", "$4$", "$3$", "$6$", "$2$", "$1$"], "A",
      r"$x$-axis: $(x^2 - 1)(x^2 - 4) = 0$, four points. $y$-axis: $(0, 4)$, one point. Total $5$.", diff=1),

    Q("GRA-07", T, "MM8.5", r"The graph of $y = f(x)$ has $f'(x) > 0$ for $x < 1$, $f'(1) = 0$, $f'(x) > 0$ for $1 < x < 3$, $f'(x) < 0$ for $x > 3$. Which of the following is true?",
      [r"$f$ has a local maximum at $x = 3$ and a stationary point of inflexion at $x = 1$", r"$f$ has a local minimum at $x = 1$ and a local maximum at $x = 3$", r"$f$ has local maxima at $x = 1$ and $x = 3$", r"$f$ has a local maximum at $x = 1$ and a local minimum at $x = 3$", r"$f$ is increasing for all $x$"], "A",
      r"At $x = 1$ the derivative is zero but does not change sign: a stationary point that is not a turning point (an inflexion). At $x = 3$ the derivative changes from positive to negative: local maximum.", diff=2),

    Q("GRA-08", T, "MM8.7", r"How many real solutions does the equation $x^3 = 3x + 1$ have?",
      ["$3$", "$1$", "$2$", "$0$", "infinitely many"], "A",
      r"Sketch $y = x^3 - 3x - 1$: turning points at $x = \pm1$ with $y(-1) = 1 > 0$ and $y(1) = -3 < 0$. A cubic whose local maximum is positive and local minimum is negative crosses the axis three times.", diff=2),

    Q("GRA-09", T, "MM8.1", r"The graph of $y = \log_2 x$ is reflected in the line $y = x$. The resulting graph has equation",
      [r"$y = 2^{x}$", r"$y = \log_2(-x)$", r"$y = -\log_2 x$", r"$y = \log_{\frac12} x$", r"$y = x^2$", r"$y = 2^{-x}$"], "A",
      r"Reflection in $y = x$ gives the inverse function: $x = \log_2 y$, i.e. $y = 2^x$.", diff=1),

    Q("GRA-10", T, "MM8.6", r"A polynomial of degree $5$ with real coefficients has how many real roots at least, and at most?",
      [r"at least $1$, at most $5$", r"at least $0$, at most $5$", r"at least $1$, at most $4$", r"at least $2$, at most $5$", r"exactly $5$", r"at least $0$, at most $4$"], "A",
      r"An odd-degree polynomial tends to opposite infinities at each end, so it crosses the axis at least once; a degree-$5$ polynomial has at most $5$ roots.", diff=1),

    Q("GRA-11", T, "MM8.7", r"The curves $y = 2^{x}$ and $y = x^2$ intersect at how many points?",
      ["$3$", "$2$", "$1$", "$0$", "$4$"], "A",
      r"They meet at $x = 2$ and $x = 4$ ($4 = 4$, $16 = 16$), and once for negative $x$ (at $x = 0$: $1 > 0$; at $x = -1$: $\frac12 < 1$). For $x > 4$, $2^x$ grows faster. Three intersections.", diff=2),

    Q("GRA-12", T, "MM8.1", r"Which of the following functions is undefined at exactly two real values of $x$?",
      [r"$f(x) = \dfrac{1}{x^2 - 4}$", r"$f(x) = \dfrac{1}{x^2 + 4}$", r"$f(x) = \dfrac{x}{x^2}$", r"$f(x) = \dfrac{1}{(x - 2)^2}$", r"$f(x) = \sqrt{x - 2}$"], "A",
      r"$x^2 - 4 = 0$ at $x = \pm 2$: two values. $x^2 + 4$ is never zero; $\frac{x}{x^2}$ and $\frac{1}{(x-2)^2}$ are undefined at one value; $\sqrt{x - 2}$ is undefined for all $x < 2$.", diff=1),

    Q("GRA-13", T, "MM8.7", r"For how many values of $k$ does the equation $|x^2 - 4| = k$ have exactly three real solutions?",
      ["$1$", "$0$", "$2$", "$3$", "infinitely many"], "A",
      r"The graph of $y = |x^2 - 4|$ is a W-shape with minima $0$ at $x = \pm2$ and a local maximum $4$ at $x = 0$. A horizontal line gives three solutions only when it passes through the local maximum: $k = 4$. One value.", diff=2),

    Q("GRA-14", T, "MM8.1", r"The graph of $y = \sqrt{x}$ is transformed to $y = \sqrt{4 - x}$. Which sequence of transformations achieves this?",
      [r"reflect in the $y$-axis, then translate $4$ units in the positive $x$-direction", r"translate $4$ units in the positive $x$-direction, then reflect in the $y$-axis", r"reflect in the $x$-axis, then translate $4$ units in the positive $y$-direction", r"translate $4$ units in the negative $x$-direction, then reflect in the $y$-axis", r"stretch parallel to the $x$-axis with factor $4$"], "A",
      r"$\sqrt{4 - x} = \sqrt{-(x - 4)}$: reflect $y = \sqrt x$ in the $y$-axis to get $\sqrt{-x}$, then translate $4$ to the right. (Translating first then reflecting gives $\sqrt{-x - 4}$.)", diff=2),

    Q("GRA-15", T, "MM8.6", r"""The cubic $y = x^3 + ax + b$ has three distinct real roots. Which of the following statements must be true?

I. $a < 0$
II. $b \neq 0$
III. The curve has two turning points.""", ROMAN3, "F",
      r"Three distinct real roots require two turning points (III), which needs $y' = 3x^2 + a$ to have two roots, so $a < 0$ (I). II is false: $x^3 - x$ has roots $0, \pm1$ and $b = 0$.", paper=2, tags=("roman",), diff=2),

    Q("GRA-16", T, "MM8.7", r"The line $y = mx$ meets the curve $y = x^3 - x$ at three distinct points. Find the complete set of values of $m$.",
      [r"$m > -1$", r"$m < -1$", r"$m > 0$", r"$m > 1$", r"$-1 < m < 0$", r"all real $m$"], "A",
      r"$x^3 - x - mx = x(x^2 - (1 + m)) = 0$: three distinct roots iff $1 + m > 0$, i.e. $m > -1$.", diff=1),
]
