"""GCSE algebra (M4.1-M4.8, M4.18, M4.19)."""
from gen.model import Q, ROMAN3

T = "gcse-algebra"

QUESTIONS = [
    Q("ALG-01", T, "M4.7", r"Make $x$ the subject of $y = \dfrac{2x + 3}{x - 1}$.",
      [r"$x = \dfrac{y + 3}{y - 2}$", r"$x = \dfrac{y - 3}{y + 2}$", r"$x = \dfrac{y + 3}{2 - y}$", r"$x = \dfrac{3 - y}{y - 2}$", r"$x = \dfrac{2y + 3}{y - 1}$", r"$x = \dfrac{y - 2}{y + 3}$"], "A",
      r"$y(x - 1) = 2x + 3 \Rightarrow xy - 2x = y + 3 \Rightarrow x(y - 2) = y + 3 \Rightarrow x = \dfrac{y + 3}{y - 2}$.", diff=1),

    Q("ALG-02", T, "M4.19", r"Find the $n$th term of the quadratic sequence $3, 8, 15, 24, 35, \ldots$",
      [r"$n^2 + 2n$", r"$n^2 + 2$", r"$2n^2 + 1$", r"$n^2 + 3n - 1$", r"$(n + 1)^2 + 1$", r"$n^2 + n + 1$"], "A",
      r"Second differences are $2$, so the $n$th term is $n^2 + bn + c$: $n = 1$ gives $1 + b + c = 3$ and $n = 2$ gives $4 + 2b + c = 8$. Subtracting, $3 + b = 5$, so $b = 2$ and $c = 0$: $n^2 + 2n = n(n + 2)$.", diff=1),

    Q("ALG-03", T, "M4.6", r"Simplify $\dfrac{x^2 - 9}{x^2 + x - 12} \times \dfrac{x^2 - 16}{x^2 - 3x}$.",
      [r"$\dfrac{(x + 3)(x - 4)}{x(x - 3)}$", r"$\dfrac{x - 4}{x}$", r"$\dfrac{(x+3)(x+4)}{x(x-3)}$", r"$\dfrac{x + 3}{x}$", r"$\dfrac{(x - 3)(x - 4)}{x(x + 3)}$", r"$\dfrac{x - 4}{x - 3}$"], "A",
      r"Factorise everything: $\dfrac{(x-3)(x+3)}{(x+4)(x-3)} \times \dfrac{(x-4)(x+4)}{x(x-3)}$. The $(x+4)$ factors cancel and one $(x-3)$ cancels, leaving $\dfrac{(x+3)(x-4)}{x(x-3)}$.", diff=2),

    Q("ALG-04", T, "M4.8", r"Which of the following is an identity (true for all values of $x$)?",
      [r"$(x + 3)^2 - (x - 3)^2 = 12x$", r"$(x + 3)^2 = x^2 + 9$", r"$(x + 3)(x - 3) = x^2 + 9$", r"$x^2 + 6x + 9 = 0$", r"$(x - 3)^2 = x^2 - 6x - 9$"], "A",
      r"$(x+3)^2 - (x-3)^2 = (x^2 + 6x + 9) - (x^2 - 6x + 9) = 12x$ for all $x$.", diff=1),

    Q("ALG-05", T, "M4.18", r"A car accelerates uniformly from rest to $20$ m/s in $8$ seconds, travels at $20$ m/s for $12$ seconds, then decelerates uniformly to rest in $10$ seconds. Find the total distance travelled.",
      ["$420$ m", "$600$ m", "$300$ m", "$380$ m", "$480$ m", "$400$ m"], "A",
      r"Area under the speed-time graph: $\frac12\cdot8\cdot20 + 12\cdot20 + \frac12\cdot10\cdot20 = 80 + 240 + 100 = 420$ m.", diff=1),

    Q("ALG-06", T, "M4.3", r"Given that $v^2 = u^2 + 2as$, find $s$ when $v = 13$, $u = 5$ and $a = 4$.",
      ["$18$", "$21$", "$12$", "$36$", "$9$", "$24$"], "A",
      r"$169 = 25 + 8s \Rightarrow s = 18$.", diff=1),

    Q("ALG-07", T, "M4.6", r"Simplify $\dfrac{3}{x + 2} - \dfrac{2}{x - 1}$.",
      [r"$\dfrac{x - 7}{(x + 2)(x - 1)}$", r"$\dfrac{x + 1}{(x + 2)(x - 1)}$", r"$\dfrac{1}{x + 3}$", r"$\dfrac{5x - 1}{(x + 2)(x - 1)}$", r"$\dfrac{x - 1}{(x + 2)(x - 1)}$", r"$\dfrac{1}{(x + 2)(x - 1)}$"], "A",
      r"$\dfrac{3(x - 1) - 2(x + 2)}{(x + 2)(x - 1)} = \dfrac{x - 7}{(x + 2)(x - 1)}$.", diff=1),

    Q("ALG-08", T, "M4.19", r"""The $n$th term of a sequence is $\dfrac{n^2 + 1}{2n}$. Which of the following statements is/are true?

I. The $5$th term is $2.6$.
II. Every term after the first is greater than the previous term.
III. Some term of the sequence equals $10$.""", ROMAN3, "E",
      r"I: $\frac{26}{10} = 2.6$. II: $u_n = \frac n2 + \frac{1}{2n}$; $u_1 = 1$, $u_2 = 1.25$, and for $n \geq 1$ the increase $\frac12 - \frac{1}{2n(n+1)} > 0$, so increasing. III: $n^2 - 20n + 1 = 0$ has no integer solutions (discriminant $396$ is not a square), so false.", paper=2, tags=("roman",), diff=2),

    Q("ALG-09", T, "M4.7", r"Given that $T = 2\pi\sqrt{\dfrac{l}{g}}$, express $l$ in terms of $T$ and $g$.",
      [r"$l = \dfrac{gT^2}{4\pi^2}$", r"$l = \dfrac{4\pi^2 g}{T^2}$", r"$l = \dfrac{T^2 g}{2\pi}$", r"$l = \dfrac{gT}{2\pi}$", r"$l = \dfrac{T^2}{4\pi^2 g}$", r"$l = 4\pi^2 g T^2$"], "A",
      r"$\frac{T}{2\pi} = \sqrt{\frac lg} \Rightarrow \frac{T^2}{4\pi^2} = \frac lg \Rightarrow l = \frac{gT^2}{4\pi^2}$.", diff=1),

    Q("ALG-10", T, "M4.18", r"A ball is thrown vertically upwards and its height after $t$ seconds is $h = 20t - 5t^2$ metres. For how long is the ball at least $15$ m above the ground?",
      ["$2$ s", "$1$ s", "$3$ s", "$4$ s", "$1.5$ s", "$0.5$ s"], "A",
      r"$20t - 5t^2 \geq 15 \Rightarrow t^2 - 4t + 3 \leq 0 \Rightarrow 1 \leq t \leq 3$: two seconds.", diff=1),

    Q("ALG-11", T, "M4.4", r"Expand and simplify $(x + 2)(x - 1)(x + 3)$.",
      [r"$x^3 + 4x^2 + x - 6$", r"$x^3 + 4x^2 - x - 6$", r"$x^3 + 2x^2 - 5x - 6$", r"$x^3 + 4x^2 + 7x - 6$", r"$x^3 - 4x^2 + x + 6$", r"$x^3 + 6x^2 + 11x + 6$"], "A",
      r"$(x^2 + x - 2)(x + 3) = x^3 + 3x^2 + x^2 + 3x - 2x - 6 = x^3 + 4x^2 + x - 6$.", diff=1),

    Q("ALG-12", T, "M4.19", r"A sequence has first term $2$ and each subsequent term is obtained by squaring the previous term and subtracting $2$. What is the $50$th term?",
      ["$2$", "$4$", "$-2$", "$0$", "$14$", "$2^{50}$"], "A",
      r"$2^2 - 2 = 2$: every term is $2$.", diff=1),

    Q("ALG-13", T, "M4.5", r"Factorise $6x^2 - 7x - 20$.",
      [r"$(3x + 4)(2x - 5)$", r"$(3x - 4)(2x + 5)$", r"$(6x + 5)(x - 4)$", r"$(3x - 5)(2x + 4)$", r"$(6x - 5)(x + 4)$", r"$(3x + 5)(2x - 4)$"], "A",
      r"$(3x + 4)(2x - 5) = 6x^2 - 15x + 8x - 20 = 6x^2 - 7x - 20$.", diff=1),

    Q("ALG-14", T, "M4.16", r"The sum of two numbers is $12$ and the difference of their squares is $48$. Find the larger number.",
      ["$8$", "$10$", "$7$", "$6$", "$9$", "$4$"], "A",
      r"$x^2 - y^2 = (x - y)(x + y) = 12(x - y) = 48 \Rightarrow x - y = 4$. So $x = 8$, $y = 4$.", diff=1),

    Q("ALG-15", T, "M4.18", r"The distance-time graph of a journey is a straight line from $(0, 0)$ to $(2, 60)$, then horizontal to $(3, 60)$, then a straight line to $(5, 0)$ (time in hours, distance from home in km). What was the average speed for the whole journey?",
      ["$24$ km/h", "$12$ km/h", "$30$ km/h", "$0$ km/h", "$20$ km/h", "$40$ km/h"], "A",
      r"Total distance $60 + 60 = 120$ km in $5$ hours: $24$ km/h. (Displacement is $0$ but distance travelled is not.)", diff=1),
]
