"""Mathematical proof (Prf1-Prf4): direct proof, cases, contradiction, counterexample, ordering steps,
conjectures. All Paper 2."""
from gen.model import Q, ROMAN3

T = "proof"

QUESTIONS = [
    Q("PRF-01", T, "Prf1", r"Consider the claim: **for every positive integer $n$, $n^2 + n$ is even.** Which of the following is a complete and valid proof?",
      [r"$n^2 + n = n(n + 1)$ is the product of two consecutive integers, one of which must be even, so the product is even.",
       r"$1^2 + 1 = 2$, $2^2 + 2 = 6$, $3^2 + 3 = 12$, which are all even, so the claim holds.",
       r"If $n$ is even then $n^2$ is even and so $n^2 + n$ is even.",
       r"$n^2 + n$ is even because both $n^2$ and $n$ are even.",
       r"Suppose $n^2 + n$ is odd. Then $n$ is odd, so $n^2$ is odd, so $n^2 + n$ is even, which is a contradiction... unless $n$ is even."], "A",
      r"A covers every $n$ with a general argument. B checks only three cases; C handles only even $n$; D is false for odd $n$; E is incomplete.", diff=1),

    Q("PRF-02", T, "Prf1", r"Which of the following is a counterexample to the claim **'if $n$ is a positive integer, then $2^n + 1$ is prime'**?",
      [r"$n = 3$", r"$n = 1$", r"$n = 2$", r"$n = 4$", r"$n = 8$"], "A",
      r"$2^3 + 1 = 9 = 3 \times 3$ is not prime. ($n = 1, 2, 4, 8$ give $3, 5, 17, 257$, all prime.)", diff=1),

    Q("PRF-03", T, "Prf1", r"""Here is a proof that $\sqrt{2}$ is irrational, with its steps in the wrong order.

I. Then $p^2 = 2q^2$, so $p^2$ is even, so $p$ is even; write $p = 2k$.
II. Suppose, for contradiction, that $\sqrt2 = \dfrac{p}{q}$ where $p$ and $q$ are positive integers with no common factor.
III. This contradicts the assumption that $p$ and $q$ have no common factor, so $\sqrt2$ is irrational.
IV. Then $4k^2 = 2q^2$, so $q^2 = 2k^2$ is even, so $q$ is even.

Which is the correct order?""",
      [r"II, I, IV, III", r"I, II, IV, III", r"II, IV, I, III", r"I, IV, II, III", r"II, I, III, IV"], "A",
      r"Assume (II), deduce $p$ even (I), deduce $q$ even (IV), reach the contradiction (III).", diff=1, tags=("fixed",)),

    Q("PRF-04", T, "Prf1", r"A student wants to prove that **the square of any odd integer leaves remainder $1$ when divided by $8$**. Which of the following is the most appropriate first step?",
      [r"Write the odd integer as $2k + 1$ for some integer $k$.", r"Check the claim for $1, 3, 5, 7$ and $9$.", r"Assume the square leaves a remainder other than $1$.", r"Write the odd integer as $2k$ for some integer $k$.", r"Assume the claim is true for all odd integers."], "A",
      r"A direct proof: $(2k+1)^2 = 4k^2 + 4k + 1 = 4k(k+1) + 1$, and $k(k+1)$ is even, so the square is $8m + 1$. Checking cases is not a proof; assuming the claim is circular.", diff=1),

    Q("PRF-05", T, "Prf3", r"The sums $1$, $1 + 3$, $1 + 3 + 5$, $1 + 3 + 5 + 7$ are $1, 4, 9, 16$. A student conjectures that the sum of the first $n$ odd numbers is $n^2$. Which of the following is a valid justification?",
      [r"The odd numbers form an arithmetic series with first term $1$ and difference $2$, so the sum of $n$ terms is $\frac n2(2 + 2(n - 1)) = n^2$.",
       r"The pattern $1, 4, 9, 16$ continues with $25$, so the conjecture is true.",
       r"Each odd number is one more than an even number, and the even numbers sum to $n(n-1)$... so the total is $n^2$ since there are $n$ of them: $n(n - 1) + n = n^2$.",
       r"The conjecture is true because $n^2$ is always odd when $n$ is odd.",
       r"Four cases have been checked, which is enough for a pattern."], "A",
      r"A applies the arithmetic-series formula to all $n$. (C also gives a correct calculation but B, D and E are not justifications.)", diff=2),

    Q("PRF-06", T, "Prf1", r"""Which of the following statements can be disproved by a single counterexample?

I. Every prime number greater than $2$ is odd.
II. Every integer of the form $4k + 3$ is prime.
III. There exists an even prime number.""", ROMAN3, "C",
      r"Only a 'for all' statement can be disproved by one counterexample. I is true (no counterexample exists). II is false and $k = 3$ ($15$) disproves it. III is an existence statement - a counterexample is meaningless; it is proved by the example $2$.", tags=("roman",), diff=2),

    Q("PRF-07", T, "Prf1", r"Prove by cases that $n^3 - n$ is divisible by $3$ for every integer $n$. Which set of cases is both sufficient and necessary to consider?",
      [r"$n = 3k$, $n = 3k + 1$, $n = 3k + 2$", r"$n$ even, $n$ odd", r"$n$ positive, $n$ zero, $n$ negative", r"$n = 3k + 1$, $n = 3k + 2$", r"$n$ prime, $n$ not prime"], "A",
      r"$n^3 - n = (n - 1)n(n + 1)$ is a product of three consecutive integers; splitting by remainder on division by $3$ shows one factor is a multiple of $3$ in every case.", diff=1),

    Q("PRF-08", T, "Prf2", r"It is given that for all real $x$: if $f(x) > 0$ then $g(x) > 0$. It is also known that $g(2) = -1$. What can be deduced?",
      [r"$f(2) \leq 0$", r"$f(2) > 0$", r"$f(2) < 0$", r"$f(2) = 0$", r"nothing about $f(2)$"], "A",
      r"Contrapositive: if $g(x) \leq 0$ then $f(x) \leq 0$. Since $g(2) = -1 \leq 0$, $f(2) \leq 0$ (it could be $0$ or negative).", diff=1),

    Q("PRF-09", T, "Prf1", r"""Here is a proof that there are infinitely many primes, with the steps out of order.

I. Then $N$ leaves remainder $1$ on division by each of $p_1, \ldots, p_n$, so no $p_i$ divides $N$.
II. Suppose there are only finitely many primes $p_1, p_2, \ldots, p_n$, and let $N = p_1 p_2 \cdots p_n + 1$.
III. So $N$ has a prime factor that is not in the list, which is a contradiction.
IV. But $N > 1$, so $N$ has at least one prime factor.

Which is the correct order?""",
      [r"II, I, IV, III", r"II, III, I, IV", r"I, II, IV, III", r"II, I, III, IV", r"IV, II, I, III"], "A",
      r"Define $N$ (II), show no listed prime divides it (I), note that $N$ nevertheless has some prime factor (IV), and conclude that this factor is a new prime (III). The conclusion III cannot come before both I and IV have been established.", diff=2, tags=("fixed",)),

    Q("PRF-10", T, "Prf1", r"Consider the claim: **if $x$ and $y$ are real numbers with $x + y > 10$, then $x > 5$ or $y > 5$.** Which of the following proves it?",
      [r"Suppose $x \leq 5$ and $y \leq 5$. Then $x + y \leq 10$, contradicting $x + y > 10$.", r"If $x > 5$ then the conclusion holds; if $y > 5$ then the conclusion holds.", r"Take $x = 6$, $y = 6$: then $x + y = 12 > 10$ and $x > 5$.", r"Suppose $x > 5$. Then $y > 10 - x$, so $y > 5$.", r"If $x + y > 10$ then the average of $x$ and $y$ is more than $5$, so both exceed $5$."], "A",
      r"A is proof by contrapositive/contradiction. B assumes the conclusion, C is an example, D proves something false, E's conclusion ('both exceed $5$') is wrong.", diff=2),

    Q("PRF-11", T, "Prf3", r"A student notices that $1 + 2 = 3$, $4 + 5 + 6 = 7 + 8$, $9 + 10 + 11 + 12 = 13 + 14 + 15$ and conjectures that the pattern continues. Which of the following describes the $n$th line of the pattern?",
      [r"The $n$th line starts at $n^2$ and has $n + 1$ numbers on the left and $n$ on the right.", r"The $n$th line starts at $n^2$ and has $n$ numbers on each side.", r"The $n$th line starts at $2n - 1$ and has $n + 1$ numbers on the left.", r"The $n$th line starts at $n^2$ and has $n$ numbers on the left and $n + 1$ on the right.", r"The $n$th line starts at $n(n+1)$ and has $n + 1$ numbers on the left."], "A",
      r"Line $1$ starts at $1$, line $2$ at $4$, line $3$ at $9$: start $n^2$. Left sides have $2, 3, 4$ numbers ($n + 1$), right sides $1, 2, 3$ ($n$).", diff=2),

    Q("PRF-12", T, "Prf2", r"For a positive integer $n$ it is known that: (i) if $n$ is a multiple of $4$ then $n$ is not a multiple of $6$; (ii) $n$ is a multiple of $12$ or $n$ is a multiple of $4$. What can be deduced?",
      [r"The premises are inconsistent unless $n$ is a multiple of $4$ but not of $6$; in particular $n$ cannot be a multiple of $12$.", r"$n$ is a multiple of $12$.", r"$n$ is a multiple of $6$.", r"$n$ is not a multiple of $4$.", r"Nothing can be deduced."], "A",
      r"If $n$ were a multiple of $12$ it would be a multiple of both $4$ and $6$, contradicting (i). So by (ii) $n$ is a multiple of $4$, and by (i) not a multiple of $6$.", diff=2),

    Q("PRF-13", T, "Prf1", r"Which of the following is a correct proof that **the sum of any three consecutive integers is divisible by $3$**?",
      [r"Let the integers be $n - 1$, $n$, $n + 1$. Their sum is $3n$, which is divisible by $3$.", r"$1 + 2 + 3 = 6$, $2 + 3 + 4 = 9$ and $3 + 4 + 5 = 12$ are all divisible by $3$.", r"Let the integers be $n$, $2n$, $3n$. Their sum is $6n$, which is divisible by $3$.", r"Any three integers include one that is a multiple of $3$, so the sum is a multiple of $3$.", r"The middle integer is the mean of the three, so the sum is three times an integer... but this needs the middle integer to be a multiple of $3$."], "A",
      r"A is general and correct. B checks cases; C uses non-consecutive integers; D's reasoning is invalid (containing a multiple of $3$ does not make the sum a multiple of $3$).", diff=1),

    Q("PRF-14", T, "Prf1", r"To prove **'if $n^2$ is even then $n$ is even'** by contradiction, which assumption should be made?",
      [r"$n^2$ is even and $n$ is odd.", r"$n$ is even and $n^2$ is odd.", r"$n^2$ is odd.", r"$n$ is odd.", r"$n^2$ is even."], "A",
      r"Assume the hypothesis holds and the conclusion fails, then derive a contradiction: $n$ odd gives $n^2$ odd, contradicting $n^2$ even.", diff=1),

    Q("PRF-15", T, "Prf3", r"""Let $u_n = n^2 - n + 41$. Which of the following statements is/are true?

I. $u_n$ is prime for $n = 1, 2, 3, 4, 5$.
II. $u_n$ is prime for all positive integers $n$.
III. $u_{41}$ is divisible by $41$.""", ROMAN3, "F",
      r"$u_1 = 41$, $u_2 = 43$, $u_3 = 47$, $u_4 = 53$, $u_5 = 61$: all prime (I). $u_{41} = 41^2 - 41 + 41 = 41^2$, divisible by $41$ (III) and not prime, so II is false - small cases do not prove a general claim.", tags=("roman",), diff=2),

    Q("PRF-16", T, "Prf4", r"""A proof that **if $a$ and $b$ are positive real numbers then $\dfrac{a + b}{2} \geq \sqrt{ab}$** is given with its lines scrambled.

I. Hence $a + b \geq 2\sqrt{ab}$, and dividing by $2$ gives the result.
II. Expanding, $a - 2\sqrt{ab} + b \geq 0$.
III. Since squares are non-negative, $(\sqrt a - \sqrt b)^2 \geq 0$.

Which order gives a valid proof?""",
      [r"III, II, I", r"I, II, III", r"II, III, I", r"III, I, II", r"II, I, III"], "A",
      r"Start from a known truth (III), expand (II), rearrange (I). Starting from the result and working backwards (I, II, III) would need every step to be reversible and is presented in the wrong direction.", diff=1, tags=("fixed",)),

    Q("PRF-17", T, "Prf1", r"Which of the following claims is FALSE, and therefore can be disproved by a counterexample?",
      [r"If $a > b$ then $a^2 > b^2$, for all real $a, b$.", r"If $a > b > 0$ then $a^2 > b^2$.", r"If $a > b$ then $a + c > b + c$, for all real $a, b, c$.", r"If $a > b$ then $a^3 > b^3$, for all real $a, b$.", r"If $a > b$ then $-a < -b$, for all real $a, b$."], "A",
      r"$a = 1$, $b = -2$: $1 > -2$ but $1 < 4$. The others are true.", diff=1),

    Q("PRF-18", T, "Prf2", r"""Every element of a set $S$ of integers is either a multiple of $3$ or a multiple of $5$. Every multiple of $3$ in $S$ is negative. $S$ contains the number $10$. Which of the following statements must be true?

I. $S$ contains a positive multiple of $5$.
II. $S$ contains no positive multiple of $3$.
III. $S$ contains a negative number.""", ROMAN3, "E",
      r"$10 \in S$ is a positive multiple of $5$ (I). Multiples of $3$ in $S$ are negative, so none is positive (II). III fails: $S = \{10\}$ satisfies everything.", tags=("roman",), diff=2),

    Q("PRF-19", T, "Prf1", r"A student proves that $\sqrt{4}$ is irrational by copying the standard proof for $\sqrt2$: 'Suppose $\sqrt4 = p/q$ in lowest terms; then $p^2 = 4q^2$, so $p^2$ is even, so $p$ is even, $p = 2k$; then $4k^2 = 4q^2$, so $k^2 = q^2$...' At which point does the argument break down compared with the $\sqrt2$ proof?",
      [r"$k^2 = q^2$ does not show that $q$ is even, so no contradiction arises.", r"$p^2 = 4q^2$ does not imply that $p$ is even.", r"$\sqrt4$ cannot be written as $p/q$.", r"It is not valid to assume $p$ and $q$ have no common factor.", r"The argument is valid, so $\sqrt4$ is irrational."], "A",
      r"For $\sqrt2$ the step $p^2 = 2q^2$ leads to $2k^2 = q^2$, making $q$ even. Here $k^2 = q^2$ carries no parity information, so the contradiction never appears - as expected since $\sqrt4 = 2$.", diff=2),

    Q("PRF-20", T, "Prf3", r"$T_n$ denotes the $n$th triangular number $\dfrac{n(n+1)}{2}$. A student observes $T_1 + T_2 = 4$, $T_2 + T_3 = 9$, $T_3 + T_4 = 16$ and conjectures that $T_n + T_{n+1}$ is always a perfect square. Which of the following proves the conjecture?",
      [r"$T_n + T_{n+1} = \dfrac{n(n+1) + (n+1)(n+2)}{2} = \dfrac{(n+1)(2n+2)}{2} = (n+1)^2$", r"$T_4 + T_5 = 25$, which is a square, so the pattern continues.", r"Triangular numbers are always squares.", r"$T_n + T_{n+1} = 2T_n + (n + 1)$, which is a square.", r"$T_{n+1} - T_n = n + 1$, so the sum is a square."], "A",
      r"Only A is a general algebraic verification.", diff=1),
]
