"""Full teaching solutions: functions and transformations (FUN-xx)."""
from gen.model import Sol

SOLUTIONS = {

"FUN-01": Sol(
    idea=r"Two transformations applied in a stated order. Apply them one at a time to the equation, in the order given.",
    steps=[
        (r"Translate $3$ in the positive $x$-direction: replace $x$ by $x - 3$, giving $y = (x - 3)^2$.",
         r"A shift **right** by $a$ replaces $x$ with $x - a$ - the sign is opposite to what it looks like, because the new graph reaches a given height $3$ later."),
        (r"Stretch parallel to the $y$-axis with factor $2$: multiply the whole function by $2$, giving $y = 2(x-3)^2$.",
         r"A vertical stretch multiplies every $y$-value, so it acts on the outside of the function."),
    ],
    pitfalls=[r"Writing $(x+3)^2$ - shifting right uses $x - 3$.",
              r"Putting the $2$ inside as $(2x - 3)^2$, which is a horizontal stretch, not a vertical one."],
    takeaway=r"Changes **inside** the function affect $x$ and act in the opposite sense; changes **outside** affect $y$ and act as they read."),

"FUN-02": Sol(
    idea=r"Find the minimum of $f$ first, then move it. Tracking the single turning point is quicker than re-completing the square.",
    steps=[
        (r"Complete the square: $f(x) = x^2 - 4x = (x-2)^2 - 4$, so $f$ has its minimum at $(2, -4)$.",
         r"Half of $-4$ is $-2$; the $-4$ outside is the minimum value."),
        (r"$y = f(x + 2)$ translates the graph $2$ units to the **left**.",
         r"Replacing $x$ by $x + a$ shifts left by $a$: the graph now reaches each value $2$ earlier."),
        (r"Move the turning point: $(2, -4) \to (0, -4)$.",
         r"Only the $x$-coordinate changes; a horizontal translation never alters $y$."),
    ],
    pitfalls=[r"Shifting right and answering $(4, -4)$.",
              r"Changing the $y$-coordinate as well, giving $(0, -2)$ or similar."],
    takeaway=r"$f(x + a)$ moves the graph $a$ to the left; horizontal shifts leave $y$-values untouched."),

"FUN-03": Sol(
    idea=r"Composite functions evaluated at a number. Work strictly from the inside out, and keep the two compositions separate.",
    steps=[
        (r"$g(2) = 2^2 - 3 = 1$, then $f(1) = 2(1) + 1 = 3$. So $f(g(2)) = 3$.",
         r"In $f(g(2))$ the inner function acts first: feed $2$ into $g$, then its output into $f$."),
        (r"$f(2) = 2(2) + 1 = 5$, then $g(5) = 25 - 3 = 22$. So $g(f(2)) = 22$.",
         r"The other order gives a completely different value - composition is not commutative."),
        (r"Subtract in the order asked: $3 - 22 = -19$.",
         r"The question is $f(g(2)) - g(f(2))$, so the small one comes first."),
    ],
    pitfalls=[r"Computing $g(f(2)) - f(g(2))$ and answering $19$.",
              r"Applying the functions in the wrong order inside one composition."],
    takeaway=r"$f(g(x))$ means $g$ first; check the order twice, because the wrong order is always an offered option."),

"FUN-04": Sol(
    idea=r"'One-to-one' means no horizontal line meets the graph twice. The quickest test is whether the function is always increasing (or always decreasing).",
    steps=[
        (r"Rule out the even and periodic functions: $|x|$ and $x^2 + 2x$ are symmetric (e.g. $|1| = |-1|$), and $\cos x$ repeats every $2\pi$.",
         r"Any symmetry or repetition immediately produces two inputs with the same output."),
        (r"Test $x^3 - x$: it equals $0$ at $x = -1, 0, 1$ - three inputs with the same output.",
         r"A cubic with three distinct roots is certainly not one-to-one."),
        (r"Test $x^3 + x$: its derivative $3x^2 + 1$ is always positive, so the function is strictly increasing.",
         r"A strictly increasing function can never take the same value twice, which is exactly one-to-one."),
        (r"So $f(x) = x^3 + x$ is the one-to-one function.",
         r"Alternatively, $x^3$ and $x$ both increase, so their sum does."),
    ],
    pitfalls=[r"Assuming every cubic is one-to-one - $x^3 - x$ is a counterexample.",
              r"Thinking $|x|$ is one-to-one because it has a 'simple' formula."],
    takeaway=r"One-to-one $\Leftrightarrow$ strictly monotonic; check for symmetry or repeated values first, then look at the derivative's sign."),

"FUN-05": Sol(
    idea=r"Track a single known point through the transformations, remembering that inside changes act inversely on $x$.",
    steps=[
        (r"Start with the known point $(4, 6)$ on $y = f(x)$.",
         r"One point is all you are given, so the answer must be its image."),
        (r"$f(2x)$ squashes horizontally by factor $\frac12$: the point with $x$-coordinate $4$ moves to $x = 2$, since $f(2 \times 2) = f(4) = 6$.",
         r"To get the same output from $f(2x)$ you need half the input - this is the inverse action of an inside change."),
        (r"Multiply by $3$: $y = 3 \times 6 = 18$. Then subtract $1$: $y = 17$.",
         r"Outside changes act directly on the output, in the order written."),
        (r"The point is $(2, 17)$.",
         r"Check: $3f(2 \times 2) - 1 = 3(6) - 1 = 17$ ✓."),
    ],
    pitfalls=[r"Doubling the $x$-coordinate to $8$ instead of halving it.",
              r"Forgetting the $-1$ and answering $(2, 18)$."],
    takeaway=r"Substitute the point back into the new equation to check: $f(2x)$ at $x = 2$ really is $f(4)$."),

"FUN-06": Sol(
    idea=r"Reflection in the $y$-axis replaces $x$ by $-x$. Only the odd powers change sign.",
    steps=[
        (r"Replace $x$ with $-x$: $y = (-x)^2 - 6(-x) + 5$.",
         r"Reflecting in the $y$-axis maps the point $(x, y)$ to $(-x, y)$, which is achieved by substituting $-x$."),
        (r"Simplify: $(-x)^2 = x^2$ and $-6(-x) = +6x$, so $y = x^2 + 6x + 5$.",
         r"Even powers are unaffected; odd powers flip sign. The constant is also unchanged."),
    ],
    pitfalls=[r"Changing the sign of the constant too, giving $x^2 + 6x - 5$.",
              r"Confusing it with reflection in the $x$-axis, which would negate the whole right-hand side."],
    takeaway=r"$y$-axis reflection: $x \to -x$, so only odd-degree terms change sign. $x$-axis reflection: $y \to -y$, so everything does."),

"FUN-07": Sol(
    idea=r"Work backwards: put the target into a form that shows the transformations. Completing the square reveals them.",
    steps=[
        (r"Factorise the target: $4x^2 - 8x + 4 = 4(x^2 - 2x + 1) = 4(x-1)^2$.",
         r"Taking out the $4$ exposes a perfect square - the shape of $f$ with a translation."),
        (r"Read it as $y = 4f(x - 1)$ where $f(x) = x^2$.",
         r"The inside $(x-1)$ is a translation, the outside $4$ is a vertical stretch."),
        (r"Translate $1$ unit in the positive $x$-direction, then stretch parallel to the $y$-axis by factor $4$.",
         r"With one inside and one outside change, the order between them does not matter - but the direction of each does."),
        (r"Confirm with a point: the vertex $(0,0)$ maps to $(1, 0)$, and the target $4(x-1)^2$ does have its vertex at $(1, 0)$ ✓.",
         r"A point check catches direction errors instantly."),
    ],
    pitfalls=[r"Translating left ($x + 1$), giving $4(x+1)^2 = 4x^2 + 8x + 4$ - the wrong sign on the middle term.",
              r"Reading the $4$ as a horizontal stretch; $y = f(2x) = 4x^2$ has no translation at all."],
    takeaway=r"Factor the target into $af(x - h) + k$ form; the numbers then name the transformations directly."),

"FUN-08": Sol(
    idea=r"The key fact is $\sqrt{x^2} = |x|$, not $x$. The question is then about when $|x| = -x$.",
    steps=[
        (r"Rewrite the left-hand side: $\sqrt{x^2} = |x|$.",
         r"The square-root symbol always means the **non-negative** root, so the output cannot be negative even when $x$ is."),
        (r"The equation becomes $|x| = -x$.",
         r"Both sides must therefore be $\geq 0$, which already forces $-x \geq 0$."),
        (r"$|x| = -x$ exactly when $x \leq 0$ (for $x < 0$, $|x| = -x$; at $x = 0$ both sides are $0$).",
         r"Split into cases $x \geq 0$ and $x < 0$, or recall the definition of $|x|$ directly."),
    ],
    pitfalls=[r"Answering 'no real $x$' on the grounds that a square root cannot equal a negative - but $-x$ is positive when $x$ is negative.",
              r"Excluding $x = 0$ and answering $x < 0$ only."],
    takeaway=r"$\sqrt{x^2} = |x|$; and $-x$ is positive when $x$ is negative, so expressions with a minus sign can still be non-negative."),

"FUN-09": Sol(
    idea=r"For $y = a\sin(bx) + c$, the amplitude, period and shift can be read straight off - as long as you know which letter does what.",
    steps=[
        (r"The $3$ inside compresses horizontally: period $= \dfrac{360^\circ}{3} = 120^\circ$.",
         r"$\sin(bx)$ completes a cycle when $bx$ increases by $360^\circ$, i.e. when $x$ increases by $360^\circ/b$."),
        (r"The $2$ outside is the amplitude: $2\sin(3x)$ ranges from $-2$ to $2$.",
         r"Multiplying the function stretches the range by that factor, symmetrically about zero."),
        (r"The $+1$ raises everything: the range becomes $-1$ to $3$, so the maximum is $3$.",
         r"A vertical translation moves the whole wave, including its maximum."),
    ],
    pitfalls=[r"Multiplying the period by $3$ to get $1080^\circ$ instead of dividing.",
              r"Giving the amplitude $2$ as the maximum and ignoring the $+1$."],
    takeaway=r"In $a\sin(bx) + c$: amplitude $|a|$, period $360^\circ/b$, midline $y = c$, maximum $c + |a|$."),

"FUN-10": Sol(
    idea=r"Three algebraic claims about one function. Each is settled by direct substitution - and the false one needs only a single value of $x$.",
    steps=[
        (r"I: $f(f(x)) = (x^2+1)^2 + 1 = x^4 + 2x^2 + 1 + 1 = x^4 + 2x^2 + 2$. **True.**",
         r"Substitute the whole of $f(x)$ into $f$; expand $(x^2+1)^2$ carefully - the cross term $2x^2$ is essential."),
        (r"II: $f(x+1) = (x+1)^2 + 1 = x^2 + 2x + 2$, whereas $f(x) + 1 = x^2 + 2$. These differ by $2x$. **False.**",
         r"A single value settles it: $x = 1$ gives $f(2) = 5$ but $f(1) + 1 = 3$."),
        (r"III: $f(2x) = 4x^2 + 1$ and $4f(x) - 3 = 4x^2 + 4 - 3 = 4x^2 + 1$. Equal for all $x$. **True.**",
         r"Compute both sides independently and compare - do not try to 'see' it."),
        (r"I and III only.",
         r"Map the verdicts onto the option list."),
    ],
    pitfalls=[r"Assuming II is true because functions 'usually' behave additively - almost none do.",
              r"Expanding $(x^2+1)^2$ as $x^4 + 1$."],
    takeaway=r"Test each claim by substitution; one numerical counterexample is enough to destroy a 'for all $x$' statement."),

"FUN-11": Sol(
    idea=r"Three transformations in a stated order. Apply them to the equation one at a time, and be careful that the last one acts on everything built so far.",
    steps=[
        (r"Reflect in the $x$-axis: $y = -f(x)$.",
         r"Negating the output flips the graph vertically."),
        (r"Translate $2$ up: $y = -f(x) + 2$.",
         r"Add to the whole expression, not just to $f$."),
        (r"Reflect in the $y$-axis: replace **every** $x$ by $-x$, giving $y = -f(-x) + 2 = 2 - f(-x)$.",
         r"Only $x$ is replaced; the constant $2$ is unaffected because it does not involve $x$."),
    ],
    pitfalls=[r"Writing $-f(-x) - 2$ by also negating the constant.",
              r"Applying the transformations in the wrong order - with mixed inside/outside operations, order matters."],
    takeaway=r"Rewrite the equation after each step; a $y$-axis reflection substitutes $-x$ for $x$ everywhere it appears."),

"FUN-12": Sol(
    idea=r"Two functions that almost invert each other. The asymmetry comes from $\sqrt{x^2} = |x|$ and from the restricted domain.",
    steps=[
        (r"I: $g(f(x)) = \left(\sqrt{x-3}\right)^2 + 3 = (x - 3) + 3 = x$ for $x \geq 3$. **True.**",
         r"Squaring a square root recovers the inside, provided the inside is non-negative - guaranteed by the stated domain $x \geq 3$."),
        (r"Compute the other order: $f(g(x)) = \sqrt{(x^2 + 3) - 3} = \sqrt{x^2} = |x|$.",
         r"Do the algebra once and read both remaining statements off it."),
        (r"II claims this equals $x$ for all real $x$: false at $x = -1$, where $|x| = 1 \neq -1$. **False.**",
         r"The square root returns the non-negative value, so it cannot reproduce a negative input."),
        (r"III says it equals $|x|$, which is exactly what we found. **True.**",
         r"Same computation, correct conclusion."),
        (r"I and III only.",
         r"Match to the options."),
    ],
    pitfalls=[r"Assuming $f(g(x)) = x$ because $f$ and $g$ 'look like' inverses - inverses require matching domains and ranges.",
              r"Writing $\sqrt{x^2} = x$."],
    takeaway=r"$f(g(x)) = x$ and $g(f(x)) = x$ are different statements; $\sqrt{x^2} = |x|$ is what breaks the symmetry here."),

"FUN-13": Sol(
    idea=r"The completed-square form is handed to you, so the vertex gives two constants and the extra point gives the third.",
    steps=[
        (r"Match the vertex: $y = a(x + b)^2 + c$ has vertex $(-b, c)$, and we are told it is $(-2, 5)$, so $b = 2$ and $c = 5$.",
         r"Note the sign: the form uses $x + b$, so the vertex $x$-coordinate is $-b$, not $b$."),
        (r"Substitute the point $(0, -3)$: $a(0 + 2)^2 + 5 = -3$.",
         r"One point is enough to find the remaining unknown."),
        (r"Solve: $4a = -8$, so $a = -2$.",
         r"Negative, which makes sense: the curve passes below its vertex, so it opens downwards."),
    ],
    pitfalls=[r"Taking $b = -2$ and getting $a = -\frac12$ from $a(0-2)^2$... (the same here, but the sign confusion bites when the point is not symmetric).",
              r"Answering $+2$ and ignoring that the parabola must open downwards to reach $y = -3$."],
    takeaway=r"Sanity-check the sign of $a$ against the picture: if the curve drops below the vertex, $a < 0$."),

"FUN-14": Sol(
    idea=r"Follow the turning point through the transformation and match coordinates - each coordinate gives one equation.",
    steps=[
        (r"$y = f(x - a) + b$ translates the graph $a$ right and $b$ up, so the maximum moves from $(3, 8)$ to $(3 + a,\; 8 + b)$.",
         r"A translation moves every point, including the turning point, by the same vector."),
        (r"Match the $x$-coordinates: $3 + a = 1$, so $a = -2$.",
         r"A negative $a$ simply means the shift is to the left."),
        (r"Match the $y$-coordinates: $8 + b = 2$, so $b = -6$.",
         r"Same for the vertical shift."),
        (r"Add: $a + b = -8$.",
         r"The question asks for the sum, not for either value alone."),
    ],
    pitfalls=[r"Using $3 - a = 1$ and getting $a = 2$, which flips the sign of the answer.",
              r"Answering $-2$ or $-6$ (one of the two constants) instead of their sum."],
    takeaway=r"$f(x - a) + b$ shifts by $(+a, +b)$; set up one equation per coordinate."),

"FUN-15": Sol(
    idea=r"A horizontal stretch of factor $\frac12$ replaces $x$ by $2x$ - the reciprocal of the factor.",
    steps=[
        (r"A stretch parallel to the $x$-axis with scale factor $k$ gives $y = f\!\left(\frac{x}{k}\right)$; with $k = \frac12$ that is $y = f(2x)$.",
         r"Inside changes act inversely: to squash the graph to half its width you must double the input."),
        (r"Substitute: $y = (2x)^3 - 3(2x)$.",
         r"Replace every $x$ in the formula, including the one in the linear term."),
        (r"Simplify: $8x^3 - 6x$.",
         r"$(2x)^3 = 8x^3$ - the coefficient is cubed too."),
    ],
    pitfalls=[r"Replacing only the first $x$, giving $8x^3 - 3x$ - an offered option.",
              r"Using $y = f(x/2)$ and getting $\frac{x^3}{8} - \frac{3x}{2}$, which is a stretch of factor $2$."],
    takeaway=r"Stretch factor $k$ parallel to the $x$-axis $\Rightarrow$ replace $x$ by $x/k$; substitute into **every** occurrence."),

"FUN-16": Sol(
    idea=r"A sum of two moduli. Splitting the line at the two 'corner' points shows the function is constant in the middle.",
    steps=[
        (r"The moduli change behaviour at $x = 2$ and $x = -2$; consider the three regions separately.",
         r"$|x - a|$ changes formula at $x = a$; the critical points split the line into pieces where the function is linear."),
        (r"For $-2 \leq x \leq 2$: $|x-2| = 2 - x$ and $|x+2| = x + 2$, so $f(x) = (2 - x) + (x + 2) = 4$.",
         r"The $x$ terms cancel exactly - the function is **constant** on this whole interval."),
        (r"For $x > 2$: $f(x) = (x - 2) + (x + 2) = 2x > 4$. For $x < -2$: $f(x) = (2 - x) + (-x - 2) = -2x > 4$.",
         r"Outside the middle the function grows, so nothing beats $4$."),
        (r"Minimum $4$, attained for every $x$ in $[-2, 2]$: infinitely many values.",
         r"The second half of the question is the real test - most students find the $4$ and then guess."),
    ],
    pitfalls=[r"Answering 'attained for exactly one $x$' by assuming a minimum must occur at a single point.",
              r"Testing only $x = 0$ and concluding the minimum is $4$ without checking whether it is attained elsewhere."],
    takeaway=r"$|x - a| + |x - b|$ is constant (and minimal) between $a$ and $b$ - it measures total distance to two fixed points."),

"FUN-17": Sol(
    idea=r"The two changes are designed to cancel at $x = 2$. Substitute and watch the terms collapse.",
    steps=[
        (r"From the original line: $2m + c = 7$.",
         r"The line passes through $(2, 7)$, so substituting gives one equation in $m$ and $c$."),
        (r"The new line is $y = (m + 1)x + (c - 2)$; evaluate it at $x = 2$: $2(m+1) + (c - 2) = 2m + 2 + c - 2$.",
         r"Substitute $x = 2$ and expand - do not try to find $m$ and $c$, which are not determined."),
        (r"Simplify: $2m + c = 7$, so $k = 7$.",
         r"The $+2$ from the gradient change and the $-2$ from the intercept change cancel exactly."),
    ],
    pitfalls=[r"Trying to solve for $m$ and $c$ individually - there is not enough information, and none is needed.",
              r"Forgetting that the gradient change is multiplied by $x = 2$, and answering $5$ or $9$."],
    takeaway=r"When a question gives only one equation for two unknowns, look for a combination that is determined - here $2m + c$."),

}
