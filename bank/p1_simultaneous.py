"""Simultaneous equations and inequalities (MM1.4, MM1.5, M4.16, M4.17)."""
from gen.model import Q, ROMAN3

T = "simultaneous-inequalities"

QUESTIONS = [
    Q("SIM-01", T, "MM1.4", r"Solve the simultaneous equations $x + 2y = 7$ and $x^2 + y^2 = 10$. Find the sum of the possible values of $x$.",
      [r"$\dfrac{14}{5}$", r"$\dfrac{28}{5}$", r"$4$", r"$\dfrac{7}{5}$", r"$2$", r"$7$"], "A",
      r"$x = 7 - 2y$: $(7-2y)^2 + y^2 = 10 \Rightarrow 5y^2 - 28y + 39 = 0 \Rightarrow (5y - 13)(y - 3) = 0$. $y = 3 \Rightarrow x = 1$; $y = \frac{13}{5} \Rightarrow x = \frac{9}{5}$. Sum of $x$ values $= 1 + \frac95 = \frac{14}{5}$."),

    Q("SIM-02", T, "MM1.5", r"Find the complete set of values of $x$ for which $2x^2 - 5x - 3 \geq 0$.",
      [r"$x \leq -\dfrac{1}{2}$ or $x \geq 3$", r"$-\dfrac{1}{2} \leq x \leq 3$", r"$x \leq -3$ or $x \geq \dfrac{1}{2}$", r"$-3 \leq x \leq \dfrac12$", r"$x \geq 3$", r"$x \leq -\dfrac12$"], "A",
      r"$(2x+1)(x-3) \geq 0$: the roots are $-\frac12$ and $3$ and the parabola opens upwards, so $x \leq -\frac12$ or $x \geq 3$.", diff=1),

    Q("SIM-03", T, "MM1.5", r"Find the set of values of $x$ satisfying both $3x - 7 < 2$ and $x^2 > 4$.",
      [r"$x < -2$ or $2 < x < 3$", r"$2 < x < 3$", r"$x < -2$", r"$-2 < x < 3$", r"$x < 3$", r"$x > 2$"], "A",
      r"$3x < 9 \Rightarrow x < 3$. $x^2 > 4 \Rightarrow x < -2$ or $x > 2$. Combining: $x < -2$ or $2 < x < 3$.", diff=1),

    Q("SIM-04", T, "MM1.4", r"The line $y = x + k$ meets the circle $x^2 + y^2 = 8$ at exactly one point. Find the possible values of $k$.",
      [r"$k = \pm 4$", r"$k = \pm 2$", r"$k = \pm 2\sqrt{2}$", r"$k = \pm \sqrt{8}$", r"$k = \pm 8$", r"$k = 4$ only"], "A",
      r"$x^2 + (x+k)^2 = 8 \Rightarrow 2x^2 + 2kx + k^2 - 8 = 0$. Tangent when $4k^2 - 8(k^2 - 8) = 0 \Rightarrow -4k^2 + 64 = 0 \Rightarrow k = \pm 4$.", diff=1),

    Q("SIM-05", T, "MM1.5", r"For how many integers $n$ is $n^2 - 10n + 16 < 0$?",
      ["$4$", "$5$", "$6$", "$7$", "$8$", "$3$"], "B",
      r"$(n-2)(n-8) < 0 \Rightarrow 2 < n < 8$, so $n = 3, 4, 5, 6, 7$: five integers.", diff=1),

    Q("SIM-06", T, "MM1.4", r"Solve $xy = 6$ and $x - y = 1$. What is the sum of all possible values of $x + y$?",
      ["$0$", "$5$", "$-5$", "$1$", "$10$", "$7$"], "A",
      r"$x = y + 1$: $y^2 + y - 6 = 0 \Rightarrow (y+3)(y-2) = 0$. Solutions $(3, 2)$ with $x + y = 5$ and $(-2, -3)$ with $x + y = -5$. The sum is $0$.", diff=1),

    Q("SIM-07", T, "MM1.5", r"The inequality $x^2 + bx + 9 > 0$ holds for all real $x$. Find the complete set of values of $b$.",
      [r"$-6 < b < 6$", r"$b < -6$ or $b > 6$", r"$b > 6$", r"$-3 < b < 3$", r"$b \geq 6$", r"all real $b$"], "A",
      r"Need discriminant negative: $b^2 - 36 < 0$, so $-6 < b < 6$.", diff=1),

    Q("SIM-08", T, "MM1.5", r"Which of the following inequalities has exactly the same solution set as $\dfrac{1}{x} > 2$?",
      [r"$0 < x < \dfrac{1}{2}$", r"$x < \dfrac{1}{2}$", r"$x > \dfrac{1}{2}$", r"$x < 0$ or $x > \dfrac12$", r"$x > 2$", r"$0 < x < 2$"], "A",
      r"If $x > 0$: $1 > 2x$, so $0 < x < \frac12$. If $x < 0$: $\frac1x$ is negative and cannot exceed $2$. So $0 < x < \frac12$. (Multiplying by $x$ without considering its sign is the classic error.)", diff=2),

    Q("SIM-09", T, "MM1.4", r"The simultaneous equations $y = x^2 + 2x + c$ and $y = 4x + 1$ have exactly one solution. Find the value of $c$.",
      ["$2$", "$0$", "$1$", "$-2$", "$3$", "$-1$"], "A",
      r"$x^2 - 2x + (c - 1) = 0$ has one solution when $4 - 4(c-1) = 0$, so $c = 2$.", diff=1),

    Q("SIM-10", T, "MM1.5", r"Find the complete set of values of $x$ for which $(x-1)(x-3)(x-5) > 0$.",
      [r"$1 < x < 3$ or $x > 5$", r"$x > 5$", r"$x < 1$ or $3 < x < 5$", r"$x > 1$", r"$1 < x < 5$", r"$x < 1$ or $x > 5$"], "A",
      r"Sign chart: the product is positive for $x > 5$, negative for $3 < x < 5$, positive for $1 < x < 3$, negative for $x < 1$.", diff=2),

    Q("SIM-11", T, "MM1.5", r"""Given that $|2x - 3| < 5$, which of the following statements is/are true?

I. $-1 < x < 4$
II. $x^2 < 16$
III. $x > -1$""", ROMAN3, "H",
      r"$-5 < 2x - 3 < 5 \Rightarrow -1 < x < 4$, so I is true and III follows from I. For II: every $x$ in $(-1, 4)$ has $x^2 < 16$ (the largest possible $|x|$ is just under $4$), so II is also true.", paper=2, tags=("roman",)),

    Q("SIM-12", T, "MM1.4", r"The curves $y = x^2 - 4$ and $y = -x^2 + 2x + k$ intersect at exactly two points. Find the complete set of values of $k$.",
      [r"$k > -\dfrac{9}{2}$", r"$k < -\dfrac{9}{2}$", r"$k > -4$", r"$k > \dfrac{9}{2}$", r"$k \neq -\dfrac92$", r"all real $k$"], "A",
      r"$2x^2 - 2x - 4 - k = 0$: discriminant $4 + 8(4 + k) > 0 \Rightarrow 36 + 8k > 0 \Rightarrow k > -\frac92$.", diff=1),

    Q("SIM-13", T, "MM1.5", r"How many integers $x$ satisfy $x^2 < 5x + 24$ and $x^2 > 3x$?",
      ["$4$", "$5$", "$6$", "$7$", "$8$", "$9$"], "C",
      r"$x^2 - 5x - 24 < 0 \Rightarrow (x-8)(x+3) < 0 \Rightarrow -3 < x < 8$. $x(x-3) > 0 \Rightarrow x < 0$ or $x > 3$. Integers: $-2, -1$ and $4, 5, 6, 7$: six.", diff=2),

    Q("SIM-14", T, "MM1.4", r"Solve $2x + 3y = 12$ and $x^2 - y^2 = 0$. How many solutions $(x, y)$ are there?",
      ["$0$", "$1$", "$2$", "$3$", "$4$", "infinitely many"], "C",
      r"$x^2 = y^2$ means $y = x$ or $y = -x$. $y = x$: $5x = 12$, one solution. $y = -x$: $-x = 12$, one solution. Two in total.", diff=1),

    Q("SIM-15", T, "MM1.5", r"The solution set of $ax^2 + bx + c < 0$ (with $a > 0$) is $-2 < x < 5$. What is the solution set of $ax^2 - bx + c < 0$?",
      [r"$-5 < x < 2$", r"$-2 < x < 5$", r"$x < -5$ or $x > 2$", r"$x < -2$ or $x > 5$", r"$2 < x < 5$", r"$-5 < x < -2$"], "A",
      r"Replacing $x$ by $-x$ reflects the graph in the $y$-axis, so the roots $-2$ and $5$ become $2$ and $-5$: $-5 < x < 2$.", diff=2),

    Q("SIM-16", T, "MM1.5", r"Find the complete set of values of $x$ for which $\dfrac{x-2}{x+1} \leq 0$.",
      [r"$-1 < x \leq 2$", r"$-1 \leq x \leq 2$", r"$x \leq -1$ or $x \geq 2$", r"$x < -1$ or $x \geq 2$", r"$x \leq 2$", r"$-2 \leq x < 1$"], "A",
      r"A fraction is $\leq 0$ when numerator and denominator have opposite signs (or the numerator is 0): $x - 2 \leq 0$ and $x + 1 > 0$ gives $-1 < x \leq 2$; $x - 2 \geq 0$ and $x + 1 < 0$ is impossible. $x = -1$ is excluded as the fraction is undefined.", diff=2),

    Q("SIM-17", T, "MM1.4", r"Two numbers have sum $10$ and the sum of their squares is $58$. What is the positive difference between them?",
      ["$2$", "$4$", "$6$", "$8$", "$3$", "$1$"], "B",
      r"$(x - y)^2 = 2(x^2 + y^2) - (x+y)^2 = 116 - 100 = 16$, so the difference is $4$ (the numbers are $3$ and $7$).", diff=1),

    Q("SIM-18", T, "MM1.5", r"Consider the statement: for all real $x$, if $x > 2$ then $x^2 - 3x + 2 > 0$. Which of the following is true?",
      ["The statement is true, and so is its converse.", "The statement is true, but its converse is false.", "The statement is false, but its converse is true.", "The statement and its converse are both false."], "B",
      r"$x^2 - 3x + 2 = (x-1)(x-2) > 0$ exactly when $x < 1$ or $x > 2$. So $x > 2$ does imply it (true), but the converse fails, e.g. $x = 0$ gives $2 > 0$ without $x > 2$.", paper=2, tags=("logic",)),
]
