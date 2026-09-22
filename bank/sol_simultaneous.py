"""Full teaching solutions: simultaneous equations and inequalities (SIM-xx)."""
from gen.model import Sol

SOLUTIONS = {

"SIM-01": Sol(
    idea=r"One linear and one quadratic equation: substitution is the only method on the specification. The question then asks for the sum of the $x$-values, so both solutions matter.",
    steps=[
        (r"Make $x$ the subject of the linear equation: $x = 7 - 2y$.",
         r"Substitute the **linear** one into the quadratic, never the other way round - it keeps the algebra to one variable and one squaring."),
        (r"Substitute: $(7 - 2y)^2 + y^2 = 10$.",
         r"Now a single quadratic in $y$."),
        (r"Expand and tidy: $49 - 28y + 4y^2 + y^2 = 10 \Rightarrow 5y^2 - 28y + 39 = 0$.",
         r"$(7-2y)^2 = 49 - 28y + 4y^2$ - the cross term is $2 \times 7 \times (-2y)$."),
        (r"Factorise: $(5y - 13)(y - 3) = 0$, so $y = 3$ or $y = \frac{13}{5}$.",
         r"Check by expanding mentally: $5y^2 - 15y - 13y + 39$. If factorising is awkward, use the formula."),
        (r"Back-substitute for $x$: $y = 3 \Rightarrow x = 1$; $y = \frac{13}{5} \Rightarrow x = 7 - \frac{26}{5} = \frac95$. Sum $= 1 + \frac95 = \frac{14}{5}$.",
         r"Always return to the **linear** equation for the second variable - it cannot introduce extra solutions."),
    ],
    pitfalls=[r"Finding only one solution and answering $1$ or $\frac95$.",
              r"Summing the $y$-values ($3 + \frac{13}{5} = \frac{28}{5}$) instead of the $x$-values - that wrong answer is offered."],
    takeaway=r"Substitute the linear equation into the quadratic, solve, then back-substitute into the linear equation; read carefully which variable's values are wanted."),

"SIM-02": Sol(
    idea=r"A quadratic inequality with a leading coefficient other than $1$. Factorise, find the roots, then use the shape of the parabola.",
    steps=[
        (r"Factorise: $2x^2 - 5x - 3 = (2x + 1)(x - 3)$.",
         r"Two numbers multiplying to $2 \times (-3) = -6$ and adding to $-5$: $-6$ and $1$, so split $-5x$ as $-6x + x$."),
        (r"Roots: $x = -\frac12$ and $x = 3$.",
         r"Set each bracket to zero."),
        (r"The coefficient of $x^2$ is positive, so the parabola opens upwards and is $\geq 0$ **outside** the roots.",
         r"A quick sketch is the safest way to convert a factorisation into an inequality answer."),
        (r"Answer: $x \leq -\frac12$ or $x \geq 3$, with $\leq$ because equality is allowed.",
         r"The question has $\geq 0$, so the roots themselves are included."),
    ],
    pitfalls=[r"Giving $-\frac12 \leq x \leq 3$, which is where the expression is negative.",
              r"Mixing up the roots as $-3$ and $\frac12$ - the root of $(2x+1)$ is $-\frac12$, not $-2$."],
    takeaway=r"Factorise, mark the roots, sketch the parabola: 'outside' for $>0$, 'between' for $<0$ when $a > 0$."),

"SIM-03": Sol(
    idea=r"Two inequalities joined by 'and'. Solve separately, then take the overlap - the second one produces two intervals, which is where the care is needed.",
    steps=[
        (r"Solve the linear one: $3x - 7 < 2 \Rightarrow 3x < 9 \Rightarrow x < 3$.",
         r"Dividing by a positive number leaves the inequality direction unchanged."),
        (r"Solve the quadratic one: $x^2 > 4 \Rightarrow |x| > 2 \Rightarrow x < -2$ or $x > 2$.",
         r"$x^2 > 4$ is satisfied by large positive **and** large negative $x$ - taking only the positive branch is the classic error."),
        (r"Intersect the sets on a number line: from $x < 3$, keep the parts of $x < -2$ (all of it) and of $x > 2$ (only up to $3$).",
         r"'Both' means intersection; drawing both solution sets on a single line prevents mistakes."),
        (r"Answer: $x < -2$ or $2 < x < 3$.",
         r"The answer is itself two intervals - a perfectly legitimate solution set."),
    ],
    pitfalls=[r"Dropping the branch $x < -2$ and answering $2 < x < 3$.",
              r"Solving $x^2 > 4$ as $x > \pm 2$, which is not a meaningful statement."],
    takeaway=r"$x^2 > k$ gives two intervals; intersect solution sets on a number line rather than in your head."),

"SIM-04": Sol(
    idea=r"A line meeting a circle exactly once is a tangency condition: substitute and set the discriminant to zero.",
    steps=[
        (r"Substitute $y = x + k$ into $x^2 + y^2 = 8$: $x^2 + (x + k)^2 = 8$.",
         r"Eliminate $y$ so the intersections are the roots of a quadratic in $x$."),
        (r"Expand and collect: $2x^2 + 2kx + (k^2 - 8) = 0$.",
         r"$(x+k)^2 = x^2 + 2kx + k^2$, so the $x^2$ terms combine to $2x^2$."),
        (r"Exactly one point means one repeated root: discriminant $= 0$, so $(2k)^2 - 4(2)(k^2 - 8) = 0$.",
         r"Tangency is precisely the repeated-root case."),
        (r"Simplify: $4k^2 - 8k^2 + 64 = 0 \Rightarrow -4k^2 = -64 \Rightarrow k^2 = 16 \Rightarrow k = \pm 4$.",
         r"Two tangent lines exist - one on each side of the circle - so both signs are genuine."),
    ],
    pitfalls=[r"Answering $k = \pm 2\sqrt2$ by confusing the radius $\sqrt8$ with the intercept.",
              r"Giving only $k = 4$; the geometry guarantees a matching tangent with $k = -4$."],
    takeaway=r"Tangent to a circle: substitute and set the discriminant to zero - or use 'distance from centre $=$ radius', which gives $\frac{|k|}{\sqrt2} = 2\sqrt2$ just as fast."),

"SIM-05": Sol(
    idea=r"Counting integers in the solution set of a quadratic inequality. The counting at the end is where the marks are won or lost.",
    steps=[
        (r"Factorise: $n^2 - 10n + 16 = (n - 2)(n - 8)$.",
         r"Two numbers multiplying to $16$, adding to $-10$: $-2$ and $-8$."),
        (r"Negative between the roots: $2 < n < 8$.",
         r"Upward parabola, so it dips below the axis strictly between its roots."),
        (r"List the integers strictly inside: $3, 4, 5, 6, 7$ - five values.",
         r"Strict inequality excludes $2$ and $8$, where the expression equals zero."),
    ],
    pitfalls=[r"Including the endpoints and answering $7$.",
              r"Counting $8 - 2 = 6$ as the number of integers - the count between $a$ and $b$ exclusive is $b - a - 1$."],
    takeaway=r"Write the integers out; the number strictly between $a$ and $b$ is $b - a - 1$, not $b - a$."),

"SIM-06": Sol(
    idea=r"A product and a difference. Substituting the linear relation gives a quadratic with two solution pairs, and the question wants a total over both.",
    steps=[
        (r"From $x - y = 1$, write $x = y + 1$.",
         r"Substituting the linear equation keeps things to one variable."),
        (r"Substitute into $xy = 6$: $(y + 1)y = 6 \Rightarrow y^2 + y - 6 = 0$.",
         r"Expand before rearranging into standard form."),
        (r"Factorise: $(y + 3)(y - 2) = 0$, so $y = -3$ or $y = 2$.",
         r"Both are valid - nothing in the question restricts the sign."),
        (r"Find the pairs: $y = 2 \Rightarrow x = 3$, giving $x + y = 5$; $y = -3 \Rightarrow x = -2$, giving $x + y = -5$. Sum of these: $0$.",
         r"The question asks for the sum of **all possible values of $x + y$**, so compute $x+y$ for each pair and add."),
    ],
    pitfalls=[r"Finding only the positive pair and answering $5$.",
              r"Adding all four numbers $3 + 2 + (-2) + (-3)$ - which happens to be $0$ too, but for the wrong reason; on another question that luck runs out."],
    takeaway=r"When a system has several solution pairs, compute the requested quantity for each pair and then combine."),

"SIM-07": Sol(
    idea=r"'True for all $x$' for an upward parabola means it never touches the axis: discriminant strictly negative.",
    steps=[
        (r"Note the leading coefficient is $1 > 0$, so the parabola opens upwards.",
         r"For $>0$ everywhere you need both the right shape and no real roots; here the shape is automatic."),
        (r"Require no real roots: $b^2 - 4(1)(9) < 0$.",
         r"If there were real roots the curve would touch or cross the axis and the expression would fail to be positive there."),
        (r"Solve: $b^2 < 36 \Rightarrow -6 < b < 6$.",
         r"$b^2 < 36$ means $|b| < 6$, a single interval."),
    ],
    pitfalls=[r"Solving $b^2 < 36$ as two outer intervals - that is the solution of $b^2 > 36$.",
              r"Using $\leq$: at $b = \pm6$ the curve touches the axis, where the expression equals $0$ and is not $> 0$."],
    takeaway=r"'Positive for all $x$' $\Leftrightarrow$ $a > 0$ **and** $b^2 - 4ac < 0$; $x^2 < k$ gives one interval, $x^2 > k$ gives two."),

"SIM-08": Sol(
    idea=r"An inequality with the variable in the denominator. You must not multiply by $x$ without knowing its sign - split into cases instead.",
    steps=[
        (r"Case $x > 0$: multiplying by $x$ keeps the direction, giving $1 > 2x$, i.e. $x < \frac12$. Combined with $x > 0$: $0 < x < \frac12$.",
         r"Multiplying an inequality by a positive quantity is safe; the case assumption must be carried into the answer."),
        (r"Case $x < 0$: then $\frac1x < 0 < 2$, so the inequality can never hold.",
         r"Rather than multiplying by a negative (and flipping), just observe the sign - a negative number is never greater than $2$."),
        (r"Case $x = 0$: $\frac1x$ is undefined, so $x = 0$ is excluded.",
         r"Always check the value that breaks the expression."),
        (r"Combine: the solution set is exactly $0 < x < \frac12$.",
         r"Only the first case contributes."),
    ],
    pitfalls=[r"Multiplying through by $x$ blindly to get $x < \frac12$, which wrongly includes every negative number.",
              r"Answering $x > 2$ by 'inverting' both sides without justification."],
    takeaway=r"Never multiply an inequality by an expression of unknown sign: split into cases, or bring everything to one side and analyse the sign of the fraction."),

"SIM-09": Sol(
    idea=r"'Exactly one solution' for a line and a parabola is again the discriminant-zero (tangency) condition.",
    steps=[
        (r"Set the expressions equal: $x^2 + 2x + c = 4x + 1$.",
         r"A simultaneous solution is a point where both $y$-values agree."),
        (r"Collect: $x^2 - 2x + (c - 1) = 0$.",
         r"Move everything to one side; the $2x - 4x$ gives $-2x$."),
        (r"Discriminant zero: $(-2)^2 - 4(1)(c - 1) = 0$.",
         r"One solution means a repeated root."),
        (r"Solve: $4 - 4c + 4 = 0 \Rightarrow 4c = 8 \Rightarrow c = 2$.",
         r"Careful with $-4(c-1) = -4c + 4$."),
    ],
    pitfalls=[r"Mishandling $-4(c-1)$ and getting $c = 0$.",
              r"Setting the discriminant $> 0$ ('has a solution') rather than $= 0$ ('exactly one')."],
    takeaway=r"Exactly one intersection between a line and a parabola always means discriminant $= 0$."),

"SIM-10": Sol(
    idea=r"A cubic inequality. With three distinct linear factors, use a sign chart - the sign alternates as you cross each root.",
    steps=[
        (r"The roots are $x = 1, 3, 5$; mark them on a number line, splitting it into four regions.",
         r"A product of linear factors can only change sign at a root."),
        (r"Test the far-right region, e.g. $x = 6$: $(5)(3)(1) > 0$.",
         r"One test value fixes the whole chart; the far right is easiest because every factor is positive."),
        (r"Alternate leftwards: positive for $x > 5$, negative on $(3,5)$, positive on $(1,3)$, negative for $x < 1$.",
         r"Each simple (unrepeated) root flips the sign exactly once."),
        (r"Collect the positive regions: $1 < x < 3$ or $x > 5$.",
         r"The answer is a union of two intervals."),
    ],
    pitfalls=[r"Answering $x > 5$ only, forgetting the middle positive region.",
              r"Assuming the expression is positive whenever $x$ is bigger than all the roots - true here, but the alternation is what you must use."],
    takeaway=r"Sign chart: find the roots, test one region, then alternate; repeated factors are the only ones that do not flip the sign."),

"SIM-11": Sol(
    idea=r"A modulus inequality plus three consequences. Solve the modulus first, then test each statement against that interval.",
    steps=[
        (r"Unpack the modulus: $|2x - 3| < 5$ means $-5 < 2x - 3 < 5$.",
         r"$|A| < k$ means $A$ lies within $k$ of zero - a double inequality, not two separate cases."),
        (r"Solve the double inequality: add $3$ throughout to get $-2 < 2x < 8$, then halve: $-1 < x < 4$. So **I is true**.",
         r"Whatever you do to one part of a double inequality you do to all three parts."),
        (r"III says $x > -1$, which is half of I. **True.**",
         r"A weaker statement implied by a true one is automatically true."),
        (r"II: for $-1 < x < 4$, the largest $|x|$ can get is just under $4$, so $x^2 < 16$ always. **True.**",
         r"For squares, what matters is the largest **absolute value** in the interval, not the largest value."),
        (r"All three hold.",
         r"Match to the option list."),
    ],
    pitfalls=[r"Treating $|2x-3| < 5$ as $2x - 3 < 5$ only, losing the lower bound.",
              r"Rejecting II by testing a value like $x = -3$ that is not in the interval at all."],
    takeaway=r"$|A| < k \Leftrightarrow -k < A < k$; when squaring an interval, check the end with the larger absolute value."),

"SIM-12": Sol(
    idea=r"Two parabolas meeting twice. Subtracting gives one quadratic, and 'two distinct points' is a positive discriminant.",
    steps=[
        (r"Set them equal: $x^2 - 4 = -x^2 + 2x + k$.",
         r"Intersections satisfy both equations, so their right-hand sides agree."),
        (r"Collect everything on one side: $2x^2 - 2x - 4 - k = 0$.",
         r"Note the $-x^2$ becomes $+x^2$ when moved across, giving $2x^2$."),
        (r"Discriminant $> 0$: $(-2)^2 - 4(2)(-4 - k) > 0$.",
         r"Here $c = -4 - k$; keeping the whole thing in brackets avoids sign errors."),
        (r"Simplify: $4 + 32 + 8k > 0 \Rightarrow 8k > -36 \Rightarrow k > -\frac92$.",
         r"$-4 \times 2 \times (-4-k) = 32 + 8k$ - two negatives make a positive."),
    ],
    pitfalls=[r"Losing a sign in $c = -4 - k$ and getting $k > \frac92$ or $k > -4$, both of which are offered.",
              r"Forgetting to combine $x^2$ with $-(-x^2)$ and working with $x^2$ instead of $2x^2$."],
    takeaway=r"Bring both curves to one side before using the discriminant, and bracket the constant term to keep signs straight."),

"SIM-13": Sol(
    idea=r"Two quadratic inequalities, then an integer count. The second one factorises without a constant term, which changes its shape.",
    steps=[
        (r"First: $x^2 - 5x - 24 < 0 \Rightarrow (x - 8)(x + 3) < 0 \Rightarrow -3 < x < 8$.",
         r"Between the roots for $< 0$."),
        (r"Second: $x^2 - 3x > 0 \Rightarrow x(x - 3) > 0 \Rightarrow x < 0$ or $x > 3$.",
         r"Roots $0$ and $3$; outside the roots for $> 0$. Do not divide by $x$ - that would lose the $x<0$ branch."),
        (r"Intersect: from $(-3, 8)$ keep $(-3, 0)$ and $(3, 8)$.",
         r"Overlap both solution sets on one number line."),
        (r"Count integers: $-2, -1$ from the first piece and $4, 5, 6, 7$ from the second: six.",
         r"Endpoints $-3, 0, 3, 8$ are all excluded by strict inequalities."),
    ],
    pitfalls=[r"Dividing $x^2 > 3x$ by $x$ to get $x > 3$, losing all the negative solutions.",
              r"Including $0$ or $3$ in the count."],
    takeaway=r"Never divide an inequality by the variable; factorise instead, then count integers explicitly."),

"SIM-14": Sol(
    idea=r"$x^2 - y^2 = 0$ factorises into two lines. The system is a line meeting a pair of lines, so count the intersections of each case.",
    steps=[
        (r"Factorise: $x^2 - y^2 = (x - y)(x + y) = 0$, so $y = x$ or $y = -x$.",
         r"A product is zero when either factor is zero - this splits the problem into two straight-line cases."),
        (r"Case $y = x$: $2x + 3x = 12 \Rightarrow 5x = 12$, one solution $\left(\frac{12}{5}, \frac{12}{5}\right)$.",
         r"Substitute into the linear equation; a linear equation in one unknown has exactly one root."),
        (r"Case $y = -x$: $2x - 3x = 12 \Rightarrow -x = 12$, one solution $(-12, 12)$.",
         r"Same method; the coefficient of $x$ is non-zero so again exactly one solution."),
        (r"Total: two solutions.",
         r"The two cases give different points, so no double counting."),
    ],
    pitfalls=[r"Taking the square root as $y = x$ only, halving the answer.",
              r"Concluding 'a line meets a quadratic in at most 2 points, so 2' without checking that neither case is parallel or degenerate."],
    takeaway=r"$A^2 = B^2$ means $A = B$ **or** $A = -B$; both branches must be followed."),

"SIM-15": Sol(
    idea=r"A transformation question hidden in an inequality. Replacing $x$ by $-x$ reflects the graph in the $y$-axis, and the solution set reflects with it.",
    steps=[
        (r"Note that $a(-x)^2 + b(-x) + c = ax^2 - bx + c$: the second expression is the first with $x$ replaced by $-x$.",
         r"Spotting this makes the question a one-liner; the alternative is to reconstruct $a$, $b$, $c$ explicitly."),
        (r"So the graph of the second is the reflection of the first in the $y$-axis.",
         r"$f(-x)$ is always the $y$-axis reflection of $f(x)$."),
        (r"The original is negative on $-2 < x < 5$; reflecting sends $x$ to $-x$, so the roots $-2$ and $5$ move to $2$ and $-5$.",
         r"Every point of the solution set flips sign, and the interval flips with it."),
        (r"The new solution set is $-5 < x < 2$.",
         r"Write the interval with the smaller number first."),
    ],
    pitfalls=[r"Leaving the interval as $2 < x < -5$, which is empty as written.",
              r"Assuming the solution set is unchanged because 'only the sign of $b$ changed'."],
    takeaway=r"Changing $b$ to $-b$ reflects a quadratic in the $y$-axis; everything about the graph, including solution sets, reflects too."),

"SIM-16": Sol(
    idea=r"A rational inequality. Never multiply by $x + 1$ (its sign is unknown) - analyse the sign of the fraction instead.",
    steps=[
        (r"Find the critical values: numerator zero at $x = 2$, denominator zero at $x = -1$.",
         r"The fraction can only change sign where the numerator or denominator vanishes."),
        (r"Test the three regions. For $x < -1$ (say $x = -2$): $\frac{-4}{-1} = 4 > 0$. For $-1 < x < 2$ (say $x = 0$): $\frac{-2}{1} = -2 < 0$. For $x > 2$ (say $x = 3$): $\frac{1}{4} > 0$.",
         r"One test value per region settles the sign throughout that region."),
        (r"Include $x = 2$ (the fraction is $0$, and $\leq 0$ allows it) but exclude $x = -1$ (undefined).",
         r"The two endpoints behave differently: a zero numerator is allowed by $\leq$; a zero denominator never is."),
        (r"Answer: $-1 < x \leq 2$.",
         r"Note the mixed brackets - strict at $-1$, inclusive at $2$."),
    ],
    pitfalls=[r"Multiplying by $x + 1$ to get $x - 2 \leq 0$, i.e. $x \leq 2$, which wrongly includes everything below $-1$.",
              r"Writing $-1 \leq x \leq 2$ and including a value where the expression is undefined."],
    takeaway=r"For $\frac{A}{B} \leq 0$, use a sign chart on $A$ and $B$; a zero denominator is always excluded, a zero numerator is included when the inequality is not strict."),

"SIM-17": Sol(
    idea=r"Symmetric information again: a sum and a sum of squares. The identity for $(x-y)^2$ gets the difference without finding the numbers.",
    steps=[
        (r"Use $(x - y)^2 = x^2 + y^2 - 2xy$ and $(x + y)^2 = x^2 + y^2 + 2xy$.",
         r"Adding these gives $(x+y)^2 + (x-y)^2 = 2(x^2 + y^2)$ - the relation that links all three given quantities."),
        (r"Rearrange: $(x - y)^2 = 2(x^2 + y^2) - (x + y)^2$.",
         r"This avoids having to find $xy$ as an intermediate step."),
        (r"Substitute: $2(58) - 10^2 = 116 - 100 = 16$.",
         r"Careful: it is $2(x^2+y^2)$, not $x^2 + y^2$."),
        (r"Take the positive square root: the difference is $4$ (the numbers are $3$ and $7$).",
         r"The question asks for the **positive** difference, so take $+4$."),
    ],
    pitfalls=[r"Forgetting the factor $2$ and getting $(x-y)^2 = -42$, which is impossible.",
              r"Giving $16$ (the square of the difference) as the answer."],
    takeaway=r"$(x+y)^2 + (x-y)^2 = 2(x^2+y^2)$: any two of sum, difference and sum-of-squares give the third."),

"SIM-18": Sol(
    idea=r"A Paper 2-style wrapper on a quadratic inequality: decide the statement and its converse separately.",
    steps=[
        (r"Factorise the quadratic: $x^2 - 3x + 2 = (x-1)(x-2)$, which is positive exactly when $x < 1$ or $x > 2$.",
         r"Knowing precisely where the expression is positive lets you test both directions quickly."),
        (r"The statement: does $x > 2$ guarantee positivity? Yes - $x > 2$ lies inside the region $x > 2$. **True.**",
         r"An implication is true when the hypothesis region sits inside the conclusion region."),
        (r"The converse: does positivity guarantee $x > 2$? No - $x = 0$ gives $(0-1)(0-2) = 2 > 0$ but $0 \not> 2$. **False.**",
         r"The positivity region is strictly larger than $x > 2$, so a counterexample must come from the extra part $x < 1$."),
        (r"So the statement is true but its converse is false.",
         r"Report both verdicts in the order the options use them."),
    ],
    pitfalls=[r"Assuming the converse holds because the implication does - converses are logically independent.",
              r"Only testing values greater than $2$, which can never refute the converse."],
    takeaway=r"An implication is true when one region is contained in the other; its converse needs the reverse containment, so look for a counterexample in the leftover region."),

}
