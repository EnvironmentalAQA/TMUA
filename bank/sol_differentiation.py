"""Full teaching solutions: differentiation (DIF-xx)."""
from gen.model import Sol

SOLUTIONS = {

"DIF-01": Sol(
    idea=r"The spec only allows differentiating powers of $x$, so the expression must first be written as a sum of such powers - expand and divide term by term.",
    steps=[
        (r"Expand the numerator: $(3x-2)^2 = 9x^2 - 12x + 4$.",
         r"There is no quotient or chain rule available, so the fraction must be dismantled."),
        (r"Divide each term by $x^2$: $y = 9 - 12x^{-1} + 4x^{-2}$.",
         r"$\frac{9x^2}{x^2} = 9$, $\frac{-12x}{x^2} = -12x^{-1}$, $\frac{4}{x^2} = 4x^{-2}$."),
        (r"Differentiate term by term with $\frac{d}{dx}x^n = nx^{n-1}$: $0 + 12x^{-2} - 8x^{-3}$.",
         r"$-12 \times (-1) = +12$ and $4 \times (-2) = -8$; the constant $9$ differentiates to $0$."),
        (r"Write in fraction form: $\dfrac{12}{x^2} - \dfrac{8}{x^3}$.",
         r"Match the form used in the options."),
    ],
    pitfalls=[r"Differentiating the bracket directly as $\frac{6(3x-2)}{x^2}$ - that would need the quotient rule (and is wrong anyway).",
              r"Sign slips: differentiating $x^{-1}$ gives $-x^{-2}$, so $-12x^{-1}$ gives $+12x^{-2}$."],
    takeaway=r"Rewrite as $\sum ax^n$ before differentiating; negative powers change sign when differentiated."),

"DIF-02": Sol(
    idea=r"Stationary points from $f' = 0$, their nature from the sign of $f''$, and the $y$-values by substitution.",
    steps=[
        (r"Differentiate: $y' = 3x^2 - 6x - 9 = 3(x^2 - 2x - 3) = 3(x-3)(x+1)$.",
         r"Factor out the $3$ first - it makes the factorisation obvious."),
        (r"Solve $y' = 0$: $x = 3$ and $x = -1$.",
         r"Stationary points are where the gradient vanishes."),
        (r"Second derivative: $y'' = 6x - 6$. At $x = -1$, $y'' = -12 < 0$ (maximum); at $x = 3$, $y'' = 12 > 0$ (minimum).",
         r"Negative second derivative means the curve bends downwards - a maximum."),
        (r"Find the $y$-values: $y(-1) = -1 - 3 + 9 + 5 = 10$; $y(3) = 27 - 27 - 27 + 5 = -22$.",
         r"Substitute into the original function, not the derivative."),
    ],
    pitfalls=[r"Swapping the natures - for a positive cubic the maximum always comes first (smaller $x$).",
              r"Substituting into $y'$ instead of $y$ for the coordinates."],
    takeaway=r"$f' = 0$ locates stationary points; the sign of $f''$ classifies them; substitute into $f$ for the heights."),

"DIF-03": Sol(
    idea=r"Tangent line: gradient from the derivative, point from the curve, then find where it meets the axis.",
    steps=[
        (r"Differentiate: $y' = 2x - 4$; at $x = 3$ the gradient is $2$.",
         r"The derivative evaluated at a point gives the tangent's gradient there."),
        (r"Find the point: $y(3) = 9 - 12 + 1 = -2$, so the tangent touches at $(3, -2)$.",
         r"The tangent passes through the curve at that $x$ - use the original function."),
        (r"Write the tangent: $y + 2 = 2(x - 3)$.",
         r"Point-gradient form with the point and gradient just found."),
        (r"Set $x = 0$: $y + 2 = -6$, so $y = -8$. The tangent meets the $y$-axis at $(0, -8)$.",
         r"The $y$-axis is $x = 0$."),
    ],
    pitfalls=[r"Using $y(3) = -2$ as the intercept and answering $(0,-2)$.",
              r"Sign slip: $y = 2x - 8$, not $2x + 8$."],
    takeaway=r"Tangent $=$ gradient from $f'$ $+$ point from $f$; then substitute $x = 0$ for the intercept."),

"DIF-04": Sol(
    idea=r"Normal line: the negative reciprocal of the tangent's gradient, through the same point.",
    steps=[
        (r"Write $y = x^{1/2}$ and differentiate: $y' = \frac12 x^{-1/2} = \dfrac{1}{2\sqrt x}$.",
         r"Convert the root to a fractional power before differentiating."),
        (r"At $x = 4$: $y' = \dfrac{1}{2 \times 2} = \dfrac14$.",
         r"$\sqrt4 = 2$."),
        (r"Normal gradient $= -\dfrac{1}{1/4} = -4$.",
         r"Normal is perpendicular to the tangent: negative reciprocal."),
        (r"Line through $(4,2)$: $y - 2 = -4(x - 4) \Rightarrow y = -4x + 18$.",
         r"$-4 \times -4 = +16$, plus the $2$."),
    ],
    pitfalls=[r"Using the tangent gradient $\frac14$ and choosing $y = \frac14x + 1$.",
              r"Arithmetic on the constant: $y = -4x + 16$ is offered."],
    takeaway=r"Normal gradient $= -1/f'(x_1)$; then substitute the point into the point-gradient form."),

"DIF-05": Sol(
    idea=r"'Decreasing' is the condition $f'(x) < 0$ - a quadratic inequality once the derivative is found.",
    steps=[
        (r"Differentiate: $f'(x) = 6x^2 - 30x + 24$.",
         r"Term by term."),
        (r"Factorise: $6(x^2 - 5x + 4) = 6(x-1)(x-4)$.",
         r"Taking out the $6$ makes the roots visible."),
        (r"Solve $f'(x) < 0$: the upward parabola is negative between its roots, so $1 < x < 4$.",
         r"The gradient is negative exactly where the function falls."),
    ],
    pitfalls=[r"Solving $f'(x) > 0$ and answering $x < 1$ or $x > 4$ - which is offered.",
              r"Forgetting the factor $6$ when factorising, giving the wrong roots."],
    takeaway=r"Decreasing $\Leftrightarrow f' < 0$; find the roots of $f'$ and use the shape of its graph."),

"DIF-06": Sol(
    idea=r"'At rest' means velocity zero, and velocity is the derivative of displacement.",
    steps=[
        (r"Differentiate the displacement: $v = \dfrac{ds}{dt} = 3t^2 - 12t + 9$.",
         r"Velocity is the rate of change of displacement."),
        (r"Factorise: $3(t^2 - 4t + 3) = 3(t-1)(t-3)$.",
         r"Take the $3$ out first."),
        (r"Set $v = 0$: $t = 1$ and $t = 3$.",
         r"'Momentarily at rest' is exactly $v = 0$."),
    ],
    pitfalls=[r"Setting $s = 0$ instead of $v = 0$, which gives $t = 0$ and $t = 3$ - an offered option.",
              r"Forgetting one of the two roots."],
    takeaway=r"Displacement $\to$ velocity $\to$ acceleration by differentiating; 'at rest' means the velocity is zero, not the displacement."),

"DIF-07": Sol(
    idea=r"A stationary point gives two conditions: the derivative vanishes there, and the point is on the curve.",
    steps=[
        (r"Differentiate: $y' = 2ax + b$. At $x = 2$: $4a + b = 0$, so $b = -4a$.",
         r"Stationary means the gradient is zero at that $x$."),
        (r"The point is on the curve: $y(2) = 4a + 2b = -8$.",
         r"Substitute $x = 2$ into the original function and set it equal to the given $y$."),
        (r"Substitute $b = -4a$: $4a - 8a = -4a = -8$, so $a = 2$ and $b = -8$.",
         r"One equation in one unknown after substitution."),
        (r"Compute $a + b = 2 + (-8) = -6$.",
         r"The question asks for the sum."),
    ],
    pitfalls=[r"Using only one of the two conditions.",
              r"Sign error giving $a = -2$ and the answer $6$."],
    takeaway=r"'Stationary point at $(p,q)$' is two equations: $f'(p) = 0$ and $f(p) = q$."),

"DIF-08": Sol(
    idea=r"Differentiating fractional powers. Factorising the derivative makes the sign change easy to see.",
    steps=[
        (r"Differentiate: $f'(x) = \frac32 x^{1/2} - 3 \times \frac12 x^{-1/2} = \frac32 x^{1/2} - 3x^{-1/2}$.",
         r"$\frac{d}{dx}x^{3/2} = \frac32 x^{1/2}$ and $\frac{d}{dx}(6x^{1/2}) = 3x^{-1/2}$."),
        (r"Factor out $\dfrac{3}{2\sqrt x}$: $f'(x) = \dfrac{3}{2\sqrt x}\left(x - 2\right)$.",
         r"$\frac32 x^{1/2} = \frac{3}{2\sqrt x}\cdot x$ and $3x^{-1/2} = \frac{3}{2\sqrt x}\cdot 2$. Factorising isolates the sign-changing part."),
        (r"Set $f' = 0$: since $\frac{3}{2\sqrt x} > 0$ for $x > 0$, the only root is $x = 2$.",
         r"A positive factor can never make the product zero."),
        (r"Check it is a minimum: $f'$ is negative for $x < 2$ and positive for $x > 2$, so the curve falls then rises.",
         r"The sign of $f'$ is the sign of $(x-2)$ - immediate from the factorised form."),
    ],
    pitfalls=[r"Making index errors: $\frac{d}{dx}x^{1/2} = \frac12 x^{-1/2}$, not $\frac12 x^{1/2}$.",
              r"Squaring both sides carelessly when solving $\frac32\sqrt x = \frac{3}{\sqrt x}$ and getting $x = 4$."],
    takeaway=r"Factor a common power out of the derivative: the remaining bracket controls the sign."),

"DIF-09": Sol(
    idea=r"A standard optimisation: express the area in one variable using the constraint, then differentiate.",
    steps=[
        (r"Let one side be $x$; the perimeter condition $2x + 2y = 40$ gives $y = 20 - x$.",
         r"Use the constraint to eliminate the second variable - optimisation needs a single variable."),
        (r"Write the area: $A = x(20 - x) = 20x - x^2$.",
         r"A quadratic in $x$."),
        (r"Differentiate and solve: $A' = 20 - 2x = 0$ at $x = 10$.",
         r"Or complete the square: $A = 100 - (x-10)^2$, which shows the maximum immediately."),
        (r"Compute the area: $A = 10 \times 10 = 100$ (a square).",
         r"$A'' = -2 < 0$ confirms a maximum."),
    ],
    pitfalls=[r"Using $x + y = 40$ instead of $2x + 2y = 40$, giving $400$ - an offered option.",
              r"Reporting the side length $10$ rather than the area."],
    takeaway=r"For fixed perimeter, the rectangle of greatest area is the square - but show it via the constraint and the derivative."),

"DIF-10": Sol(
    idea=r"Known stationary points mean known roots of $f'$. Compare the factorised derivative with its expanded form.",
    steps=[
        (r"Differentiate: $y' = 3x^2 + 2px + q$.",
         r"A cubic's derivative is a quadratic."),
        (r"The stationary points are its roots, so $y' = 3(x-1)(x-3)$.",
         r"The leading coefficient must be $3$ to match $3x^2$."),
        (r"Expand: $3(x^2 - 4x + 3) = 3x^2 - 12x + 9$.",
         r"Multiply out to compare coefficients."),
        (r"Compare constants: $q = 9$ (and comparing $x$ terms gives $2p = -12$, so $p = -6$).",
         r"The question asks only for $q$."),
    ],
    pitfalls=[r"Forgetting the leading $3$ and getting $q = 3$.",
              r"Answering $-6$, which is $p$."],
    takeaway=r"Stationary points are roots of $f'$: build $f'$ in factorised form with the correct leading coefficient."),

"DIF-11": Sol(
    idea=r"Three claims about a cubic. The derivative settles the first two; the third is about global behaviour, where cubics are unbounded.",
    steps=[
        (r"Differentiate: $f'(x) = 3x^2 - 3 = 3(x-1)(x+1)$.",
         r"The roots $\pm1$ are the stationary points."),
        (r"I: for $x > 1$ both factors are positive, so $f' > 0$ and $f$ is increasing. **True.**",
         r"Sign analysis of the factorised derivative."),
        (r"II: $f'' = 6x$, so $f''(-1) = -6 < 0$: local maximum at $x = -1$. **True.**",
         r"Negative second derivative means a local maximum."),
        (r"III: the local minimum is $f(1) = -2$, but as $x \to -\infty$, $f(x) \to -\infty$ - for instance $f(-3) = -27 + 9 = -18$. **False.**",
         r"A **local** minimum is not a global one; odd-degree polynomials are unbounded below."),
        (r"I and II only.",
         r"Match to the options."),
    ],
    pitfalls=[r"Assuming the local minimum value bounds the whole function.",
              r"Confusing the maximum and minimum positions - for $+x^3$ the maximum is at the smaller $x$."],
    takeaway=r"Cubics have no global maximum or minimum; 'local' claims need $f'$, 'global' claims need the end behaviour."),

"DIF-12": Sol(
    idea=r"Tangency via calculus: the gradients must match, which locates the point of contact.",
    steps=[
        (r"Differentiate the curve: $y' = 2x + 2$.",
         r"The tangent's gradient equals the curve's gradient at the contact point."),
        (r"Set it equal to the line's gradient: $2x + 2 = 4$, so $x = 1$.",
         r"This finds **where** the tangent touches."),
        (r"Find the $y$-value on the curve: $y(1) = 1 + 2 + 5 = 8$.",
         r"The contact point is on the curve."),
        (r"The point must also be on the line: $8 = 4(1) + c$, so $c = 4$.",
         r"Substituting the contact point into the line's equation gives $c$."),
    ],
    pitfalls=[r"Using the discriminant route but mis-expanding and getting $c = 1$ or $5$ (both offered).",
              r"Substituting into the line the $y$-value from the wrong $x$."],
    takeaway=r"Tangency: equal gradients give the $x$; equal $y$-values give the constant."),

"DIF-13": Sol(
    idea=r"Reading a factorised derivative. A squared factor does **not** change the sign, so it gives a stationary point that is not a turning point.",
    steps=[
        (r"The stationary points are the roots of $f'$: $x = -1$ and $x = 2$.",
         r"$f'(x) = 0$ at both."),
        (r"Near $x = -1$: $(x-2)^2 > 0$ always, so the sign of $f'$ is the sign of $(x+1)$ - negative then positive.",
         r"A sign change from $-$ to $+$ means the function falls then rises: a local minimum."),
        (r"Near $x = 2$: $(x+1) > 0$ there, and $(x-2)^2 \geq 0$, so $f' \geq 0$ on both sides - no sign change.",
         r"A repeated (even-power) factor touches zero without crossing, so the gradient does not change sign."),
        (r"Conclusion: local minimum at $x = -1$; stationary but **not** a turning point at $x = 2$.",
         r"That is a stationary point of inflexion."),
    ],
    pitfalls=[r"Assuming every root of $f'$ is a turning point.",
              r"Using $f''(2) = 0$ to conclude 'maximum' or 'minimum' - a zero second derivative is inconclusive."],
    takeaway=r"Odd-power factors of $f'$ change sign (turning points); even-power factors do not (inflexions)."),

"DIF-14": Sol(
    idea=r"Two differentiations of powers, with negative and fractional indices. Rewrite first.",
    steps=[
        (r"Rewrite: $y = x^{-2} + 4x^{1/2}$.",
         r"Roots and reciprocals must become powers before the rule applies."),
        (r"First derivative: $y' = -2x^{-3} + 4 \times \frac12 x^{-1/2} = -2x^{-3} + 2x^{-1/2}$.",
         r"$-2 \times x^{-2-1}$ and $\frac12 \times 4 = 2$."),
        (r"Second derivative: $y'' = -2(-3)x^{-4} + 2\left(-\frac12\right)x^{-3/2} = 6x^{-4} - x^{-3/2}$.",
         r"Differentiate again, watching the signs: $-3$ times $-2$ gives $+6$."),
        (r"Write it as $\dfrac{6}{x^4} - x^{-3/2}$.",
         r"Matching the option format."),
    ],
    pitfalls=[r"Losing a sign and answering $\frac{6}{x^4} + x^{-3/2}$.",
              r"Stopping after the first derivative."],
    takeaway=r"Differentiate twice, carefully: each negative index gains one more negative factor."),

"DIF-15": Sol(
    idea=r"Maximise a cubic on an interval. Differentiate, find the interior stationary point, and evaluate.",
    steps=[
        (r"Differentiate: $V' = 8x - 3x^2 = x(8 - 3x)$.",
         r"Factorise to find the roots easily."),
        (r"Roots at $x = 0$ and $x = \frac83$. Only $x = \frac83$ is inside $0 < x < 4$ with $V' $ changing from $+$ to $-$ there.",
         r"$x = 0$ is an endpoint (and gives zero volume), so the maximum is at $\frac83$."),
        (r"Evaluate: $V = 4\left(\frac83\right)^2 - \left(\frac83\right)^3 = \frac{256}{9} - \frac{512}{27}$.",
         r"$\left(\frac83\right)^2 = \frac{64}{9}$, so $4 \times \frac{64}{9} = \frac{256}{9}$; and $\left(\frac83\right)^3 = \frac{512}{27}$."),
        (r"Common denominator $27$: $\dfrac{768 - 512}{27} = \dfrac{256}{27}$.",
         r"$\frac{256}{9} = \frac{768}{27}$."),
    ],
    pitfalls=[r"Arithmetic slips with the fractions - $\frac{128}{27}$ and $\frac{64}{27}$ are both offered.",
              r"Taking $x = 0$ as the maximiser."],
    takeaway=r"Optimise on an interval: check interior stationary points **and** whether they are maxima; keep fractions exact."),

"DIF-16": Sol(
    idea=r"A tangent meeting the curve again. The tangency shows up as a repeated root, which lets you factorise the cubic without solving it.",
    steps=[
        (r"Find the tangent at $(a, a^3)$: $y' = 3x^2$, so the gradient is $3a^2$ and the line is $y = 3a^2(x - a) + a^3 = 3a^2x - 2a^3$.",
         r"Point-gradient form, then simplify."),
        (r"Set the tangent equal to the curve: $x^3 = 3a^2 x - 2a^3$, i.e. $x^3 - 3a^2x + 2a^3 = 0$.",
         r"Intersections satisfy both equations."),
        (r"$x = a$ is a **repeated** root (that is what tangency means), so factor out $(x-a)^2$: $x^3 - 3a^2x + 2a^3 = (x-a)^2(x + 2a)$.",
         r"Check by comparing the constant term: $(-a)^2(2a) = 2a^3$ ✓."),
        (r"The remaining root is $x = -2a$.",
         r"That is where the tangent cuts the curve again."),
    ],
    pitfalls=[r"Forgetting that tangency gives a **double** root and trying to factor out only one $(x-a)$.",
              r"Sign error giving $x = 2a$."],
    takeaway=r"A tangent meets the curve in a repeated root; factor $(x - a)^2$ out and read off the third root."),

"DIF-17": Sol(
    idea=r"Find the second crossing point in terms of $k$, then impose the gradient condition there.",
    steps=[
        (r"Find the $x$-intercepts: $x^2 + kx = x(x + k) = 0$, so $x = 0$ or $x = -k$. Thus $P = (-k, 0)$.",
         r"With $k < 0$, $-k$ is positive - the curve crosses to the right of the origin."),
        (r"Differentiate: $y' = 2x + k$.",
         r"The gradient at any point."),
        (r"Evaluate at $P$: $y'(-k) = -2k + k = -k$.",
         r"Substituting $x = -k$."),
        (r"Set equal to $6$: $-k = 6$, so $k = -6$.",
         r"Consistent with the given condition $k < 0$ ✓."),
    ],
    pitfalls=[r"Using $x = k$ for the second intercept, giving $k = 2$ or $3k = 6$.",
              r"Answering $6$ and ignoring the stated sign of $k$."],
    takeaway=r"Find the point in terms of the parameter first, then apply the gradient condition; check any sign restriction at the end."),

"DIF-18": Sol(
    idea=r"Minimising $x + \frac4x$. Differentiate, solve, and confirm it is a minimum.",
    steps=[
        (r"Write as powers: $y = x + 4x^{-1}$ and differentiate: $y' = 1 - 4x^{-2}$.",
         r"$\frac{d}{dx}(4x^{-1}) = -4x^{-2}$."),
        (r"Solve $y' = 0$: $1 = \dfrac{4}{x^2} \Rightarrow x^2 = 4 \Rightarrow x = 2$ (taking the positive root since $x > 0$).",
         r"The restriction $x > 0$ discards $x = -2$."),
        (r"Confirm a minimum: $y'' = 8x^{-3} > 0$ for $x > 0$.",
         r"Positive second derivative means the curve bends upwards."),
        (r"Evaluate: $y = 2 + \dfrac42 = 4$.",
         r"(Also follows from AM-GM: $x + \frac4x \geq 2\sqrt{4} = 4$.)"),
    ],
    pitfalls=[r"Giving the minimising $x = 2$ instead of the minimum value $4$ - both are offered.",
              r"Including $x = -2$, where the expression equals $-4$ but $x > 0$ is required."],
    takeaway=r"$x + \frac kx \geq 2\sqrt k$ for $x > 0$, with equality at $x = \sqrt k$ - worth recognising instantly."),

"DIF-19": Sol(
    idea=r"Three general claims about differentiable functions. The first is the classic false one; the others are standard facts.",
    steps=[
        (r"I: test $f(x) = x^3$ at $a = 0$: $f'(0) = 0$ but the function is increasing throughout, so there is no maximum or minimum. **False.**",
         r"A stationary point can be a point of inflexion."),
        (r"II: at an interior local minimum of a differentiable function the derivative must vanish (otherwise you could move downhill in one direction). **True.**",
         r"This is Fermat's stationary-point theorem, and is why we solve $f' = 0$ in the first place."),
        (r"III: if $f' > 0$ everywhere then $f$ is strictly increasing, so $f(3) > f(2)$. **True.**",
         r"Positive gradient throughout means the value rises as $x$ rises."),
        (r"II and III only.",
         r"Match to the options."),
    ],
    pitfalls=[r"Accepting I because 'we find maxima and minima by setting $f' = 0$' - that finds candidates, not guarantees.",
              r"Doubting II by thinking of endpoints, which the word 'every real number' excludes."],
    takeaway=r"$f'(a) = 0$ is necessary but not sufficient for a turning point; inflexions are the counterexample."),

"DIF-20": Sol(
    idea=r"Find both stationary points and add their $y$-values - two substitutions after one factorisation.",
    steps=[
        (r"Differentiate: $y' = 6x^2 - 18x + 12 = 6(x^2 - 3x + 2) = 6(x-1)(x-2)$.",
         r"Take out the $6$, then factorise."),
        (r"Stationary points at $x = 1$ and $x = 2$.",
         r"Roots of the derivative."),
        (r"Compute the $y$-values: $y(1) = 2 - 9 + 12 - 3 = 2$; $y(2) = 16 - 36 + 24 - 3 = 1$.",
         r"Substitute into the original cubic, carefully: $2(8) = 16$ and $9(4) = 36$."),
        (r"Add: $2 + 1 = 3$.",
         r"The question asks for the sum of the $y$-coordinates."),
    ],
    pitfalls=[r"Adding the $x$-coordinates ($1 + 2 = 3$) - the same answer here by coincidence, but the wrong method.",
              r"Arithmetic slips in $y(2)$; recompute $16 - 36 = -20$, $-20 + 24 = 4$, $4 - 3 = 1$."],
    takeaway=r"Two stationary points mean two substitutions into the original function - the derivative gives only the positions."),

}
