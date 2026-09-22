"""Sequences and series (MM2.1, MM2.2, MM2.3, M4.19)."""
from gen.model import Q, ROMAN3

T = "sequences-series"

QUESTIONS = [
    Q("SEQ-01", T, "MM2.2", r"An arithmetic series has first term $5$ and common difference $3$. Find the sum of the first $40$ terms.",
      ["$2540$", "$2500$", "$2440$", "$1270$", "$2580$", "$2600$"], "A",
      r"$S_{40} = \frac{40}{2}\left(2\cdot5 + 39\cdot3\right) = 20(10 + 117) = 2540$.", diff=1),

    Q("SEQ-02", T, "MM2.3", r"Find the sum to infinity of the geometric series $12 - 4 + \dfrac{4}{3} - \dfrac{4}{9} + \ldots$",
      ["$9$", "$18$", "$8$", "$16$", "$6$", "$24$"], "A",
      r"$a = 12$, $r = -\frac13$. $S_\infty = \dfrac{12}{1 + \frac13} = \dfrac{12}{4/3} = 9$.", diff=1),

    Q("SEQ-03", T, "MM2.1", r"A sequence is defined by $x_{n+1} = 3x_n - 2$ with $x_1 = 2$. Find $x_5$.",
      ["$82$", "$28$", "$54$", "$80$", "$244$", "$162$"], "A",
      r"$x_2 = 4$, $x_3 = 10$, $x_4 = 28$, $x_5 = 82$.", diff=1),

    Q("SEQ-04", T, "MM2.2", r"The $n$th term of an arithmetic sequence is $u_n = 7 - 4n$. Find the sum of the first $30$ terms.",
      ["$-1650$", "$-1770$", "$-1590$", "$-1530$", "$-1740$", "$-1860$"], "A",
      r"$u_1 = 3$, $u_{30} = 7 - 120 = -113$. $S_{30} = \frac{30}{2}(3 - 113) = 15(-110) = -1650$.", diff=1),

    Q("SEQ-05", T, "MM2.3", r"A geometric series has first term $a$ and common ratio $r$ with $|r| < 1$. Its sum to infinity is $8$ and the sum to infinity of the squares of its terms is $\dfrac{64}{3}$. Find $r$.",
      [r"$\dfrac{1}{2}$", r"$\dfrac{1}{3}$", r"$\dfrac{2}{3}$", r"$\dfrac{1}{4}$", r"$\dfrac{3}{4}$", r"$-\dfrac12$"], "A",
      r"$\dfrac{a}{1-r} = 8$ and $\dfrac{a^2}{1 - r^2} = \dfrac{64}{3}$. Dividing the second by the square of the first: $\dfrac{1-r}{1+r} = \dfrac{64/3}{64} = \dfrac13$, so $3 - 3r = 1 + r$ and $r = \frac12$.", diff=2),

    Q("SEQ-06", T, "MM2.2", r"The sum of the first $n$ terms of a series is $S_n = 2n^2 + 3n$. Find the $10$th term.",
      ["$41$", "$230$", "$39$", "$43$", "$21$", "$189$"], "A",
      r"$u_{10} = S_{10} - S_9 = (200 + 30) - (162 + 27) = 230 - 189 = 41$.", diff=1),

    Q("SEQ-07", T, "MM2.1", r"A sequence satisfies $x_{n+1} = \dfrac{1}{1 - x_n}$ with $x_1 = 2$. Find $x_{100}$.",
      [r"$-1$", r"$\dfrac{1}{2}$", r"$2$", r"$-\dfrac12$", r"$1$", r"$0$"], "C",
      r"$x_2 = \frac{1}{1-2} = -1$, $x_3 = \frac{1}{1-(-1)} = \frac12$, $x_4 = \frac{1}{1 - 1/2} = 2 = x_1$: the sequence has period $3$. Since $100 = 3\times33 + 1$, $x_{100} = x_1 = 2$."),

    Q("SEQ-08", T, "MM2.3", r"The second term of a geometric sequence is $6$ and the fifth term is $48$. Find the sum of the first $6$ terms.",
      ["$189$", "$186$", "$192$", "$93$", "$126$", "$381$"], "A",
      r"$ar = 6$, $ar^4 = 48$, so $r^3 = 8$, $r = 2$, $a = 3$. $S_6 = 3\cdot\dfrac{2^6 - 1}{2 - 1} = 3 \times 63 = 189$.", diff=1),

    Q("SEQ-09", T, "MM2.2", r"How many terms of the arithmetic series $3 + 7 + 11 + \ldots$ are needed for the sum to first exceed $500$?",
      ["$15$", "$16$", "$17$", "$14$", "$18$", "$11$"], "B",
      r"$S_n = \frac n2(6 + 4(n-1)) = n(2n + 1)$. $n = 15$: $465$; $n = 16$: $528 > 500$. So $16$.", diff=1),

    Q("SEQ-10", T, "MM2.3", r"A geometric series has first term $2$ and common ratio $r > 0$. The sum of the first three terms is $14$. Find the sum of the first five terms.",
      ["$62$", "$30$", "$126$", "$46$", "$52$", "$94$"], "A",
      r"$2 + 2r + 2r^2 = 14 \Rightarrow r^2 + r - 6 = 0 \Rightarrow r = 2$. $S_5 = 2(2^5 - 1) = 62$.", diff=1),

    Q("SEQ-11", T, "MM2.2", r"The sum of the first $n$ natural numbers is $S$. The sum of the first $2n$ natural numbers is $kS$. Which of the following is true?",
      [r"$k = 4$ for all $n$", r"$k = 2$ for all $n$", r"$k = \dfrac{2(2n+1)}{n+1}$", r"$k = \dfrac{4n + 2}{n}$", r"$k = 4 - \dfrac{2}{n}$"], "C",
      r"$S = \frac{n(n+1)}{2}$ and the sum to $2n$ is $\frac{2n(2n+1)}{2} = n(2n+1)$. So $k = \dfrac{n(2n+1)}{n(n+1)/2} = \dfrac{2(2n+1)}{n+1}$.", diff=2),

    Q("SEQ-12", T, "MM2.3", r"""Which of the following geometric series is/are convergent?

I. $1 + 0.9 + 0.81 + \ldots$
II. $3 - 3 + 3 - 3 + \ldots$
III. $100 + 10 + 1 + 0.1 + \ldots$""", ROMAN3, "F",
      r"A geometric series converges if and only if $|r| < 1$. I has $r = 0.9$, III has $r = 0.1$: both converge. II has $r = -1$ and does not converge.", paper=2, tags=("roman",), diff=1),

    Q("SEQ-13", T, "MM2.2", r"An arithmetic sequence has $u_3 = 10$ and $u_8 = 25$. Find the smallest value of $n$ for which $u_n > 100$.",
      ["$33$", "$34$", "$32$", "$35$", "$31$", "$36$"], "B",
      r"$5d = 15 \Rightarrow d = 3$, $a = 4$. $u_n = 4 + 3(n-1) = 3n + 1 > 100 \Rightarrow n > 33$, so $n = 34$.", diff=1),

    Q("SEQ-14", T, "MM2.1", r"The sequence $u_n = n^2 - 10n + 30$ is defined for positive integers $n$. What is the smallest value taken by any term of the sequence?",
      ["$5$", "$6$", "$30$", "$0$", "$-5$", "$21$"], "A",
      r"$u_n = (n-5)^2 + 5$, minimised at $n = 5$ with value $5$.", diff=1),

    Q("SEQ-15", T, "MM2.3", r"Evaluate $\displaystyle\sum_{k=1}^{10} 3 \times 2^{k}$.",
      ["$6138$", "$3069$", "$6141$", "$3072$", "$6144$", "$3066$"], "A",
      r"This is $6 + 12 + \ldots + 6\cdot2^{9}$: first term $6$, ratio $2$, $10$ terms: $6(2^{10} - 1) = 6 \times 1023 = 6138$.", diff=1),

    Q("SEQ-16", T, "MM2.2", r"The sum of the first $n$ terms of an arithmetic series is $S_n$. Given that $S_{10} = 145$ and $S_{20} = 490$, find the common difference.",
      ["$2$", "$3$", "$1$", "$4$", r"$\dfrac{3}{2}$", "$5$"], "A",
      r"$S_{10} = 5(2a + 9d) = 145 \Rightarrow 2a + 9d = 29$; $S_{20} = 10(2a + 19d) = 490 \Rightarrow 2a + 19d = 49$. Subtract: $10d = 20$, $d = 2$.", diff=1),

    Q("SEQ-17", T, "MM2.3", r"A ball is dropped from a height of $10$ m. After each bounce it rises to $\dfrac{3}{5}$ of its previous height. Find the total distance travelled by the ball before it comes to rest.",
      ["$40$ m", "$25$ m", "$30$ m", "$50$ m", "$35$ m", "$20$ m"], "A",
      r"Down: $10 + 6 + 3.6 + \ldots = \dfrac{10}{1 - 3/5} = 25$. Up: $6 + 3.6 + \ldots = 15$. Total $40$ m.", diff=2),

    Q("SEQ-18", T, "MM2.1", r"A sequence is defined by $u_1 = 1$ and $u_{n+1} = u_n + 2n + 1$. Which of the following is an expression for $u_n$?",
      [r"$n^2$", r"$n^2 + 1$", r"$2n - 1$", r"$n^2 - n + 1$", r"$n(n+1)/2$", r"$2^{n} - 1$"], "A",
      r"$u_2 = 4$, $u_3 = 9$, $u_4 = 16$: $u_n = n^2$. Check: $(n+1)^2 = n^2 + 2n + 1$.", diff=1),

    Q("SEQ-19", T, "MM2.3", r"The first three terms of a geometric sequence are $x$, $x + 6$ and $x + 15$. Find the fourth term.",
      [r"$\dfrac{125}{4}$", r"$\dfrac{75}{2}$", r"$\dfrac{125}{2}$", r"$45$", r"$\dfrac{225}{4}$", r"$\dfrac{81}{2}$"], "F",
      r"Geometric: $(x+6)^2 = x(x+15) \Rightarrow x^2 + 12x + 36 = x^2 + 15x \Rightarrow x = 12$. The terms are $12, 18, 27$ with ratio $\frac32$, so the fourth term is $27 \times \frac32 = \frac{81}{2}$."),

    Q("SEQ-20", T, "MM2.2", r"The integers from $1$ to $100$ inclusive are written down. What is the sum of those that are multiples of $3$ or $5$ (or both)?",
      ["$2418$", "$2318$", "$2733$", "$2103$", "$2350$", "$2500$"], "A",
      r"Multiples of $3$: $3 + \ldots + 99 = 3(1 + \ldots + 33) = 3 \times 561 = 1683$. Multiples of $5$: $5(1 + \ldots + 20) = 1050$. Multiples of $15$: $15(1 + \ldots + 6) = 315$. Total $1683 + 1050 - 315 = 2418$.", diff=2),

    Q("SEQ-21", T, "MM2.1", r"""A sequence has $u_1 = 3$ and $u_{n+1} = \dfrac{u_n + 5}{2}$. Which of the following statements is/are true?

I. The sequence is increasing.
II. $u_n < 5$ for all $n$.
III. $u_n = 5 - 2^{2-n}$ for all $n$.""", ROMAN3, "H",
      r"$u_2 = 4$, $u_3 = 4.5$, $u_4 = 4.75$. If $u_n < 5$ then $u_{n+1} = \frac{u_n + 5}{2} < 5$ and $u_{n+1} - u_n = \frac{5 - u_n}{2} > 0$, so I and II hold. III: $5 - 2^{2-n}$ gives $3, 4, 4.5, \ldots$ and satisfies the recurrence: $\frac{5 - 2^{2-n} + 5}{2} = 5 - 2^{1-n}$. All three are true.", paper=2, tags=("roman",), diff=3),
]

