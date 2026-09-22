"""Indices and surds (MM1.1, MM1.2, M2.7, M2.11, M2.12)."""
from gen.model import Q, ROMAN3

T = "indices-surds"

QUESTIONS = [
    Q("IND-01", T, "MM1.1", r"Simplify $\dfrac{(2x^3)^4 \times 8x^{-5}}{4x^2}$.",
      [r"$x^{5}$", r"$4x^{5}$", r"$16x^{5}$", r"$32x^{5}$", r"$32x^{9}$", r"$16x^{7}$"], "D",
      r"$(2x^3)^4 = 16x^{12}$, so the numerator is $16x^{12}\times 8x^{-5} = 128x^{7}$. Dividing by $4x^2$ gives $32x^{5}$.", diff=1),

    Q("IND-02", T, "MM1.1", r"Find the value of $\left(\dfrac{27}{8}\right)^{-\frac{2}{3}}$.",
      [r"$\dfrac{9}{4}$", r"$\dfrac{4}{9}$", r"$\dfrac{2}{3}$", r"$-\dfrac{9}{4}$", r"$\dfrac{3}{2}$", r"$-\dfrac{4}{9}$"], "B",
      r"The negative index inverts the fraction: $\left(\frac{8}{27}\right)^{2/3}$. Cube root first: $\left(\frac{2}{3}\right)^2 = \frac{4}{9}$.", diff=1),

    Q("IND-03", T, "MM1.1", r"Solve $4^{x+1} = 8^{2x-3}$.",
      [r"$x = \dfrac{5}{4}$", r"$x = \dfrac{11}{4}$", r"$x = 2$", r"$x = \dfrac{7}{2}$", r"$x = \dfrac{9}{4}$", r"$x = 4$"], "B",
      r"Write both sides as powers of 2: $2^{2x+2} = 2^{6x-9}$. So $2x + 2 = 6x - 9$, giving $4x = 11$ and $x = \frac{11}{4}$.", diff=1),

    Q("IND-04", T, "MM1.2", r"Express $\dfrac{5}{3+2\sqrt{5}}$ in the form $a + b\sqrt{5}$ where $a$ and $b$ are rational.",
      [r"$\dfrac{15 - 10\sqrt{5}}{11}$", r"$\dfrac{-15 + 10\sqrt{5}}{11}$", r"$\dfrac{15 + 10\sqrt{5}}{29}$", r"$\dfrac{-15 + 10\sqrt{5}}{29}$", r"$-15 + 10\sqrt{5}$", r"$15 - 10\sqrt{5}$"], "B",
      r"Multiply top and bottom by $3 - 2\sqrt{5}$: denominator $9 - 20 = -11$, numerator $15 - 10\sqrt{5}$. So the value is $\dfrac{15-10\sqrt{5}}{-11} = \dfrac{-15+10\sqrt{5}}{11}$.", diff=1),

    Q("IND-05", T, "MM1.2", r"Simplify $\sqrt{75} - \sqrt{27} + \sqrt{12}$.",
      [r"$2\sqrt{3}$", r"$4\sqrt{3}$", r"$5\sqrt{3}$", r"$\sqrt{60}$", r"$6\sqrt{3}$", r"$10\sqrt{3}$"], "B",
      r"$\sqrt{75} = 5\sqrt{3}$, $\sqrt{27} = 3\sqrt{3}$, $\sqrt{12} = 2\sqrt{3}$, so the total is $(5 - 3 + 2)\sqrt{3} = 4\sqrt{3}$.", diff=1),

    Q("IND-06", T, "MM1.2", r"Given that $(2 + \sqrt{3})^2 = a + b\sqrt{3}$ and $(2+\sqrt{3})^{-1} = c + d\sqrt{3}$, where $a$, $b$, $c$, $d$ are integers, find the value of $a + b + c + d$.",
      ["$8$", "$10$", "$12$", "$14$", "$6$", "$4$"], "C",
      r"$(2+\sqrt3)^2 = 7 + 4\sqrt3$, so $a = 7$, $b = 4$. $(2+\sqrt3)^{-1} = \dfrac{2-\sqrt3}{4-3} = 2 - \sqrt3$, so $c = 2$, $d = -1$. Sum $= 7 + 4 + 2 - 1 = 12$."),

    Q("IND-07", T, "MM1.1", r"Which of the following is equal to $\dfrac{x^2 \sqrt{x}}{\sqrt[3]{x}}$ for $x > 0$?",
      [r"$x^{\frac{7}{3}}$", r"$x^{\frac{13}{6}}$", r"$x^{\frac{11}{6}}$", r"$x^{\frac{5}{2}}$", r"$x^{\frac{17}{6}}$", r"$x^{3}$"], "B",
      r"The index is $2 + \frac12 - \frac13 = \frac{12 + 3 - 2}{6} = \frac{13}{6}$."),

    Q("IND-08", T, "MM1.1", r"Solve $9^{x} - 4\times 3^{x} + 3 = 0$.",
      [r"$x = 1$ only", r"$x = 0$ or $x = 1$", r"$x = 1$ or $x = 3$", r"$x = 0$ only", r"$x = -1$ or $x = 0$", r"$x = \log_3 4$"], "B",
      r"Let $y = 3^x$: $y^2 - 4y + 3 = (y-1)(y-3) = 0$, so $3^x = 1$ or $3^x = 3$, giving $x = 0$ or $x = 1$.", diff=1),

    Q("IND-09", T, "MM1.2", r"Find the value of $\dfrac{1}{\sqrt{2}+1} + \dfrac{1}{\sqrt{3}+\sqrt{2}} + \dfrac{1}{2+\sqrt{3}}$.",
      ["$1$", "$2$", r"$\sqrt{2}$", r"$\sqrt{3}$", r"$2 - \sqrt{3}$", r"$\sqrt{3} + 1$"], "A",
      r"Rationalising each term gives $(\sqrt2 - 1) + (\sqrt3 - \sqrt2) + (2 - \sqrt3)$, which telescopes to $1$.", diff=2),

    Q("IND-10", T, "MM1.1", r"The value of $\dfrac{2^{n+2} + 2^{n}}{2^{n+1}}$ is",
      ["$2$", r"$\dfrac{3}{2}$", r"$\dfrac{5}{2}$", "$3$", "$5$", r"$2^{n}$"], "C",
      r"Factor $2^n$: numerator $= 2^n(4 + 1) = 5\cdot 2^n$; denominator $= 2\cdot 2^n$. Quotient $= \frac52$.", diff=1),

    Q("IND-11", T, "MM1.2", r"Given that $x = \sqrt{7} + \sqrt{3}$ and $y = \sqrt{7} - \sqrt{3}$, find $x^2 + y^2 - xy$.",
      ["$16$", "$20$", "$24$", "$12$", r"$20 - 2\sqrt{21}$", "$4$"], "A",
      r"$x^2 + y^2 = (10 + 2\sqrt{21}) + (10 - 2\sqrt{21}) = 20$ and $xy = 7 - 3 = 4$. So $20 - 4 = 16$."),

    Q("IND-12", T, "MM1.1", r"For how many integer values of $n$ with $1 \leq n \leq 100$ is $\sqrt{n} + \sqrt{n+1}$ rational?",
      ["$0$", "$1$", "$2$", "$9$", "$10$", "$100$"], "A",
      r"For the sum to be rational, both $\sqrt n$ and $\sqrt{n+1}$ would need to be rational (if one is irrational, $\sqrt n + \sqrt{n+1}$ squared gives $2n + 1 + 2\sqrt{n(n+1)}$ and $n(n+1)$ is never a perfect square for $n \geq 1$ since $n^2 < n(n+1) < (n+1)^2$). No two consecutive positive integers are both squares, so the answer is $0$.", paper=2, diff=3),

    Q("IND-13", T, "MM1.1", r"Simplify $\left(\dfrac{a^{\frac{1}{2}} b^{-2}}{a^{-1} b^{\frac{1}{2}}}\right)^{4}$.",
      [r"$a^{6}b^{-10}$", r"$a^{2}b^{-6}$", r"$a^{6}b^{-6}$", r"$a^{-2}b^{10}$", r"$a^{6}b^{10}$", r"$a^{2}b^{-10}$"], "A",
      r"Inside the bracket: $a^{\frac12 + 1} b^{-2 - \frac12} = a^{\frac32} b^{-\frac52}$. Raise to the 4th power: $a^{6} b^{-10}$.", diff=1),

    Q("IND-14", T, "MM1.2", r"The number $\dfrac{\sqrt{50} + \sqrt{18}}{\sqrt{8}}$ is equal to",
      ["$4$", r"$2\sqrt{2}$", r"$\dfrac{8}{\sqrt 2}$", r"$\sqrt{34}$", r"$4\sqrt{2}$", "$8$"], "A",
      r"$\sqrt{50} = 5\sqrt2$, $\sqrt{18} = 3\sqrt2$, $\sqrt8 = 2\sqrt2$. So $\dfrac{8\sqrt2}{2\sqrt2} = 4$.", diff=1),

    Q("IND-15", T, "MM1.1", r"Given that $2^{x} = 5$ and $2^{y} = 20$, find the value of $2^{2x - y}$.",
      [r"$\dfrac{5}{4}$", r"$\dfrac{4}{5}$", r"$\dfrac{1}{4}$", "$5$", "$-10$", r"$\dfrac{25}{2}$"], "A",
      r"$2^{2x - y} = \dfrac{(2^x)^2}{2^y} = \dfrac{25}{20} = \dfrac54$.", diff=1),

    Q("IND-16", T, "MM1.2", r"""Which of the following statements is/are true for all positive real numbers $a$ and $b$?

I. $\sqrt{a} \sqrt{b} = \sqrt{ab}$
II. $\sqrt{a + b} = \sqrt{a} + \sqrt{b}$
III. $\sqrt{a^2 + b^2} < a + b$""", ROMAN3, "F",
      r"I is a law of surds. II fails for $a = b = 1$: $\sqrt2 \neq 2$. III: $(a+b)^2 = a^2 + b^2 + 2ab > a^2 + b^2$ since $ab > 0$, and both sides are positive, so III is true.", paper=2, tags=("roman",)),

    Q("IND-17", T, "MM1.1", r"Solve $x^{\frac{3}{2}} = 8x^{-\frac{3}{2}}$ for $x > 0$.",
      ["$x = 2$", "$x = 4$", r"$x = \sqrt{2}$", "$x = 8$", r"$x = 2\sqrt{2}$", "$x = 16$"], "A",
      r"Multiply by $x^{3/2}$: $x^3 = 8$, so $x = 2$.", diff=1),

    Q("IND-18", T, "MM1.2", r"The expression $\dfrac{3}{7 - 2\sqrt{3}} - \dfrac{3}{7 + 2\sqrt{3}}$ simplifies to",
      [r"$\dfrac{12\sqrt{3}}{37}$", r"$\dfrac{42}{37}$", r"$\dfrac{12\sqrt{3}}{61}$", r"$\dfrac{6\sqrt{3}}{37}$", r"$\dfrac{42}{61}$", r"$0$"], "A",
      r"Common denominator $(7-2\sqrt3)(7+2\sqrt3) = 49 - 12 = 37$. Numerator: $3(7 + 2\sqrt3) - 3(7 - 2\sqrt3) = 12\sqrt3$."),

    Q("IND-19", T, "MM1.1", r"How many real solutions does the equation $2^{x^2} = 16 \times 2^{-3x}$ have?",
      ["$0$", "$1$", "$2$", "$3$", "$4$", "infinitely many"], "C",
      r"$2^{x^2} = 2^{4 - 3x}$, so $x^2 + 3x - 4 = 0$, i.e. $(x+4)(x-1) = 0$: two real solutions.", diff=1),

    Q("IND-20", T, "MM1.2", r"Given that $\sqrt{a} - \sqrt{b} = 2$ and $a - b = 12$, find $\sqrt{a} + \sqrt{b}$.",
      ["$3$", "$4$", "$6$", "$8$", "$10$", "$24$"], "C",
      r"$a - b = (\sqrt a - \sqrt b)(\sqrt a + \sqrt b)$, so $12 = 2(\sqrt a + \sqrt b)$, giving $6$.", diff=1),

    Q("IND-21", T, "MM1.1", r"If $x = 2^{p}$, $y = 2^{q}$ and $\dfrac{x^{3}}{y^{2}} = 2^{5}$ with $xy = 2^{10}$, find $p$.",
      ["$3$", "$4$", "$5$", "$6$", "$7$", "$8$"], "C",
      r"$3p - 2q = 5$ and $p + q = 10$. From the second, $q = 10 - p$; then $3p - 20 + 2p = 5$, so $5p = 25$ and $p = 5$.", diff=1),

    Q("IND-22", T, "MM1.2", r"Which one of the following is the largest?",
      [r"$\sqrt{2} + \sqrt{7}$", r"$\sqrt{3} + \sqrt{6}$", r"$\sqrt{4} + \sqrt{5}$", r"$\sqrt{1} + \sqrt{8}$", r"$2\sqrt{4.5}$"], "E",
      r"Each option is $\sqrt a + \sqrt b$ with $a + b = 9$. Squaring gives $9 + 2\sqrt{ab}$, which is largest when the product $ab$ is largest, "
      r"i.e. when $a$ and $b$ are as close as possible. Option E has $a = b = 4.5$ (product $20.25$), beating $4 \times 5 = 20$ for option C. "
      r"Numerically: E $= \sqrt{18} \approx 4.243$, C $= 2 + \sqrt5 \approx 4.236$.", diff=2),
]
