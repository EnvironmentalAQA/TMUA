"""Full teaching solutions: polynomials, factor and remainder theorems (POL-xx)."""
from gen.model import Sol

SOLUTIONS = {

"POL-01": Sol(
    idea=r"A remainder is given, so use the Remainder Theorem: substitute the root of the divisor and set the result equal to the remainder.",
    steps=[
        (r"The divisor $(x - 3)$ is zero at $x = 3$.",
         r"The Remainder Theorem says the remainder on dividing by $(x - a)$ is $f(a)$; you need the value of $x$ that makes the divisor vanish."),
        (r"Substitute: $f(3) = 27 - 36 + 3k + 6 = 3k - 3$.",
         r"Work the numerical terms out first ($27 - 36 + 6 = -3$) so only the $k$ term is left to carry."),
        (r"Set equal to the given remainder: $3k - 3 = -6$.",
         r"This is what the Remainder Theorem gives you - an equation, not an identity."),
        (r"Solve: $3k = -3$, so $k = -1$.",
         r"Simple linear equation."),
    ],
    pitfalls=[r"Substituting $x = -3$ (the sign of the root of $x - 3$ is $+3$), which gives a different value of $k$.",
              r"Setting $f(3) = 0$ out of habit - that is the Factor Theorem, and only applies when the remainder is zero."],
    takeaway=r"Divisor $(x - a)$ $\Rightarrow$ substitute $x = a$; the result is the remainder, which is zero only when $(x-a)$ is a factor."),

"POL-02": Sol(
    idea=r"'Is a factor' means remainder zero, so the Factor Theorem turns the statement into a single equation for $a$.",
    steps=[
        (r"$(x + 2)$ vanishes at $x = -2$.",
         r"Write $x + 2 = x - (-2)$ if the sign is confusing; the root is the value that makes the bracket zero."),
        (r"Substitute: $f(-2) = 2(-8) + a(4) - 5(-2) - 6 = -16 + 4a + 10 - 6$.",
         r"Careful with the odd power: $(-2)^3 = -8$, while $(-2)^2 = +4$."),
        (r"Simplify: $4a - 12$.",
         r"$-16 + 10 - 6 = -12$."),
        (r"Set to zero (factor $\Rightarrow$ remainder zero): $4a = 12$, so $a = 3$.",
         r"That is precisely the Factor Theorem."),
    ],
    pitfalls=[r"Using $x = 2$ instead of $x = -2$, which gives $a = -3$ - an offered option.",
              r"Sign slips on $(-2)^3$ and $-5(-2)$; write each term out separately."],
    takeaway=r"Factor $(x + k)$ means substitute $x = -k$ and set the result to zero."),

"POL-03": Sol(
    idea=r"Factorising a cubic: find one root by inspection, divide it out, then factorise the quadratic that remains.",
    steps=[
        (r"Test small factors of the constant term $6$: $f(1) = 1 - 7 + 6 = 0$, so $(x - 1)$ is a factor.",
         r"Any integer root must divide the constant term, so only $\pm1, \pm2, \pm3, \pm6$ are worth testing - and $1$ is always the quickest to try."),
        (r"Divide: $x^3 - 7x + 6 = (x - 1)(x^2 + x - 6)$.",
         r"Note the missing $x^2$ term in the original - treat it as $0x^2$ when dividing or comparing coefficients."),
        (r"Factorise the quadratic: $x^2 + x - 6 = (x + 3)(x - 2)$.",
         r"Two numbers multiplying to $-6$ and adding to $+1$."),
        (r"Full factorisation: $(x-1)(x-2)(x+3)$.",
         r"Check by multiplying the constants: $(-1)(-2)(3) = 6$. ✓"),
    ],
    pitfalls=[r"Forgetting the missing $x^2$ term and producing the wrong quadratic factor.",
              r"Sign errors giving $(x-1)(x+2)(x-3)$, whose constant term is $+6$ too - always check the $x$ coefficient as well."],
    takeaway=r"Root-hunt among the divisors of the constant term, divide out, then factorise what remains; check by multiplying the constants back."),

"POL-04": Sol(
    idea=r"A divisor of the form $ax - b$. The Remainder Theorem still applies, but the substitution value is $\frac{b}{a}$, not $b$.",
    steps=[
        (r"$2x - 1 = 0$ at $x = \frac12$.",
         r"The remainder on dividing by $(ax - b)$ is $f(b/a)$ - the root of the divisor, whatever the leading coefficient."),
        (r"Substitute: $\left(\frac12\right)^4 + 2\left(\frac12\right)^3 - 3\left(\frac12\right) + 1 = \frac{1}{16} + \frac{2}{8} - \frac32 + 1$.",
         r"Work each power out separately: $\frac1{16}$, $\frac18$, then the linear and constant terms."),
        (r"Put everything over $16$: $\frac{1}{16} + \frac{4}{16} - \frac{24}{16} + \frac{16}{16} = -\frac{3}{16}$.",
         r"A common denominator prevents fraction slips; $\frac{2}{8} = \frac{4}{16}$ and $\frac32 = \frac{24}{16}$."),
    ],
    pitfalls=[r"Substituting $x = 1$ or $x = 2$ instead of $\frac12$.",
              r"Arithmetic sign slips giving $+\frac{3}{16}$, which is offered."],
    takeaway=r"For divisor $ax - b$, evaluate at $x = \frac ba$; convert everything to a common denominator before adding."),

"POL-05": Sol(
    idea=r"A cubic with two known factors has a third. The constant term alone pins it down - no division needed.",
    steps=[
        (r"Write $p(x) = (x - 1)(x + 2)(x - r)$, where $(x-r)$ is the unknown factor.",
         r"The leading coefficient is $1$, so the product of the three monic linear factors is the whole cubic."),
        (r"Compare constant terms: the constant of the product is $(-1)(2)(-r) = 2r$, and $p(x)$ has constant term $4$.",
         r"The constant term of a product of brackets is the product of their constant terms - much faster than expanding everything."),
        (r"Solve: $2r = 4$, so $r = 2$ and the third factor is $(x - 2)$.",
         r"Check: $(-1)(2)(-2) = 4$ ✓."),
    ],
    pitfalls=[r"Reading the third factor as $(x + 2)$ by forgetting the sign flip between the root $r$ and the factor $(x - r)$.",
              r"Trying to find $a$ and $b$ first - unnecessary work."],
    takeaway=r"Compare constant terms to find a missing factor: the product of the constants in the brackets equals the constant term."),

"POL-06": Sol(
    idea=r"Dividing by a **quadratic** leaves a remainder of degree at most $1$. Write it as $ax + b$ and use the two given remainders to find $a$ and $b$.",
    steps=[
        (r"Write the division statement: $p(x) = (x^2 - 1)Q(x) + ax + b$.",
         r"The remainder always has lower degree than the divisor, so with a quadratic divisor it is linear (or constant)."),
        (r"Note $x^2 - 1 = (x-1)(x+1)$, so substituting $x = 1$ or $x = -1$ kills the $Q(x)$ term.",
         r"Choosing the roots of the divisor is what makes the unknown quotient disappear."),
        (r"$x = 1$: $p(1) = a + b$. The Remainder Theorem gives $p(1) = 3$, so $a + b = 3$.",
         r"The remainder on dividing by $(x-1)$ is $p(1)$, which is given as $3$."),
        (r"$x = -1$: $p(-1) = -a + b = -1$.",
         r"Same reasoning with the other root."),
        (r"Solve: adding gives $2b = 2$, so $b = 1$ and $a = 2$. Remainder $2x + 1$.",
         r"Two linear equations in two unknowns."),
    ],
    pitfalls=[r"Assuming the remainder is a constant and trying to force a single number.",
              r"Sign error at $x = -1$: $a(-1) + b = -a + b$, not $a - b$, which would give $2x - 1$ (an offered option)."],
    takeaway=r"Remainder on division by a degree-$n$ divisor has degree $< n$; substitute the divisor's roots to find its coefficients."),

"POL-07": Sol(
    idea=r"A division question where only the quotient is wanted. Comparing coefficients is quicker and safer than long division.",
    steps=[
        (r"Write $2x^3 - 3x^2 + 4x - 5 = (x - 1)(Ax^2 + Bx + C) + R$.",
         r"Dividing a cubic by a linear factor gives a quadratic quotient and a constant remainder."),
        (r"Compare $x^3$ terms: $A = 2$.",
         r"Only one product contributes to the highest power, so the leading coefficient comes free."),
        (r"Compare $x^2$ terms: $B - A = -3$, so $B = -1$.",
         r"The $x^2$ term comes from $x \cdot Bx$ and $-1 \cdot Ax^2$."),
        (r"Compare $x$ terms: $C - B = 4$, so $C = 3$. The quotient is $2x^2 - x + 3$.",
         r"The $x$ term comes from $x \cdot C$ and $-1 \cdot Bx$. (The constant term then gives $R = -2$, but the question does not need it.)"),
    ],
    pitfalls=[r"Getting the sign of $B$ wrong, giving $2x^2 + x + 3$ - which is offered.",
              r"Reporting the remainder instead of the quotient."],
    takeaway=r"Comparing coefficients from the top down finds a quotient one coefficient at a time, with no long-division layout to get wrong."),

"POL-08": Sol(
    idea=r"Three statements about one cubic. Factorising it first makes all three immediate.",
    steps=[
        (r"Factorise: $p(1) = 1 - 6 + 11 - 6 = 0$, so $(x-1)$ is a factor and $p(x) = (x-1)(x-2)(x-3)$.",
         r"Test the divisors of $6$; the resulting quadratic $x^2 - 5x + 6$ factorises easily."),
        (r"I: the roots $1$, $2$, $3$ are distinct. **True.**",
         r"Three distinct linear factors means three distinct roots."),
        (r"II: $(x-4)$ is a factor of $p(x) - 6$ iff $p(4) - 6 = 0$. Now $p(4) = 3 \times 2 \times 1 = 6$, so $p(4) - 6 = 0$. **True.**",
         r"Factor Theorem applied to the shifted polynomial - evaluate the whole expression $p(x) - 6$ at $x = 4$."),
        (r"III: for $x > 3$ each factor $x-1$, $x-2$, $x-3$ is positive, so the product is positive. **True.**",
         r"Sign analysis from the factorised form; beyond the largest root everything is positive."),
        (r"All three: 'I, II and III'.",
         r"Match verdicts to options."),
    ],
    pitfalls=[r"Expanding $p(x) - 6$ and re-testing from scratch instead of just evaluating $p(4) - 6$.",
              r"Checking III at one value like $x = 10$ and calling it proved - the factor argument covers every $x > 3$."],
    takeaway=r"Factorise first: roots, sign and shifted-factor questions then all read off the same form."),

"POL-09": Sol(
    idea=r"$x^4 + 4$ has no real roots, so it cannot be split into linear factors - but it can be split into two quadratics via a difference of two squares.",
    steps=[
        (r"Complete the square in $x^2$: $x^4 + 4 = (x^2 + 2)^2 - 4x^2$.",
         r"$(x^2+2)^2 = x^4 + 4x^2 + 4$, which is $4x^2$ too big - so subtract it back. This manufactured square is the standard trick (the Sophie Germain identity)."),
        (r"Recognise a difference of two squares: $A^2 - B^2$ with $A = x^2 + 2$, $B = 2x$.",
         r"$4x^2 = (2x)^2$, so the expression is now in the form that factorises."),
        (r"Factorise: $(x^2 + 2 - 2x)(x^2 + 2 + 2x) = (x^2 - 2x + 2)(x^2 + 2x + 2)$.",
         r"$A^2 - B^2 = (A-B)(A+B)$."),
        (r"Add the $x$-coefficients: $-2 + 2 = 0$.",
         r"The question asks only for this sum, which the symmetry makes obvious."),
    ],
    pitfalls=[r"Concluding it cannot be factorised because it has no real roots - a quartic with no real roots still factorises into two quadratics.",
              r"Adding the constant terms ($2 + 2 = 4$) instead of the $x$-coefficients."],
    takeaway=r"$x^4 + 4a^4 = (x^2 - 2ax + 2a^2)(x^2 + 2ax + 2a^2)$: manufacture a square, then use the difference of two squares."),

"POL-10": Sol(
    idea=r"A repeated factor $(x-2)^2$ means $x = 2$ is a double root. Comparing coefficients in the factorised form gives $q$ without any calculus.",
    steps=[
        (r"Write $x^3 + px + q = (x - 2)^2(x - r)$.",
         r"A cubic with a repeated root $2$ and one other root $r$ must take this form (leading coefficient $1$)."),
        (r"Compare $x^2$ coefficients. The left-hand side has none, so the coefficient is $0$; expanding the right gives $-(4 + r)\,$... more precisely $(x^2 - 4x + 4)(x - r)$ has $x^2$ coefficient $-r - 4$.",
         r"The **absence** of a term is information: its coefficient is zero."),
        (r"So $-r - 4 = 0$, giving $r = -4$.",
         r"One comparison is enough to find the third root."),
        (r"Constant term: $4 \times (-r) = 4 \times 4 = 16$, so $q = 16$.",
         r"The constant of $(x-2)^2(x-r)$ is $4 \times (-r)$; with $r = -4$ that is $16$."),
    ],
    pitfalls=[r"Forgetting that the missing $x^2$ term forces a condition, and trying to solve with only the constant term.",
              r"Sign slip on $-r$, giving $q = -16$."],
    takeaway=r"A missing power in a polynomial is a coefficient equal to zero - often the most useful equation available."),

"POL-11": Sol(
    idea=r"Only one coefficient is wanted, so do not expand everything: collect just the ways of making $x^2$.",
    steps=[
        (r"Multiply the first two brackets: $(x+1)(x-2) = x^2 - x - 2$.",
         r"Two brackets at a time keeps the bookkeeping small."),
        (r"To get $x^2$ from $(x^2 - x - 2)(2x + 3)$, pair $x^2$ with $3$, and $-x$ with $2x$.",
         r"An $x^2$ term arises from (degree 2)$\times$(degree 0) and (degree 1)$\times$(degree 1) - list the pairings rather than expanding."),
        (r"Add the contributions: $3x^2 + (-x)(2x) = 3x^2 - 2x^2 = x^2$, so the coefficient is $1$.",
         r"Only these two products can contribute."),
    ],
    pitfalls=[r"Missing the $(-x)(2x)$ contribution and answering $3$.",
              r"Expanding everything under time pressure and losing a sign."],
    takeaway=r"For a single coefficient, list the pairs of terms whose degrees add to the one you want."),

"POL-12": Sol(
    idea=r"Division by a quadratic again: remainder is linear. Comparing coefficients is fastest because the divisor has no $x$ term.",
    steps=[
        (r"Write $x^3 - 3x^2 + 2x + 7 = (x^2 + 1)(x + c) + (ax + b)$.",
         r"Cubic divided by quadratic gives a linear quotient and a linear remainder."),
        (r"Expand the right: $x^3 + cx^2 + x + c + ax + b$.",
         r"$(x^2+1)(x+c) = x^3 + cx^2 + x + c$."),
        (r"Compare $x^2$: $c = -3$.",
         r"Only the quotient contributes to $x^2$."),
        (r"Compare $x$: $1 + a = 2$, so $a = 1$. Compare constants: $c + b = 7$, so $b = 7 + 3 = 10$.",
         r"Work down the powers; each comparison introduces exactly one new unknown."),
        (r"Remainder: $x + 10$.",
         r"Degree $1 <$ degree $2$ ✓."),
    ],
    pitfalls=[r"Forgetting the $+x$ that $(x^2+1)(x)$ contributes, giving $a = 2$ and the remainder $2x + 10$.",
              r"Using the Remainder Theorem with $x^2 + 1$ - it has no real roots, so that route needs complex numbers and is off-specification."],
    takeaway=r"Comparing coefficients handles any divisor; only use root substitution when the divisor has real roots."),

"POL-13": Sol(
    idea=r"A quartic that is quadratic in $x^2$. Factorise fully and read off which of the offered factors appears.",
    steps=[
        (r"Substitute $u = x^2$: $u^2 - 5u + 4 = (u - 1)(u - 4)$.",
         r"Only even powers appear, so the substitution works."),
        (r"Undo it: $x^4 - 5x^2 + 4 = (x^2 - 1)(x^2 - 4)$.",
         r"Replace $u$ by $x^2$ in each bracket."),
        (r"Factorise each as a difference of two squares: $(x-1)(x+1)(x-2)(x+2)$.",
         r"$x^2 - a^2 = (x-a)(x+a)$ - do not stop at the quadratics."),
        (r"Compare with the options: $(x + 2)$ appears.",
         r"Equivalently, a factor $(x - a)$ exists iff $f(a) = 0$: $f(-2) = 16 - 20 + 4 = 0$ ✓."),
    ],
    pitfalls=[r"Choosing $x^2 + 1$ or $x^2 + 4$ - these are sums, not differences, and are not factors.",
              r"Testing only positive values when checking $f(a) = 0$."],
    takeaway=r"Factorise as far as possible; a quick check of $f(a) = 0$ confirms any candidate factor $(x-a)$."),

"POL-14": Sol(
    idea=r"Three roots determine a cubic up to a constant multiple. One extra value fixes the multiple.",
    steps=[
        (r"Write $p(x) = a(x-1)(x-2)(x-3)$.",
         r"Given roots, start from the factorised form; the leading coefficient $a$ is the only freedom left."),
        (r"Use $p(0) = 12$: $a(-1)(-2)(-3) = -6a = 12$, so $a = -2$.",
         r"Three negative factors give a negative product - a very common sign slip."),
        (r"Evaluate $p(4) = -2(3)(2)(1) = -12$.",
         r"Substitute directly into the factorised form; no expansion needed."),
    ],
    pitfalls=[r"Taking $a = 2$ from $6a = 12$ and answering $+12$.",
              r"Assuming $a = 1$ because the question says 'a cubic' - the leading coefficient is not given."],
    takeaway=r"Roots give the shape, one extra point gives the scale; keep everything in factorised form."),

"POL-15": Sol(
    idea=r"You could expand, but $a + b + c$ is the sum of the non-leading coefficients, which $p(1)$ delivers instantly.",
    steps=[
        (r"Note $p(1) = 1 + a + b + c$, so $a + b + c = p(1) - 1$.",
         r"Substituting $x = 1$ turns every power into $1$, so $p(1)$ is the sum of **all** coefficients including the leading $1$."),
        (r"Write the factorised form from the roots: $p(x) = (x-2)(x+1)(x-3)$.",
         r"Monic, because the given polynomial starts with $x^3$."),
        (r"Evaluate: $p(1) = (-1)(2)(-2) = 4$.",
         r"Two negatives and one positive give a positive."),
        (r"So $a + b + c = 4 - 1 = 3$.",
         r"Remember to subtract the leading coefficient."),
    ],
    pitfalls=[r"Answering $4$ by forgetting the leading $1$ in $p(1) = 1 + a + b + c$.",
              r"Expanding and mis-collecting; the expansion is $x^3 - 4x^2 + x + 6$, so $-4 + 1 + 6 = 3$ ✓."],
    takeaway=r"$p(1)$ is the sum of all coefficients - a one-second route to questions like this."),

"POL-16": Sol(
    idea=r"An 'assume it exists' question where the honest answer is that it does not. Comparing coefficients over-determines $k$, and the system is inconsistent.",
    steps=[
        (r"If $x^2 - x + k$ divides exactly, the quotient is linear: $x^3 - 2x^2 + 3x - 4 = (x^2 - x + k)(x + m)$.",
         r"Cubic $\div$ quadratic $=$ linear, and 'divides exactly' means no remainder term."),
        (r"Compare $x^2$: $m - 1 = -2$, so $m = -1$.",
         r"The $x^2$ terms are $mx^2$ and $-x^2$."),
        (r"Compare $x$: $k - m = 3$, so $k = 2$.",
         r"The $x$ terms are $kx$ and $-mx$."),
        (r"Check the constant term: $km = 2 \times (-1) = -2$, but the cubic has $-4$. Contradiction.",
         r"With three equations and two unknowns the system is over-determined - the last equation is a genuine test, not a formality."),
        (r"So no value of $k$ works: the answer is 'no such value exists'.",
         r"The bracketed 'assume such a value exists' is a deliberate misdirection."),
    ],
    pitfalls=[r"Stopping at $k = 2$ and never checking the constant term.",
              r"Trusting the question's hint that a value exists - always verify all the coefficients."],
    takeaway=r"When comparing coefficients gives more equations than unknowns, the leftover equations must be checked; they can reveal that no solution exists."),

}
