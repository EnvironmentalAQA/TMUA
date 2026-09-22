"""Full teaching solutions: binomial expansion (BIN-xx)."""
from gen.model import Sol

SOLUTIONS = {

"BIN-01": Sol(
    idea=r"A single coefficient from $(a + bx)^n$. Use the general term rather than expanding the whole thing.",
    steps=[
        (r"Write the general term: $\binom{5}{r} 2^{5-r}(3x)^r$.",
         r"Every term of $(a+b)^n$ has the form $\binom nr a^{n-r}b^r$; the powers of the two parts always add to $n$."),
        (r"For $x^3$ take $r = 3$: $\binom53 2^{2}(3x)^3$.",
         r"The power of $x$ comes only from the second bracket, so $r$ is the power you want."),
        (r"Evaluate each factor: $\binom53 = 10$, $2^2 = 4$, $3^3 = 27$.",
         r"Keep them separate - combining too early is where slips happen."),
        (r"Multiply: $10 \times 4 \times 27 = 1080$.",
         r"$10 \times 108 = 1080$."),
    ],
    pitfalls=[r"Forgetting the $2^{2}$ and answering $270$.",
              r"Using $3^3 = 9$ or cubing only the $x$, giving $360$ - both are offered."],
    takeaway=r"The general term $\binom nr a^{n-r}b^r$ carries **three** factors: the binomial coefficient and a power of each part."),

"BIN-02": Sol(
    idea=r"A coefficient is given and a constant inside the bracket is unknown. Set up the coefficient equation and solve.",
    steps=[
        (r"General term of $(1 + kx)^6$: $\binom6r (kx)^r$, so the $x^2$ coefficient is $\binom62 k^2$.",
         r"The $1^{6-r}$ factor is invisible, which is why this form is the easiest to work with."),
        (r"Compute $\binom62 = 15$, so the equation is $15k^2 = 60$.",
         r"$\binom62 = \frac{6 \times 5}{2} = 15$."),
        (r"Solve: $k^2 = 4$, so $k = \pm 2$; the condition $k > 0$ gives $k = 2$.",
         r"Squaring means two roots; the stated condition selects one."),
    ],
    pitfalls=[r"Forgetting to square $k$ and solving $15k = 60$ to get $k = 4$ - which is offered.",
              r"Using $\binom62 = 30$ (that is $6 \times 5$ without dividing by $2$)."],
    takeaway=r"The $x^r$ coefficient of $(1 + kx)^n$ is $\binom nr k^r$ - the constant is raised to the same power as $x$."),

"BIN-03": Sol(
    idea=r"'Term independent of $x$' means the power of $x$ is zero. Track the power of $x$ in the general term and solve for $r$.",
    steps=[
        (r"General term: $\binom6r (x^2)^{6-r}\left(\frac2x\right)^r = \binom6r 2^r x^{12 - 2r - r}$.",
         r"$(x^2)^{6-r}$ gives $x^{12-2r}$ and $\left(\frac2x\right)^r$ gives $2^r x^{-r}$; combine the powers."),
        (r"So the power of $x$ is $12 - 3r$.",
         r"Getting this expression right is the whole question."),
        (r"Set it to zero: $12 - 3r = 0$, so $r = 4$.",
         r"'Independent of $x$' means $x^0$."),
        (r"Evaluate the term: $\binom64 \times 2^4 = 15 \times 16 = 240$.",
         r"$\binom64 = \binom62 = 15$ by symmetry."),
    ],
    pitfalls=[r"Using the power $12 - 2r$ and getting $r = 6$, giving $2^6 = 64$.",
              r"Forgetting the $2^r$ factor and answering $15$."],
    takeaway=r"Write the power of $x$ in the general term as a linear expression in $r$, then set it to the value you need."),

"BIN-04": Sol(
    idea=r"Sum of all coefficients: substitute $x = 1$. No expansion needed at all.",
    steps=[
        (r"Note that setting $x = 1$ makes every power of $x$ equal to $1$, so the expansion collapses to the sum of its coefficients.",
         r"If $(3x-2)^7 = \sum c_k x^k$ then putting $x = 1$ gives $\sum c_k$."),
        (r"Evaluate the original expression at $x = 1$: $(3 - 2)^7 = 1^7 = 1$.",
         r"You never need a single coefficient."),
    ],
    pitfalls=[r"Expanding and trying to add eight terms under time pressure.",
              r"Substituting $x = 0$, which gives only the constant term $(-2)^7 = -128$ - an offered option."],
    takeaway=r"$f(1)$ is the sum of the coefficients; $f(0)$ is the constant term; $f(-1)$ is the alternating sum."),

"BIN-05": Sol(
    idea=r"A short calculation made trivial by the symmetry of binomial coefficients.",
    steps=[
        (r"Use the symmetry $\binom nr = \binom n{n-r}$: since $3 + 7 = 10$, $\binom{10}{3} = \binom{10}{7}$.",
         r"Choosing $3$ objects from $10$ is the same as choosing which $7$ to leave behind."),
        (r"So the first two terms cancel, leaving $\binom92$.",
         r"Spotting the cancellation avoids computing $120$ twice."),
        (r"Evaluate $\binom92 = \frac{9 \times 8}{2} = 36$.",
         r"$\binom n2 = \frac{n(n-1)}{2}$."),
    ],
    pitfalls=[r"Computing all three coefficients and mis-adding, e.g. $120 - 120 + 36$ done as $156$.",
              r"Thinking $\binom{10}{3} - \binom{10}{7}$ is $\binom{10}{-4}$ or similar."],
    takeaway=r"$\binom nr = \binom n{n-r}$: look for pairs whose lower entries add to $n$."),

"BIN-06": Sol(
    idea=r"Two equal binomial coefficients from the same row. Symmetry gives the answer without computing factorials.",
    steps=[
        (r"The condition is $\binom n4 = \binom n5$.",
         r"In $(1+x)^n$ the coefficient of $x^r$ is $\binom nr$."),
        (r"Within one row of Pascal's triangle, two different entries are equal only when they are symmetric partners: $\binom nr = \binom ns$ with $r \neq s$ forces $r + s = n$.",
         r"The row rises to a single peak and falls symmetrically, so equal values are mirror images."),
        (r"Hence $n = 4 + 5 = 9$.",
         r"Check: $\binom94 = 126 = \binom95$ ✓."),
    ],
    pitfalls=[r"Setting up the factorial equation and mis-cancelling to get $n = 10$ or $n = 8$.",
              r"Assuming $n = 5$ because the coefficients 'stop' there."],
    takeaway=r"Equal entries in the same row of Pascal's triangle are symmetric partners: $r + s = n$."),

"BIN-07": Sol(
    idea=r"A product of a binomial expansion with a linear factor. Only two products can give $x^2$, so collect just those.",
    steps=[
        (r"Expand $(1-2x)^4$: coefficients $\binom4r(-2)^r$ give $1 - 8x + 24x^2 - 32x^3 + 16x^4$.",
         r"$\binom41(-2) = -8$ and $\binom42(-2)^2 = 6 \times 4 = 24$; remember to raise the $-2$ to the power as well."),
        (r"To make $x^2$ in the product, pair $1 \times 24x^2$ and $3x \times (-8x)$.",
         r"Degrees must add to $2$: $(0, 2)$ and $(1, 1)$ are the only options."),
        (r"Add: $24 + (-24) = 0$.",
         r"The two contributions cancel exactly - the answer is $0$, not 'no term'."),
    ],
    pitfalls=[r"Taking the $x^2$ coefficient of $(1-2x)^4$ as $+24$ but forgetting the $3x \times (-8x)$ contribution, giving $24$.",
              r"Sign error making $(-2)^2 = -4$."],
    takeaway=r"For a coefficient in a product, list the degree pairs that add to the target and sum their contributions."),

"BIN-08": Sol(
    idea=r"Two coefficients, two unknowns ($a$ and $n$). Dividing the equations cleverly eliminates $a$.",
    steps=[
        (r"Write the first two coefficients: $\binom n1 a = na = 12$ and $\binom n2 a^2 = \frac{n(n-1)}{2}a^2 = 54$.",
         r"The expansion of $(1+ax)^n$ starts $1 + nax + \frac{n(n-1)}{2}a^2x^2$."),
        (r"Square the first equation: $n^2a^2 = 144$.",
         r"Squaring makes the power of $a$ match the second equation, so dividing will cancel it."),
        (r"Divide the second by this: $\dfrac{n(n-1)a^2/2}{n^2a^2} = \dfrac{n-1}{2n} = \dfrac{54}{144} = \dfrac38$.",
         r"Both $a^2$ and one factor of $n$ cancel."),
        (r"Cross-multiply: $8(n-1) = 6n \Rightarrow 8n - 8 = 6n \Rightarrow n = 4$.",
         r"Then $a = 3$; check $\binom42 \times 9 = 6 \times 9 = 54$ ✓."),
    ],
    pitfalls=[r"Dividing the second equation by the first (not its square), which leaves an $a$ behind and stalls.",
              r"Using $\binom n2 = \frac{n^2}{2}$."],
    takeaway=r"To eliminate a constant that appears to different powers, raise one equation to the matching power first, then divide."),

"BIN-09": Sol(
    idea=r"Three standard properties of binomial coefficients. Each has a one-line reason and a one-line check.",
    steps=[
        (r"I: $\binom nr = \binom n{n-r}$ - choosing $r$ objects is the same as choosing the $n-r$ to leave. **True.**",
         r"Visible as the left-right symmetry of each row of Pascal's triangle."),
        (r"II: $\binom nr + \binom n{r+1} = \binom{n+1}{r+1}$ - Pascal's rule, i.e. each entry is the sum of the two above it. **True.**",
         r"Check with numbers: $\binom32 + \binom33 = 3 + 1 = 4 = \binom43$ ✓."),
        (r"III: $\sum_{r=0}^n \binom nr = 2^n$ - put $x = 1$ in $(1+x)^n$. **True.**",
         r"Equivalently, a set with $n$ elements has $2^n$ subsets, counted by size."),
        (r"All three: 'I, II and III'.",
         r"Match to the options."),
    ],
    pitfalls=[r"Doubting Pascal's rule because of the index shift on the right - test it with small numbers.",
              r"Thinking the sum in III is $2^{n+1}$ by miscounting the $n+1$ terms."],
    takeaway=r"Symmetry, Pascal's rule and row sum $2^n$ are the three facts about $\binom nr$ worth knowing cold."),

"BIN-10": Sol(
    idea=r"Two binomials with the same bracket: combine the powers first, then use a single coefficient.",
    steps=[
        (r"Combine: $(1+x)^3(1+x)^4 = (1+x)^7$.",
         r"Same base, so add the indices - this converts a product of expansions into one expansion."),
        (r"The coefficient of $x^5$ is $\binom75$.",
         r"Standard general term with $r = 5$."),
        (r"Evaluate using symmetry: $\binom75 = \binom72 = \frac{7 \times 6}{2} = 21$.",
         r"Computing $\binom72$ is quicker than $\binom75$ and gives the same value."),
    ],
    pitfalls=[r"Multiplying the separate expansions term by term and mis-collecting.",
              r"Multiplying the coefficients $\binom35$ and $\binom45$ - both of which are zero, and neither is relevant."],
    takeaway=r"Combine equal brackets before expanding; then one binomial coefficient does the whole job."),

"BIN-11": Sol(
    idea=r"Adding conjugate expansions. The odd-power terms cancel, so you only need the even ones - and the surds disappear.",
    steps=[
        (r"Expand both with the binomial theorem. Their terms are identical except that odd powers of $1$ and $-1$ alternate in sign.",
         r"$(\sqrt2 + 1)^4$ and $(\sqrt2 - 1)^4$ differ only in the sign of the odd-numbered terms."),
        (r"Adding doubles the even-power terms and cancels the odd ones: $2\left[(\sqrt2)^4 + \binom42(\sqrt2)^2 + 1\right]$.",
         r"The terms kept are $r = 0, 2, 4$ in $\binom4r(\sqrt2)^{4-r}$ - exactly those with an even power of $\sqrt2$, which are rational."),
        (r"Evaluate: $(\sqrt2)^4 = 4$, $\binom42(\sqrt2)^2 = 6 \times 2 = 12$, and $1$.",
         r"$(\sqrt2)^2 = 2$ and $(\sqrt2)^4 = 4$."),
        (r"Total: $2(4 + 12 + 1) = 2 \times 17 = 34$.",
         r"Rational, as expected - a sure sign the cancellation was done correctly."),
    ],
    pitfalls=[r"Forgetting the factor $2$ and answering $17$.",
              r"Keeping a surd term and choosing $34 + 24\sqrt2$, which is $(\sqrt2+1)^4$ alone."],
    takeaway=r"Adding conjugate binomials kills the odd terms, leaving a rational answer - expand only the even ones."),

"BIN-12": Sol(
    idea=r"Which powers of $x$ actually occur. Find the general power as an expression in $r$ and see which target values it can hit.",
    steps=[
        (r"General term: $\binom9r (2x)^{9-r}\left(-x^{-2}\right)^r$, whose power of $x$ is $(9 - r) + (-2r) = 9 - 3r$.",
         r"Add the powers contributed by each bracket; the $-\frac{1}{x^2}$ contributes $-2$ per copy."),
        (r"As $r$ runs from $0$ to $9$, the power takes the values $9, 6, 3, 0, -3, -6, -9, -12, -15, -18$.",
         r"They step down by $3$ - so only multiples of $3$ appear, all the way down to $-18$."),
        (r"$k = 0$ needs $r = 3$ ✓; $k = 3$ needs $r = 2$ ✓; $k = -6$ needs $r = 5$ ✓.",
         r"Each value of $r$ must be a whole number between $0$ and $9$ - that is the only restriction."),
        (r"All three occur: 'I, II and III'.",
         r"Solve $9 - 3r = k$ for each target and check that $r$ is a valid index."),
    ],
    pitfalls=[r"Forgetting that the second bracket contributes $x^{-2r}$, not $x^{-r}$.",
              r"Assuming negative powers cannot appear because it is a 'binomial expansion'."],
    takeaway=r"Express the power of $x$ as a linear function of $r$; a term exists exactly when the required $r$ is an integer in range."),

"BIN-13": Sol(
    idea=r"An approximation with a small quantity. The binomial expansion converges fast because $0.01$ is tiny.",
    steps=[
        (r"Write $1.01^5 = (1 + 0.01)^5$ and expand: $1 + 5(0.01) + 10(0.01)^2 + 10(0.01)^3 + \ldots$",
         r"Coefficients from row 5 of Pascal's triangle: $1, 5, 10, 10, 5, 1$."),
        (r"Evaluate the terms: $1 + 0.05 + 0.001 + 0.00001 + \ldots$",
         r"$(0.01)^2 = 0.0001$, so the third term is $10 \times 0.0001 = 0.001$."),
        (r"Add as far as the 4-decimal-place accuracy requires: $1.05101\ldots \approx 1.0510$.",
         r"The fourth term only affects the fifth decimal place, so three terms suffice."),
    ],
    pitfalls=[r"Stopping after two terms and answering $1.0500$.",
              r"Mis-scaling $(0.01)^2$ as $0.001$, which gives $1.0600$-style errors."],
    takeaway=r"With a small $x$, each binomial term is much smaller than the last - take just enough terms for the required accuracy."),

"BIN-14": Sol(
    idea=r"A trinomial expansion. Counting the distinct terms is a counting problem: how many ways can the powers add to $4$?",
    steps=[
        (r"Every term has the form $x^ay^bz^c$ with $a + b + c = 4$ and $a, b, c \geq 0$.",
         r"Each of the four brackets contributes exactly one of $x$, $y$ or $z$, so the powers add to $4$."),
        (r"Count systematically by the value of $a$: if $a = 0$ then $b + c = 4$, giving $5$ pairs; $a = 1$ gives $4$; $a=2$ gives $3$; $a=3$ gives $2$; $a=4$ gives $1$.",
         r"For a fixed $a$, the number of $(b,c)$ pairs is $(4 - a) + 1$."),
        (r"Total: $5 + 4 + 3 + 2 + 1 = 15$.",
         r"A triangular number - the standard result $\binom{n+2}{2}$ for three variables, here $\binom62 = 15$."),
    ],
    pitfalls=[r"Answering $3^4 = 81$ - that counts the terms **before** collecting like terms.",
              r"Answering $5$ by counting only the powers of $x$."],
    takeaway=r"Distinct terms of $(x+y+z)^n$ correspond to solutions of $a+b+c=n$ in non-negative integers: $\binom{n+2}{2}$ of them."),

"BIN-15": Sol(
    idea=r"Two expansions added. Write both coefficients in factorial form and the sum simplifies remarkably.",
    steps=[
        (r"The $x^2$ coefficients are $\binom n2$ and $\binom{n+1}{2}$.",
         r"One from each expansion; the total coefficient of $x^2$ is their sum."),
        (r"Write them out: $\dfrac{n(n-1)}{2} + \dfrac{(n+1)n}{2} = \dfrac{n\left[(n-1) + (n+1)\right]}{2}$.",
         r"Factor out $\frac n2$ - the brackets then collapse."),
        (r"Simplify: $\dfrac{n \times 2n}{2} = n^2$.",
         r"A surprisingly clean result; recognising it makes the final step trivial."),
        (r"Solve $n^2 = 36$, so $n = 6$ (positive integer).",
         r"$n$ counts an index, so the negative root is rejected."),
    ],
    pitfalls=[r"Using Pascal's rule to write the sum as $\binom{n+1}{3}$ - that rule adds **adjacent** entries in the same row, not the same entry in different rows.",
              r"Taking $n = \pm 6$ and offering $-6$."],
    takeaway=r"$\binom n2 + \binom{n+1}{2} = n^2$: write coefficients in factorial form and look for common factors before solving."),

}
