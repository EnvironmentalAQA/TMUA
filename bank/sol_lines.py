"""Full teaching solutions: straight lines (LIN-xx)."""
from gen.model import Sol

SOLUTIONS = {

"LIN-01": Sol(
    idea=r"Perpendicular line through a point: find the gradient of the given line, take the negative reciprocal, then use the point-gradient form.",
    steps=[
        (r"Rearrange $3x - 2y + 5 = 0$ into $y = \frac32 x + \frac52$, so its gradient is $\frac32$.",
         r"Alternatively use the shortcut: $ax + by + c = 0$ has gradient $-\frac ab = -\frac{3}{-2} = \frac32$."),
        (r"Perpendicular gradient: $-\dfrac{1}{3/2} = -\dfrac23$.",
         r"Perpendicular gradients multiply to $-1$; invert and change sign."),
        (r"Use $y - y_1 = m(x - x_1)$ at $(2, -3)$: $y + 3 = -\frac23(x - 2)$.",
         r"$y - (-3)$ is $y + 3$ - the commonest sign slip in this whole topic."),
        (r"Clear fractions and tidy: $3y + 9 = -2x + 4 \Rightarrow 2x + 3y + 5 = 0$.",
         r"Multiply through by $3$ first, then collect everything on one side."),
    ],
    pitfalls=[r"Using $y - 3$ instead of $y + 3$, which gives $2x + 3y - 5 = 0$ - an offered option.",
              r"Taking the perpendicular gradient as $-\frac32$ or $\frac23$."],
    takeaway=r"Negative **reciprocal**, and substitute the point with its own sign: $y - (-3) = y + 3$."),

"LIN-02": Sol(
    idea=r"Collinear points have equal gradients between any pair. Set two gradients equal and solve.",
    steps=[
        (r"Gradient of $AB$: $\dfrac{4 - 2}{5 - 1} = \dfrac{2}{4} = \dfrac12$.",
         r"Any two of the three points determine the line, so compute the gradient from the pair with known coordinates."),
        (r"Gradient of $AC$: $\dfrac{8 - 2}{k - 1} = \dfrac{6}{k-1}$.",
         r"Use the same starting point $A$ for both gradients to avoid sign confusion."),
        (r"Set them equal: $\dfrac{6}{k-1} = \dfrac12$.",
         r"Collinear means the gradient between any pair is the same."),
        (r"Cross-multiply: $k - 1 = 12$, so $k = 13$.",
         r"Check: from $B(5,4)$ to $C(13,8)$ the gradient is $\frac48 = \frac12$ ✓."),
    ],
    pitfalls=[r"Forgetting the $-1$ and answering $12$.",
              r"Inverting the gradient and solving $\frac{k-1}{6} = \frac12$, which gives $k = 4$."],
    takeaway=r"Collinearity is an equal-gradient condition; always verify with the third pair of points."),

"LIN-03": Sol(
    idea=r"Perpendicular distance from a point to a line. The 'area two ways' method avoids memorising the distance formula.",
    steps=[
        (r"The line cuts the axes at $(4,0)$ and $(0,6)$, so with the origin it forms a right-angled triangle of area $\frac12 \times 4 \times 6 = 12$.",
         r"The two intercepts and the origin make a triangle whose legs lie along the axes - its area is easy."),
        (r"The hypotenuse (the segment of $L$) has length $\sqrt{4^2 + 6^2} = \sqrt{52} = 2\sqrt{13}$.",
         r"Pythagoras on the same triangle."),
        (r"Compute the area again using the hypotenuse as base and the required distance $d$ as height: $\frac12 \times 2\sqrt{13} \times d = 12$.",
         r"The perpendicular distance from the origin to $L$ **is** the height of that triangle on that base."),
        (r"Solve: $d = \dfrac{12}{\sqrt{13}}$.",
         r"Equivalently, the formula $\frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$ with $3x + 2y = 12$ gives $\frac{12}{\sqrt{13}}$."),
    ],
    pitfalls=[r"Using the distance to one of the intercepts ($4$, $6$ or $2\sqrt{13}$) instead of the perpendicular distance.",
              r"Forgetting the square root and answering $\frac{12}{13}$."],
    takeaway=r"Area computed two ways turns a distance problem into arithmetic; or use $\frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$."),

"LIN-04": Sol(
    idea=r"A triangle bounded by two lines and an axis. Find the three vertices, then use the axis segment as the base.",
    steps=[
        (r"Find where the two lines meet: $2x + 1 = -x + 7 \Rightarrow 3x = 6 \Rightarrow x = 2$, $y = 5$. Apex $(2,5)$.",
         r"Equate the two expressions for $y$."),
        (r"Find the $x$-intercepts: $2x + 1 = 0$ gives $x = -\frac12$; $-x + 7 = 0$ gives $x = 7$.",
         r"The third side is along the $x$-axis, so the other two vertices are the $x$-intercepts."),
        (r"Base length: from $-\frac12$ to $7$ is $7 - (-\frac12) = \frac{15}{2}$.",
         r"Subtract, do not add; the negative intercept makes the base longer, not shorter."),
        (r"Height is the $y$-coordinate of the apex, $5$: area $= \frac12 \times \frac{15}{2} \times 5 = \frac{75}{4}$.",
         r"With a horizontal base, the height is just the apex's distance from the axis."),
    ],
    pitfalls=[r"Using base $7 - \frac12 = \frac{13}{2}$ by mishandling the negative intercept.",
              r"Using the apex $x$-coordinate $2$ as the height."],
    takeaway=r"Put the base on an axis whenever you can: the height is then simply a coordinate."),

"LIN-05": Sol(
    idea=r"Parallel means equal gradient. Convert each option to gradient form - or compare the coefficient ratios directly.",
    steps=[
        (r"Gradient of $4x + 6y = 9$ is $-\frac{4}{6} = -\frac23$.",
         r"For $ax + by = c$ the gradient is $-\frac ab$."),
        (r"Test the options: $2x + 3y = 1$ has gradient $-\frac23$ ✓.",
         r"Equivalently, the coefficients $(2,3)$ are proportional to $(4,6)$ - the constant term is irrelevant to direction."),
        (r"Reject the rest: $3x - 2y = 4$ gives $\frac32$ (perpendicular), $4x - 6y = 9$ gives $\frac23$, $6x + 4y = 9$ gives $-\frac32$, and $y = \frac32x+1$ gives $\frac32$.",
         r"Note how many distractors are the **perpendicular** gradient - a deliberate trap."),
    ],
    pitfalls=[r"Choosing $6x + 4y = 9$ because the numbers $4$ and $6$ reappear - but swapped, so the gradient changes.",
              r"Forgetting the minus sign in $-\frac ab$."],
    takeaway=r"Parallel $\Leftrightarrow$ the coefficients of $x$ and $y$ are in the same ratio; the constant plays no part."),

"LIN-06": Sol(
    idea=r"Perpendicular bisector: through the midpoint, perpendicular to the segment. Two small calculations, then the point-gradient form.",
    steps=[
        (r"Midpoint: $\left(\frac{1+7}{2}, \frac{5+1}{2}\right) = (4, 3)$.",
         r"The bisector must pass through the middle of the segment."),
        (r"Gradient of the segment: $\dfrac{1 - 5}{7 - 1} = -\dfrac{4}{6} = -\dfrac23$.",
         r"Keep the order of subtraction consistent in numerator and denominator."),
        (r"Perpendicular gradient: $\dfrac32$.",
         r"Negative reciprocal of $-\frac23$."),
        (r"Line through $(4,3)$: $y - 3 = \frac32(x - 4) \Rightarrow 2y - 6 = 3x - 12 \Rightarrow 3x - 2y = 6$.",
         r"Multiply by $2$ to clear the fraction, then collect."),
    ],
    pitfalls=[r"Rearranging to $3x - 2y = 18$ by a sign slip on the constant.",
              r"Using the segment's gradient instead of the perpendicular one."],
    takeaway=r"Perpendicular bisector $=$ midpoint $+$ negative reciprocal gradient; it is the locus of points equidistant from the two ends."),

"LIN-07": Sol(
    idea=r"Intercepts are points on the line. Substitute each one to get an equation for $a$ and for $b$ separately.",
    steps=[
        (r"$x$-intercept $3$ means the point $(3, 0)$ lies on the line: $3a + 0 = 12$, so $a = 4$.",
         r"At an $x$-intercept, $y = 0$."),
        (r"$y$-intercept $-4$ means $(0, -4)$ lies on it: $0 - 4b = 12$, so $b = -3$.",
         r"At a $y$-intercept, $x = 0$. The negative intercept makes $b$ negative."),
        (r"Compute $a - b = 4 - (-3) = 7$.",
         r"Subtracting a negative adds."),
    ],
    pitfalls=[r"Writing $b = 3$ and answering $1$.",
              r"Mixing up which intercept is which and substituting $(0,3)$ and $(-4,0)$."],
    takeaway=r"An intercept is just a point with one coordinate zero - substitute it into the equation."),

"LIN-08": Sol(
    idea=r"A perpendicularity condition with the parameter in both equations. Write both gradients, multiply, set to $-1$.",
    steps=[
        (r"First line $kx + 3y = 2$ has gradient $-\dfrac k3$.",
         r"Using $-\frac ab$ avoids rearranging."),
        (r"Second line $2x - (k-1)y = 5$ has gradient $-\dfrac{2}{-(k-1)} = \dfrac{2}{k-1}$.",
         r"Here $b = -(k-1)$, so the two minus signs cancel."),
        (r"Set the product to $-1$: $-\dfrac{k}{3} \times \dfrac{2}{k-1} = -1$, i.e. $\dfrac{-2k}{3(k-1)} = -1$.",
         r"Perpendicular lines have gradients multiplying to $-1$."),
        (r"Solve: $-2k = -3(k-1) \Rightarrow -2k = -3k + 3 \Rightarrow k = 3$.",
         r"Check: gradients $-1$ and $1$, product $-1$ ✓."),
    ],
    pitfalls=[r"Mishandling the sign of $b$ in the second line and getting $k = -3$ - which is offered.",
              r"Setting the product to $+1$ or the gradients equal (that would be the parallel condition)."],
    takeaway=r"Read gradients as $-\frac ab$ straight from $ax + by = c$, watching the sign of $b$ carefully."),

"LIN-09": Sol(
    idea=r"'Equidistant from two points' means 'on their perpendicular bisector'. Intersect that with the given line.",
    steps=[
        (r"Find the perpendicular bisector of $(0,0)$ and $(4,2)$: midpoint $(2,1)$, segment gradient $\frac12$, so bisector gradient $-2$.",
         r"Equidistant points form the perpendicular bisector - far quicker than setting two distance formulas equal and squaring."),
        (r"Its equation: $y - 1 = -2(x - 2)$, i.e. $y = -2x + 5$.",
         r"Point-gradient form, then tidy."),
        (r"Solve simultaneously with $y = 2x - 1$: $2x - 1 = -2x + 5 \Rightarrow 4x = 6 \Rightarrow x = \frac32$.",
         r"Equate the two expressions for $y$."),
        (r"Then $y = 2(\frac32) - 1 = 2$, so $P = \left(\frac32, 2\right)$.",
         r"Check: distance to $(0,0)$ is $\sqrt{\frac94 + 4}$ and to $(4,2)$ is $\sqrt{\frac{25}{4} + 0}$ - both $\frac52$ ✓."),
    ],
    pitfalls=[r"Using the midpoint $(2,1)$ as the answer without checking it lies on $y = 2x - 1$ (it does not).",
              r"Algebra slips when squaring distances, if you take that longer route."],
    takeaway=r"'Equidistant from two points' $\Rightarrow$ perpendicular bisector; then intersect with whatever else is given."),

"LIN-10": Sol(
    idea=r"The intercept form of a line, plus an optimisation. Statements I and II are quick; III needs a minimisation argument.",
    steps=[
        (r"I: a line with intercepts $a$ and $b$ has equation $\frac xa + \frac yb = 1$; substituting $(2,3)$ gives $\frac2a + \frac3b = 1$. **True.**",
         r"The intercept form is worth knowing precisely for questions like this."),
        (r"II: since $\frac2a$ and $\frac3b$ are both positive and sum to $1$, each is less than $1$, so $a > 2$ and $b > 3$. **True.**",
         r"Two positive numbers summing to $1$ are each below $1$ - a clean argument with no algebra."),
        (r"III: from I, $b = \dfrac{3a}{a - 2}$, so $ab = \dfrac{3a^2}{a-2}$. Put $a = 2 + t$ with $t > 0$: $ab = \dfrac{3(2+t)^2}{t} = 3\left(\dfrac4t + 4 + t\right)$.",
         r"The substitution $a = 2 + t$ clears the awkward denominator and exposes the structure $\frac4t + t$."),
        (r"By AM-GM, $\dfrac4t + t \geq 2\sqrt{4} = 4$, with equality when $t = 2$. So $ab \geq 3(4 + 4) = 24$, attained at $a = 4$, $b = 6$. **True.**",
         r"$u + \frac ku \geq 2\sqrt k$ for positive $u$ - here it gives both the bound and the case of equality, which is what 'smallest possible value' demands."),
        (r"All three are true.",
         r"Match to the options."),
    ],
    pitfalls=[r"Assuming II fails because $a$ and $b$ 'could be anything' - the positivity constraint forces both bounds.",
              r"Claiming III without checking equality is attainable; a lower bound is only the minimum if some case achieves it."],
    takeaway=r"$\frac xa + \frac yb = 1$ is the intercept form; and $t + \frac4t \geq 4$ (AM-GM) is the standard tool for such minimisations."),

"LIN-11": Sol(
    idea=r"A line through a vertex bisects a triangle's area exactly when it hits the midpoint of the opposite side - the two halves then have equal bases and the same height.",
    steps=[
        (r"Identify the side opposite $C$: it is $AB$, from $(0,0)$ to $(6,0)$.",
         r"The line must pass through $C$, so it cuts the opposite side."),
        (r"Its midpoint is $(3, 0)$.",
         r"A median divides the triangle into two triangles with equal bases ($3$ each) and the same apex height, hence equal areas."),
        (r"Find the line through $C(2,4)$ and $(3,0)$: gradient $= \dfrac{0-4}{3-2} = -4$.",
         r"Two points give the gradient directly."),
        (r"Equation: $y - 0 = -4(x - 3)$, i.e. $y = -4x + 12$.",
         r"Using the simpler point $(3,0)$ keeps the arithmetic clean."),
    ],
    pitfalls=[r"Using the midpoint of the wrong side, or the centroid.",
              r"Sign slip giving $y = 4x - 4$, which passes through $(1,0)$ - an offered option."],
    takeaway=r"A median (vertex to opposite midpoint) always bisects the area, whatever the triangle's shape."),

"LIN-12": Sol(
    idea=r"Two conditions on the intersection point. Find the intersection in terms of $m$, then impose positivity on each coordinate.",
    steps=[
        (r"Find the intersection: $mx + 4 = 3x - 2 \Rightarrow x(m - 3) = -6 \Rightarrow x = \dfrac{6}{3 - m}$.",
         r"Keep the denominator as $3 - m$ so that positivity is easy to read."),
        (r"$x > 0$ requires $3 - m > 0$, i.e. $m < 3$.",
         r"The numerator $6$ is positive, so the sign of $x$ is the sign of $3 - m$."),
        (r"$y > 0$: since $y = 3x - 2$, this needs $x > \frac23$, i.e. $\dfrac{6}{3-m} > \dfrac23$.",
         r"Use whichever line is simpler to express $y$ in terms of $x$."),
        (r"With $3 - m > 0$ we may multiply safely: $18 > 2(3 - m) \Rightarrow 18 > 6 - 2m \Rightarrow m > -6$.",
         r"Multiplying by a positive quantity is safe - and we already know $3 - m > 0$ from the first condition."),
        (r"Combine: $-6 < m < 3$.",
         r"Both conditions must hold at once."),
    ],
    pitfalls=[r"Checking only $x > 0$ and answering $m < 3$.",
              r"Multiplying by $3 - m$ without noting its sign - legitimate here only because the first condition established it."],
    takeaway=r"Impose one condition at a time, and use the first to justify the algebra needed for the second."),

"LIN-13": Sol(
    idea=r"Distance between parallel lines. Either use the coefficient formula or take any point on one line and measure to the other.",
    steps=[
        (r"Note both lines have the same left-hand side $3x + 4y$, so they are parallel with normal direction $(3, 4)$, of length $5$.",
         r"The vector of coefficients is perpendicular to the line; its length normalises the distance formula."),
        (r"Use $\text{distance} = \dfrac{|c_1 - c_2|}{\sqrt{a^2 + b^2}} = \dfrac{|20 - 5|}{5}$.",
         r"This is the point-to-line formula applied to any point on the first line."),
        (r"Evaluate: $\dfrac{15}{5} = 3$.",
         r"Check with a concrete point: $(0, \frac54)$ is on the first line, and its distance to $3x + 4y = 20$ is $\frac{|5 - 20|}{5} = 3$ ✓."),
    ],
    pitfalls=[r"Answering $15$ by forgetting to divide by $\sqrt{a^2+b^2}$.",
              r"Using $\sqrt{3^2+4^2} = 7$ (adding instead of squaring), giving $\frac{15}{7}$ - an offered option."],
    takeaway=r"For $ax+by=c_1$ and $ax+by=c_2$: distance $= \frac{|c_1-c_2|}{\sqrt{a^2+b^2}}$; the coefficients must match exactly first."),

"LIN-14": Sol(
    idea=r"The midpoint condition determines both intercepts, and two points give the gradient.",
    steps=[
        (r"Let $A = (p, 0)$ and $B = (0, q)$. Their midpoint is $\left(\frac p2, \frac q2\right)$.",
         r"One intercept on each axis, so each has a zero coordinate."),
        (r"Set the midpoint equal to $(1,2)$: $\frac p2 = 1$ and $\frac q2 = 2$, so $p = 2$, $q = 4$.",
         r"Equate coordinates separately."),
        (r"Gradient through $(2,0)$ and $(0,4)$: $\dfrac{4 - 0}{0 - 2} = -2$.",
         r"Consistent order of subtraction in numerator and denominator."),
    ],
    pitfalls=[r"Halving instead of doubling, giving $A = (\frac12, 0)$ and the wrong gradient.",
              r"Answering $2$ by ignoring that the line falls from left to right."],
    takeaway=r"If $(1,2)$ is the midpoint of the intercepts, the intercepts are $(2,0)$ and $(0,4)$ - double each coordinate."),

}
