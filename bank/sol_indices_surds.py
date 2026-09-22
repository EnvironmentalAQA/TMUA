"""Full teaching solutions: indices and surds (IND-xx)."""
from gen.model import Sol

SOLUTIONS = {

"IND-01": Sol(
    idea=r"A pure index-laws question. Nothing here needs thought once you treat the numbers and the powers of $x$ as two separate bookkeeping jobs.",
    steps=[
        (r"Deal with the bracket first: $(2x^3)^4 = 2^4 x^{12} = 16x^{12}$.",
         r"A power outside a bracket multiplies **every** factor inside, so the $2$ is raised to the 4th power as well as the $x^3$. This is the step people skip."),
        (r"Multiply the numerator: $16x^{12} \times 8x^{-5} = 128x^{7}$.",
         r"Multiplying powers of the same base adds the indices: $12 + (-5) = 7$. The numbers just multiply normally."),
        (r"Divide by $4x^2$: $\dfrac{128x^{7}}{4x^{2}} = 32x^{5}$.",
         r"Dividing subtracts indices: $7 - 2 = 5$, and $128 \div 4 = 32$."),
    ],
    pitfalls=[r"Forgetting to raise the $2$ to the 4th power gives $2x^{12}$ at step 1 and the answer $4x^5$.",
              r"Subtracting instead of adding the $-5$ gives $x^{9}$ and the answer $32x^{9}$ - which is offered."],
    takeaway=r"Handle the number part and the index part separately, and always distribute an outside power over everything in the bracket."),

"IND-02": Sol(
    idea=r"A fractional **negative** index of a fraction. Three separate instructions are packed into $-\frac23$: invert, take the cube root, square.",
    steps=[
        (r"The minus sign inverts the fraction: $\left(\frac{27}{8}\right)^{-2/3} = \left(\frac{8}{27}\right)^{2/3}$.",
         r"$a^{-n} = \frac{1}{a^n}$, and the reciprocal of a fraction is the fraction turned upside down. Doing this first keeps the numbers small."),
        (r"Take the cube root of top and bottom: $\left(\frac{8}{27}\right)^{1/3} = \frac{2}{3}$.",
         r"$a^{m/n} = \left(\sqrt[n]{a}\right)^m$; rooting before powering keeps you working with $2$ and $3$ rather than $64$ and $729$."),
        (r"Square the result: $\left(\frac23\right)^2 = \frac49$.",
         r"The numerator $2$ in the index is the power."),
    ],
    pitfalls=[r"Treating the minus sign as making the answer negative gives $-\frac94$ or $-\frac49$; a negative index never makes a positive number negative.",
              r"Forgetting to square gives $\frac23$; forgetting to invert gives $\frac94$. All three are offered as options."],
    takeaway=r"Read a fractional index as three instructions - sign (invert), denominator (root), numerator (power) - and do them in that order."),

"IND-03": Sol(
    idea=r"An exponential equation where both sides can be written as powers of the **same** base. Once the bases match, the indices must be equal.",
    steps=[
        (r"Spot that $4 = 2^2$ and $8 = 2^3$.",
         r"Both numbers are powers of $2$, so the whole equation can be rewritten in base $2$ and the exponentials compared directly."),
        (r"Rewrite: $4^{x+1} = 2^{2(x+1)} = 2^{2x+2}$ and $8^{2x-3} = 2^{3(2x-3)} = 2^{6x-9}$.",
         r"$(a^m)^n = a^{mn}$: the outer index multiplies the whole inner index, so brackets are essential."),
        (r"Equate the indices: $2x + 2 = 6x - 9$, so $4x = 11$ and $x = \frac{11}{4}$.",
         r"$2^u = 2^v$ forces $u = v$ because $2^x$ is a one-to-one function (it never takes the same value twice)."),
    ],
    pitfalls=[r"Multiplying out as $3 \times 2x - 3$ instead of $3(2x - 3)$ loses the bracket and gives a different linear equation.",
              r"Writing $8 = 2^4$ (a slip) gives $x = \frac{7}{2}$, which is offered."],
    takeaway=r"Whenever an equation has different bases, look for a common base first; comparing indices is then legitimate because exponentials are one-to-one."),

"IND-04": Sol(
    idea=r"Rationalising a denominator of the form $p + q\sqrt{n}$. The tool is the difference of two squares, which turns the surd denominator into an integer.",
    steps=[
        (r"Multiply numerator and denominator by the conjugate $3 - 2\sqrt5$.",
         r"$(p + q\sqrt n)(p - q\sqrt n) = p^2 - q^2 n$, which contains no surd. Multiplying top and bottom by the same thing does not change the value."),
        (r"Denominator: $3^2 - (2\sqrt5)^2 = 9 - 4 \times 5 = -11$.",
         r"Square the **whole** second term, coefficient included: $(2\sqrt5)^2 = 4 \times 5$, not $2 \times 5$."),
        (r"Numerator: $5(3 - 2\sqrt5) = 15 - 10\sqrt5$.",
         r"Nothing subtle - just expand."),
        (r"Tidy the signs: $\dfrac{15 - 10\sqrt5}{-11} = \dfrac{-15 + 10\sqrt5}{11}$.",
         r"A negative denominator is not 'in the form $a + b\sqrt5$' with the usual convention, and both versions are offered, so the sign handling decides the mark."),
    ],
    pitfalls=[r"$(2\sqrt5)^2 = 10$ (forgetting to square the $2$) gives denominator $-1$ and a wildly different answer.",
              r"Leaving $\frac{15 - 10\sqrt5}{-11}$ and picking the option with $+11$ in the denominator but the wrong signs on top."],
    takeaway=r"Multiply by the conjugate, square the coefficient as well as the surd, then fix the sign of the denominator at the end."),

"IND-05": Sol(
    idea=r"Simplifying a sum of surds. They can only be combined once each is written as a multiple of the **same** surd.",
    steps=[
        (r"Pull out the largest square factor from each: $\sqrt{75} = \sqrt{25 \times 3} = 5\sqrt3$, $\sqrt{27} = \sqrt{9\times3} = 3\sqrt3$, $\sqrt{12} = \sqrt{4\times3} = 2\sqrt3$.",
         r"$\sqrt{ab} = \sqrt a\sqrt b$, so a perfect-square factor comes out as a whole number. All three reduce to multiples of $\sqrt3$, which is why the sum simplifies at all."),
        (r"Collect like terms: $5\sqrt3 - 3\sqrt3 + 2\sqrt3 = 4\sqrt3$.",
         r"Once every term has the same surd part, $\sqrt3$ behaves exactly like an algebraic $x$."),
    ],
    pitfalls=[r"Adding under one root sign: $\sqrt{75} - \sqrt{27} \neq \sqrt{48}$. Roots do not distribute over $+$ or $-$.",
              r"Using $\sqrt{75} = 3\sqrt5$ (wrong square factor) - always take out the **largest** square."],
    takeaway=r"Surds add only when their irrational parts match, so simplify each one fully before trying to combine."),

"IND-06": Sol(
    idea=r"Two standard surd manipulations in one: squaring a bracket and rationalising a reciprocal. The question then just asks you to keep track of the four integers.",
    steps=[
        (r"Square the bracket: $(2 + \sqrt3)^2 = 4 + 4\sqrt3 + 3 = 7 + 4\sqrt3$, so $a = 7$, $b = 4$.",
         r"Use $(x+y)^2 = x^2 + 2xy + y^2$ with $y = \sqrt3$, and remember $(\sqrt3)^2 = 3$ - that is what makes the rational part $4 + 3$."),
        (r"Rationalise the reciprocal: $\dfrac{1}{2+\sqrt3} \times \dfrac{2 - \sqrt3}{2-\sqrt3} = \dfrac{2-\sqrt3}{4 - 3} = 2 - \sqrt3$, so $c = 2$, $d = -1$.",
         r"The conjugate gives denominator $2^2 - 3 = 1$, which is why this particular reciprocal is so clean."),
        (r"Add: $7 + 4 + 2 + (-1) = 12$.",
         r"The question wants the sum, so the sign of $d$ matters."),
    ],
    pitfalls=[r"Taking $d = 1$ and getting $14$ - the rationalised form is $2 - \sqrt3$, so $d$ is negative.",
              r"Writing $(2+\sqrt3)^2 = 4 + 3 = 7$ (forgetting the cross term $2 \times 2 \times \sqrt3$)."],
    takeaway=r"$(a+\sqrt b)$ and $(a - \sqrt b)$ multiply to the integer $a^2 - b$; that single fact drives both halves of this question."),

"IND-07": Sol(
    idea=r"Roots disguised as indices. Convert every root to a fractional power and the question becomes adding and subtracting fractions.",
    steps=[
        (r"Rewrite the roots: $\sqrt x = x^{1/2}$ and $\sqrt[3]{x} = x^{1/3}$.",
         r"$\sqrt[n]{x} = x^{1/n}$. In index form the laws apply; in root form they do not."),
        (r"Combine: $\dfrac{x^2 \cdot x^{1/2}}{x^{1/3}} = x^{2 + \frac12 - \frac13}$.",
         r"Multiplication adds indices, division subtracts them - the three operations become one sum."),
        (r"Add the fractions over a common denominator $6$: $2 + \frac12 - \frac13 = \frac{12 + 3 - 2}{6} = \frac{13}{6}$.",
         r"$6$ is the lowest common denominator of $1$, $2$ and $3$; converting $2$ to $\frac{12}{6}$ is where slips happen."),
    ],
    pitfalls=[r"Adding the $\frac13$ instead of subtracting gives $x^{17/6}$, which is offered.",
              r"Forgetting to convert the whole number $2$ into sixths."],
    takeaway=r"Turn every root into a fractional index immediately; then all you are doing is arithmetic with fractions."),

"IND-08": Sol(
    idea=r"A hidden quadratic. The key observation is $9^x = (3^2)^x = (3^x)^2$, so the equation is quadratic in $3^x$.",
    steps=[
        (r"Write $9^x = (3^x)^2$ and substitute $y = 3^x$: $y^2 - 4y + 3 = 0$.",
         r"Spotting that one exponential is the square of the other is the whole question; without it there is no route in."),
        (r"Factorise: $(y - 1)(y - 3) = 0$, so $y = 1$ or $y = 3$.",
         r"Ordinary quadratic technique once the substitution is made."),
        (r"Undo the substitution: $3^x = 1 \Rightarrow x = 0$; $3^x = 3 \Rightarrow x = 1$.",
         r"$a^0 = 1$ for any $a$ - the root $y = 1$ is easy to lose because it looks trivial."),
    ],
    pitfalls=[r"Stopping at $y = 1, 3$ and offering those as the answers - the question asks for $x$, not $3^x$.",
              r"Rejecting $y = 1$ as 'not a real solution'. Only **non-positive** values of $y$ must be rejected, because $3^x > 0$ always."],
    takeaway=r"If an equation contains $a^{2x}$ and $a^x$, substitute $y = a^x$; afterwards discard only the roots with $y \leq 0$."),

"IND-09": Sol(
    idea=r"A telescoping sum. Each term rationalises to a difference of two surds, and almost everything cancels - so do not compute decimals.",
    steps=[
        (r"Rationalise each term: $\dfrac{1}{\sqrt2+1} = \sqrt2 - 1$, $\dfrac{1}{\sqrt3+\sqrt2} = \sqrt3 - \sqrt2$, $\dfrac{1}{2+\sqrt3} = 2 - \sqrt3$.",
         r"Each denominator has the form $\sqrt{n+1} + \sqrt n$ whose conjugate gives $(n+1) - n = 1$ - the denominators all become $1$, which is the point of the construction."),
        (r"Add them: $(\sqrt2 - 1) + (\sqrt3 - \sqrt2) + (2 - \sqrt3)$.",
         r"Write the terms in a line so the cancelling pairs are visible."),
        (r"Cancel: $\sqrt2$ with $-\sqrt2$, $\sqrt3$ with $-\sqrt3$, leaving $-1 + 2 = 1$.",
         r"This is a telescoping sum - the surds annihilate in pairs and only the two ends survive."),
    ],
    pitfalls=[r"Approximating numerically and choosing $\sqrt2$ or $\sqrt3$ because the total 'looks about right'.",
              r"Rationalising with the wrong conjugate sign, which flips one term and destroys the cancellation."],
    takeaway=r"$\dfrac{1}{\sqrt{n+1}+\sqrt n} = \sqrt{n+1} - \sqrt n$: recognise this and long chains of such fractions collapse instantly."),

"IND-10": Sol(
    idea=r"Powers with an unknown exponent. Factorising out the smallest power turns the expression into a number.",
    steps=[
        (r"Write every term with the common factor $2^n$: $2^{n+2} = 4\cdot 2^n$, $2^{n+1} = 2\cdot 2^n$.",
         r"$2^{n+k} = 2^k \cdot 2^n$. Choosing the *smallest* power ($2^n$) as the common factor makes every remaining factor a whole number."),
        (r"Substitute: $\dfrac{4\cdot2^n + 2^n}{2\cdot 2^n} = \dfrac{5 \cdot 2^n}{2\cdot 2^n}$.",
         r"Factorising the numerator is legitimate because both terms contain $2^n$."),
        (r"Cancel $2^n$: the value is $\frac52$, independent of $n$.",
         r"$2^n \neq 0$ for every $n$, so cancelling is always valid here."),
    ],
    pitfalls=[r"'Cancelling' the $n$'s in the indices, e.g. claiming $\frac{2^{n+2}}{2^{n+1}} = 2^{2}/2^{1}$ term by term across a sum - you cannot split a fraction over a sum in the denominator.",
              r"Answering $2^n$ because the $n$ 'has to appear somewhere'."],
    takeaway=r"With unknown exponents, factor out the lowest power; the $n$ almost always cancels and the answer is a plain number."),

"IND-11": Sol(
    idea=r"A symmetric surd expression. Computing $x^2$, $y^2$ and $xy$ separately is much cleaner than expanding everything, because the irrational parts cancel.",
    steps=[
        (r"$x^2 = (\sqrt7+\sqrt3)^2 = 7 + 2\sqrt{21} + 3 = 10 + 2\sqrt{21}$ and $y^2 = 10 - 2\sqrt{21}$.",
         r"The cross terms have opposite signs because $y$ is the conjugate of $x$ - that is what makes the sum rational."),
        (r"Add: $x^2 + y^2 = 20$.",
         r"The $\pm 2\sqrt{21}$ terms cancel exactly."),
        (r"$xy = (\sqrt7+\sqrt3)(\sqrt7-\sqrt3) = 7 - 3 = 4$.",
         r"Difference of two squares again - no cross terms at all."),
        (r"Combine: $x^2 + y^2 - xy = 20 - 4 = 16$.",
         r"Subtract in the order the question asks."),
    ],
    pitfalls=[r"Computing $x^2 + y^2$ as $(x+y)^2$ and getting $28$ - remember $(x+y)^2 = x^2 + y^2 + 2xy$.",
              r"Giving $20 - 2\sqrt{21}$ by forgetting that the surds cancel when the squares are **added**."],
    takeaway=r"With conjugate pairs, $x + y$, $xy$ and $x^2 + y^2$ are all rational; build the expression from those rather than expanding blindly."),

"IND-12": Sol(
    idea=r"A 'for how many' question that is really about irrationality. The answer is $0$, and seeing why needs one sharp observation about consecutive integers.",
    steps=[
        (r"Suppose $\sqrt n + \sqrt{n+1} = r$ is rational and square it: $2n + 1 + 2\sqrt{n(n+1)} = r^2$.",
         r"Squaring is the standard way to get at a sum of surds; the rational parts separate from the single remaining surd."),
        (r"Rearrange: $\sqrt{n(n+1)} = \dfrac{r^2 - 2n - 1}{2}$, so $n(n+1)$ would have to be a perfect square.",
         r"A rational square root of an integer is an integer, so $n(n+1)$ must be a perfect square."),
        (r"But $n^2 < n(n+1) < (n+1)^2$ for every $n \geq 1$, so $n(n+1)$ lies strictly between consecutive squares.",
         r"There is no integer square strictly between $n^2$ and $(n+1)^2$ - this is the contradiction."),
        (r"Hence no $n$ in $1 \leq n \leq 100$ works: the answer is $0$.",
         r"The bound $100$ is a red herring; the argument rules out every positive integer."),
    ],
    pitfalls=[r"Testing $n = 3$ ($\sqrt3 + 2$) and concluding 'sometimes it works' because one of the two roots is nice.",
              r"Answering $9$ or $10$ by counting perfect squares up to $100$ - that would answer a different question."],
    takeaway=r"$n(n+1)$ is never a perfect square for $n \geq 1$, because it is squeezed strictly between $n^2$ and $(n+1)^2$."),

"IND-13": Sol(
    idea=r"Index laws with two variables. Simplify inside the bracket first, then apply the outside power to each index.",
    steps=[
        (r"Simplify the $a$'s inside: $\dfrac{a^{1/2}}{a^{-1}} = a^{1/2 - (-1)} = a^{3/2}$.",
         r"Dividing subtracts indices, and subtracting a negative adds - the commonest slip in the question."),
        (r"Simplify the $b$'s: $\dfrac{b^{-2}}{b^{1/2}} = b^{-2 - 1/2} = b^{-5/2}$.",
         r"Same rule; keep the two variables in separate columns so signs do not get mixed up."),
        (r"Raise the bracket to the 4th power: $\left(a^{3/2}b^{-5/2}\right)^4 = a^{6}b^{-10}$.",
         r"$(a^m)^n = a^{mn}$ applies to each base separately: $\frac32 \times 4 = 6$ and $-\frac52 \times 4 = -10$."),
    ],
    pitfalls=[r"Getting $a^{-1/2}$ at step 1 by subtracting the wrong way round, leading to $a^{-2}b^{10}$ - which is offered.",
              r"Applying the power $4$ to only the first factor."],
    takeaway=r"Simplify inside the bracket to a single power of each base before applying the outer index."),

"IND-14": Sol(
    idea=r"A quotient of surds that collapses completely. Simplify each root first and the $\sqrt2$'s cancel.",
    steps=[
        (r"Simplify: $\sqrt{50} = 5\sqrt2$, $\sqrt{18} = 3\sqrt2$, $\sqrt8 = 2\sqrt2$.",
         r"Every number is (square) $\times\, 2$, so every root is a multiple of $\sqrt2$ - which is why the fraction will be rational."),
        (r"Add the numerator: $5\sqrt2 + 3\sqrt2 = 8\sqrt2$.",
         r"Like terms again - $\sqrt2$ behaves as a common factor."),
        (r"Divide: $\dfrac{8\sqrt2}{2\sqrt2} = 4$.",
         r"The $\sqrt2$ cancels top and bottom, leaving plain arithmetic."),
    ],
    pitfalls=[r"Working out $\sqrt{50} + \sqrt{18} = \sqrt{68}$, which is wrong and leads nowhere.",
              r"Cancelling only the numbers and leaving a stray $\sqrt2$, giving $4\sqrt2$."],
    takeaway=r"Simplify every surd to the form $k\sqrt m$ before adding or dividing; common surd factors then cancel visibly."),

"IND-15": Sol(
    idea=r"You are given two exponentials and asked for a third. Express the target in terms of the given ones using index laws - you never need to find $x$ or $y$.",
    steps=[
        (r"Split the index: $2^{2x - y} = \dfrac{2^{2x}}{2^{y}}$.",
         r"Subtraction in the index is division - this is what lets you use the two given facts separately."),
        (r"Write $2^{2x} = (2^x)^2 = 5^2 = 25$.",
         r"A coefficient in the index is a power of the whole exponential: $2^{2x} = (2^x)^2$, not $2 \times 2^x$."),
        (r"Substitute: $\dfrac{25}{20} = \dfrac54$.",
         r"$2^y = 20$ is given directly."),
    ],
    pitfalls=[r"Using $2^{2x} = 2 \times 2^x = 10$, giving $\frac12$.",
              r"Trying to solve for $x = \log_2 5$ and $y = \log_2 20$ first - correct but slow, and it invites arithmetic slips."],
    takeaway=r"Rewrite the target index as sums and multiples of the given ones; substitution then beats solving for the unknowns."),

"IND-16": Sol(
    idea=r"Three surd 'rules', two of which are genuine. The exam skill is knowing which laws distribute and finding a counterexample for the one that does not.",
    steps=[
        (r"Statement I: $\sqrt a\sqrt b = \sqrt{ab}$ is a law of surds, valid for all $a, b \geq 0$. **True.**",
         r"Roots distribute over multiplication and division, and the condition $a, b > 0$ in the question is exactly what the law needs."),
        (r"Statement II: test $a = b = 1$: $\sqrt{1+1} = \sqrt2 \approx 1.41$ but $\sqrt1 + \sqrt1 = 2$. **False.**",
         r"One counterexample is enough to kill a 'for all' statement - and the simplest numbers usually work."),
        (r"Statement III: square both sides. $(a+b)^2 = a^2 + b^2 + 2ab > a^2 + b^2$ since $ab > 0$, and both sides are positive, so $\sqrt{a^2+b^2} < a + b$. **True.**",
         r"Squaring is safe here precisely because both sides are known to be positive; that is what makes the comparison valid in both directions."),
        (r"I and III are true: the answer is 'I and III only'.",
         r"Match your three verdicts to the option list rather than reasoning about the options themselves."),
    ],
    pitfalls=[r"Assuming roots distribute over addition because they distribute over multiplication - II is the classic error this question is built around.",
              r"Rejecting III because the triangle-inequality picture feels like it should be an equality."],
    takeaway=r"Roots split over $\times$ and $\div$ but never over $+$ or $-$; to compare positive quantities, square them."),

"IND-17": Sol(
    idea=r"An equation with the unknown in two fractional powers. Multiplying by the negative power clears it entirely.",
    steps=[
        (r"Multiply both sides by $x^{3/2}$: $x^{3/2} \cdot x^{3/2} = 8$, i.e. $x^3 = 8$.",
         r"$x^{-3/2}$ becomes $x^0 = 1$ on the right, and the left gains $\frac32 + \frac32 = 3$. Multiplying by a positive quantity (we are told $x > 0$) cannot introduce false solutions."),
        (r"Take the cube root: $x = 2$.",
         r"$x^3 = 8$ has one real root."),
    ],
    pitfalls=[r"Cancelling the powers to get $x = 8$.",
              r"Dividing by $x^{3/2}$ instead of multiplying, which leaves $x^{3} = 8$ on the wrong side and invites sign errors in the index."],
    takeaway=r"To clear a negative fractional power, multiply through by that power - stated positivity guarantees the step is reversible."),

"IND-18": Sol(
    idea=r"A difference of two rationalisable fractions. Using a single common denominator is faster than rationalising each one.",
    steps=[
        (r"Use the common denominator $(7 - 2\sqrt3)(7 + 2\sqrt3) = 49 - 12 = 37$.",
         r"The two denominators are conjugates, so their product is automatically rational - no separate rationalising needed."),
        (r"Numerator: $3(7 + 2\sqrt3) - 3(7 - 2\sqrt3) = 3 \times 4\sqrt3 = 12\sqrt3$.",
         r"When you subtract conjugates the rational parts cancel and the surd parts double - so only the surd survives."),
        (r"Result: $\dfrac{12\sqrt3}{37}$.",
         r"Already rationalised, since the denominator is an integer."),
    ],
    pitfalls=[r"$(2\sqrt3)^2 = 4 \times 3 = 12$, not $6$; using $6$ gives denominator $43$.",
              r"Adding the numerators instead of subtracting, giving $\frac{42}{37}$ - which is offered."],
    takeaway=r"A difference of conjugate fractions leaves only the surd part; their product denominator is rational from the start."),

"IND-19": Sol(
    idea=r"'How many real solutions' with exponentials - convert to a single base and the exponents give a quadratic whose discriminant answers the question.",
    steps=[
        (r"Write $16 = 2^4$, so the right-hand side is $2^{4}\cdot2^{-3x} = 2^{4 - 3x}$.",
         r"Multiplying powers of the same base adds indices; this puts both sides in base $2$."),
        (r"Equate indices: $x^2 = 4 - 3x$, i.e. $x^2 + 3x - 4 = 0$.",
         r"Legitimate because $2^u$ is one-to-one."),
        (r"Factorise: $(x+4)(x-1) = 0$ - two distinct real roots.",
         r"The question asks only for the *number* of solutions, so the discriminant ($9 + 16 > 0$) would do; factorising confirms both roots are real."),
    ],
    pitfalls=[r"Rejecting $x = -4$ because it is negative - the **exponent** may be negative; it is $2^x$ that must stay positive.",
              r"Reading $16 \times 2^{-3x}$ as $(16 \times 2)^{-3x}$."],
    takeaway=r"Same base $\Rightarrow$ equate exponents; then it is an ordinary quadratic and every real root counts."),

"IND-20": Sol(
    idea=r"You are given a difference of surds and a difference of the numbers. The link is the difference of two squares - no need to find $a$ and $b$.",
    steps=[
        (r"Factorise $a - b$ as a difference of two squares in $\sqrt a$ and $\sqrt b$: $a - b = (\sqrt a - \sqrt b)(\sqrt a + \sqrt b)$.",
         r"$a = (\sqrt a)^2$ for $a \geq 0$, so the whole expression is $X^2 - Y^2$ with $X = \sqrt a$, $Y = \sqrt b$ - this is the only structural idea in the question."),
        (r"Substitute the given values: $12 = 2 \times (\sqrt a + \sqrt b)$.",
         r"The first bracket is exactly the quantity given as $2$."),
        (r"Divide: $\sqrt a + \sqrt b = 6$.",
         r"Direct."),
    ],
    pitfalls=[r"Solving simultaneously for $a$ and $b$ (possible: $a = 16$, $b = 4$) - correct but three times the work and easy to fumble.",
              r"Answering $24$ by multiplying rather than dividing."],
    takeaway=r"$a - b = (\sqrt a - \sqrt b)(\sqrt a + \sqrt b)$ converts between sums and differences of surds instantly."),

"IND-21": Sol(
    idea=r"Two equations in disguise. Writing both conditions in base $2$ turns them into simultaneous linear equations in $p$ and $q$.",
    steps=[
        (r"$\dfrac{x^3}{y^2} = \dfrac{2^{3p}}{2^{2q}} = 2^{3p - 2q}$, so $3p - 2q = 5$.",
         r"Powers of powers multiply indices, division subtracts them; equating indices is valid because base $2$ is one-to-one."),
        (r"$xy = 2^{p}\cdot 2^{q} = 2^{p+q}$, so $p + q = 10$.",
         r"Multiplication adds indices."),
        (r"Solve: from the second, $q = 10 - p$; substituting, $3p - 2(10 - p) = 5 \Rightarrow 5p = 25 \Rightarrow p = 5$.",
         r"Substitution is quickest with only two unknowns; note the bracket when substituting a negative."),
    ],
    pitfalls=[r"Dropping the bracket to get $3p - 20 - 2p = 5$ and hence $p = 25$.",
              r"Equating $x^3/y^2 = 2^5$ to $3p/2q = 5$ - indices subtract, they do not divide."],
    takeaway=r"Converting everything to one base turns exponential conditions into linear equations in the exponents."),

"IND-22": Sol(
    idea=r"A comparison question. Every option has the form $\sqrt a + \sqrt b$ with $a + b = 9$ - spotting that shared structure turns guesswork into a one-line argument.",
    steps=[
        (r"Notice that in every option the two numbers under the roots add to $9$ (including $2\sqrt{4.5} = \sqrt{4.5} + \sqrt{4.5}$).",
         r"When all the candidates share a constraint, compare them through that constraint rather than by estimating each one."),
        (r"Square a general option: $(\sqrt a + \sqrt b)^2 = a + b + 2\sqrt{ab} = 9 + 2\sqrt{ab}$.",
         r"All the options are positive, so the largest option is the one with the largest square - and only the $ab$ term varies."),
        (r"With a fixed sum, $ab$ is largest when $a$ and $b$ are closest together. The closest pair here is $a = b = 4.5$, giving $ab = 20.25$, beating $4 \times 5 = 20$.",
         r"This is the standard 'fixed perimeter, maximum area' fact; it decides the question without any decimals."),
        (r"So $2\sqrt{4.5} = \sqrt{18} \approx 4.243$ is the largest (option C, $2 + \sqrt5 \approx 4.236$, is a close second).",
         r"Worth a sanity check because the top two are so close."),
    ],
    pitfalls=[r"Estimating roots to one decimal place - $4.24$ versus $4.24$ does not separate the top two options.",
              r"Assuming $\sqrt1 + \sqrt8$ is biggest because it contains the largest single number; the spread-out pair is actually the smallest."],
    takeaway=r"For a fixed sum $a + b$, the product $ab$ - and hence $\sqrt a + \sqrt b$ - is maximised when $a$ and $b$ are as close as possible."),

}
