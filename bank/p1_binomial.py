"""Binomial expansion (MM2.4)."""
from gen.model import Q, ROMAN3

T = "binomial"

QUESTIONS = [
    Q("BIN-01", T, "MM2.4", r"Find the coefficient of $x^3$ in the expansion of $(2 + 3x)^5$.",
      ["$1080$", "$720$", "$360$", "$270$", "$540$", "$2160$"], "A",
      r"$\binom{5}{3} 2^{2} (3x)^3 = 10 \times 4 \times 27 x^3 = 1080x^3$.", diff=1),

    Q("BIN-02", T, "MM2.4", r"The coefficient of $x^2$ in the expansion of $(1 + kx)^6$ is $60$. Given that $k > 0$, find $k$.",
      ["$2$", "$4$", r"$\sqrt{10}$", "$10$", r"$\dfrac{1}{2}$", "$3$"], "A",
      r"$\binom62 k^2 = 15k^2 = 60$, so $k^2 = 4$ and $k = 2$.", diff=1),

    Q("BIN-03", T, "MM2.4", r"Find the term independent of $x$ in the expansion of $\left(x^2 + \dfrac{2}{x}\right)^6$.",
      ["$240$", "$160$", "$60$", "$480$", "$120$", "$15$"], "A",
      r"General term $\binom6r (x^2)^{6-r} \left(\frac2x\right)^r = \binom6r 2^r x^{12 - 3r}$. Need $12 - 3r = 0$, $r = 4$: $\binom64 \times 16 = 15 \times 16 = 240$.", diff=2),

    Q("BIN-04", T, "MM2.4", r"What is the sum of the coefficients in the expansion of $(3x - 2)^{7}$?",
      ["$1$", "$-1$", "$128$", "$-128$", "$2187$", "$0$"], "A",
      r"Put $x = 1$: $(3 - 2)^7 = 1$.", diff=1),

    Q("BIN-05", T, "MM2.4", r"Evaluate $\binom{10}{3} - \binom{10}{7} + \binom{9}{2}$.",
      ["$36$", "$156$", "$0$", "$120$", "$84$", "$240$"], "A",
      r"$\binom{10}{3} = \binom{10}{7}$, so the first two cancel; $\binom92 = 36$.", diff=1),

    Q("BIN-06", T, "MM2.4", r"In the expansion of $(1 + x)^n$, the coefficients of $x^4$ and $x^5$ are equal. Find $n$.",
      ["$9$", "$10$", "$8$", "$11$", "$20$", "$5$"], "A",
      r"$\binom n4 = \binom n5$ requires $4 + 5 = n$ (by symmetry $\binom nr = \binom n{n-r}$), so $n = 9$.", diff=1),

    Q("BIN-07", T, "MM2.4", r"Expand $(1 - 2x)^4$ and hence find the coefficient of $x^2$ in $(1 + 3x)(1 - 2x)^4$.",
      ["$0$", "$24$", "$48$", "$-24$", "$12$", "$-48$"], "A",
      r"$(1-2x)^4 = 1 - 8x + 24x^2 - 32x^3 + 16x^4$. Coefficient of $x^2$ in the product: $1\cdot 24 + 3\cdot(-8) = 0$.", diff=1),

    Q("BIN-08", T, "MM2.4", r"The first three terms in the expansion of $(1 + ax)^n$ in ascending powers of $x$ are $1 + 12x + 54x^2$. Find $n$.",
      ["$8$", "$6$", "$9$", "$12$", "$4$", "$10$"], "E",
      r"$na = 12$ and $\frac{n(n-1)}{2}a^2 = 54$. Dividing the second by the square of the first: $\frac{n-1}{2n} = \frac{54}{144} = \frac38$, so $8n - 8 = 6n$ and $n = 4$ (then $a = 3$; check $\binom42 \cdot 9 = 54$).", diff=2),

    Q("BIN-09", T, "MM2.4", r"""Which of the following statements is/are true?

I. $\binom{n}{r} = \binom{n}{n-r}$ for all integers $0 \leq r \leq n$
II. $\binom{n}{r} + \binom{n}{r+1} = \binom{n+1}{r+1}$ for all integers $0 \leq r < n$
III. $\displaystyle\sum_{r=0}^{n} \binom{n}{r} = 2^{n}$ for all positive integers $n$""", ROMAN3, "H",
      r"I is the symmetry of Pascal's triangle; II is Pascal's rule (each entry is the sum of the two above it); III is $(1+1)^n$ expanded. All true.", paper=2, tags=("roman",)),

    Q("BIN-10", T, "MM2.4", r"Find the coefficient of $x^5$ in the expansion of $(1 + x)^{3}(1 + x)^{4}$.",
      ["$21$", "$35$", "$7$", "$1$", "$12$", "$28$"], "A",
      r"$(1+x)^3(1+x)^4 = (1+x)^7$, and $\binom75 = 21$.", diff=1),

    Q("BIN-11", T, "MM2.4", r"Find the value of $(\sqrt{2} + 1)^4 + (\sqrt{2} - 1)^4$.",
      ["$34$", "$17$", r"$24\sqrt{2}$", "$36$", "$16$", r"$34 + 24\sqrt2$"], "A",
      r"Odd powers of $\sqrt2$ cancel: $2\left[(\sqrt2)^4 + \binom42(\sqrt2)^2 + 1\right] = 2[4 + 12 + 1] = 34$.", diff=2),

    Q("BIN-12", T, "MM2.4", r"""The expansion of $\left(2x - \dfrac{1}{x^2}\right)^{9}$ contains a term in $x^{k}$ for each of which of the following values of $k$?

I. $k = 0$
II. $k = 3$
III. $k = -6$""", ROMAN3, "H",
      r"General term: $\binom9r (2x)^{9-r}(-x^{-2})^r$ has power $9 - r - 2r = 9 - 3r$, which takes values $9, 6, 3, 0, -3, \ldots, -18$. $k = 0$ needs $r = 3$: yes. $k = 3$ needs $r = 2$: yes. $k = -6$ needs $r = 5$: yes. All three.", paper=2, tags=("roman",), diff=2),

    Q("BIN-13", T, "MM2.4", r"Use the binomial expansion to find the value of $1.01^{5}$ correct to $4$ decimal places.",
      ["$1.0510$", "$1.0500$", "$1.0501$", "$1.0505$", "$1.0515$", "$1.0410$"], "A",
      r"$(1 + 0.01)^5 = 1 + 5(0.01) + 10(0.0001) + 10(0.000001) + \ldots = 1 + 0.05 + 0.001 + 0.00001 + \ldots \approx 1.0510$.", diff=1),

    Q("BIN-14", T, "MM2.4", r"How many terms in the expansion of $(x + y + z)^{4}$ (after collecting like terms) are there?",
      ["$15$", "$12$", "$10$", "$5$", "$16$", "$81$"], "A",
      r"Terms are $x^ay^bz^c$ with $a + b + c = 4$, $a, b, c \geq 0$. Counting: for $a = 0$ there are $5$ choices of $(b, c)$, $a = 1$: $4$, ..., $a = 4$: $1$. Total $5 + 4 + 3 + 2 + 1 = 15$.", diff=3),

    Q("BIN-15", T, "MM2.4", r"The coefficient of $x^2$ in $(1 + x)^n + (1 + x)^{n+1}$ is $36$. Find $n$.",
      ["$6$", "$7$", "$8$", "$5$", "$9$", "$4$"], "A",
      r"$\binom n2 + \binom{n+1}2 = \frac{n(n-1) + (n+1)n}{2} = n^2 = 36$, so $n = 6$.", diff=2),
]
