"""Full teaching solutions: graphs of functions (GRA-xx)."""
from gen.model import Sol

SOLUTIONS = {

"GRA-01": Sol(
    idea=r"Axis crossings are roots. Factorise fully and count **distinct** roots.",
    steps=[
        (r"Factor out $x$: $x^3 - x^2 - 6x = x(x^2 - x - 6)$.",
         r"There is no constant term, so $x$ is a factor - always check this first."),
        (r"Factorise the quadratic: $x^2 - x - 6 = (x-3)(x+2)$.",
         r"Two numbers multiplying to $-6$, adding to $-1$."),
        (r"Roots: $x = 0, 3, -2$ - three distinct values, each a simple root, so the graph crosses three times.",
         r"Distinct simple roots mean genuine crossings; a repeated root would be a touch."),
    ],
    pitfalls=[r"Missing the root $x = 0$ and answering $2$.",
              r"Counting the $y$-intercept as an extra crossing of the $x$-axis."],
    takeaway=r"Factor out $x$ when there is no constant term; count distinct roots for the number of axis meetings."),

"GRA-02": Sol(
    idea=r"A horizontal line meeting a parabola twice: the line must be above the minimum.",
    steps=[
        (r"Complete the square: $x^2 - 2x = (x-1)^2 - 1$, so the minimum value is $-1$ at $x = 1$.",
         r"The turning point governs how many times a horizontal line can cut the curve."),
        (r"A line $y = k$ meets the parabola twice when $k$ is **strictly above** the minimum.",
         r"At $k = -1$ the line is tangent at the vertex: exactly one point. Below it: none."),
        (r"So $k > -1$.",
         r"Strict inequality, because equality gives only one intersection."),
    ],
    pitfalls=[r"Including $k = -1$ and choosing $k \geq -1$ - offered as a distractor.",
              r"Using the $y$-intercept $0$ instead of the minimum value."],
    takeaway=r"Count intersections with a horizontal line by sliding it against the turning point; equality gives tangency."),

"GRA-03": Sol(
    idea=r"Build the cubic from its root behaviour, then use the $y$-intercept to fix the sign.",
    steps=[
        (r"'Touches at $x = 2$' means a repeated factor $(x-2)^2$; 'crosses at $x = -1$' means a simple factor $(x+1)$.",
         r"Even-power factors touch the axis; odd-power factors cross it."),
        (r"So the cubic is $y = a(x-2)^2(x+1)$ for some constant $a \neq 0$.",
         r"Degree $2 + 1 = 3$ ✓."),
        (r"Compute the $y$-intercept: at $x = 0$, $y = a(4)(1) = 4a$.",
         r"Substitute $x = 0$ into the factorised form."),
        (r"A negative intercept needs $a < 0$, so $y = -(x-2)^2(x+1)$ works (intercept $-4$).",
         r"The option with $a = +1$ has intercept $+4$ and is the trap."),
    ],
    pitfalls=[r"Choosing $(x-2)^2(x+1)$ and ignoring the sign of the intercept.",
              r"Swapping which root is repeated, e.g. $(x-2)(x+1)^2$."],
    takeaway=r"Repeated factor $\Rightarrow$ touch; simple factor $\Rightarrow$ cross; the $y$-intercept fixes the leading sign."),

"GRA-04": Sol(
    idea=r"A 'find the values' question whose honest answer is 'none'. Substituting shows the discriminant can never be negative.",
    steps=[
        (r"Set the expressions equal: $x + c = \dfrac1x$.",
         r"Intersections satisfy both equations."),
        (r"Multiply by $x$ (noting $x \neq 0$, since $\frac1x$ is undefined there): $x^2 + cx - 1 = 0$.",
         r"Clearing the fraction gives a quadratic whose roots are the intersection $x$-values."),
        (r"Compute the discriminant: $c^2 - 4(1)(-1) = c^2 + 4$.",
         r"The $-1$ constant is what makes the discriminant unavoidably positive."),
        (r"$c^2 + 4 > 0$ for every real $c$, so there are always two intersections: no value of $c$ avoids them.",
         r"Also check the roots are non-zero: their product is $-1 \neq 0$, so neither is the excluded $x = 0$."),
    ],
    pitfalls=[r"Assuming a line and a hyperbola must sometimes miss, and choosing an interval.",
              r"Sign error making the discriminant $c^2 - 4$, which would give $-2 < c < 2$ - an offered option."],
    takeaway=r"Do the algebra even when the answer 'feels' like an interval; $b^2 - 4ac$ with $ac < 0$ is always positive."),

"GRA-05": Sol(
    idea=r"Three properties of a modulus graph. Rewriting $|2x-4|$ as $2|x-2|$ makes all three obvious.",
    steps=[
        (r"Rewrite: $|2x - 4| = 2|x - 2|$.",
         r"Factoring the $2$ out of the modulus is legitimate because $|2u| = 2|u|$."),
        (r"I: the graph meets $y = 0$ when $|x-2| = 0$, i.e. only at $x = 2$. **True.**",
         r"A V-shape touches the axis at its single vertex."),
        (r"II: $|x - 2|$ depends only on the distance from $2$, so the graph is symmetric about $x = 2$. **True.**",
         r"Replacing $x$ by $4 - x$ leaves the value unchanged."),
        (r"III: a modulus is never negative, so the graph lies on or above the $x$-axis. **True.**",
         r"$|u| \geq 0$ by definition."),
        (r"All three.",
         r"Match to the option list."),
    ],
    pitfalls=[r"Thinking the graph crosses the axis twice because $|x^2 - 4|$-type graphs do - this one is linear inside the modulus.",
              r"Reading the line of symmetry as $x = 4$."],
    takeaway=r"$|ax + b| = |a|\left|x + \frac ba\right|$: a V-shape with its vertex at the root, never below the axis."),

"GRA-06": Sol(
    idea=r"Count both axes. The $x$-axis meetings come from the roots; the $y$-axis always contributes exactly one point.",
    steps=[
        (r"Factorise: $x^4 - 5x^2 + 4 = (x^2-1)(x^2-4)$.",
         r"Quadratic in $x^2$: two numbers multiplying to $4$ and adding to $-5$."),
        (r"Solve: $x = \pm1$ and $x = \pm2$ - four $x$-axis crossings.",
         r"Each positive value of $x^2$ gives two values of $x$."),
        (r"$y$-axis: substitute $x = 0$ to get $y = 4$ - one point.",
         r"A function meets the $y$-axis exactly once."),
        (r"Total: $4 + 1 = 5$.",
         r"The $y$-intercept is a separate point (it is not one of the roots here, since $y(0) \neq 0$)."),
    ],
    pitfalls=[r"Forgetting the $y$-axis and answering $4$.",
              r"Counting $x^2 = 1, 4$ as only two points."],
    takeaway=r"'Meets the coordinate axes' means both axes: roots plus the single $y$-intercept."),

"GRA-07": Sol(
    idea=r"Reading a function's shape from the sign of its derivative. A zero derivative **without** a sign change is an inflexion, not a turning point.",
    steps=[
        (r"Before and after $x = 1$: $f' > 0$ on both sides, with $f'(1) = 0$.",
         r"The gradient dips to zero and comes back positive - the curve flattens momentarily but keeps rising."),
        (r"So $x = 1$ is a stationary point that is **not** a turning point: a stationary point of inflexion.",
         r"Turning points require a change of sign in $f'$."),
        (r"At $x = 3$: $f' > 0$ just before and $f' < 0$ just after, so the curve rises then falls - a local maximum.",
         r"A $+ \to -$ sign change is exactly a local maximum."),
        (r"So: local maximum at $x = 3$, stationary inflexion at $x = 1$.",
         r"Match to the options."),
    ],
    pitfalls=[r"Assuming $f'(1) = 0$ must be a maximum or minimum.",
              r"Reading the $+ \to -$ change at $x = 3$ as a minimum."],
    takeaway=r"$f' = 0$ with no sign change $=$ inflexion; $+ \to -$ is a maximum, $- \to +$ is a minimum."),

"GRA-08": Sol(
    idea=r"Counting roots of a cubic. Find the turning values and see whether they straddle the axis.",
    steps=[
        (r"Rearrange to $f(x) = x^3 - 3x - 1 = 0$.",
         r"Everything on one side, so the question becomes 'how many roots?'."),
        (r"Differentiate: $f'(x) = 3x^2 - 3 = 3(x-1)(x+1)$, so the turning points are at $x = \pm1$.",
         r"A cubic with two turning points can have one, two or three roots."),
        (r"Evaluate: $f(-1) = -1 + 3 - 1 = 1 > 0$ (local maximum) and $f(1) = 1 - 3 - 1 = -3 < 0$ (local minimum).",
         r"The **values** at the turning points decide the count."),
        (r"The local maximum is above the axis and the local minimum below, so the curve crosses three times.",
         r"It comes up from $-\infty$, crosses, comes down past the axis, crosses, then rises again."),
    ],
    pitfalls=[r"Trying to factorise - this cubic has no rational roots, so factorising wastes time.",
              r"Answering $1$ because 'a cubic always has at least one root' without checking the turning values."],
    takeaway=r"Cubic root count: find the turning values; three roots iff the local max and min lie on opposite sides of the axis."),

"GRA-09": Sol(
    idea=r"Reflection in $y = x$ produces the inverse function - swap $x$ and $y$ and re-solve.",
    steps=[
        (r"Reflecting in $y = x$ swaps the roles of $x$ and $y$: the new graph satisfies $x = \log_2 y$.",
         r"Every point $(a,b)$ maps to $(b,a)$."),
        (r"Rewrite in exponential form: $y = 2^x$.",
         r"$\log_2 y = x$ means $y = 2^x$ - logs and exponentials are inverse functions."),
    ],
    pitfalls=[r"Choosing $y = \log_2(-x)$ (a $y$-axis reflection) or $-\log_2 x$ (an $x$-axis reflection).",
              r"Thinking the inverse of a log is $x^2$ because of the base $2$."],
    takeaway=r"Reflection in $y = x$ gives the inverse; $y = a^x$ and $y = \log_a x$ are mirror images in that line."),

"GRA-10": Sol(
    idea=r"Two standard facts about polynomial roots: the maximum is the degree, and odd degree forces at least one real root.",
    steps=[
        (r"At most: a degree-$5$ polynomial has at most $5$ roots, since each root contributes a linear factor.",
         r"More than $5$ factors would raise the degree above $5$."),
        (r"At least: as $x \to +\infty$ and $x \to -\infty$, an odd-degree polynomial tends to opposite infinities.",
         r"The leading term $ax^5$ dominates and changes sign with $x$."),
        (r"A continuous function that is positive somewhere and negative somewhere must cross zero, so there is at least one real root.",
         r"Intermediate value reasoning; this is why every odd-degree polynomial has a real root."),
        (r"At least $1$, at most $5$.",
         r"Match to the options."),
    ],
    pitfalls=[r"Saying 'at least $0$' by analogy with even degrees like $x^2 + 1$, which genuinely have none.",
              r"Saying 'exactly $5$', which counts complex roots or ignores repeats."],
    takeaway=r"Odd degree $\Rightarrow$ at least one real root; degree $n$ $\Rightarrow$ at most $n$ real roots."),

"GRA-11": Sol(
    idea=r"Exponential versus quadratic. Test the obvious integer points and use end behaviour to be sure nothing is missed.",
    steps=[
        (r"Try small integers: $x = 2$ gives $4 = 4$ ✓ and $x = 4$ gives $16 = 16$ ✓ - two intersections already.",
         r"$2^x = x^2$ has these two well-known solutions."),
        (r"Check negative $x$: at $x = 0$, $2^0 = 1 > 0 = x^2$; at $x = -1$, $2^{-1} = \frac12 < 1 = x^2$. The order swaps, so there is a crossing between $-1$ and $0$.",
         r"A sign change in the difference $2^x - x^2$ guarantees a crossing."),
        (r"Check beyond $x = 4$: $2^x$ grows faster than $x^2$ (e.g. at $x = 5$, $32 > 25$), so they never meet again.",
         r"Exponential growth eventually outpaces any polynomial."),
        (r"Total: three intersections.",
         r"One negative, and $x = 2$, $x = 4$."),
    ],
    pitfalls=[r"Finding only $x = 2$ and $x = 4$ and answering $2$.",
              r"Forgetting that $x^2$ is positive for negative $x$ while $2^x$ stays small but positive."],
    takeaway=r"Test integer points, then check the two ends: a sign change in the difference means an extra crossing."),

"GRA-12": Sol(
    idea=r"'Undefined' means division by zero (or a negative under a square root). Count the offending values for each option.",
    steps=[
        (r"$\dfrac{1}{x^2-4}$: the denominator vanishes at $x = 2$ and $x = -2$ - **two** values.",
         r"Difference of two squares gives two distinct roots."),
        (r"$\dfrac{1}{x^2+4}$: the denominator is always at least $4$, so it is never zero - defined everywhere.",
         r"A sum of a square and a positive constant is never zero."),
        (r"$\dfrac{x}{x^2}$ and $\dfrac{1}{(x-2)^2}$: each has a single problem value ($0$ and $2$ respectively).",
         r"A repeated factor still vanishes at only one point."),
        (r"$\sqrt{x-2}$: undefined for **all** $x < 2$ - infinitely many values, not two.",
         r"Square roots need a non-negative argument."),
    ],
    pitfalls=[r"Counting $(x-2)^2$ as two values because of the power.",
              r"Thinking $x^2 + 4$ has roots $\pm 2$."],
    takeaway=r"Count the distinct values that break the expression: repeated factors give one, sums of squares give none."),

"GRA-13": Sol(
    idea=r"Sliding a horizontal line across a modulus graph. Three solutions happen only at the height of the local maximum.",
    steps=[
        (r"Sketch $y = |x^2 - 4|$: the parabola $x^2 - 4$ with the part between $x = -2$ and $x = 2$ flipped above the axis.",
         r"Reflecting the negative part gives a W-shape with two zeros and a hump."),
        (r"Identify the key heights: zeros at $x = \pm2$, and a local maximum of $4$ at $x = 0$.",
         r"At $x = 0$, $|0 - 4| = 4$ - the top of the central hump."),
        (r"Count intersections with $y = k$: for $0 < k < 4$ there are four; for $k > 4$ there are two; for $k = 0$ there are two; for $k = 4$ the line passes through the hump's peak **and** cuts the outer arms: three.",
         r"At the peak, two of the four intersections merge into one."),
        (r"So exactly one value of $k$ (namely $4$) gives three solutions.",
         r"The question asks how many values of $k$, not how many solutions."),
    ],
    pitfalls=[r"Answering $4$ (the value of $k$) instead of $1$ (the number of such $k$).",
              r"Forgetting $k = 0$ gives two solutions, not three."],
    takeaway=r"Slide the horizontal line and note the heights where the count changes: those are the turning values."),

"GRA-14": Sol(
    idea=r"Order matters when combining a reflection with a translation. Rewrite the target to reveal the correct sequence.",
    steps=[
        (r"Rewrite the target: $\sqrt{4 - x} = \sqrt{-(x - 4)}$.",
         r"Factoring out the $-1$ exposes both operations: a negation of $x$ and a shift."),
        (r"Reading it as $f(-(x-4))$ where $f(x) = \sqrt x$: first reflect in the $y$-axis (giving $\sqrt{-x}$), then translate $4$ right (replacing $x$ by $x - 4$).",
         r"For nested transformations, the operation applied directly to $x$ (here the shift) is done **last**."),
        (r"Check with a point: $y = \sqrt{4-x}$ passes through $(4, 0)$; $\sqrt{-x}$ passes through $(0,0)$, which moves to $(4,0)$ after shifting right ✓.",
         r"A point check settles order questions decisively."),
        (r"Verify the other order fails: translating first gives $\sqrt{x-4}$, then reflecting gives $\sqrt{-x-4}$ - not the target.",
         r"Different sequences give genuinely different graphs."),
    ],
    pitfalls=[r"Choosing 'translate then reflect', which gives $\sqrt{-x-4}$.",
              r"Reflecting in the $x$-axis instead of the $y$-axis."],
    takeaway=r"Rewrite as $f(\pm(x - h))$ and test a point; with mixed reflections and shifts the order is not interchangeable."),

"GRA-15": Sol(
    idea=r"Conditions for a cubic to have three distinct roots. Two claims follow from the shape; the third needs a counterexample.",
    steps=[
        (r"III: three distinct real roots force the curve to turn twice (up, down, up), so it must have two turning points. **True.**",
         r"Between consecutive roots the curve must turn around."),
        (r"I: $y' = 3x^2 + a$ has two real roots only when $a < 0$ (so that $x^2 = -\frac a3$ has solutions). **True.**",
         r"This follows directly from III: two turning points require $y'$ to have two roots."),
        (r"II: test $y = x^3 - x = x(x-1)(x+1)$: three distinct roots $0, \pm1$, and here $b = 0$. **False.**",
         r"One counterexample is enough; $b = 0$ simply means the origin is a root."),
        (r"I and III only.",
         r"Match to the options."),
    ],
    pitfalls=[r"Assuming $b \neq 0$ because 'otherwise the cubic factorises' - it does, and that is fine.",
              r"Failing to link I to III and guessing the sign of $a$."],
    takeaway=r"Three distinct roots $\Leftrightarrow$ two turning points with values of opposite sign; that forces $a < 0$ but says nothing about $b$."),

"GRA-16": Sol(
    idea=r"Intersections of a line through the origin with a cubic. Factor out the common $x$ and use the discriminant on what remains.",
    steps=[
        (r"Set them equal: $mx = x^3 - x$, so $x^3 - x - mx = 0$.",
         r"Bring everything to one side."),
        (r"Factor out $x$: $x\left(x^2 - (1 + m)\right) = 0$.",
         r"$x = 0$ is always a solution, because both graphs pass through the origin."),
        (r"The other roots satisfy $x^2 = 1 + m$, which has two distinct non-zero solutions exactly when $1 + m > 0$.",
         r"If $1 + m = 0$ the root coincides with $x = 0$; if negative, there are no more real roots."),
        (r"So $m > -1$.",
         r"Three distinct points in total."),
    ],
    pitfalls=[r"Forgetting the root $x = 0$ and requiring three roots from the quadratic.",
              r"Including $m = -1$, where all three roots coincide at $x = 0$."],
    takeaway=r"A line through the origin always meets $y = x^3 - x$ there; factor out $x$ and analyse the quadratic that remains."),

}
