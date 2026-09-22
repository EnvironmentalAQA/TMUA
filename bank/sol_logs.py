"""Full teaching solutions: exponentials and logarithms (LOG-xx)."""
from gen.model import Sol

SOLUTIONS = {

"LOG-01": Sol(
    idea=r"Combine everything into a single logarithm using the laws, then evaluate.",
    steps=[
        (r"Combine the first two: $\log_2 40 - \log_2 5 = \log_2\dfrac{40}{5} = \log_2 8$.",
         r"A difference of logs (same base) is the log of the quotient."),
        (r"Add the third: $\log_2 8 + \log_2\frac14 = \log_2\left(8 \times \frac14\right) = \log_2 2$.",
         r"A sum of logs is the log of the product. Note $\log_2\frac14$ is negative, so this step reduces the total."),
        (r"Evaluate: $\log_2 2 = 1$.",
         r"$\log_a a = 1$ for any valid base."),
    ],
    pitfalls=[r"Treating $\log_2\frac14$ as $+2$ rather than $-2$ and answering $5$.",
              r"Dividing the logarithms instead of subtracting them."],
    takeaway=r"$\log$ turns $\times$ into $+$ and $\div$ into $-$; combine into one log before evaluating."),

"LOG-02": Sol(
    idea=r"Solving $a^{kx} = b$. Take logs to the given base and simplify the right-hand side.",
    steps=[
        (r"Take $\log_3$ of both sides: $\log_3 3^{2x} = \log_3 4$, so $2x = \log_3 4$.",
         r"$\log_3 3^{u} = u$ - logs and exponentials with the same base undo each other."),
        (r"Rewrite the right-hand side: $\log_3 4 = \log_3 2^2 = 2\log_3 2$.",
         r"The power law $\log a^k = k\log a$ brings the exponent down."),
        (r"Divide by $2$: $x = \log_3 2$.",
         r"The factor $2$ cancels exactly, which is why the answer is so clean."),
    ],
    pitfalls=[r"Stopping at $x = \frac12\log_3 4$ and then mis-simplifying to $\frac12 \log_3 2$.",
              r"Writing $\log_3 4 = \log_3 2 \times \log_3 2$."],
    takeaway=r"$\log a^k = k \log a$; rewriting numbers as powers often makes fractions cancel."),

"LOG-03": Sol(
    idea=r"A hidden quadratic in $2^x$. The middle term needs rewriting before the substitution is visible.",
    steps=[
        (r"Rewrite the middle term: $3 \cdot 2^{x+2} = 3 \cdot 2^2 \cdot 2^x = 12 \cdot 2^x$.",
         r"$2^{x+2} = 2^x \times 4$ - separating the constant part is essential before substituting."),
        (r"Substitute $y = 2^x$, noting $2^{2x} = y^2$: $y^2 - 12y + 32 = 0$.",
         r"$2^{2x} = (2^x)^2$; that is what makes it quadratic."),
        (r"Factorise: $(y-4)(y-8) = 0$, so $y = 4$ or $y = 8$.",
         r"Both are positive, so both give solutions for $x$."),
        (r"Convert back: $2^x = 4 \Rightarrow x = 2$; $2^x = 8 \Rightarrow x = 3$. Sum $= 5$.",
         r"The question asks for the sum of the $x$ values, not the $y$ values."),
    ],
    pitfalls=[r"Summing the $y$ values ($4 + 8 = 12$) - which is offered.",
              r"Reading $2^{x+2}$ as $2^x + 2$."],
    takeaway=r"$a^{x+k} = a^k a^x$: split off the constant before substituting, then convert the roots back to $x$."),

"LOG-04": Sol(
    idea=r"Break the expression apart with the log laws, then substitute the given values.",
    steps=[
        (r"Split the quotient and product: $\log_a\dfrac{x^2\sqrt y}{a} = \log_a x^2 + \log_a \sqrt y - \log_a a$.",
         r"Products become sums, quotients become differences."),
        (r"Bring the powers down: $2\log_a x + \frac12\log_a y - \log_a a$.",
         r"$\sqrt y = y^{1/2}$, so its log is $\frac12\log_a y$."),
        (r"Substitute $\log_a x = 3$, $\log_a y = 5$, $\log_a a = 1$: $6 + \frac52 - 1$.",
         r"$\log_a a = 1$ always - a fact worth having instantly available."),
        (r"Add: $\frac{12 + 5 - 2}{2} = \frac{15}{2}$.",
         r"Put everything over $2$."),
    ],
    pitfalls=[r"Forgetting $\log_a a = 1$ and answering $\frac{17}{2}$.",
              r"Using $\log_a\sqrt y = \sqrt{\log_a y}$."],
    takeaway=r"Expand fully with the three laws before substituting; $\log_a a = 1$ and $\log_a 1 = 0$."),

"LOG-05": Sol(
    idea=r"Combine the logs, convert to an equation, then **check the domain** - that is what this question is really testing.",
    steps=[
        (r"Combine: $\log_3\left[(x+6)(x-2)\right] = 2$.",
         r"Sum of logs is the log of the product."),
        (r"Convert to exponential form: $(x+6)(x-2) = 3^2 = 9$.",
         r"$\log_a N = c$ means $N = a^c$."),
        (r"Expand and solve: $x^2 + 4x - 12 = 9 \Rightarrow x^2 + 4x - 21 = 0 \Rightarrow (x+7)(x-3) = 0$, so $x = -7$ or $x = 3$.",
         r"Ordinary quadratic work."),
        (r"Check both in the **original** equation: $x = 3$ gives $\log_3 9 + \log_3 1$ ✓; $x = -7$ gives $\log_3(-1)$, which is undefined. So $x = 3$ only.",
         r"Logarithms of negative numbers (or zero) do not exist, so roots that break the original expression must be rejected."),
    ],
    pitfalls=[r"Giving both roots - the option '$x = -7$ or $x = 3$' exists precisely to catch this.",
              r"Checking only one of the two logarithms."],
    takeaway=r"Always substitute your solutions back: combining logs can create solutions the original equation never had."),

"LOG-06": Sol(
    idea=r"A translation of an exponential graph is also a stretch. The algebra shows why.",
    steps=[
        (r"Translating $3$ right replaces $x$ by $x - 3$: $y = 2^{x-3}$.",
         r"A shift to the right by $a$ substitutes $x - a$."),
        (r"Split the index: $2^{x-3} = 2^x \times 2^{-3} = \dfrac{1}{8}\cdot 2^x$.",
         r"$a^{m-n} = \frac{a^m}{a^n}$ - the translation has become multiplication by a constant."),
        (r"So the new graph is the old one stretched vertically by factor $\frac18$.",
         r"This is special to exponentials: horizontal translation and vertical stretch are the same thing."),
    ],
    pitfalls=[r"Writing $2^{x-3} = 2^x - 3$ and choosing that option.",
              r"Using $2^{+3} = 8$ as the factor, which corresponds to a shift to the **left**."],
    takeaway=r"$a^{x-k} = a^{-k}a^x$: for exponentials, translating horizontally is the same as stretching vertically."),

"LOG-07": Sol(
    idea=r"Three log 'laws', two of which are fabrications. Test each against the genuine rules.",
    steps=[
        (r"I: $\log(x+y)$ has no expansion. Test $x = y = 1$: $\log 2 \approx 0.30$ but $\log 1 + \log 1 = 0$. **False.**",
         r"The product law is $\log(xy) = \log x + \log y$; the sum inside is a different animal entirely."),
        (r"II: $\log(xy)^2 = 2\log(xy) = 2(\log x + \log y) = 2\log x + 2\log y$. **True.**",
         r"Power law first, then product law - both applied correctly."),
        (r"III: $\log x - \log y = \log\frac xy$, which is not the same as $\frac{\log x}{\log y}$. Test $x = 100$, $y = 10$: left $= 1$, right $= \frac21 = 2$. **False.**",
         r"Difference of logs is the log of a quotient, not the quotient of logs."),
        (r"II only.",
         r"Match to the options."),
    ],
    pitfalls=[r"Accepting I by analogy with the product law.",
              r"Accepting III because 'subtraction corresponds to division' - it does, but inside the log."],
    takeaway=r"The laws act on what is **inside** the log: $\log(xy)$, $\log\frac xy$, $\log x^k$. Nothing simplifies $\log(x+y)$."),

"LOG-08": Sol(
    idea=r"Two exponential facts that chain together. Raising the first to the power $y$ links them.",
    steps=[
        (r"Raise the first equation to the power $y$: $(5^x)^y = 2^y$, i.e. $5^{xy} = 2^y$.",
         r"$(a^x)^y = a^{xy}$ - this is what connects the two statements."),
        (r"Substitute the second fact: $2^y = 125$.",
         r"Given directly."),
        (r"Write $125$ as a power of $5$: $5^{xy} = 5^3$.",
         r"Both sides are now powers of $5$."),
        (r"Equate the indices: $xy = 3$.",
         r"Valid because $5^u$ is one-to-one."),
    ],
    pitfalls=[r"Trying to compute $x$ and $y$ separately as logarithms and getting stuck without a calculator.",
              r"Multiplying the two equations to get $10^{x+y} = 250$, which leads nowhere."],
    takeaway=r"To find a **product** of exponents, raise one equation to the other's exponent and chain the results."),

"LOG-09": Sol(
    idea=r"A quotient of two logs with the same base. Rewriting the numerator's argument as a power makes it cancel.",
    steps=[
        (r"Write $27 = 3^3$, so $\log_5 27 = \log_5 3^3 = 3\log_5 3$.",
         r"The power law applies to the argument, whatever the base of the log."),
        (r"Form the quotient: $\dfrac{3\log_5 3}{\log_5 3} = 3$.",
         r"The common factor $\log_5 3$ cancels (it is non-zero)."),
    ],
    pitfalls=[r"Subtracting to get $\log_5 24$ - a quotient of logs is not the log of a quotient.",
              r"Dividing the arguments to get $\frac{27}{3} = 9$ in log form."],
    takeaway=r"$\frac{\log_c a}{\log_c b} = \log_b a$: quotients of logs change the base, they do not divide the arguments."),

"LOG-10": Sol(
    idea=r"Quadratic in $2^x$ again, but this time one root must be rejected - which changes the count.",
    steps=[
        (r"Rewrite: $4^x = (2^2)^x = (2^x)^2$ and $2^{x+1} = 2\cdot 2^x$.",
         r"Get everything in terms of $2^x$ before substituting."),
        (r"Let $y = 2^x$: $y^2 + 2y - 8 = 0$, which factorises as $(y+4)(y-2) = 0$.",
         r"Standard quadratic."),
        (r"Reject $y = -4$: $2^x$ is positive for every real $x$, so it can never equal a negative number.",
         r"This is the crucial filter - exponentials are always strictly positive."),
        (r"From $y = 2$: $2^x = 2$, so $x = 1$. Exactly **one** real solution.",
         r"The question asks how many, so the count is the answer."),
    ],
    pitfalls=[r"Answering $2$ because the quadratic has two roots.",
              r"Rejecting $y = 2$ as well, and answering $0$."],
    takeaway=r"After substituting $y = a^x$, discard every root with $y \leq 0$ - then count what remains."),

"LOG-11": Sol(
    idea=r"Two different bases. The hint converts one to the other, after which it is a linear equation in $\log_2 x$.",
    steps=[
        (r"Use the given relation $\log_4 x = \frac12\log_2 x$.",
         r"It holds because $4 = 2^2$: it takes twice as many factors of $2$ as of $4$ to build $x$."),
        (r"Substitute: $\log_2 x + \frac12\log_2 x = 6$, i.e. $\frac32\log_2 x = 6$.",
         r"Both terms now involve the same quantity, so treat $\log_2 x$ as a single unknown."),
        (r"Solve for the log: $\log_2 x = 4$.",
         r"Multiply by $\frac23$."),
        (r"Convert: $x = 2^4 = 16$.",
         r"$\log_2 x = 4$ means $x = 2^4$."),
    ],
    pitfalls=[r"Solving $\log_2 x = 6$ and answering $64$ - which is offered (twice, as $64$ and $2^6$).",
              r"Adding the bases or the arguments instead of using the relation."],
    takeaway=r"Get every logarithm to the same base first; then it is ordinary algebra in that one quantity."),

"LOG-12": Sol(
    idea=r"Two points on an exponential curve. Dividing eliminates any constant and isolates a power of $a$.",
    steps=[
        (r"Write both facts: $a^2 = 12$ and $a^4 = 108$.",
         r"Substitute each point into $y = a^x$."),
        (r"Divide: $\dfrac{a^4}{a^2} = a^2 = \dfrac{108}{12} = 9$.",
         r"Dividing subtracts indices, giving a single power of $a$ - the standard move with two points."),
        (r"Solve: $a = 3$ (bases of exponentials are positive).",
         r"Reject $a = -3$: $y = a^x$ requires $a > 0$."),
    ],
    pitfalls=[r"Answering $9$ - that is $a^2$, not $a$.",
              r"Subtracting the $y$-values instead of dividing."],
    takeaway=r"Divide two points on an exponential curve; the index difference gives a clean power of the base."),

"LOG-13": Sol(
    idea=r"Express the number in terms of the given primes, then apply the log laws.",
    steps=[
        (r"Write $0.75 = \dfrac34$.",
         r"Decimals must become fractions of small numbers before the laws help."),
        (r"Split: $\log_{10}\frac34 = \log_{10}3 - \log_{10}4$.",
         r"Quotient law."),
        (r"Write $4 = 2^2$: $\log_{10}4 = 2\log_{10}2 = 2p$.",
         r"Only $\log 2$ and $\log 3$ are available, so every number must be built from $2$s and $3$s."),
        (r"Combine: $q - 2p$.",
         r"Substituting $\log_{10}3 = q$."),
    ],
    pitfalls=[r"Using $\log 4 = p^2$ or $= 2 + p$.",
              r"Getting the subtraction backwards and answering $2p - q$."],
    takeaway=r"Factorise the argument into the primes you have been given, then apply product/quotient/power laws."),

"LOG-14": Sol(
    idea=r"A double inequality in powers of $2$. Locate $1000$ between consecutive powers, then translate into conditions on $n$.",
    steps=[
        (r"Find where $1000$ sits: $2^9 = 512$ and $2^{10} = 1024$, so $2^9 < 1000 < 2^{10}$.",
         r"Powers of $2$ up to $1024$ are worth knowing by heart."),
        (r"The left condition $2^n < 1000$ requires $n \leq 9$.",
         r"$2^{10} = 1024 > 1000$, so $n = 10$ fails."),
        (r"The right condition $1000 < 2^{n+3}$ requires $n + 3 \geq 10$, i.e. $n \geq 7$.",
         r"$2^{9} = 512 < 1000$, so $n + 3 = 9$ (i.e. $n = 6$) fails."),
        (r"Combine: $7 \leq n \leq 9$, giving $n = 7, 8, 9$ - three integers.",
         r"Count the integers in the range, inclusive."),
    ],
    pitfalls=[r"Counting $9 - 7 = 2$ instead of $3$.",
              r"Using strict inequalities on $n$ where the powers allow equality."],
    takeaway=r"Convert conditions on $2^n$ into conditions on $n$ by comparing with the nearest powers, then count inclusively."),

"LOG-15": Sol(
    idea=r"Combine the logs; the algebraic fraction simplifies dramatically because the numerator factorises.",
    steps=[
        (r"Combine: $\log_2\dfrac{x^2-4}{x-2} = 3$.",
         r"Difference of logs is the log of the quotient."),
        (r"Factorise and cancel: $\dfrac{(x-2)(x+2)}{x-2} = x + 2$ (valid since $x \neq 2$).",
         r"The domain requires $x > 2$ for $\log_2(x-2)$ to exist, so cancelling is legitimate."),
        (r"Convert: $\log_2(x+2) = 3 \Rightarrow x + 2 = 8 \Rightarrow x = 6$.",
         r"$2^3 = 8$."),
        (r"Check the domain: $x = 6$ gives $x^2 - 4 = 32 > 0$ and $x - 2 = 4 > 0$ ✓.",
         r"Always verify against the original."),
    ],
    pitfalls=[r"Forgetting the domain and including a spurious negative solution.",
              r"Cancelling incorrectly to get $x - 2$ or $x^2 - 2$."],
    takeaway=r"Factorise before cancelling inside a log, and confirm every solution keeps all arguments positive."),

"LOG-16": Sol(
    idea=r"Three numerical tests. Nothing conceptual - just careful arithmetic with small powers.",
    steps=[
        (r"I: $x = 0$ gives $3^0 = 1$ and $2^{1} = 2$. Is $1 < 2$? Yes. **True.**",
         r"$a^0 = 1$ for any $a$."),
        (r"II: $x = 1$ gives $3^1 = 3$ and $2^2 = 4$. Is $3 < 4$? Yes. **True.**",
         r"Careful with the index $x + 1 = 2$."),
        (r"III: $x = 2$ gives $3^2 = 9$ and $2^3 = 8$. Is $9 < 8$? No. **False.**",
         r"$3^x$ has overtaken $2^{x+1}$ by here - exponential growth with the larger base always wins eventually."),
        (r"I and II only.",
         r"Match to the option list."),
    ],
    pitfalls=[r"Computing $2^{x+1}$ as $2^x + 1$.",
              r"Assuming the inequality holds for all $x$ because it holds for the first two."],
    takeaway=r"Substitute each value carefully; a larger base always overtakes eventually, whatever the head start."),

"LOG-17": Sol(
    idea=r"A quadratic in $3^x$ with a parameter. 'Exactly one real solution' is a condition on the **positive** roots, not simply on the discriminant.",
    steps=[
        (r"Substitute $y = 3^x$, noting $y > 0$: $y^2 - ky + 9 = 0$.",
         r"$9^x = (3^x)^2$. The restriction $y > 0$ is the heart of the question."),
        (r"The product of the roots is $9 > 0$, so the roots have the same sign; their sum is $k$, so both are positive exactly when $k > 0$.",
         r"Sum and product of roots decide the signs without solving."),
        (r"For exactly one value of $x$, we need exactly one positive root, which (given both roots share a sign) means a **repeated** root: discriminant $k^2 - 36 = 0$, so $k = \pm6$.",
         r"Two distinct positive roots would give two solutions for $x$; two negative roots would give none."),
        (r"Check the signs: $k = 6$ gives the repeated root $y = 3 > 0$, so $x = 1$ - exactly one solution. $k = -6$ gives $y = -3 < 0$, so no solutions at all. Hence $k = 6$.",
         r"The final sign check is what rules out $-6$, which is offered."),
    ],
    pitfalls=[r"Answering $\pm6$ from the discriminant alone.",
              r"Forgetting that $y$ must be positive and counting $y = -3$ as a solution."],
    takeaway=r"With $y = a^x$, translate conditions on $x$ into conditions on the **positive** roots in $y$, using sum and product to check signs."),

"LOG-18": Sol(
    idea=r"A chain of logarithms. Convert each statement to exponential form and substitute.",
    steps=[
        (r"$\log_a b = 2$ means $b = a^2$.",
         r"$\log_a b = c \Leftrightarrow a^c = b$."),
        (r"$\log_b c = 3$ means $c = b^3$.",
         r"Same conversion with the next pair."),
        (r"Substitute: $c = (a^2)^3 = a^6$.",
         r"Powers of powers multiply."),
        (r"Therefore $\log_a c = 6$.",
         r"Read the exponent straight off. (In general $\log_a c = \log_a b \times \log_b c = 2 \times 3$.)"),
    ],
    pitfalls=[r"Adding the values to get $5$.",
              r"Reading $(a^2)^3$ as $a^5$."],
    takeaway=r"Logarithms chain by multiplication: $\log_a c = \log_a b \times \log_b c$."),

"LOG-19": Sol(
    idea=r"Exponential decay. Build the model, then take logs - and be careful which expression the answer takes.",
    steps=[
        (r"Model: after $t$ hours the quantity is multiplied by $\left(\frac12\right)^{t/5}$, because $t/5$ half-lives have passed.",
         r"Dividing $t$ by the half-life counts how many halvings have occurred."),
        (r"Set it equal to $\frac{1}{10}$: $\left(\frac12\right)^{t/5} = \dfrac{1}{10}$.",
         r"'Falls to one tenth' is a statement about the multiplier."),
        (r"Take $\log_{10}$: $\dfrac t5\log_{10}\dfrac12 = \log_{10}\dfrac{1}{10} = -1$, i.e. $-\dfrac t5\log_{10}2 = -1$.",
         r"$\log\frac12 = -\log 2$ and $\log\frac1{10} = -1$; the two minus signs will cancel."),
        (r"Solve: $t = \dfrac{5}{\log_{10}2}$ (about $16.6$ hours).",
         r"Multiply both sides by $-\frac{5}{\log_{10}2}$."),
    ],
    pitfalls=[r"Answering $5\log_{10}2$ - the reciprocal, which would be under a second.",
              r"Sanity check: the quantity halves in $5$ h and $\frac1{10} < \frac18$, so $t$ must exceed $15$ h; $5\log_{10}2 \approx 1.5$ is obviously wrong."],
    takeaway=r"Set up the multiplier, take logs, and sanity-check the size of the answer against a couple of half-lives."),

}
