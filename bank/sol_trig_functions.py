"""Full teaching solutions: trigonometric functions and equations (TRG-xx)."""
from gen.model import Sol

SOLUTIONS = {

"TRG-01": Sol(
    idea=r"Counting solutions of $\sin(kx) = c$. Transform the interval for the inside expression and count there.",
    steps=[
        (r"Let $u = 2x$. As $x$ runs over $[0, 2\pi)$, $u$ runs over $[0, 4\pi)$.",
         r"Multiplying the variable by $2$ doubles the range of the inside expression - this is the whole trick."),
        (r"$[0, 4\pi)$ contains exactly two full periods of $\sin$.",
         r"$\sin$ has period $2\pi$, so a $4\pi$-long interval holds two complete waves."),
        (r"In each period, $\sin u = \frac12$ has two solutions (one on the way up, one on the way down).",
         r"A horizontal line strictly between $-1$ and $1$ cuts each wave twice."),
        (r"Total: $2 \times 2 = 4$ solutions.",
         r"Each $u$ gives exactly one $x$ via $x = u/2$, so no solutions are lost or duplicated."),
    ],
    pitfalls=[r"Answering $2$ by counting solutions for $x$ as if the $2$ were not there.",
              r"Answering $8$ by doubling twice."],
    takeaway=r"For $\sin(kx) = c$ on an interval of length $L$, the inside runs over length $kL$ - count solutions there."),

"TRG-02": Sol(
    idea=r"A mixed $\sin$/$\cos$ equation. Use $\cos^2 = 1 - \sin^2$ to make it a quadratic in $\sin x$, then count solutions carefully.",
    steps=[
        (r"Replace $\cos^2 x$ with $1 - \sin^2 x$: $2(1 - \sin^2 x) + 3\sin x - 3 = 0$.",
         r"The identity $\sin^2+\cos^2=1$ is the only way to get a single trig function - always convert the squared one."),
        (r"Tidy: $-2\sin^2 x + 3\sin x - 1 = 0$, or $2\sin^2 x - 3\sin x + 1 = 0$.",
         r"Multiply through by $-1$ so the leading coefficient is positive."),
        (r"Factorise: $(2\sin x - 1)(\sin x - 1) = 0$, giving $\sin x = \frac12$ or $\sin x = 1$.",
         r"Treat $\sin x$ as a single unknown."),
        (r"Count solutions in $0^\circ \leq x \leq 360^\circ$: $\sin x = \frac12$ gives $30^\circ$ and $150^\circ$; $\sin x = 1$ gives only $90^\circ$.",
         r"A maximum value like $\sin x = 1$ is reached just once per period, not twice - this is what makes the total odd."),
        (r"Total: $3$.",
         r"Count, do not assume 'two roots means four solutions'."),
    ],
    pitfalls=[r"Assuming each value of $\sin x$ gives two solutions and answering $4$.",
              r"Sign slips when substituting the identity, producing an unfactorisable quadratic."],
    takeaway=r"Convert to one trig function, factorise, then count solutions per value - endpoints $\pm1$ give only one each."),

"TRG-03": Sol(
    idea=r"Pure recall of exact values. (It is also $\sin(60^\circ + 30^\circ) = \sin 90^\circ$, but the addition formula is off-specification.)",
    steps=[
        (r"Write down the exact values: $\sin 60^\circ = \frac{\sqrt3}{2}$, $\cos 30^\circ = \frac{\sqrt3}{2}$, $\cos 60^\circ = \frac12$, $\sin 30^\circ = \frac12$.",
         r"These come from the half-equilateral triangle with sides $1, \sqrt3, 2$ - worth being able to redraw in seconds."),
        (r"Substitute: $\dfrac{\sqrt3}{2}\cdot\dfrac{\sqrt3}{2} + \dfrac12\cdot\dfrac12 = \dfrac34 + \dfrac14$.",
         r"$(\sqrt3)^2 = 3$, so the first product is $\frac34$."),
        (r"Add: $1$.",
         r"A clean answer - the sign that the exact values were right."),
    ],
    pitfalls=[r"Using $\sin 60^\circ = \frac12$ (that is $\sin 30^\circ$), giving $\frac{\sqrt3}{2}$.",
              r"Writing $\left(\frac{\sqrt3}{2}\right)^2 = \frac{\sqrt3}{4}$."],
    takeaway=r"$\sin$ and $\cos$ of $30^\circ$ and $60^\circ$ swap over; square a surd fraction by squaring top and bottom."),

"TRG-04": Sol(
    idea=r"$\tan$ has period $\pi$, so solutions come one per period. Find the first, add $\pi$, then check the interval.",
    steps=[
        (r"The principal solution: $\tan x = \sqrt3$ at $x = \dfrac{\pi}{3}$.",
         r"From the exact values: $\tan 60^\circ = \sqrt3$."),
        (r"$\tan$ repeats every $\pi$, so the next solution is $\dfrac{\pi}{3} + \pi = \dfrac{4\pi}{3}$.",
         r"Unlike $\sin$ and $\cos$, $\tan$ has period $\pi$, not $2\pi$."),
        (r"Check the interval $[0, 2\pi]$: $\frac{\pi}{3}$ and $\frac{4\pi}{3}$ are in it; the next, $\frac{7\pi}{3}$, is not.",
         r"$\frac{7\pi}{3} > 2\pi$, so stop there."),
        (r"Sum: $\dfrac{\pi}{3} + \dfrac{4\pi}{3} = \dfrac{5\pi}{3}$.",
         r"Common denominator $3$."),
    ],
    pitfalls=[r"Using period $2\pi$ and finding only $\frac\pi3$.",
              r"Including $\frac{7\pi}{3}$ and answering $\frac{7\pi}{3}$ or more - which is offered."],
    takeaway=r"$\tan$ repeats every $\pi$: solutions are $x_0 + k\pi$, so there are usually two in a $2\pi$ interval."),

"TRG-05": Sol(
    idea=r"Three properties of the cosine graph. Each is a standard fact; the false one is about the period.",
    steps=[
        (r"I: $\cos(-x) = \cos x$, so the graph is unchanged by reflection in the $y$-axis. **True.**",
         r"Cosine is an even function - its graph is symmetric about the $y$-axis, unlike sine."),
        (r"II: $\sin\left(x + \frac\pi2\right) = \cos x$, and replacing $x$ by $x + \frac\pi2$ shifts the graph $\frac\pi2$ to the **left**. **True.**",
         r"Check a point: $\sin$ at $x = \frac\pi2$ equals $1$, and $\cos$ reaches $1$ at $x = 0$ - shifted left by $\frac\pi2$ ✓."),
        (r"III: the period of $\cos$ is $2\pi$, not $\pi$. **False.**",
         r"$\cos(x + \pi) = -\cos x$, so a shift of $\pi$ flips the graph rather than repeating it."),
        (r"I and II only.",
         r"Match to the option list."),
    ],
    pitfalls=[r"Thinking the period is $\pi$ because $\cos$ returns to zero every $\pi$ - the **whole** shape must repeat.",
              r"Getting the direction of the shift in II backwards."],
    takeaway=r"$\cos$ is even with period $2\pi$; $\cos x = \sin(x + \frac\pi2)$ is a shift to the left."),

"TRG-06": Sol(
    idea=r"From one ratio to another, with a quadrant condition fixing the signs. Use a right-angled triangle plus CAST.",
    steps=[
        (r"From $\sin\theta = \frac35$, the reference triangle has opposite $3$ and hypotenuse $5$, so the third side is $4$ (a 3-4-5 triangle).",
         r"Pythagoras gives the missing side; the $3$-$4$-$5$ triple appears constantly."),
        (r"$\theta$ is obtuse, so it lies in the second quadrant where $\sin$ is positive but $\cos$ and $\tan$ are negative.",
         r"CAST: only sine is positive in the second quadrant."),
        (r"So $\cos\theta = -\frac45$ and $\tan\theta = \dfrac{\sin\theta}{\cos\theta} = \dfrac{3/5}{-4/5} = -\dfrac34$.",
         r"The fives cancel; the sign comes from the quadrant."),
    ],
    pitfalls=[r"Ignoring 'obtuse' and answering $\frac34$.",
              r"Inverting the ratio and answering $-\frac43$."],
    takeaway=r"Build the reference triangle from the given ratio, then let the quadrant decide the signs."),

"TRG-07": Sol(
    idea=r"A squared trig equation. Taking the square root produces **two** values, each with its own solutions.",
    steps=[
        (r"Take square roots: $\sin x = \pm\dfrac{\sqrt3}{2}$.",
         r"$X^2 = k$ has two roots - forgetting the negative one halves the answer."),
        (r"$\sin x = \frac{\sqrt3}{2}$ gives $x = \frac{\pi}{3}$ and $\frac{2\pi}{3}$.",
         r"Second-quadrant partner: $\pi - \frac\pi3$."),
        (r"$\sin x = -\frac{\sqrt3}{2}$ gives $x = \frac{4\pi}{3}$ and $\frac{5\pi}{3}$.",
         r"Third and fourth quadrants, by symmetry below the axis."),
        (r"Total: $4$ solutions in $[0, 2\pi)$.",
         r"Count them; symmetry says there should be an even number here."),
    ],
    pitfalls=[r"Taking only the positive root and answering $2$.",
              r"Reading $\sin^2 x$ as $\sin(x^2)$."],
    takeaway=r"$\sin^2 x = c$ gives $\sin x = \pm\sqrt c$, and each sign contributes its own solutions."),

"TRG-08": Sol(
    idea=r"An equation with a shifted argument. Solve for the bracket first, then unshift - and be careful about which solution is smallest.",
    steps=[
        (r"Let $u = x - \frac\pi6$ and solve $\cos u = -\frac12$.",
         r"Substituting keeps the shift out of the way until the end."),
        (r"$\cos u = -\frac12$ at $u = \frac{2\pi}{3}$ and $u = \frac{4\pi}{3}$ (second and third quadrants).",
         r"$\cos$ is negative in quadrants 2 and 3; the reference angle is $\frac\pi3$."),
        (r"Convert back: $x = u + \frac\pi6$, giving $x = \frac{2\pi}{3} + \frac{\pi}{6} = \frac{5\pi}{6}$ and $x = \frac{4\pi}{3} + \frac{\pi}{6} = \frac{3\pi}{2}$.",
         r"Common denominator $6$: $\frac{4\pi}{6} + \frac{\pi}{6} = \frac{5\pi}{6}$."),
        (r"The smallest positive one is $\dfrac{5\pi}{6}$.",
         r"Compare the candidates; $\frac{5\pi}{6} < \frac{3\pi}{2}$."),
    ],
    pitfalls=[r"Subtracting the shift instead of adding when converting back.",
              r"Using the reference angle $\frac\pi3$ directly, which gives $\frac\pi2$ - an offered option."],
    takeaway=r"Solve for the whole bracket, then undo the shift; adjust the interval for the bracket if the question restricts $x$."),

"TRG-09": Sol(
    idea=r"Simplification using the two permitted identities. Work on the denominator and numerator separately.",
    steps=[
        (r"Denominator: $\cos\theta\tan\theta = \cos\theta \times \dfrac{\sin\theta}{\cos\theta} = \sin\theta$.",
         r"$\tan\theta = \frac{\sin\theta}{\cos\theta}$, and the $\cos\theta$ cancels (legitimate where the expression is defined)."),
        (r"Numerator: $1 - \cos^2\theta = \sin^2\theta$.",
         r"Rearranged Pythagorean identity."),
        (r"Divide: $\dfrac{\sin^2\theta}{\sin\theta} = \sin\theta$.",
         r"One power of $\sin\theta$ cancels."),
    ],
    pitfalls=[r"Cancelling to $\sin^2\theta$ by forgetting to simplify the denominator.",
              r"Writing $1 - \cos^2\theta = \cos^2\theta - 1$ (sign flip), giving $-\sin\theta$."],
    takeaway=r"Convert $\tan$ into $\frac{\sin}{\cos}$ and use $1 - \cos^2 = \sin^2$; then cancel."),

"TRG-10": Sol(
    idea=r"A transcendental equation - it cannot be solved algebraically. Count intersections of $y = \sin x$ with the straight line $y = \frac{x}{10}$ by sketching.",
    steps=[
        (r"Bound the solutions: $|\sin x| \leq 1$, so $\left|\frac{x}{10}\right| \leq 1$, i.e. $-10 \leq x \leq 10$.",
         r"Outside that range the line is beyond the reach of the sine curve, so no intersections are possible."),
        (r"Note both sides are odd functions, so intersections come in $\pm$ pairs; count for $x > 0$ and double, then add $x = 0$ (which is a solution).",
         r"$\sin(-x) = -\sin(-x)$... more simply, if $x_0$ is a solution so is $-x_0$, because both sides change sign together."),
        (r"For $0 < x \leq 10$: on $(0, \pi)$ the sine hump starts steeper than the line and ends below it, giving **one** crossing. On $(\pi, 2\pi)$ the sine is negative while the line is positive: **none**.",
         r"Near $0$, $\sin x$ rises much faster than $\frac{x}{10}$; by $x = \pi$ it has returned to $0$, below the line's value $0.31$."),
        (r"On $(2\pi, 3\pi)$ (i.e. up to $9.42$) the line runs from $0.63$ to $0.94$ while the sine hump rises to $1$ and falls back: **two** crossings. Beyond $3\pi$ the next hump starts past $x = 4\pi > 10$.",
         r"A hump that rises above the line and comes back down crosses it twice."),
        (r"So $3$ positive solutions, $3$ negative and $x = 0$: **7** in total.",
         r"Doubling the positive count and adding the origin."),
    ],
    pitfalls=[r"Forgetting $x = 0$ and answering $6$.",
              r"Missing that the hump near $x = 8$ crosses the line **twice**, and answering $5$."],
    takeaway=r"For $\sin x = kx$, sketch both graphs, bound the region by $|kx| \leq 1$, and use oddness to halve the counting."),

"TRG-11": Sol(
    idea=r"Range of $a\sin(bx) + c$. Only $a$ and $c$ matter - the $b$ affects the period, not the values taken.",
    steps=[
        (r"$\sin(2x)$ takes every value in $[-1, 1]$.",
         r"Compressing horizontally changes how fast the wave oscillates, not how high it goes."),
        (r"Multiply by $3$: the range becomes $[-3, 3]$.",
         r"Amplitude $|a| = 3$."),
        (r"Subtract $1$: the range becomes $[-4, 2]$.",
         r"The whole wave shifts down by $1$."),
        (r"Difference between maximum and minimum: $2 - (-4) = 6$.",
         r"Equivalently $2 \times$ amplitude $= 2 \times 3 = 6$ - the vertical shift cancels out of a difference."),
    ],
    pitfalls=[r"Answering $3$ (the amplitude) instead of the full range $2a$.",
              r"Letting the $-1$ affect the difference, giving $7$ or $5$."],
    takeaway=r"Max minus min for $a\sin(\cdot) + c$ is always $2|a|$; vertical shifts cancel."),

"TRG-12": Sol(
    idea=r"A squared tangent equation. Two values of $\tan x$, each giving solutions once per $\pi$.",
    steps=[
        (r"Take square roots: $\tan x = \pm\sqrt3$.",
         r"Both signs are needed."),
        (r"$\tan x = \sqrt3$ gives $x = \frac{\pi}{3}$ and $\frac{\pi}{3} + \pi = \frac{4\pi}{3}$.",
         r"Period $\pi$ for $\tan$."),
        (r"$\tan x = -\sqrt3$ gives $x = \frac{2\pi}{3}$ and $\frac{2\pi}{3} + \pi = \frac{5\pi}{3}$.",
         r"$\tan$ is negative in quadrants 2 and 4; the reference angle is still $\frac\pi3$."),
        (r"Four solutions in $[0, 2\pi)$.",
         r"Two values $\times$ two periods."),
    ],
    pitfalls=[r"Taking only the positive root and answering $2$.",
              r"Using period $2\pi$ for $\tan$."],
    takeaway=r"$\tan^2 x = k$ gives $\tan x = \pm\sqrt k$, and each has one solution per interval of length $\pi$."),

"TRG-13": Sol(
    idea=r"Expanding two brackets whose cross terms cancel. The Pythagorean identity finishes it.",
    steps=[
        (r"Expand the first: $(\sin\theta + \cos\theta)^2 = \sin^2\theta + 2\sin\theta\cos\theta + \cos^2\theta$.",
         r"Standard $(a+b)^2$ expansion."),
        (r"Expand the second: $(\sin\theta - \cos\theta)^2 = \sin^2\theta - 2\sin\theta\cos\theta + \cos^2\theta$.",
         r"Only the middle sign changes."),
        (r"Add: the $\pm2\sin\theta\cos\theta$ terms cancel, leaving $2(\sin^2\theta + \cos^2\theta)$.",
         r"This cancellation is the point of the question."),
        (r"Apply the identity: $2 \times 1 = 2$.",
         r"$\sin^2 + \cos^2 = 1$ for every $\theta$, so the answer is a constant."),
    ],
    pitfalls=[r"Keeping a cross term and choosing $2 + 2\sin\theta\cos\theta$ - an offered option.",
              r"Answering $1$ by forgetting the factor $2$."],
    takeaway=r"$(a+b)^2 + (a-b)^2 = 2(a^2+b^2)$; with $\sin$ and $\cos$ that is always $2$."),

"TRG-14": Sol(
    idea=r"Another quadratic in $\sin x$, but this one has no constant term, so factorising gives $\sin x = 0$ as well - and the interval is open.",
    steps=[
        (r"Replace $\cos^2 x$: $12(1 - \sin^2 x) + 6\sin x - 10 = 2$.",
         r"Convert to a single trig function."),
        (r"Tidy: $12 - 12\sin^2x + 6\sin x - 12 = 0 \Rightarrow -12\sin^2 x + 6\sin x = 0 \Rightarrow 6\sin x(2\sin x - 1) = 0$.",
         r"The constants cancel completely, leaving a **factorisable** expression with no constant term - do not divide by $\sin x$, or you lose solutions."),
        (r"$\sin x = 0$ gives $x = 180^\circ$ within the open interval ($0^\circ$ and $360^\circ$ are excluded).",
         r"The interval is $0^\circ < x < 360^\circ$, strict at both ends - so the endpoints are out but $180^\circ$ is in."),
        (r"$\sin x = \frac12$ gives $x = 30^\circ$ and $150^\circ$.",
         r"First and second quadrants."),
        (r"Complete set: $30^\circ, 150^\circ, 180^\circ$.",
         r"Three solutions - the $180^\circ$ is what distinguishes the correct option."),
    ],
    pitfalls=[r"Dividing by $\sin x$ and losing $180^\circ$, giving just $30^\circ, 150^\circ$ - an offered option.",
              r"Including $0^\circ$ and $360^\circ$, which the strict inequalities exclude."],
    takeaway=r"Never divide by a trig function: factorise, so the zero solutions survive; then read the interval's endpoints carefully."),

"TRG-15": Sol(
    idea=r"A graphical comparison. The line $y = x$ grows without bound while $\sin x$ is trapped between $-1$ and $1$.",
    steps=[
        (r"Note $x = 0$ is a solution: $\sin 0 = 0$.",
         r"Both graphs pass through the origin."),
        (r"For $x > 0$, $\sin x < x$ always (the sine curve leaves the origin with gradient $1$ and then bends away below the line).",
         r"The gradient of $\sin x$ is at most $1$, and it is strictly less than $1$ after the origin, so the line pulls ahead immediately."),
        (r"For $x < 0$, by symmetry (both functions are odd), $\sin x > x$.",
         r"Odd symmetry means the picture is rotated, not reflected - so again no crossing."),
        (r"Hence exactly one intersection, at the origin.",
         r"The answer is $1$."),
    ],
    pitfalls=[r"Answering 'infinitely many' by confusing $y = x$ with a horizontal line like $y = 0.5$.",
              r"Thinking there must be crossings because the sine oscillates - it oscillates, but only within $[-1,1]$."],
    takeaway=r"$|\sin x| \leq 1$ while $|x|$ grows: only the origin can satisfy $\sin x = x$."),

"TRG-16": Sol(
    idea=r"Convert a sum of $\sin$ and $\cos$ into a single $\tan$ equation by dividing.",
    steps=[
        (r"Rearrange: $\sin x = -\cos x$.",
         r"Move one term across."),
        (r"Divide by $\cos x$: $\tan x = -1$. (Check $\cos x = 0$ separately: then $\sin x = 0$ too, impossible.)",
         r"Dividing by $\cos x$ is safe only after ruling out $\cos x = 0$ - and here that case gives a contradiction."),
        (r"Solve on $[0, 2\pi)$: $\tan x = -1$ at $x = \frac{3\pi}{4}$ and $x = \frac{3\pi}{4} + \pi = \frac{7\pi}{4}$.",
         r"Reference angle $\frac\pi4$, negative tangent in quadrants 2 and 4."),
        (r"Sum: $\frac{3\pi}{4} + \frac{7\pi}{4} = \frac{10\pi}{4} = \frac{5\pi}{2}$.",
         r"Add over the common denominator and simplify."),
    ],
    pitfalls=[r"Finding only one solution and answering $\frac{3\pi}{4}$ - an offered option.",
              r"Forgetting to justify dividing by $\cos x$ (here it is fine, but the habit matters)."],
    takeaway=r"$a\sin x + b\cos x = 0$ becomes $\tan x = -\frac ba$; check the $\cos x = 0$ case before dividing."),

"TRG-17": Sol(
    idea=r"Three identity claims. Two are standard, one is a classic false 'linearity' claim.",
    steps=[
        (r"I: $\sin^2 x + \cos^2 x = 1$ is the Pythagorean identity, true for every $x$. **True.**",
         r"It follows from Pythagoras applied to the unit circle."),
        (r"II: test $x = \frac{\pi}{2}$: $\sin\pi = 0$ but $2\sin\frac\pi2 = 2$. **False.**",
         r"Trig functions are not linear: $\sin(2x) \neq 2\sin x$ (the correct identity, off-specification here, is $2\sin x\cos x$)."),
        (r"III: shifting $\sin$ by half a period reflects it: $\sin(x + \pi) = -\sin x$. **True.**",
         r"Check at $x = 0$: $\sin\pi = 0 = -\sin 0$ ✓; at $x = \frac\pi2$: $\sin\frac{3\pi}{2} = -1 = -\sin\frac\pi2$ ✓."),
        (r"I and III only.",
         r"Match to the options."),
    ],
    pitfalls=[r"Accepting II because it 'looks like' a factor coming out.",
              r"Doubting III - test it at two values to be sure."],
    takeaway=r"Functions are almost never linear: $f(2x) \neq 2f(x)$ in general. Test suspicious identities at $x = \frac\pi2$."),

"TRG-18": Sol(
    idea=r"Exact-value recall plus one squared value. The first product is designed to collapse to $1$.",
    steps=[
        (r"$\tan 30^\circ = \dfrac{1}{\sqrt3}$ and $\tan 60^\circ = \sqrt3$, so their product is $1$.",
         r"$30^\circ$ and $60^\circ$ are complementary, and $\tan\theta\tan(90^\circ - \theta) = 1$ always."),
        (r"$\sin 45^\circ = \dfrac{\sqrt2}{2}$, so $\sin^2 45^\circ = \dfrac{2}{4} = \dfrac12$.",
         r"Square top and bottom: $(\sqrt2)^2 = 2$ and $2^2 = 4$."),
        (r"Add: $1 + \frac12 = \frac32$.",
         r"Straightforward once both pieces are exact."),
    ],
    pitfalls=[r"Writing $\sin^2 45^\circ = \frac{\sqrt2}{2}$ (forgetting to square), giving $1 + \frac{\sqrt2}{2}$.",
              r"Using $\tan 30^\circ = \sqrt3$, which makes the product $3$."],
    takeaway=r"$\tan\theta \tan(90^\circ - \theta) = 1$, and $\sin^2 45^\circ = \cos^2 45^\circ = \frac12$."),

}
