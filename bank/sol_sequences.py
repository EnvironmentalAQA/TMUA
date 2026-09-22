"""Full teaching solutions: sequences and series (SEQ-xx)."""
from gen.model import Sol

SOLUTIONS = {

"SEQ-01": Sol(
    idea=r"A direct application of the arithmetic sum formula. The only decision is which version of the formula to use.",
    steps=[
        (r"Identify $a = 5$, $d = 3$, $n = 40$.",
         r"'First term' and 'common difference' name $a$ and $d$ exactly; $n$ is how many terms you are adding."),
        (r"Use $S_n = \frac n2\left[2a + (n-1)d\right]$: $S_{40} = 20\left[10 + 39 \times 3\right]$.",
         r"Use this version when you know $a$ and $d$; the other version $\frac n2(a + l)$ needs the last term first."),
        (r"Evaluate the bracket: $10 + 117 = 127$, so $S_{40} = 20 \times 127 = 2540$.",
         r"Note $(n-1)d = 39 \times 3$, not $40 \times 3$ - there are $39$ steps between $40$ terms."),
    ],
    pitfalls=[r"Using $40d$ instead of $39d$, giving $2600$.",
              r"Forgetting to halve $n$, or halving the bracket instead."],
    takeaway=r"$S_n = \frac n2[2a + (n-1)d]$ - the number of **gaps** is $n - 1$, one fewer than the number of terms."),

"SEQ-02": Sol(
    idea=r"A sum to infinity. Find the ratio (including its sign) and check $|r| < 1$ before using the formula.",
    steps=[
        (r"Find $r$ by dividing consecutive terms: $\frac{-4}{12} = -\frac13$.",
         r"Always divide a term by the one before it; the alternating signs mean $r$ is negative."),
        (r"Check convergence: $\left|-\frac13\right| < 1$ ✓.",
         r"The sum to infinity only exists when $|r| < 1$; otherwise the formula is meaningless."),
        (r"Apply $S_\infty = \dfrac{a}{1 - r} = \dfrac{12}{1 - (-\frac13)} = \dfrac{12}{\frac43}$.",
         r"$1 - r$ with a negative $r$ becomes $1 + \frac13$ - the double negative is the main trap."),
        (r"Divide: $12 \times \frac34 = 9$.",
         r"Dividing by a fraction is multiplying by its reciprocal."),
    ],
    pitfalls=[r"Using $r = +\frac13$ and getting $18$.",
              r"Computing $\frac{12}{\frac43}$ as $16$ by multiplying instead of dividing."],
    takeaway=r"$S_\infty = \frac{a}{1-r}$; if $r$ is negative the denominator grows, so the sum is smaller than $a/(1-|r|)$."),

"SEQ-03": Sol(
    idea=r"A recurrence with a small index - just iterate. There is no shortcut worth finding for only four steps.",
    steps=[
        (r"Apply the rule repeatedly from $x_1 = 2$: $x_2 = 3(2) - 2 = 4$.",
         r"$x_{n+1} = 3x_n - 2$ means 'triple the last term, subtract 2'."),
        (r"$x_3 = 3(4) - 2 = 10$; $x_4 = 3(10) - 2 = 28$; $x_5 = 3(28) - 2 = 82$.",
         r"Write each step on its own line - the numbers grow quickly and a single slip propagates."),
    ],
    pitfalls=[r"Stopping at $x_4 = 28$ (an offered option) by miscounting the steps: going from $x_1$ to $x_5$ takes **four** applications.",
              r"Reading the rule as $3(x_n - 2)$, which gives $x_5 = 162$ - also offered."],
    takeaway=r"Count the applications carefully: reaching $x_k$ from $x_1$ takes $k - 1$ steps."),

"SEQ-04": Sol(
    idea=r"You are given the $n$th term rather than $a$ and $d$. Generate the first and last terms and use the $\frac n2(a + l)$ form.",
    steps=[
        (r"First term: $u_1 = 7 - 4 = 3$. Common difference: the coefficient of $n$ is $-4$, so $d = -4$.",
         r"In $u_n = An + B$ the gradient $A$ is the common difference - the sequence is linear in $n$."),
        (r"Last term: $u_{30} = 7 - 120 = -113$.",
         r"Substitute $n = 30$ directly."),
        (r"Use $S_n = \frac n2(a + l) = 15(3 + (-113)) = 15 \times (-110)$.",
         r"This version is quickest when the first and last terms are easy to compute."),
        (r"Evaluate: $-1650$.",
         r"Negative, as expected - most terms are negative."),
    ],
    pitfalls=[r"Taking $d = 7$ or $a = 7$ from the formula rather than computing $u_1$.",
              r"Sign slips when adding $3 + (-113)$."],
    takeaway=r"For $u_n = An + B$: $d = A$ and $u_1 = A + B$; then either sum formula works."),

"SEQ-05": Sol(
    idea=r"Two infinite sums, two unknowns. Dividing one equation by the (square of the) other eliminates $a$ elegantly.",
    steps=[
        (r"Write the two facts: $\dfrac{a}{1 - r} = 8$ and, for the squares (first term $a^2$, ratio $r^2$), $\dfrac{a^2}{1 - r^2} = \dfrac{64}{3}$.",
         r"Squaring every term of a geometric series gives another geometric series with first term $a^2$ and ratio $r^2$."),
        (r"Square the first: $\dfrac{a^2}{(1-r)^2} = 64$.",
         r"Squaring makes the numerators match, so they can be eliminated by division."),
        (r"Divide the second equation by this: $\dfrac{(1-r)^2}{1 - r^2} = \dfrac{64/3}{64} = \dfrac13$.",
         r"Dividing kills $a^2$ entirely - the standard move when two equations share a factor."),
        (r"Simplify using $1 - r^2 = (1-r)(1+r)$: $\dfrac{1 - r}{1 + r} = \dfrac13$.",
         r"One factor of $(1-r)$ cancels."),
        (r"Cross-multiply: $3 - 3r = 1 + r \Rightarrow 4r = 2 \Rightarrow r = \frac12$.",
         r"Check: $a = 4$, and $\frac{16}{1 - 1/4} = \frac{64}{3}$ ✓."),
    ],
    pitfalls=[r"Using ratio $r$ (not $r^2$) for the series of squares.",
              r"Forgetting to square the first equation before dividing, which leaves an $a$ behind."],
    takeaway=r"Squaring a geometric series squares both $a$ and $r$; divide equations to eliminate the unknown you do not want."),

"SEQ-06": Sol(
    idea=r"Given a formula for $S_n$, individual terms come from the difference of consecutive sums.",
    steps=[
        (r"Use $u_{10} = S_{10} - S_9$.",
         r"The 10th term is what the total gains when you add it - this works for any series, arithmetic or not."),
        (r"$S_{10} = 2(100) + 30 = 230$.",
         r"Substitute $n = 10$."),
        (r"$S_9 = 2(81) + 27 = 189$.",
         r"Substitute $n = 9$; $2 \times 81 = 162$."),
        (r"Subtract: $230 - 189 = 41$.",
         r"Both wrong intermediate values ($230$ and $189$) are offered as distractors."),
    ],
    pitfalls=[r"Answering $230$ (that is the sum of ten terms, not the tenth term).",
              r"Substituting $n = 10$ into a 'term' formula that was never given."],
    takeaway=r"$u_n = S_n - S_{n-1}$ recovers terms from a sum formula."),

"SEQ-07": Sol(
    idea=r"A recurrence with a huge index. Compute a few terms, spot the cycle, then use arithmetic on the index.",
    steps=[
        (r"Iterate: $x_2 = \frac{1}{1-2} = -1$, $x_3 = \frac{1}{1-(-1)} = \frac12$, $x_4 = \frac{1}{1 - \frac12} = 2$.",
         r"When an index like $100$ appears, always compute the first few terms - the sequence is almost certainly periodic."),
        (r"$x_4 = x_1$, so the sequence repeats with period $3$: $2, -1, \frac12, 2, -1, \frac12, \ldots$",
         r"Once a value repeats, the whole sequence from that point repeats identically."),
        (r"Reduce the index: $100 = 3 \times 33 + 1$, so $x_{100}$ is in the same position of the cycle as $x_1$.",
         r"Terms with indices differing by a multiple of the period are equal; compare remainders on division by $3$."),
        (r"Therefore $x_{100} = x_1 = 2$.",
         r"Check the convention: the indices $1, 4, 7, \ldots$ all leave remainder $1$ on division by $3$, and $100$ does too."),
    ],
    pitfalls=[r"Finding that $100$ leaves remainder $1$ but then reading off $x_0$ or $x_3$ - line the remainders up with the actual starting index.",
              r"Giving up after two terms and guessing $-1$ or $\frac12$."],
    takeaway=r"Large-index recurrence questions are periodicity questions: find the cycle length, then work with the index modulo it."),

"SEQ-08": Sol(
    idea=r"Two terms of a geometric sequence determine $a$ and $r$. Dividing the two equations isolates $r$.",
    steps=[
        (r"Write the facts: $ar = 6$ and $ar^4 = 48$.",
         r"The $k$th term is $ar^{k-1}$: the second term has $r^1$, the fifth has $r^4$."),
        (r"Divide: $\dfrac{ar^4}{ar} = r^3 = \dfrac{48}{6} = 8$, so $r = 2$.",
         r"Division cancels $a$ - always the first move with two geometric terms."),
        (r"Back-substitute: $a(2) = 6$, so $a = 3$.",
         r"Use the simpler of the two equations."),
        (r"Sum: $S_6 = a\dfrac{r^6 - 1}{r - 1} = 3 \times \dfrac{64 - 1}{1} = 189$.",
         r"With $r = 2$ the denominator is $1$, making the arithmetic easy."),
    ],
    pitfalls=[r"Using $r^4/r^1 = r^4$ instead of $r^3$ and getting a non-integer ratio.",
              r"Computing $S_6$ with $2^6 = 32$ instead of $64$."],
    takeaway=r"Divide two geometric terms to find $r$; the index difference tells you which power of $r$ you get."),

"SEQ-09": Sol(
    idea=r"An inequality on a sum. Form $S_n$, then find the first integer $n$ that works - by trial, since $n$ must be a whole number.",
    steps=[
        (r"Identify $a = 3$, $d = 4$ and form the sum: $S_n = \frac n2\left[6 + 4(n-1)\right] = \frac n2(4n + 2) = n(2n+1)$.",
         r"Simplifying to $n(2n+1)$ makes the trial values much easier to compute."),
        (r"Test $n = 15$: $15 \times 31 = 465$, which is less than $500$.",
         r"Estimate first: $2n^2 \approx 500$ gives $n \approx 15.8$, so start near there."),
        (r"Test $n = 16$: $16 \times 33 = 528 > 500$ ✓.",
         r"The sum is increasing, so the first $n$ that exceeds $500$ is the answer."),
        (r"Answer: $16$ terms.",
         r"Check the one below to be sure it fails - that is what 'first exceeds' demands."),
    ],
    pitfalls=[r"Solving $2n^2 + n = 500$ and rounding down to $15$.",
              r"Forgetting that $n$ must be a positive integer and quoting a decimal."],
    takeaway=r"For 'first exceeds' questions, solve approximately then test the two neighbouring integers."),

"SEQ-10": Sol(
    idea=r"The first three terms give a quadratic in $r$; the positivity condition picks one root.",
    steps=[
        (r"Write the sum of three terms: $2 + 2r + 2r^2 = 14$.",
         r"Terms are $a$, $ar$, $ar^2$ with $a = 2$."),
        (r"Divide by $2$ and rearrange: $r^2 + r - 6 = 0$.",
         r"Dividing first keeps the numbers small."),
        (r"Factorise: $(r+3)(r-2) = 0$, so $r = 2$ or $r = -3$. The condition $r > 0$ gives $r = 2$.",
         r"The question's restriction exists precisely to discard the negative root."),
        (r"Sum five terms: $S_5 = 2\dfrac{2^5 - 1}{2-1} = 2 \times 31 = 62$.",
         r"$2^5 = 32$, so the bracket is $31$."),
    ],
    pitfalls=[r"Using $r = -3$ and getting $S_5 = 2 \times \frac{-243-1}{-4} = 122$.",
              r"Adding two more terms by hand and slipping: $2 + 4 + 8 + 16 + 32 = 62$ is a good check."],
    takeaway=r"Conditions like '$r > 0$' are there to select between roots - apply them before continuing."),

"SEQ-11": Sol(
    idea=r"A ratio of two triangular numbers. The answer depends on $n$, so the constant options can be eliminated immediately.",
    steps=[
        (r"Write both sums: $S = \dfrac{n(n+1)}{2}$ and the sum to $2n$ is $\dfrac{2n(2n+1)}{2} = n(2n+1)$.",
         r"Use $1 + 2 + \cdots + m = \frac{m(m+1)}{2}$ with $m = n$ and $m = 2n$."),
        (r"Form the ratio: $k = \dfrac{n(2n+1)}{\frac{n(n+1)}{2}}$.",
         r"$k$ is defined by 'sum to $2n$' $= k \times$ 'sum to $n$'."),
        (r"Simplify: multiply top and bottom by $2$ and cancel $n$: $k = \dfrac{2n(2n+1)}{n(n+1)} = \dfrac{2(2n+1)}{n+1}$.",
         r"Cancelling $n$ is legitimate since $n \geq 1$."),
        (r"Sanity check with $n = 1$: sums are $1$ and $3$, so $k = 3$; the formula gives $\frac{2 \times 3}{2} = 3$ ✓.",
         r"A single numerical check rules out all the other options at once."),
    ],
    pitfalls=[r"Answering $k = 4$ because 'doubling $n$ roughly quadruples a quadratic' - true in the limit, false for finite $n$.",
              r"Forgetting the factor $2$ when dividing by a fraction."],
    takeaway=r"When the options are a mix of constants and formulas, substitute a small value of $n$ - it eliminates most of them instantly."),

"SEQ-12": Sol(
    idea=r"Convergence of a geometric series depends only on $|r| < 1$. Compute $r$ for each and apply the test.",
    steps=[
        (r"I: $r = \frac{0.9}{1} = 0.9$, and $|0.9| < 1$: **converges**.",
         r"A ratio just below $1$ still converges, though slowly."),
        (r"II: $r = \frac{-3}{3} = -1$, and $|-1| = 1$ is not less than $1$: **does not converge**.",
         r"The partial sums oscillate between $3$ and $0$ forever - they never settle, so there is no sum to infinity."),
        (r"III: $r = \frac{10}{100} = 0.1$: **converges**.",
         r"Small ratio, rapid convergence."),
        (r"I and III only.",
         r"Match the verdicts to the option list."),
    ],
    pitfalls=[r"Thinking II converges to $0$ or to $1.5$ because the terms 'average out' - the partial sums must approach a single limit.",
              r"Judging by the size of the terms rather than the ratio: III starts at $100$ but converges fastest."],
    takeaway=r"Convergence is decided by $|r| < 1$ alone - not by the size of the first term or by whether the terms alternate."),

"SEQ-13": Sol(
    idea=r"Two terms give $a$ and $d$; then solve an inequality for $n$ and round to the correct integer.",
    steps=[
        (r"Subtract the two facts: $u_8 - u_3 = 5d = 25 - 10 = 15$, so $d = 3$.",
         r"From $u_3$ to $u_8$ is five steps, so the difference is $5d$ - count the gaps, not the terms."),
        (r"Find $a$: $u_3 = a + 2d = 10$, so $a = 10 - 6 = 4$.",
         r"The third term is $a + 2d$, not $a + 3d$."),
        (r"Write the general term: $u_n = 4 + 3(n-1) = 3n + 1$.",
         r"Simplify before solving - it avoids bracket errors."),
        (r"Solve $3n + 1 > 100 \Rightarrow n > 33$, so the smallest integer is $n = 34$.",
         r"Strict inequality: $n = 33$ gives exactly $100$, which is not greater than $100$."),
    ],
    pitfalls=[r"Answering $33$, where $u_{33} = 100$ exactly.",
              r"Using $u_8 - u_3 = 8d - 3d$ correctly but then $u_3 = a + 3d$ incorrectly."],
    takeaway=r"$u_p$ to $u_q$ spans $q - p$ common differences; and 'greater than' excludes the boundary case."),

"SEQ-14": Sol(
    idea=r"A quadratic sequence. Completing the square finds the minimum - but $n$ must be a positive integer, so check that the optimum is attainable.",
    steps=[
        (r"Complete the square: $n^2 - 10n + 30 = (n - 5)^2 + 5$.",
         r"Half of $-10$ is $-5$; $30 - 25 = 5$."),
        (r"The square is smallest when $n = 5$, giving $u_5 = 5$.",
         r"$(n-5)^2 \geq 0$ with equality only at $n = 5$."),
        (r"$n = 5$ is a positive integer, so the minimum is attained: the smallest term is $5$.",
         r"If the vertex had been at a non-integer (say $4.5$), you would have to test the integers either side."),
    ],
    pitfalls=[r"Giving $n = 5$ (the position) instead of $5$ (the value) - here they coincide, which hides the error.",
              r"Taking $u_1 = 21$ as the smallest by assuming sequences always increase."],
    takeaway=r"Minimise a quadratic sequence by completing the square, then check the nearest **integer** values of $n$."),

"SEQ-15": Sol(
    idea=r"Sigma notation hiding a geometric series. Write out the first term and the ratio, and count the terms carefully.",
    steps=[
        (r"Write out the start: $k = 1$ gives $3 \times 2 = 6$; $k = 2$ gives $12$. So $a = 6$, $r = 2$.",
         r"The first term is the value at the **lower limit**, not $3$."),
        (r"Count the terms: $k$ runs from $1$ to $10$, which is $10$ terms.",
         r"Upper minus lower plus one."),
        (r"Apply the sum formula: $S_{10} = 6\dfrac{2^{10} - 1}{2 - 1} = 6 \times 1023$.",
         r"$2^{10} = 1024$ is worth knowing by heart."),
        (r"Evaluate: $6138$.",
         r"$6 \times 1000 = 6000$ plus $6 \times 23 = 138$."),
    ],
    pitfalls=[r"Taking $a = 3$ (ignoring the $k = 1$ factor of $2$), giving $3069$.",
              r"Using $2^{10}$ instead of $2^{10} - 1$, giving $6144$."],
    takeaway=r"In $\sum a r^k$ the first term is the value at the lower limit; count terms as (upper $-$ lower $+ 1$)."),

"SEQ-16": Sol(
    idea=r"Two sums give two equations in $a$ and $d$. Subtracting eliminates $a$ - and only $d$ is wanted.",
    steps=[
        (r"$S_{10} = \frac{10}{2}\left[2a + 9d\right] = 145$, so $2a + 9d = 29$.",
         r"Divide out the $\frac n2$ factor straight away to keep the equations clean."),
        (r"$S_{20} = \frac{20}{2}\left[2a + 19d\right] = 490$, so $2a + 19d = 49$.",
         r"Same formula with $n = 20$."),
        (r"Subtract: $10d = 20$, so $d = 2$.",
         r"The $2a$ terms are identical in both equations, so subtraction removes them at once."),
    ],
    pitfalls=[r"Using $(n-1)d$ as $10d$ and $20d$ rather than $9d$ and $19d$.",
              r"Dividing $490$ by $20$ instead of by $10$."],
    takeaway=r"Two sums, two unknowns: write both in the $2a + (n-1)d$ form and subtract to eliminate $a$."),

"SEQ-17": Sol(
    idea=r"A classic bouncing-ball problem: the ball goes down **and** up. Two geometric series, or one with a correction.",
    steps=[
        (r"Downward distances: $10, 6, 3.6, \ldots$ - geometric with $a = 10$, $r = \frac35$. Sum $= \dfrac{10}{1 - \frac35} = 25$.",
         r"After each bounce it falls from the new height, so every rise is matched by an equal fall."),
        (r"Upward distances: $6, 3.6, \ldots$ - the same series without the initial $10$. Sum $= 25 - 10 = 15$.",
         r"The ball never rises $10$ m: the first rise is $6$ m, so the up-series starts one term later."),
        (r"Total: $25 + 15 = 40$ m.",
         r"Add the two, or use $2 \times 25 - 10 = 40$ (double everything, then remove the un-matched first drop)."),
    ],
    pitfalls=[r"Answering $25$ by counting only the downward distances.",
              r"Answering $50$ by doubling without subtracting the initial drop."],
    takeaway=r"Distance travelled counts every metre in both directions: total $= 2S - (\text{first drop})$."),

"SEQ-18": Sol(
    idea=r"A recurrence that generates a familiar sequence. Compute terms, recognise the pattern, then verify it satisfies the rule.",
    steps=[
        (r"Generate terms: $u_1 = 1$, $u_2 = 1 + 3 = 4$, $u_3 = 4 + 5 = 9$, $u_4 = 9 + 7 = 16$.",
         r"The increments $3, 5, 7$ are the odd numbers - a strong hint."),
        (r"Recognise $1, 4, 9, 16$ as the squares: conjecture $u_n = n^2$.",
         r"Pattern-spotting is legitimate here because the options let you verify."),
        (r"Verify against the recurrence: if $u_n = n^2$ then $u_n + 2n + 1 = n^2 + 2n + 1 = (n+1)^2 = u_{n+1}$ ✓.",
         r"This is the crucial step: checking the formula satisfies the rule turns a guess into a proof."),
    ],
    pitfalls=[r"Choosing $2n - 1$ (the increments) instead of the terms themselves.",
              r"Testing only $u_1$, which several options match."],
    takeaway=r"Spot the pattern from a few terms, then prove it by substituting into the recurrence."),

"SEQ-19": Sol(
    idea=r"Three consecutive geometric terms: the middle one squared equals the product of its neighbours. That single equation finds $x$.",
    steps=[
        (r"Use the geometric condition $\dfrac{x+6}{x} = \dfrac{x+15}{x+6}$, i.e. $(x+6)^2 = x(x+15)$.",
         r"Consecutive terms have a constant ratio, so equating the two ratios gives the condition $b^2 = ac$."),
        (r"Expand: $x^2 + 12x + 36 = x^2 + 15x$.",
         r"The $x^2$ terms cancel, leaving a linear equation - which is why this method is quick."),
        (r"Solve: $36 = 3x$, so $x = 12$.",
         r"The terms are $12, 18, 27$."),
        (r"Find $r = \frac{18}{12} = \frac32$ and the fourth term $27 \times \frac32 = \frac{81}{2}$.",
         r"The ratio need not be an integer; leave the answer as an improper fraction."),
    ],
    pitfalls=[r"Assuming the common ratio is $\frac{x+6}{x+15}$ (upside down).",
              r"Stopping at the third term $27$ or giving the ratio instead of the fourth term."],
    takeaway=r"Three terms in geometric progression satisfy $b^2 = ac$; the $x^2$ terms always cancel, leaving a linear equation."),

"SEQ-20": Sol(
    idea=r"A counting-and-summing problem needing inclusion-exclusion: multiples of $15$ belong to both lists and would otherwise be counted twice.",
    steps=[
        (r"Multiples of $3$ up to $100$: $3 + 6 + \cdots + 99 = 3(1 + 2 + \cdots + 33) = 3 \times \frac{33 \times 34}{2} = 3 \times 561 = 1683$.",
         r"Factor out the $3$ so the bracket is a plain triangular number."),
        (r"Multiples of $5$: $5(1 + \cdots + 20) = 5 \times 210 = 1050$.",
         r"$\lfloor 100/5 \rfloor = 20$ terms."),
        (r"Multiples of both, i.e. of $15$: $15(1 + \cdots + 6) = 15 \times 21 = 315$.",
         r"'Or' in mathematics includes 'both', and multiples of $15$ have been counted in each of the first two sums."),
        (r"Inclusion-exclusion: $1683 + 1050 - 315 = 2418$.",
         r"Add the two sets, subtract the overlap once."),
    ],
    pitfalls=[r"Forgetting to subtract the multiples of $15$, giving $2733$ - which is offered.",
              r"Using $\text{lcm}(3,5) = 8$ or $30$ instead of $15$."],
    takeaway=r"For 'multiples of $a$ or $b$', subtract the multiples of $\text{lcm}(a,b)$ once."),

"SEQ-21": Sol(
    idea=r"A recurrence converging to a limit. Compute terms for intuition, then prove the two general claims and verify the closed form.",
    steps=[
        (r"Generate terms: $u_1 = 3$, $u_2 = \frac{3+5}{2} = 4$, $u_3 = 4.5$, $u_4 = 4.75$ - rising towards $5$.",
         r"The rule averages $u_n$ with $5$, so each term sits halfway between the previous one and $5$."),
        (r"II: show $u_n < 5$ always. If $u_n < 5$ then $u_{n+1} = \frac{u_n + 5}{2} < \frac{5+5}{2} = 5$; and $u_1 = 3 < 5$. **True.**",
         r"This is an induction argument in miniature: true at the start, and preserved by the rule."),
        (r"I: $u_{n+1} - u_n = \frac{u_n + 5}{2} - u_n = \frac{5 - u_n}{2} > 0$ because $u_n < 5$. So the sequence increases. **True.**",
         r"Compute the difference algebraically rather than relying on the first few terms; it also shows *why* it increases - the gap to $5$ is always positive."),
        (r"III: test $5 - 2^{2-n}$: at $n=1$ it gives $5 - 2 = 3$ ✓, and $\frac{(5 - 2^{2-n}) + 5}{2} = 5 - 2^{1-n}$, which is the formula at $n+1$ ✓. **True.**",
         r"Check the starting value **and** that the formula satisfies the recurrence - both are needed."),
        (r"All three are true.",
         r"Match to the options."),
    ],
    pitfalls=[r"Concluding II from the first four terms alone - the general argument is what makes it certain.",
              r"Checking III only at $n = 1$; many formulas share a first term."],
    takeaway=r"To prove a claim about every term: check the first case, then show the recurrence preserves the property."),

}
