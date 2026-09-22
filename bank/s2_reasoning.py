"""Chains of reasoning (Prf2, Prf3, Prf5): must / could be true, extremal and parity arguments,
pigeonhole counting, working systematically. All Paper 2."""
from gen.model import Q, ROMAN3

T = "reasoning"

QUESTIONS = [
    Q("RSN-01", T, "Prf5", r"A selection of $n$ distinct integers is taken from $1, 2, \ldots, 20$. What is the smallest $n$ that guarantees two of the chosen integers differ by exactly $10$?",
      ["$11$", "$10$", "$12$", "$20$", "$2$", "$15$"], "A",
      r"Pair up $\{1, 11\}, \{2, 12\}, \ldots, \{10, 20\}$: ten pairs. Choosing $11$ numbers forces two from the same pair (pigeonhole); choosing one from each pair gives $10$ numbers with no such difference.", diff=2),

    Q("RSN-02", T, "Prf5", r"""The integers $a, b, c$ satisfy $a + b + c = 0$ and $abc = 12$. Which of the following statements must be true?

I. Exactly one of $a, b, c$ is positive.
II. $a^2 + b^2 + c^2$ is even.
III. One of $a, b, c$ is divisible by $3$.""", ROMAN3, "H",
      r"$abc > 0$ means either none or exactly two of them are negative; they cannot all be positive with sum $0$, so exactly two are negative and one positive (I). $a^2 + b^2 + c^2 = (a+b+c)^2 - 2(ab + bc + ca) = -2(ab + bc + ca)$ is even (II). $3$ is prime and divides $abc$, so it divides one of them (III). (Example: $-1, -3, 4$.)", tags=("roman",), diff=3),

    Q("RSN-03", T, "Prf5", r"Five friends each shake hands with some of the others (each pair shakes hands at most once). Which of the following is impossible?",
      [r"The numbers of handshakes made by the five friends are $4, 4, 4, 4, 1$.", r"Every friend shakes hands with exactly two others.", r"Every friend shakes hands with exactly four others.", r"The numbers of handshakes made are $1, 1, 2, 2, 2$.", r"Exactly one friend shakes no hands at all."], "A",
      r"If four people each shook hands with all four others, everyone shook hands with everyone, so the fifth person also made $4$ handshakes, not $1$. (The total $4+4+4+4+1 = 17$ is odd, which is a second reason.) The others can happen: 'exactly two each' is a pentagon of handshakes, 'exactly four each' is everyone with everyone, $1,1,2,2,2$ is a chain, and one person shaking no hands just leaves them out.", diff=2),

    Q("RSN-04", T, "Prf5", r"$x$ and $y$ are positive integers with $x^2 - y^2 = 45$. How many possible pairs $(x, y)$ are there?",
      ["$3$", "$2$", "$1$", "$4$", "$6$", "$0$"], "A",
      r"$(x - y)(x + y) = 45$ with $0 < x - y < x + y$: $(1, 45), (3, 15), (5, 9)$ give $(x, y) = (23, 22), (9, 6), (7, 2)$. Three pairs.", diff=2),

    Q("RSN-05", T, "Prf5", r"In a knockout tournament with $37$ players, each match eliminates exactly one player and the tournament ends when one player remains. How many matches are played?",
      ["$36$", "$37$", "$18$", "$19$", "$64$", "$35$"], "A",
      r"Each match eliminates one player and $36$ must be eliminated, so $36$ matches - whatever the draw looks like.", diff=1),

    Q("RSN-06", T, "Prf5", r"""Three statements are made about a positive integer $N$:

- $N$ is a perfect square.
- $N$ is a multiple of $6$.
- $N$ is less than $50$.

Exactly two of the statements are true. Which of the following could NOT be $N$?""",
      ["$36$", "$16$", "$48$", "$144$", "$25$", "$12$"], "A",
      r"$36$ makes all three statements true, not exactly two. Each of the others makes exactly two true: $16$ and $25$ (square, $< 50$), $48$ and $12$ (multiple of $6$, $< 50$), $144$ (square, multiple of $6$).", diff=2),

    Q("RSN-07", T, "Prf5", r"The digits $1$ to $9$ are placed in a $3 \times 3$ grid so that every row and every column has the same sum. What is that sum?",
      ["$15$", "$45$", "$12$", "$18$", "$10$", "$20$"], "A",
      r"The three rows together contain every digit once, so $3 \times$ (row sum) $= 1 + 2 + \cdots + 9 = 45$, giving $15$.", diff=1),

    Q("RSN-08", T, "Prf5", r"""$a$, $b$ and $c$ are real numbers with $a < b < c$. Which of the following statements must be true?

I. $a + b < 2c$
II. $ab < bc$
III. $\dfrac{a + c}{2} < c$""", ROMAN3, "F",
      r"I: $a + b < c + c$. III: $\frac{a + c}{2} < \frac{c + c}{2} = c$. II fails when $b$ is negative: $a = -3$, $b = -2$, $c = -1$ gives $ab = 6 > bc = 2$.", tags=("roman",), diff=2),

    Q("RSN-09", T, "Prf5", r"A rectangle has integer side lengths and its area (in cm$^2$) is numerically equal to its perimeter (in cm). How many such rectangles are there (counting $a \times b$ and $b \times a$ once)?",
      ["$2$", "$1$", "$3$", "$4$", "$0$", "infinitely many"], "A",
      r"$ab = 2a + 2b \Rightarrow (a - 2)(b - 2) = 4$: $(a - 2, b - 2) = (1, 4)$ or $(2, 2)$, giving $3 \times 6$ and $4 \times 4$.", diff=2),

    Q("RSN-10", T, "Prf5", r"Each of $100$ cards has a different integer from $1$ to $100$ written on it. What is the smallest number of cards that must be drawn (without looking) to be certain of having two cards whose numbers sum to $101$?",
      ["$51$", "$50$", "$52$", "$100$", "$2$", "$99$"], "A",
      r"The $50$ pairs $\{1, 100\}, \{2, 99\}, \ldots, \{50, 51\}$ each sum to $101$. Fifty cards (one from each pair) may avoid it; $51$ cannot.", diff=1),

    Q("RSN-11", T, "Prf5", r"""The product of three consecutive positive integers is $N$, and the middle one of the three integers is $m$. Which of the following statements must be true?

I. $N$ is divisible by $6$.
II. $N$ is divisible by $4$.
III. $N + m$ is a perfect cube.""", ROMAN3, "F",
      r"Among three consecutive integers there is a multiple of $2$ and a multiple of $3$ (I). II fails for $1 \cdot 2 \cdot 3 = 6$. III: $N + m = (m - 1)m(m + 1) + m = m^3 - m + m = m^3$.", tags=("roman",), diff=2),

    Q("RSN-12", T, "Prf5", r"How many positive integers less than $1000$ are divisible by neither $2$ nor $5$?",
      ["$400$", "$500$", "$300$", "$600$", "$399$", "$450$"], "A",
      r"Of $1$ to $999$: $499$ multiples of $2$, $199$ of $5$, $99$ of $10$. Divisible by $2$ or $5$: $499 + 199 - 99 = 599$. Neither: $999 - 599 = 400$.", diff=2),

    Q("RSN-13", T, "Prf5", r"$p$ and $q$ are prime numbers with $p + q = 45$. Find $pq$.",
      ["$86$", "$140$", "$50$", "$102$", "$247$", "$94$"], "A",
      r"An odd sum of two primes needs one of them to be $2$ (the only even prime): $q = 43$, which is prime. $pq = 86$.", diff=2),

    Q("RSN-14", T, "Prf5", r"In a class every student studies at least one of Maths and Physics. $70\%$ study Maths and $60\%$ study Physics. A student is picked at random. What is the probability they study both?",
      [r"$0.3$", r"$0.42$", r"$0.1$", r"$0.2$", r"$0.5$", r"it cannot be determined"], "A",
      r"$P(M \text{ or } P) = 1 = 0.7 + 0.6 - P(\text{both})$, so $P(\text{both}) = 0.3$.", diff=1),

    Q("RSN-15", T, "Prf5", r"""A sequence of $10$ integers is such that the sum of any three consecutive terms is positive and the sum of any five consecutive terms is negative. Which of the following statements must be true?

I. The sum of all $10$ terms is negative.
II. The sequence contains at least one negative term.
III. The sequence contains at least one positive term.""", ROMAN3, "H",
      r"Terms $1$-$5$ and $6$-$10$ are two blocks of five, each with negative sum (I). A five-block has negative sum, so some term is negative (II). A three-block has positive sum, so some term is positive (III).", tags=("roman",), diff=2),

    Q("RSN-16", T, "Prf5", r"The sum of $5$ consecutive odd numbers is $S$. Which of the following is always a factor of $S$?",
      ["$5$", "$10$", "$15$", "$3$", "$4$", "$25$"], "A",
      r"$(m - 4) + (m - 2) + m + (m + 2) + (m + 4) = 5m$ where $m$ is the middle (odd) number; $5m$ is odd, so $10$ is never a factor.", diff=1),

    Q("RSN-17", T, "Prf5", r"Alice, Ben and Cara each make one statement. Alice: 'Ben is lying.' Ben: 'Cara is lying.' Cara: 'Alice and Ben are both lying.' Exactly one of them is telling the truth. Who is it?",
      ["Ben", "Alice", "Cara", "It cannot be determined.", "The situation is impossible."], "A",
      r"If Alice is truthful then Ben lies, so Cara is truthful: two truth-tellers, impossible. If Cara is truthful then Alice and Ben both lie; but Alice lying means Ben is truthful: contradiction. So Ben is the truth-teller: Cara lies (indeed Ben is not lying) and Alice lies (Ben is not lying), which is consistent.", diff=2, tags=("fixed",)),

    Q("RSN-18", T, "Prf5", r"How many ordered pairs of positive integers $(m, n)$ satisfy $\dfrac{1}{m} + \dfrac{1}{n} = \dfrac{1}{4}$?",
      ["$5$", "$3$", "$4$", "$6$", "$8$", "$2$"], "A",
      r"$4n + 4m = mn \Rightarrow (m - 4)(n - 4) = 16$. Positive factor pairs of $16$ as ordered pairs: $(1,16), (2,8), (4,4), (8,2), (16,1)$: five. (Negative factor pairs would make $m$ or $n$ non-positive.)", diff=3),

    Q("RSN-19", T, "Prf5", r"A bag contains red and blue balls only. If one red ball is removed, one quarter of the remaining balls are red. If instead two blue balls are removed, one third of the remaining balls are red. How many balls are in the bag?",
      ["$17$", "$12$", "$16$", "$8$", "$20$", "$14$"], "A",
      r"With $r$ red and $b$ blue: $r - 1 = \frac14(r + b - 1)$ and $r = \frac13(r + b - 2)$. The second gives $b = 2r + 2$; substituting into the first, $4r - 4 = 3r + 1$, so $r = 5$, $b = 12$: $17$ balls.", diff=2),

    Q("RSN-20", T, "Prf5", r"$n$ is a positive integer such that $n^2$ has exactly $3$ positive divisors. Which of the following must be true?",
      [r"$n$ is prime", r"$n$ is a perfect square", r"$n$ is even", r"$n$ is odd", r"$n = 3$"], "A",
      r"A number with exactly $3$ divisors is the square of a prime; so $n^2 = p^2$ and $n = p$ is prime.", diff=2),

    Q("RSN-21", T, "Prf5", r"""Seven consecutive integers are written down. Which of the following statements is/are true?

I. Their sum is divisible by $7$.
II. Their product is divisible by $7$.
III. Their sum is odd.""", ROMAN3, "E",
      r"The sum is $7m$ where $m$ is the middle integer (I). Seven consecutive integers cover every remainder mod $7$, so one is a multiple of $7$ (II). $7m$ is odd only when $m$ is odd, so III need not hold.", tags=("roman",), diff=1),

    Q("RSN-22", T, "Prf5", r"A $4 \times 4$ grid of squares is coloured so that every row and every column contains exactly two black squares. How many black squares are there in the grid?",
      ["$8$", "$4$", "$6$", "$16$", "$12$", "$10$"], "A",
      r"Each of the $4$ rows contains exactly $2$ black squares: $8$ in total.", diff=1),
]
