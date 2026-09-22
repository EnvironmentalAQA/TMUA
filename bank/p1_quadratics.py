"""Quadratic functions (MM1.3, M4.5, M4.11-M4.14)."""
from gen.model import Q, ROMAN3

T = "quadratics"

QUESTIONS = [
    Q("QUA-01", T, "MM1.3", r"The equation $x^2 + (k-2)x + (k+1) = 0$ has two distinct real roots. Find the complete set of possible values of $k$.",
      [r"$k < 0$ or $k > 8$", r"$0 < k < 8$", r"$k < -2$ or $k > 4$", r"$-2 < k < 4$", r"$k < 0$ or $k > 4$", r"all real $k$"], "A",
      r"Discriminant $(k-2)^2 - 4(k+1) = k^2 - 8k = k(k-8) > 0$, so $k < 0$ or $k > 8$.", diff=1),

    Q("QUA-02", T, "MM1.3", r"By completing the square, find the minimum value of $2x^2 - 12x + 23$.",
      ["$5$", "$23$", "$-13$", "$3$", "$7$", "$-5$"], "A",
      r"$2x^2 - 12x + 23 = 2(x-3)^2 - 18 + 23 = 2(x-3)^2 + 5$, so the minimum is $5$ (at $x = 3$).", diff=1),

    Q("QUA-03", T, "MM1.3", r"The quadratic $y = ax^2 + bx + c$ has its vertex at $(2, -3)$ and passes through $(0, 5)$. Find $a + b + c$.",
      ["$-1$", "$1$", "$3$", "$5$", "$-3$", "$7$"], "A",
      r"$y = a(x-2)^2 - 3$; at $x = 0$: $4a - 3 = 5$, so $a = 2$. Then $y = 2(x-2)^2 - 3 = 2x^2 - 8x + 5$, and $a + b + c = 2 - 8 + 5 = -1$ (which is just $y(1)$).", diff=1),

    Q("QUA-04", T, "MM1.3", r"The roots of $x^2 - 5x + 2 = 0$ are $\alpha$ and $\beta$. Find the value of $\alpha^2 + \beta^2$.",
      ["$21$", "$25$", "$29$", "$23$", "$27$", "$17$"], "A",
      r"$\alpha + \beta = 5$ and $\alpha\beta = 2$. So $\alpha^2 + \beta^2 = (\alpha+\beta)^2 - 2\alpha\beta = 25 - 4 = 21$."),

    Q("QUA-05", T, "MM1.3", r"For what value of $c$ does the line $y = 2x + c$ touch the parabola $y = x^2 - 4x + 7$?",
      ["$-2$", "$-1$", "$0$", "$2$", "$5$", "$7$"], "A",
      r"Equate: $x^2 - 6x + (7 - c) = 0$. Tangency needs discriminant zero: $36 - 4(7-c) = 0$, so $8 + 4c = 0$ and $c = -2$.", diff=1),

    Q("QUA-06", T, "MM1.3", r"""The function $f(x) = x^2 - 6x + 13$ is defined for all real $x$. Which of the following statements is/are true?

I. $f(x) > 0$ for all real $x$
II. The graph of $y = f(x)$ is symmetric about the line $x = 3$
III. The equation $f(x) = 4$ has exactly one real solution""", ROMAN3, "H",
      r"$f(x) = (x-3)^2 + 4 \geq 4 > 0$, so I is true. The axis of symmetry is $x = 3$, so II is true. $f(x) = 4$ only when $(x-3)^2 = 0$, i.e. $x = 3$: exactly one solution, so III is true.", paper=2, tags=("roman",)),

    Q("QUA-07", T, "MM1.3", r"How many real solutions does the equation $x^4 - 5x^2 + 4 = 0$ have?",
      ["$0$", "$1$", "$2$", "$3$", "$4$", "$5$"], "E",
      r"Let $u = x^2$: $u^2 - 5u + 4 = (u-1)(u-4) = 0$, so $x^2 = 1$ or $x^2 = 4$, giving $x = \pm1, \pm2$: four solutions.", diff=1),

    Q("QUA-08", T, "MM1.3", r"The equation $kx^2 + 4x + k = 0$ has no real roots. Find the complete set of values of $k$.",
      [r"$k < -2$ or $k > 2$", r"$-2 < k < 2$", r"$k > 2$", r"$-2 < k < 0$ or $0 < k < 2$", r"$k < -2$", r"$0 < k < 2$"], "A",
      r"Need $16 - 4k^2 < 0$, i.e. $k^2 > 4$, so $k < -2$ or $k > 2$. (If $k = 0$ the equation is linear with one root, so $k = 0$ is excluded anyway.)", diff=1),

    Q("QUA-09", T, "MM1.3", r"Find the sum of all real values of $x$ satisfying $(x^2 - 3x)^2 - 2(x^2 - 3x) - 8 = 0$.",
      ["$3$", "$6$", "$0$", "$-3$", "$9$", "$2$"], "B",
      r"Let $u = x^2 - 3x$: $(u-4)(u+2) = 0$. $x^2 - 3x - 4 = 0$ gives $x = 4, -1$ (sum 3). $x^2 - 3x + 2 = 0$ gives $x = 1, 2$ (sum 3). Total $6$."),

    Q("QUA-10", T, "MM1.3", r"The quadratic $x^2 + px + q$ has minimum value $-4$ and one of its roots is $0$. Which of the following could be the quadratic?",
      [r"$x^2 - 2x - 3$", r"$x^2 - 4x$", r"$x^2 + 6x + 5$", r"$x^2 - 6x + 8$", r"$x^2 + 2x - 8$"], "B",
      r"Minimum $-4$ means $x^2 + px + q = (x-h)^2 - 4$, with roots $h \pm 2$. One root is $0$, so $h = \pm 2$: the quadratic is $x^2 - 4x$ or $x^2 + 4x$. Only $x^2 - 4x$ is offered.", diff=1),

    Q("QUA-11", T, "MM1.3", r"The curve $y = x^2 - 2ax + a^2 + a - 6$ has its vertex on the $x$-axis. Find the value of $a$.",
      ["$6$", "$-6$", "$3$", "$-2$", "$2$", "$0$"], "A",
      r"Complete the square: $y = (x-a)^2 + a - 6$. The vertex is $(a, a-6)$, which lies on the $x$-axis when $a = 6$.", diff=1),

    Q("QUA-12", T, "MM1.3", r"The roots of $2x^2 + bx + 18 = 0$ are equal. Find the sum of the possible values of $b$.",
      ["$0$", "$12$", "$24$", "$-12$", "$36$", "$6$"], "A",
      r"$b^2 - 144 = 0$, so $b = \pm 12$; their sum is $0$.", diff=1),

    Q("QUA-13", T, "MM1.3", r"Which of the following quadratics has its vertex in the second quadrant (where $x < 0$ and $y > 0$)?",
      [r"$y = x^2 + 4x + 1$", r"$y = x^2 - 4x + 5$", r"$y = -x^2 - 2x - 3$", r"$y = x^2 + 6x + 10$", r"$y = -x^2 + 2x + 1$"], "D",
      r"Complete the square: A vertex $(-2, -3)$; B $(2, 1)$; C $(-1, -2)$; D $(-3, 1)$, which has $x < 0$ and $y > 0$; E $(1, 2)$. So D.", diff=1),

    Q("QUA-14", T, "MM1.3", r"The equation $x^2 - 2mx + m + 6 = 0$ has two distinct positive roots. Find the complete set of values of $m$.",
      [r"$m > 3$", r"$m < -2$ or $m > 3$", r"$m > -6$", r"$-6 < m < -2$", r"$m > 0$", r"$-2 < m < 3$"], "A",
      r"Distinct real roots: $4m^2 - 4(m + 6) > 0 \Rightarrow m^2 - m - 6 > 0 \Rightarrow (m-3)(m+2) > 0$, so $m < -2$ or $m > 3$. Both roots positive needs sum $2m > 0$ and product $m + 6 > 0$, so $m > 0$. Combined: $m > 3$.", diff=2),

    Q("QUA-15", T, "MM1.3", r"The graph of $y = x^2 + bx + c$ crosses the $x$-axis at $(1, 0)$ and $(5, 0)$. What is the $y$-coordinate of the vertex?",
      ["$-4$", "$-5$", "$-9$", "$5$", "$-3$", "$4$"], "A",
      r"$y = (x-1)(x-5)$, vertex at $x = 3$: $y = (2)(-2) = -4$.", diff=1),

    Q("QUA-16", T, "MM1.3", r"Given that $x^2 + y^2 = 10$ and $x + y = 4$, find the value of $xy$.",
      ["$3$", "$6$", "$4$", "$2$", "$5$", "$-3$"], "A",
      r"$(x+y)^2 = x^2 + y^2 + 2xy$, so $16 = 10 + 2xy$ and $xy = 3$.", diff=1),

    Q("QUA-17", T, "MM1.3", r"""The quadratic equation $ax^2 + bx + c = 0$ (with $a \neq 0$) has real coefficients. Which of the following statements is/are always true?

I. If $ac < 0$, the equation has two distinct real roots.
II. If $b = 0$, the equation has no real roots.
III. If the equation has a repeated root, then $b^2 = 4ac$.""", ROMAN3, "F",
      r"I: $b^2 - 4ac > 0$ whenever $ac < 0$, so true. II: $x^2 - 4 = 0$ has $b = 0$ and real roots, so false. III: a repeated root means the discriminant is zero, so true.", paper=2, tags=("roman",)),

    Q("QUA-18", T, "MM1.3", r"Find the range of values of $x$ for which $x^2 - 7x + 10 < 0$ and $x^2 - 4 > 0$.",
      [r"$2 < x < 5$", r"$-2 < x < 2$", r"$x > 5$", r"$2 < x < 5$ or $x < -2$", r"$x < -2$", r"no values"], "A",
      r"$(x-2)(x-5) < 0$ gives $2 < x < 5$; $x^2 > 4$ gives $x < -2$ or $x > 2$. The intersection is $2 < x < 5$.", diff=1),

    Q("QUA-19", T, "MM1.3", r"The expression $x^2 + 6x + c$ can be written as $(x + p)^2 + q$. Given that $q = -c$, find the value of $c$.",
      [r"$\dfrac{9}{2}$", "$9$", "$-9$", r"$-\dfrac{9}{2}$", "$3$", "$0$"], "A",
      r"$(x+3)^2 + (c - 9)$, so $q = c - 9 = -c$, giving $2c = 9$ and $c = \frac92$.", diff=1),

    Q("QUA-20", T, "MM1.3", r"For how many integer values of $k$ does $x^2 + kx + 12 = 0$ have integer roots?",
      ["$2$", "$3$", "$4$", "$6$", "$8$", "$12$"], "D",
      r"Integer roots $r, s$ with $rs = 12$: pairs $(1,12), (2,6), (3,4)$ and their negatives, giving $k = -(r+s) = -13, -8, -7, 13, 8, 7$: six values."),

    Q("QUA-21", T, "MM1.3", r"The parabola $y = x^2 - 4x + 3$ is reflected in the $x$-axis and then translated $2$ units in the positive $y$-direction. What is the maximum value of the resulting function?",
      ["$1$", "$2$", "$3$", "$-1$", "$-3$", "$5$"], "C",
      r"$x^2 - 4x + 3 = (x-2)^2 - 1$, minimum $-1$. Reflecting gives maximum $1$; translating up by $2$ gives maximum $3$.", diff=1),

    Q("QUA-22", T, "MM1.3", r"The equation $x^2 + ax + b = 0$ has roots $3$ and $-5$. The equation $x^2 + bx + a = 0$ has roots $p$ and $q$. Find $p^2 + q^2$.",
      ["$229$", "$221$", "$225$", "$255$", "$195$", "$4$"], "B",
      r"Sum of roots $3 + (-5) = -a$, so $a = 2$; product $-15 = b$. Then $x^2 - 15x + 2 = 0$ has $p + q = 15$ and $pq = 2$, so $p^2 + q^2 = 15^2 - 2(2) = 221$.", diff=2),

    Q("QUA-23", T, "MM1.3", r"The line $y = mx$ meets the curve $y = x^2 + 9$ at two distinct points. Find the complete set of values of $m$.",
      [r"$m < -6$ or $m > 6$", r"$-6 < m < 6$", r"$m > 6$", r"$m < -3$ or $m > 3$", r"$-3 < m < 3$", r"all real $m$"], "A",
      r"$x^2 - mx + 9 = 0$ needs $m^2 - 36 > 0$, so $m < -6$ or $m > 6$.", diff=1),

    Q("QUA-24", T, "MM1.3", r"Let $f(x) = x^2 - 2x - 8$. For how many integers $n$ is $f(n) < 0$?",
      ["$4$", "$5$", "$6$", "$3$", "$7$", "$8$"], "B",
      r"$(x-4)(x+2) < 0$ gives $-2 < x < 4$; the integers are $-1, 0, 1, 2, 3$: five of them.", diff=1),
]
