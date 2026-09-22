"""Full teaching solutions: GCSE algebra (ALG-xx)."""
from gen.model import Sol

SOLUTIONS = {

"ALG-01": Sol(
    idea=r"Rearranging when the new subject appears **twice**. The key move is collecting both $x$ terms on one side and factorising.",
    steps=[
        (r"Clear the fraction: multiply both sides by $(x-1)$: $y(x - 1) = 2x + 3$.",
         r"Get rid of the denominator first; everything else is then ordinary algebra."),
        (r"Expand: $xy - y = 2x + 3$.",
         r"Multiply through the bracket."),
        (r"Collect the $x$ terms on one side: $xy - 2x = y + 3$.",
         r"Both terms containing $x$ must end up together - this is the step the question is testing."),
        (r"Factorise and divide: $x(y - 2) = y + 3$, so $x = \dfrac{y+3}{y-2}$.",
         r"Factoring out $x$ turns two occurrences into one, which can then be divided out."),
    ],
    pitfalls=[r"Dividing by $y$ too early, leaving $x$ on both sides.",
              r"Sign slip in collecting, giving $\frac{y+3}{2-y}$ - an offered option."],
    takeaway=r"When the subject appears twice: expand, gather its terms, factorise, divide."),

"ALG-02": Sol(
    idea=r"A quadratic sequence. The second difference identifies the $n^2$ coefficient; two terms then fix the rest.",
    steps=[
        (r"First differences: $5, 7, 9, 11$. Second differences: $2$ (constant).",
         r"Constant second differences mean the sequence is quadratic."),
        (r"The $n^2$ coefficient is half the second difference: $\frac22 = 1$, so the $n$th term is $n^2 + bn + c$.",
         r"For $an^2 + bn + c$, the second difference is always $2a$."),
        (r"Use $n = 1$: $1 + b + c = 3$; and $n = 2$: $4 + 2b + c = 8$.",
         r"Two equations for the two remaining unknowns."),
        (r"Subtract: $3 + b = 5$, so $b = 2$ and then $c = 0$: the $n$th term is $n^2 + 2n$.",
         r"Check $n = 4$: $16 + 8 = 24$ ✓."),
    ],
    pitfalls=[r"Using the second difference itself as $a$, giving $2n^2 + \ldots$",
              r"Checking only the first term, which several options match."],
    takeaway=r"Second difference $= 2a$; then substitute two terms and verify with a third."),

"ALG-03": Sol(
    idea=r"Multiplying algebraic fractions: factorise everything first, then cancel common factors across the product.",
    steps=[
        (r"Factorise each part: $x^2-9 = (x-3)(x+3)$; $x^2+x-12 = (x+4)(x-3)$; $x^2-16 = (x-4)(x+4)$; $x^2-3x = x(x-3)$.",
         r"Nothing can be cancelled until everything is in factor form."),
        (r"Write the product: $\dfrac{(x-3)(x+3)}{(x+4)(x-3)} \times \dfrac{(x-4)(x+4)}{x(x-3)}$.",
         r"In a product of fractions any top factor can cancel with any bottom factor."),
        (r"Cancel: the $(x+4)$ pair, and one $(x-3)$ from the first numerator with the first denominator.",
         r"There are two $(x-3)$s on the bottom but only one on top, so one survives below."),
        (r"What remains: $\dfrac{(x+3)(x-4)}{x(x-3)}$.",
         r"Count the leftovers carefully - this is where marks are lost."),
    ],
    pitfalls=[r"Cancelling both $(x-3)$ factors and losing one from the denominator.",
              r"Cancelling terms rather than factors, e.g. striking out the $x^2$s."],
    takeaway=r"Factorise fully, then cancel factor-by-factor and count how many copies of each remain."),

"ALG-04": Sol(
    idea=r"An identity holds for **every** $x$. Expand each candidate and compare, or test values to eliminate.",
    steps=[
        (r"Expand the first option: $(x+3)^2 - (x-3)^2 = (x^2 + 6x + 9) - (x^2 - 6x + 9)$.",
         r"Expand both squares fully, including the cross terms."),
        (r"Simplify: the $x^2$ and $9$ cancel, leaving $12x$ - true for all $x$. **This is the identity.**",
         r"Both sides agree identically, which is what 'identity' requires."),
        (r"Check the others quickly: $(x+3)^2 = x^2 + 6x + 9 \neq x^2 + 9$; $(x+3)(x-3) = x^2 - 9$, not $+9$; $x^2 + 6x + 9 = 0$ holds only at $x = -3$; $(x-3)^2 = x^2 - 6x + 9$, not $-9$.",
         r"Each wrong option drops or mis-signs a term - a quick test at $x = 1$ kills them all."),
    ],
    pitfalls=[r"Confusing an equation (true sometimes) with an identity (true always).",
              r"Forgetting the middle term when squaring a bracket."],
    takeaway=r"$a^2 - b^2 = (a-b)(a+b)$ applied to brackets gives quick identities; test $x = 1$ to eliminate impostors."),

"ALG-05": Sol(
    idea=r"On a speed-time graph, distance is the **area** underneath. Split the shape into simple pieces.",
    steps=[
        (r"Acceleration phase: a triangle of base $8$ s and height $20$ m/s: area $\frac12(8)(20) = 80$ m.",
         r"Uniform acceleration from rest gives a straight line from the origin, so the region is a triangle."),
        (r"Constant-speed phase: a rectangle $12 \times 20 = 240$ m.",
         r"Constant speed gives a horizontal line."),
        (r"Deceleration phase: a triangle $\frac12(10)(20) = 100$ m.",
         r"Uniform deceleration to rest gives another triangle."),
        (r"Add: $80 + 240 + 100 = 420$ m.",
         r"Total area under the whole graph."),
    ],
    pitfalls=[r"Treating the accelerating phases as rectangles, giving $600$ m - an offered option.",
              r"Using the gradient (acceleration) rather than the area."],
    takeaway=r"Speed-time graph: area $=$ distance, gradient $=$ acceleration."),

"ALG-06": Sol(
    idea=r"Substitution into a formula. Evaluate the squares first, then solve the linear equation.",
    steps=[
        (r"Substitute: $13^2 = 5^2 + 2(4)s$, i.e. $169 = 25 + 8s$.",
         r"Compute each square separately; $2as = 2 \times 4 \times s = 8s$."),
        (r"Rearrange: $8s = 144$.",
         r"$169 - 25 = 144$."),
        (r"Divide: $s = 18$.",
         r"$144 \div 8 = 18$."),
    ],
    pitfalls=[r"Forgetting the factor $2$ in $2as$ and getting $36$ - an offered option.",
              r"Computing $13^2 = 139$ or $5^2 = 10$."],
    takeaway=r"Substitute numbers for every letter, evaluate powers first, then solve."),

"ALG-07": Sol(
    idea=r"Subtracting algebraic fractions: common denominator, then expand the numerator carefully - especially the minus sign.",
    steps=[
        (r"Common denominator: $(x+2)(x-1)$.",
         r"The denominators share no factor, so their product is the lowest common denominator."),
        (r"Rewrite each fraction: $\dfrac{3(x-1)}{(x+2)(x-1)} - \dfrac{2(x+2)}{(x+2)(x-1)}$.",
         r"Multiply each numerator by whatever its denominator was missing."),
        (r"Combine and expand: $3x - 3 - (2x + 4) = 3x - 3 - 2x - 4 = x - 7$.",
         r"The minus sign applies to **both** terms of the second bracket - the classic error."),
        (r"So the answer is $\dfrac{x-7}{(x+2)(x-1)}$.",
         r"Numerator does not factorise further."),
    ],
    pitfalls=[r"Getting $x + 1$ by only negating the $2x$ - an offered option.",
              r"Subtracting the denominators as well."],
    takeaway=r"Bracket the whole second numerator before subtracting, then distribute the minus sign."),

"ALG-08": Sol(
    idea=r"Three claims about a sequence. Splitting the formula makes the behaviour transparent.",
    steps=[
        (r"I: $u_5 = \dfrac{25+1}{10} = \dfrac{26}{10} = 2.6$. **True.**",
         r"Direct substitution."),
        (r"Split the formula: $u_n = \dfrac{n^2+1}{2n} = \dfrac n2 + \dfrac{1}{2n}$.",
         r"Splitting shows one growing part and one shrinking part - much easier to reason about."),
        (r"II: $u_{n+1} - u_n = \frac12 - \frac{1}{2n(n+1)}$, which is positive for all $n \geq 1$ since $\frac{1}{2n(n+1)} \leq \frac14$. **True.**",
         r"The $\frac n2$ term grows by $\frac12$ each step, while the $\frac{1}{2n}$ term shrinks by less than that."),
        (r"III: solve $\dfrac{n^2+1}{2n} = 10 \Rightarrow n^2 - 20n + 1 = 0$, whose discriminant $400 - 4 = 396$ is not a perfect square, so $n$ is not an integer. **False.**",
         r"Terms exist only for whole-number $n$, so a non-integer solution means no term equals $10$."),
        (r"I and II only.",
         r"Match to the options."),
    ],
    pitfalls=[r"Accepting III because the equation has real solutions - they must be **positive integers**.",
              r"Testing II on only the first two terms."],
    takeaway=r"Split a rational formula into simpler pieces; and remember sequence indices must be whole numbers."),

"ALG-09": Sol(
    idea=r"Rearranging a formula containing a square root. Isolate the root, square, then solve.",
    steps=[
        (r"Isolate the square root: $\dfrac{T}{2\pi} = \sqrt{\dfrac lg}$.",
         r"Divide both sides by $2\pi$ before squaring, so the $2\pi$ gets squared correctly."),
        (r"Square both sides: $\dfrac{T^2}{4\pi^2} = \dfrac lg$.",
         r"$(2\pi)^2 = 4\pi^2$ - squaring a product squares every factor."),
        (r"Multiply by $g$: $l = \dfrac{gT^2}{4\pi^2}$.",
         r"$g$ was dividing $l$, so it multiplies across."),
    ],
    pitfalls=[r"Squaring before isolating, leaving $2\pi$ unsquared and giving $\frac{T^2g}{2\pi}$ - an offered option.",
              r"Putting $g$ in the denominator, giving $\frac{T^2}{4\pi^2 g}$."],
    takeaway=r"Isolate the root first, then square everything on that side - constants included."),

"ALG-10": Sol(
    idea=r"A quadratic inequality in a real context. Solve it, then answer the question about **duration**.",
    steps=[
        (r"Set up: $20t - 5t^2 \geq 15$.",
         r"'At least $15$ m' means the height is greater than or equal to $15$."),
        (r"Rearrange and divide by $-5$ (reversing the inequality): $-5t^2 + 20t - 15 \geq 0 \Rightarrow t^2 - 4t + 3 \leq 0$.",
         r"Dividing an inequality by a negative number flips its direction."),
        (r"Factorise: $(t-1)(t-3) \leq 0$, so $1 \leq t \leq 3$.",
         r"Between the roots for $\leq 0$."),
        (r"The **duration** is $3 - 1 = 2$ seconds.",
         r"The question asks how long, not when - a common misread."),
    ],
    pitfalls=[r"Answering $3$ (the later time) or $1$ (the earlier time) instead of the interval length.",
              r"Forgetting to flip the inequality when dividing by $-5$."],
    takeaway=r"Solve for the interval, then read whether the question wants a time or a length of time."),

"ALG-11": Sol(
    idea=r"Expanding three brackets: do two at a time, then multiply the result by the third.",
    steps=[
        (r"Multiply the first two: $(x+2)(x-1) = x^2 + x - 2$.",
         r"$2x - x = x$ for the middle term."),
        (r"Multiply by $(x+3)$: $(x^2 + x - 2)(x+3) = x^3 + 3x^2 + x^2 + 3x - 2x - 6$.",
         r"Every term of the first bracket multiplies every term of the second - six products."),
        (r"Collect: $x^3 + 4x^2 + x - 6$.",
         r"$3x^2 + x^2 = 4x^2$ and $3x - 2x = x$."),
    ],
    pitfalls=[r"Sign slip on the $x$ term, giving $x^3 + 4x^2 - x - 6$ - an offered option.",
              r"Missing one of the six products."],
    takeaway=r"Two brackets at a time, and check the constant term ($2 \times -1 \times 3 = -6$) as a quick verification."),

"ALG-12": Sol(
    idea=r"A recurrence with a fixed point. Computing one term reveals the sequence never changes.",
    steps=[
        (r"Apply the rule to the first term: $u_2 = 2^2 - 2 = 2$.",
         r"'Square then subtract 2' applied to $2$ returns $2$."),
        (r"Since $u_2 = u_1$, the same calculation repeats forever: every term is $2$.",
         r"$2$ is a fixed point of the map $x \mapsto x^2 - 2$."),
        (r"So $u_{50} = 2$.",
         r"No need to iterate fifty times."),
    ],
    pitfalls=[r"Assuming the terms must grow because of the squaring, and choosing $2^{50}$.",
              r"Computing $2^2 - 2$ as $0$ or $-2$."],
    takeaway=r"Always compute the second term: if it repeats the first, the sequence is constant."),

"ALG-13": Sol(
    idea=r"Factorising $ax^2 + bx + c$ with $a \neq 1$. Use the 'split the middle term' method, or expand the options.",
    steps=[
        (r"Multiply $a$ and $c$: $6 \times (-20) = -120$. Find two numbers with product $-120$ and sum $-7$: $-15$ and $8$.",
         r"This is the standard method; the pair always exists when the quadratic factorises over the integers."),
        (r"Split the middle term: $6x^2 - 15x + 8x - 20$.",
         r"Order does not matter."),
        (r"Factor in pairs: $3x(2x - 5) + 4(2x - 5) = (3x+4)(2x-5)$.",
         r"The bracket must match in both halves - that is the check that the split was right."),
        (r"Verify by expanding: $6x^2 - 15x + 8x - 20 = 6x^2 - 7x - 20$ ✓.",
         r"Expanding the chosen option is the fastest check in a multiple-choice setting."),
    ],
    pitfalls=[r"Choosing $(3x-5)(2x+4)$, which has a common factor $2$ in the second bracket - a sign it cannot be right for this expression.",
              r"Getting the signs the wrong way round: $(3x-4)(2x+5)$ gives $+7x$."],
    takeaway=r"Split the middle term using two numbers with product $ac$ and sum $b$; then expand your answer to check."),

"ALG-14": Sol(
    idea=r"A sum and a difference of squares. Factorising the difference of squares links them without solving for both numbers.",
    steps=[
        (r"Factorise: $x^2 - y^2 = (x-y)(x+y)$.",
         r"This is the identity that connects the two given facts."),
        (r"Substitute the known sum: $48 = (x-y)(12)$, so $x - y = 4$.",
         r"The sum $x + y = 12$ is given directly."),
        (r"Solve the pair $x + y = 12$, $x - y = 4$: adding gives $2x = 16$, so $x = 8$ (and $y = 4$).",
         r"Adding the two equations eliminates $y$."),
        (r"The larger number is $8$.",
         r"Check: $64 - 16 = 48$ ✓."),
    ],
    pitfalls=[r"Answering $4$ (the smaller number or the difference).",
              r"Trying to solve $x^2 - y^2 = 48$ by trial."],
    takeaway=r"$x^2 - y^2 = (x-y)(x+y)$ converts a difference of squares into a linear pair."),

"ALG-15": Sol(
    idea=r"Average speed uses **total distance**, not net displacement - and this journey returns home.",
    steps=[
        (r"Read the outward distance: the traveller goes from $0$ to $60$ km, so $60$ km out.",
         r"The graph shows distance **from home** against time."),
        (r"The horizontal section is a stop (no distance covered), and the final section returns to $0$: another $60$ km.",
         r"Coming back still counts as distance travelled."),
        (r"Total distance $= 60 + 60 = 120$ km over a total time of $5$ hours.",
         r"Include the stopped hour in the time - it is part of the journey."),
        (r"Average speed $= \dfrac{120}{5} = 24$ km/h.",
         r"Total distance divided by total time."),
    ],
    pitfalls=[r"Using the net displacement $0$ and answering $0$ km/h - an offered option.",
              r"Excluding the stopped hour, giving $30$ km/h."],
    takeaway=r"Average speed $=$ total distance $\div$ total time; stops count in the time, return legs count in the distance."),

}
