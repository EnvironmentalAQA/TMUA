"""Number, units and estimation (M1.1, M1.2, M2.1-M2.14)."""
from gen.model import Q, ROMAN3

T = "number"

QUESTIONS = [
    Q("NUM-01", T, "M2.3", r"Find the highest common factor of $2^{3}\times 3^{2}\times 5$ and $2^{2}\times 3^{3}\times 7$.",
      ["$36$", "$12$", "$72$", "$18$", "$108$", "$6$"], "A",
      r"Take the lower power of each common prime: $2^2 \times 3^2 = 36$.", diff=1),

    Q("NUM-02", T, "M2.3", r"The lowest common multiple of $12$, $18$ and $n$ is $180$. Which of the following could be $n$?",
      ["$20$", "$24$", "$8$", "$50$", "$27$", "$40$"], "A",
      r"$\text{lcm}(12, 18) = 36 = 2^2\cdot3^2$ and $180 = 2^2\cdot3^2\cdot5$, so $n$ must be a divisor of $180$ that is a multiple of $5$. Only $20$ qualifies: $24$, $8$ and $27$ have no factor $5$, and $50$ and $40$ do not divide $180$.", diff=2),

    Q("NUM-03", T, "M2.9", r"Express the recurring decimal $0.\dot{2}\dot{7}$ as a fraction in its lowest terms.",
      [r"$\dfrac{3}{11}$", r"$\dfrac{27}{100}$", r"$\dfrac{27}{99}$", r"$\dfrac{5}{18}$", r"$\dfrac{3}{10}$", r"$\dfrac{9}{33}$"], "A",
      r"$x = 0.2727\ldots$, $100x = 27.2727\ldots$, so $99x = 27$ and $x = \frac{27}{99} = \frac{3}{11}$.", diff=1),

    Q("NUM-04", T, "M2.13", r"A length is given as $4.6$ cm correct to $1$ decimal place, and a width as $3$ cm correct to the nearest cm. Find the upper bound of the area.",
      [r"$16.275$ cm$^2$", r"$13.8$ cm$^2$", r"$16.1$ cm$^2$", r"$14.375$ cm$^2$", r"$11.375$ cm$^2$", r"$16.45$ cm$^2$"], "A",
      r"Upper bounds $4.65$ and $3.5$: $4.65 \times 3.5 = 16.275$.", diff=1),

    Q("NUM-05", T, "M2.8", r"Evaluate $\dfrac{(3 \times 10^{4}) \times (8 \times 10^{-2})}{6 \times 10^{-3}}$, giving your answer in standard form.",
      [r"$4 \times 10^{5}$", r"$4 \times 10^{4}$", r"$4 \times 10^{6}$", r"$2.4 \times 10^{5}$", r"$4 \times 10^{-1}$", r"$1.5 \times 10^{5}$"], "A",
      r"$\frac{24 \times 10^{2}}{6 \times 10^{-3}} = 4 \times 10^{5}$.", diff=1),

    Q("NUM-06", T, "M2.5", r"A code consists of two letters from A, B, C, D, E followed by two digits from $1$ to $9$. Letters may be repeated but the two digits must be different. How many codes are possible?",
      ["$1800$", "$2025$", "$1620$", "$1440$", "$900$", "$3240$"], "A",
      r"$5 \times 5 \times 9 \times 8 = 1800$.", diff=1),

    Q("NUM-07", T, "M1.2", r"A car travels at $90$ km/h. What is this speed in metres per second?",
      ["$25$ m/s", "$15$ m/s", "$30$ m/s", "$324$ m/s", "$1.5$ m/s", "$54$ m/s"], "A",
      r"$90\,000$ m in $3600$ s: $90000/3600 = 25$ m/s.", diff=1),

    Q("NUM-08", T, "M2.14", r"Estimate the value of $\dfrac{4.92 \times \sqrt{99.3}}{0.198}$ by rounding each number to $1$ significant figure.",
      ["$250$", "$25$", "$2500$", "$500$", "$100$", "$50$"], "A",
      r"$\frac{5 \times 10}{0.2} = 250$.", diff=1),

    Q("NUM-09", T, "M2.3", r"How many positive divisors does $360$ have?",
      ["$24$", "$12$", "$20$", "$18$", "$36$", "$16$"], "A",
      r"$360 = 2^3\cdot3^2\cdot5$, so the number of divisors is $(3+1)(2+1)(1+1) = 24$.", diff=2),

    Q("NUM-10", T, "M2.13", r"A number $x$ is truncated (not rounded) to $2$ decimal places and the result is $3.14$. Which inequality describes the possible values of $x$?",
      [r"$3.14 \leq x < 3.15$", r"$3.135 \leq x < 3.145$", r"$3.13 < x \leq 3.14$", r"$3.14 < x < 3.15$", r"$3.135 < x < 3.145$", r"$3.14 \leq x \leq 3.15$"], "A",
      r"Truncation removes the later digits, so $x$ is at least $3.14$ and less than $3.15$.", diff=1),

    Q("NUM-11", T, "M2.2", r"Evaluate $\left(2\dfrac{1}{3} - 1\dfrac{3}{4}\right) \div \dfrac{7}{6}$.",
      [r"$\dfrac{1}{2}$", r"$\dfrac{7}{24}$", r"$\dfrac{49}{72}$", r"$\dfrac{2}{3}$", r"$\dfrac{7}{12}$", r"$1$"], "A",
      r"$\frac73 - \frac74 = \frac{28 - 21}{12} = \frac{7}{12}$; $\frac{7}{12} \times \frac67 = \frac12$.", diff=1),

    Q("NUM-12", T, "M2.3", r"""$n$ is a positive integer such that $n$, $n + 2$ and $n + 4$ are all prime. Which of the following statements is/are true?

I. There is exactly one such value of $n$.
II. $n$ must be odd.
III. One of $n$, $n + 2$, $n + 4$ must be divisible by $3$.""", ROMAN3, "H",
      r"Among any three numbers of the form $n, n+2, n+4$ one is a multiple of $3$ (they cover all residues mod $3$) - III. So one of them must equal $3$ itself for all to be prime, giving $n = 3$ only ($3, 5, 7$) - I. And $3$ is odd - II.", paper=2, tags=("roman",), diff=2),

    Q("NUM-13", T, "M2.7", r"Which of the following is equal to $\dfrac{8^{4} \times 2^{-5}}{4^{3}}$?",
      ["$2$", "$4$", "$1$", r"$\dfrac12$", "$8$", "$16$"], "A",
      r"$\frac{2^{12}\cdot2^{-5}}{2^{6}} = 2^{1} = 2$.", diff=1),

    Q("NUM-14", T, "M2.12", r"Simplify $\sqrt{48} \times \sqrt{27} \div \sqrt{12}$.",
      ["$18$", r"$6\sqrt3$", "$12$", r"$9\sqrt{3}$", "$36$", "$6$"], "B",
      r"$\sqrt{48} = 4\sqrt3$, $\sqrt{27} = 3\sqrt3$, $\sqrt{12} = 2\sqrt3$. So $\dfrac{4\sqrt3 \times 3\sqrt3}{2\sqrt3} = \dfrac{36}{2\sqrt3} = \dfrac{18}{\sqrt3} = 6\sqrt3$.", diff=1),

    Q("NUM-15", T, "M2.5", r"How many three-digit positive integers have digits that are all different and all odd?",
      ["$60$", "$125$", "$100$", "$120$", "$24$", "$30$"], "A",
      r"Odd digits $1, 3, 5, 7, 9$: $5 \times 4 \times 3 = 60$.", diff=1),

    Q("NUM-16", T, "M1.1", r"Water flows through a pipe at $1.2$ litres per second. How long does it take to fill a tank of volume $3.6$ m$^3$? (1 m$^3$ = 1000 litres.)",
      ["$50$ minutes", "$5$ minutes", "$30$ minutes", "$3$ hours", "$500$ seconds", "$1$ hour"], "A",
      r"$3600$ litres at $1.2$ litres/s takes $3000$ s $= 50$ minutes.", diff=1),

    Q("NUM-17", T, "M2.13", r"$a = 5.0$ and $b = 2.0$, each correct to $2$ significant figures. Find the lower bound of $\dfrac{a}{b}$.",
      [r"$\dfrac{4.95}{2.05}$", r"$\dfrac{4.95}{1.95}$", r"$\dfrac{5.05}{2.05}$", r"$\dfrac{5.05}{1.95}$", r"$2.4$", r"$\dfrac{4.5}{2.5}$"], "A",
      r"Smallest numerator over largest denominator: $\frac{4.95}{2.05}$.", diff=1),

    Q("NUM-18", T, "M2.3", r"What is the smallest positive integer that is divisible by every integer from $1$ to $10$?",
      ["$2520$", "$5040$", "$1260$", "$3628800$", "$840$", "$720$"], "A",
      r"$\text{lcm}(1, \ldots, 10) = 2^3\cdot3^2\cdot5\cdot7 = 2520$.", diff=1),

    Q("NUM-19", T, "M2.9", r"Which of the following fractions has a terminating decimal expansion?",
      [r"$\dfrac{7}{40}$", r"$\dfrac{5}{12}$", r"$\dfrac{4}{15}$", r"$\dfrac{11}{14}$", r"$\dfrac{2}{9}$", r"$\dfrac{3}{22}$"], "A",
      r"A fraction in lowest terms terminates iff its denominator has no prime factors other than $2$ and $5$: $40 = 2^3 \cdot 5$.", diff=1),

    Q("NUM-20", T, "M2.11", r"Find the exact value of $\left(\sqrt{5} - 1\right)^2 + \left(\sqrt{5} + 1\right)^2$.",
      ["$12$", "$10$", r"$12 + 4\sqrt5$", "$8$", r"$4\sqrt5$", "$6$"], "A",
      r"$(6 - 2\sqrt5) + (6 + 2\sqrt5) = 12$.", diff=1),
]
