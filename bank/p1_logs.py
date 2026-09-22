"""Exponentials and logarithms (MM5.1-MM5.3)."""
from gen.model import Q, ROMAN3

T = "exp-logs"

QUESTIONS = [
    Q("LOG-01", T, "MM5.2", r"Find the value of $\log_2 40 - \log_2 5 + \log_2 \dfrac{1}{4}$.",
      ["$1$", "$2$", "$3$", "$5$", "$-1$", "$0$"], "A",
      r"$\log_2\left(\frac{40}{5}\cdot\frac14\right) = \log_2 2 = 1$.", diff=1),

    Q("LOG-02", T, "MM5.3", r"Solve $3^{2x} = 4$. Give $x$ in terms of logarithms to base $3$.",
      [r"$x = \log_3 2$", r"$x = \dfrac{1}{2}\log_3 2$", r"$x = 2\log_3 2$", r"$x = \log_3 4 - 2$", r"$x = \dfrac{\log_3 4}{4}$", r"$x = \log_2 3$"], "A",
      r"$2x = \log_3 4 = 2\log_3 2$, so $x = \log_3 2$.", diff=1),

    Q("LOG-03", T, "MM5.3", r"Solve $2^{2x} - 3\cdot 2^{x+2} + 32 = 0$. Find the sum of the solutions.",
      ["$5$", "$4$", "$6$", "$3$", "$12$", "$8$"], "A",
      r"Let $y = 2^x$: $y^2 - 12y + 32 = (y - 4)(y - 8) = 0$, so $2^x = 4$ or $8$: $x = 2$ or $3$. Sum $5$.", diff=1),

    Q("LOG-04", T, "MM5.2", r"Given that $\log_a x = 3$ and $\log_a y = 5$, find $\log_a \left(\dfrac{x^2 \sqrt{y}}{a}\right)$.",
      [r"$\dfrac{15}{2}$", r"$\dfrac{17}{2}$", r"$\dfrac{13}{2}$", r"$8$", r"$\dfrac{11}{2}$", r"$10$"], "A",
      r"$2\log_a x + \frac12\log_a y - \log_a a = 6 + \frac52 - 1 = \frac{15}{2}$.", diff=1),

    Q("LOG-05", T, "MM5.2", r"Solve $\log_3(x + 6) + \log_3(x - 2) = 2$.",
      ["$x = 3$", "$x = -7$ or $x = 3$", "$x = 3$ or $x = 7$", "$x = -3$", "$x = 5$", "$x = 1$"], "A",
      r"$(x+6)(x-2) = 9 \Rightarrow x^2 + 4x - 21 = 0 \Rightarrow (x+7)(x-3) = 0$. $x = -7$ makes both logs undefined, so $x = 3$ only.", diff=1),

    Q("LOG-06", T, "MM5.1", r"The graph of $y = 2^{x}$ is translated $3$ units in the positive $x$-direction. The resulting graph has equation",
      [r"$y = \dfrac{1}{8}\cdot 2^{x}$", r"$y = 8\cdot 2^{x}$", r"$y = 2^{x} - 3$", r"$y = 2^{x} + 3$", r"$y = 2^{3x}$", r"$y = 2^{x/3}$"], "A",
      r"$y = 2^{x - 3} = 2^{-3}\cdot 2^x = \frac18 \cdot 2^x$. (A translation of an exponential is also a stretch.)", diff=2),

    Q("LOG-07", T, "MM5.2", r"""Which of the following statements is/are true for all positive real $x$ and $y$?

I. $\log_{10}(x + y) = \log_{10} x + \log_{10} y$
II. $\log_{10}(xy)^2 = 2\log_{10} x + 2\log_{10} y$
III. $\log_{10} x - \log_{10} y = \log_{10} x \div \log_{10} y$""", ROMAN3, "C",
      r"II is correct: $\log(xy)^2 = 2\log(xy) = 2\log x + 2\log y$. I and III confuse the laws: $\log$ of a sum has no simple form, and a difference of logs is $\log$ of a quotient, not a quotient of logs.", paper=2, tags=("roman",), diff=1),

    Q("LOG-08", T, "MM5.3", r"Given that $5^{x} = 2$ and $2^{y} = 125$, find the value of $xy$.",
      ["$3$", "$1$", "$5$", "$6$", r"$\log_5 2 \cdot \log_2 125$", "$2$"], "A",
      r"$5^{xy} = (5^x)^y = 2^y = 125 = 5^3$, so $xy = 3$.", diff=2),

    Q("LOG-09", T, "MM5.2", r"Find the value of $\dfrac{\log_5 27}{\log_5 3}$.",
      ["$3$", "$9$", r"$\log_5 24$", r"$\log_5 9$", "$24$", r"$\dfrac{27}{3}$"], "A",
      r"$\log_5 27 = \log_5 3^3 = 3\log_5 3$, so the quotient is $3$.", diff=1),

    Q("LOG-10", T, "MM5.3", r"How many real solutions does the equation $4^{x} + 2^{x+1} - 8 = 0$ have?",
      ["$1$", "$2$", "$0$", "$3$", "infinitely many"], "A",
      r"$y = 2^x$: $y^2 + 2y - 8 = (y + 4)(y - 2) = 0$. $y = -4$ is impossible, $y = 2$ gives $x = 1$. One solution.", diff=1),

    Q("LOG-11", T, "MM5.2", r"Solve $\log_2 x + \log_4 x = 6$. (You may use $\log_4 x = \dfrac{1}{2}\log_2 x$.)",
      ["$x = 16$", "$x = 8$", "$x = 64$", "$x = 4$", "$x = 32$", "$x = 2^{6}$"], "A",
      r"$\frac32\log_2 x = 6 \Rightarrow \log_2 x = 4 \Rightarrow x = 16$.", diff=1),

    Q("LOG-12", T, "MM5.1", r"The curve $y = a^{x}$ passes through $(2, 12)$ and $(4, 108)$. Find $a$.",
      ["$3$", "$2$", "$6$", "$9$", r"$\sqrt{12}$", "$4$"], "A",
      r"$\frac{a^4}{a^2} = a^2 = \frac{108}{12} = 9$, so $a = 3$ (as $a > 0$).", diff=1),

    Q("LOG-13", T, "MM5.2", r"Given that $\log_{10} 2 = p$ and $\log_{10} 3 = q$, express $\log_{10} 0.75$ in terms of $p$ and $q$.",
      [r"$q - 2p$", r"$q + 2p$", r"$2p - q$", r"$q - p$", r"$\dfrac{q}{2p}$", r"$3q - 4p$"], "A",
      r"$0.75 = \frac34$, so $\log 0.75 = \log 3 - \log 4 = q - 2p$.", diff=1),

    Q("LOG-14", T, "MM5.3", r"The number of integers $n$ satisfying $2^{n} < 1000 < 2^{n+3}$ is",
      ["$3$", "$2$", "$1$", "$4$", "$0$", "$10$"], "A",
      r"$2^9 = 512 < 1000 < 1024 = 2^{10}$. Need $n \leq 9$ and $n + 3 \geq 10$, so $n = 7, 8, 9$: three integers.", diff=2),

    Q("LOG-15", T, "MM5.2", r"Solve $\log_2 (x^2 - 4) - \log_2 (x - 2) = 3$.",
      ["$x = 6$", "$x = 10$", "$x = -10$ or $x = 6$", "$x = 2$", "$x = 8$", "$x = 4$"], "A",
      r"For $x > 2$: $\log_2\frac{(x-2)(x+2)}{x-2} = \log_2(x + 2) = 3 \Rightarrow x + 2 = 8 \Rightarrow x = 6$.", diff=1),

    Q("LOG-16", T, "MM5.1", r"""For which of the following values of $x$ is $3^{x} < 2^{x+1}$?

I. $x = 0$
II. $x = 1$
III. $x = 2$""", ROMAN3, "E",
      r"$x = 0$: $1 < 2$ true. $x = 1$: $3 < 4$ true. $x = 2$: $9 < 8$ false. So I and II.", paper=2, tags=("roman",), diff=1),

    Q("LOG-17", T, "MM5.3", r"The equation $9^{x} - k\cdot 3^{x} + 9 = 0$ has exactly one real solution. Find the value of $k$.",
      ["$6$", "$-6$", r"$\pm 6$", "$3$", "$9$", "$0$"], "A",
      r"With $y = 3^x > 0$: $y^2 - ky + 9 = 0$. Exactly one solution for $x$ means exactly one positive root: a repeated root ($k^2 = 36$, product $9 > 0$ so the roots have the sign of $k$): $k = 6$ (repeated root $y = 3$, $x = 1$). $k = -6$ gives $y = -3$, no solutions. (Two distinct positive roots would give two solutions.)", diff=2),

    Q("LOG-18", T, "MM5.2", r"If $\log_a b = 2$ and $\log_b c = 3$, find $\log_a c$.",
      ["$6$", "$5$", r"$\dfrac{3}{2}$", r"$\dfrac{2}{3}$", "$8$", "$9$"], "A",
      r"$b = a^2$ and $c = b^3 = a^6$, so $\log_a c = 6$.", diff=1),

    Q("LOG-19", T, "MM5.3", r"A quantity halves every $5$ hours. Which expression gives the number of hours for it to fall to $\dfrac{1}{10}$ of its initial value?",
      [r"$5\log_{10} 2$", r"$5\log_2 5$", r"$\dfrac{5}{\log_{10} 2}$", r"$50\log_{10} 2$", r"$\dfrac{\log_{10} 2}{5}$", r"$25$"], "C",
      r"$\left(\frac12\right)^{t/5} = \frac{1}{10}$. Taking logs to base $10$: $-\frac t5 \log_{10} 2 = -1$, so $t = \dfrac{5}{\log_{10} 2}$ (about $16.6$ hours).", diff=2),
]
