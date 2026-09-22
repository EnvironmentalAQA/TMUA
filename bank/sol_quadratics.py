"""Full teaching solutions: quadratic functions (QUA-xx)."""
from gen.model import Sol

SOLUTIONS = {

"QUA-01": Sol(
    idea=r"'Two distinct real roots' is always a discriminant condition. The unknown is in the coefficients, so the discriminant becomes a quadratic **in $k$** and you finish with an inequality.",
    steps=[
        (r"Identify $a = 1$, $b = k - 2$, $c = k + 1$ and write the discriminant: $(k-2)^2 - 4(k+1)$.",
         r"'Two distinct real roots' $\Leftrightarrow$ $b^2 - 4ac > 0$. Everything else in the question is decoration."),
        (r"Expand and simplify: $k^2 - 4k + 4 - 4k - 4 = k^2 - 8k$.",
         r"The constants cancel, which is the sign you have expanded correctly."),
        (r"Factorise and solve $k(k - 8) > 0$.",
         r"A quadratic inequality needs its roots and its shape: roots $0$ and $8$, opening upwards."),
        (r"The upward parabola is positive outside its roots: $k < 0$ or $k > 8$.",
         r"Sketch it if in doubt - 'outside the roots' for $> 0$, 'between the roots' for $< 0$."),
    ],
    pitfalls=[r"Expanding $(k-2)^2$ as $k^2 - 4$, which gives $k^2 - 4k - 8$ and a different answer set.",
              r"Reading the sign chart backwards and choosing $0 < k < 8$ - that is where the discriminant is **negative** and there are no real roots."],
    takeaway=r"Conditions on the number of roots are conditions on $b^2 - 4ac$; if the coefficients contain a parameter, you end up solving a quadratic inequality in that parameter."),

"QUA-02": Sol(
    idea=r"Minimum value of a quadratic: complete the square. The leading coefficient $2$ must be factored out **before** completing the square.",
    steps=[
        (r"Factor the $2$ out of the $x$ terms: $2(x^2 - 6x) + 23$.",
         r"Completing the square only works on $x^2 + (\text{something})x$; the coefficient of $x^2$ must be $1$ inside the bracket."),
        (r"Complete the square inside: $x^2 - 6x = (x-3)^2 - 9$, so the expression is $2\left[(x-3)^2 - 9\right] + 23$.",
         r"Halve the coefficient of $x$ ($-6 \to -3$) and subtract the square of that half."),
        (r"Multiply out the $2$: $2(x-3)^2 - 18 + 23 = 2(x-3)^2 + 5$.",
         r"The $-9$ is inside the bracket, so it is multiplied by $2$ as well - this is where marks are lost."),
        (r"$2(x-3)^2 \geq 0$, so the least value is $5$, at $x = 3$.",
         r"A square is never negative, and it is zero exactly at the vertex."),
    ],
    pitfalls=[r"Forgetting to multiply the $-9$ by $2$, giving $2(x-3)^2 + 14$ and the answer $14$.",
              r"Quoting the $x$-coordinate $3$ instead of the minimum value $5$ - both are offered."],
    takeaway=r"Take the leading coefficient outside first, complete the square, then multiply back in; the constant left outside is the minimum."),

"QUA-03": Sol(
    idea=r"Given a vertex, the completed-square form is the natural one. The clever final step is noticing that $a + b + c$ is just $y(1)$.",
    steps=[
        (r"Write the completed-square form using the vertex: $y = a(x - 2)^2 - 3$.",
         r"The vertex $(h, k)$ appears directly in $y = a(x-h)^2 + k$, so two of the three unknowns are already known."),
        (r"Use the point $(0, 5)$: $a(0-2)^2 - 3 = 5 \Rightarrow 4a = 8 \Rightarrow a = 2$.",
         r"One extra point is exactly what is needed to pin down the remaining constant."),
        (r"Note that $a + b + c$ is the value of $ax^2 + bx + c$ at $x = 1$.",
         r"Substituting $x = 1$ makes every power of $x$ equal to $1$ - a standard shortcut worth remembering."),
        (r"Evaluate: $y(1) = 2(1-2)^2 - 3 = 2 - 3 = -1$.",
         r"No need to expand into $2x^2 - 8x + 5$ at all."),
    ],
    pitfalls=[r"Expanding and then mis-collecting: $2(x-2)^2 - 3 = 2x^2 - 8x + 5$, and slips in the $-8$ give $3$ or $7$.",
              r"Using the vertex as $(-2, -3)$ - in $a(x - h)^2 + k$ the sign of $h$ is already flipped."],
    takeaway=r"$f(1)$ is the sum of the coefficients; and a given vertex means you should start from $a(x-h)^2 + k$."),

"QUA-04": Sol(
    idea=r"A symmetric function of the roots. The roots themselves are irrational, so use the sum and product rather than the quadratic formula.",
    steps=[
        (r"Read off $\alpha + \beta = -\frac{b}{a} = 5$ and $\alpha\beta = \frac{c}{a} = 2$.",
         r"These come straight from the coefficients; you never need the actual roots."),
        (r"Use the identity $\alpha^2 + \beta^2 = (\alpha + \beta)^2 - 2\alpha\beta$.",
         r"Expanding $(\alpha+\beta)^2$ gives $\alpha^2 + 2\alpha\beta + \beta^2$, so subtracting $2\alpha\beta$ leaves the sum of squares."),
        (r"Substitute: $25 - 2(2) = 21$.",
         r"Arithmetic only."),
    ],
    pitfalls=[r"Using $(\alpha+\beta)^2 = \alpha^2 + \beta^2$ and answering $25$.",
              r"Subtracting $\alpha\beta$ once instead of twice, giving $23$ - both wrong values are offered."],
    takeaway=r"Any symmetric expression in the roots can be built from $\alpha + \beta = -b/a$ and $\alpha\beta = c/a$; the quadratic formula is rarely needed."),

"QUA-05": Sol(
    idea=r"'Touches' means exactly one intersection, which after substitution means a repeated root: discriminant zero.",
    steps=[
        (r"Set the two expressions equal: $2x + c = x^2 - 4x + 7$.",
         r"Intersections of $y = f(x)$ and $y = g(x)$ are the solutions of $f(x) = g(x)$."),
        (r"Collect into a standard quadratic: $x^2 - 6x + (7 - c) = 0$.",
         r"Everything to one side, so the discriminant test can be applied."),
        (r"Set the discriminant to zero: $(-6)^2 - 4(1)(7 - c) = 0$.",
         r"Touching means a repeated root, i.e. the line meets the curve once - exactly the $b^2 = 4ac$ case."),
        (r"Solve: $36 - 28 + 4c = 0 \Rightarrow 4c = -8 \Rightarrow c = -2$.",
         r"Watch the double negative: $-4(7 - c) = -28 + 4c$."),
    ],
    pitfalls=[r"Sign slip in $-4(7-c)$ giving $c = 2$, which is offered.",
              r"Using $b^2 - 4ac > 0$ (crossing) rather than $= 0$ (touching)."],
    takeaway=r"Tangency between a line and a curve: substitute, then set the discriminant of the resulting quadratic to zero."),

"QUA-06": Sol(
    idea=r"Three statements about one quadratic. Completing the square once answers all three at a stroke.",
    steps=[
        (r"Complete the square: $x^2 - 6x + 13 = (x - 3)^2 + 4$.",
         r"This single form contains the range, the line of symmetry and the vertex - so do it first, before looking at the statements."),
        (r"I: $(x-3)^2 \geq 0$ so $f(x) \geq 4 > 0$ for every $x$. **True.**",
         r"The minimum value is $4$, comfortably positive; equivalently the discriminant $36 - 52 < 0$, so the curve never reaches the axis."),
        (r"II: the vertex is at $x = 3$, and a parabola is symmetric about the vertical line through its vertex. **True.**",
         r"Symmetry about $x = h$ is immediate from the $(x - h)^2$ form."),
        (r"III: $f(x) = 4$ means $(x-3)^2 = 0$, so $x = 3$ only - exactly one solution. **True.**",
         r"A horizontal line through the vertex meets the parabola once; any higher line meets it twice."),
        (r"All three hold, so the answer is 'I, II and III'.",
         r"Decide each statement independently, then match to the option list."),
    ],
    pitfalls=[r"Assuming $f(x) = 4$ has two solutions because quadratics 'usually' do - $y = 4$ is the tangent line at the vertex.",
              r"Reading the symmetry line off as $x = -3$."],
    takeaway=r"Completing the square answers questions about sign, range, symmetry and repeated roots all at once."),

"QUA-07": Sol(
    idea=r"A quartic that is quadratic in $x^2$. The trap is counting the solutions of the substituted equation rather than of the original.",
    steps=[
        (r"Substitute $u = x^2$: $u^2 - 5u + 4 = 0$.",
         r"Only even powers of $x$ appear, which is what makes the substitution work."),
        (r"Factorise: $(u - 1)(u - 4) = 0$, so $u = 1$ or $u = 4$.",
         r"Two values of $u$ - but $u$ is not the answer."),
        (r"Undo the substitution: $x^2 = 1$ gives $x = \pm1$; $x^2 = 4$ gives $x = \pm2$.",
         r"Each **positive** value of $u$ produces **two** values of $x$; a negative value would produce none."),
        (r"Count: four real solutions.",
         r"The question asks how many, not what they are."),
    ],
    pitfalls=[r"Answering $2$ because the quadratic in $u$ has two roots.",
              r"Forgetting the negative square roots and answering $2$ again."],
    takeaway=r"After a substitution, always translate back: each positive value of $x^2$ gives two values of $x$, zero gives one, negative gives none."),

"QUA-08": Sol(
    idea=r"'No real roots' is the discriminant $< 0$. The extra subtlety is the coefficient $k$ appearing in the $x^2$ term, so $k = 0$ needs a thought.",
    steps=[
        (r"Write the discriminant: $4^2 - 4(k)(k) = 16 - 4k^2$.",
         r"Here $a = k$ and $c = k$ - both the first and last coefficients are the parameter."),
        (r"Set it negative: $16 - 4k^2 < 0 \Rightarrow k^2 > 4$.",
         r"No real roots $\Leftrightarrow b^2 - 4ac < 0$."),
        (r"Solve $k^2 > 4$: $k < -2$ or $k > 2$.",
         r"$k^2 > 4$ means $|k| > 2$, which is two separate intervals, not $-2 < k < 2$."),
        (r"Check $k = 0$ separately: the equation becomes $4x = 0$, which has the root $x = 0$.",
         r"If $k = 0$ it is not a quadratic at all, so the discriminant test does not apply - but $k = 0$ is excluded by the answer anyway."),
    ],
    pitfalls=[r"Solving $k^2 > 4$ as $-2 < k < 2$ - that is the solution of $k^2 < 4$.",
              r"Ignoring the possibility $k = 0$ entirely (harmless here, fatal in questions where $0$ lies inside the answer set)."],
    takeaway=r"$k^2 > c$ gives two outer intervals; and whenever the leading coefficient contains the parameter, check the value that makes it zero."),

"QUA-09": Sol(
    idea=r"A quadratic in the expression $x^2 - 3x$. After substituting back you get two quadratics, and the question only wants the total of all four roots.",
    steps=[
        (r"Let $u = x^2 - 3x$: the equation becomes $u^2 - 2u - 8 = 0$.",
         r"The same expression appears squared and linearly, which is the signal for a substitution."),
        (r"Factorise: $(u - 4)(u + 2) = 0$, so $u = 4$ or $u = -2$.",
         r"Both values are usable - neither is ruled out, because $x^2 - 3x$ can take any value $\geq -\frac94$."),
        (r"Case $u = 4$: $x^2 - 3x - 4 = 0$. Its roots sum to $3$ (sum $= -b/a$). Discriminant $9 + 16 > 0$, so both are real.",
         r"You never need the roots themselves - the sum of roots comes straight from the coefficients."),
        (r"Case $u = -2$: $x^2 - 3x + 2 = 0$. Roots sum to $3$; discriminant $9 - 8 > 0$, so both are real.",
         r"Check the discriminant in each case: a case with no real roots would contribute nothing to the total."),
        (r"Total: $3 + 3 = 6$.",
         r"Four real values of $x$, summing to $6$."),
    ],
    pitfalls=[r"Answering $3$ by solving only one of the two cases.",
              r"Adding the $u$ values ($4 + (-2) = 2$) instead of the $x$ values."],
    takeaway=r"With a substitution, each value of $u$ gives its own equation in $x$; check each for real roots and use 'sum of roots $= -b/a$' to avoid solving."),

"QUA-10": Sol(
    idea=r"Two pieces of information about a quadratic - its minimum and one root - pin the whole thing down. Working in completed-square form makes the roots visible.",
    steps=[
        (r"Minimum $-4$ and leading coefficient $1$ means $x^2 + px + q = (x - h)^2 - 4$ for some $h$.",
         r"A monic quadratic with minimum $m$ must be $(x - h)^2 + m$; only the position $h$ is unknown."),
        (r"Its roots satisfy $(x - h)^2 = 4$, i.e. $x = h \pm 2$.",
         r"Solve the completed-square form directly rather than expanding."),
        (r"One root is $0$, so $h + 2 = 0$ or $h - 2 = 0$: $h = -2$ or $h = 2$.",
         r"Both cases are legitimate; the options decide which one is wanted."),
        (r"That gives $x^2 + 4x$ or $x^2 - 4x$; the list offers $x^2 - 4x$.",
         r"Check it: $x^2 - 4x = (x-2)^2 - 4$, minimum $-4$, roots $0$ and $4$."),
    ],
    pitfalls=[r"Picking $x^2 - 2x - 3$: its minimum is $-4$ but its roots are $-1$ and $3$, so $0$ is not a root.",
              r"Checking only the minimum (several options have minimum $-4$) or only the roots."],
    takeaway=r"Test every stated condition - an option that satisfies one of them is designed to catch you."),

"QUA-11": Sol(
    idea=r"'Vertex on the $x$-axis' means the minimum value is zero, i.e. the quadratic has a repeated root. Completing the square is quicker than the discriminant here.",
    steps=[
        (r"Complete the square in $x$, treating $a$ as a constant: $x^2 - 2ax + a^2 = (x - a)^2$, so $y = (x-a)^2 + (a - 6)$.",
         r"The first three terms are already a perfect square - that is why the question is built with $a^2$ in it."),
        (r"Read off the vertex: $(a,\; a - 6)$.",
         r"In $(x - h)^2 + k$ the vertex is $(h, k)$."),
        (r"On the $x$-axis means the $y$-coordinate is zero: $a - 6 = 0$, so $a = 6$.",
         r"'On the $x$-axis' is a statement about $y$, not $x$ - the commonest misread in this question."),
    ],
    pitfalls=[r"Setting the $x$-coordinate to zero and answering $a = 0$.",
              r"Using the discriminant but mis-expanding $4a^2 - 4(a^2 + a - 6)$, which should collapse to $-4(a - 6)$."],
    takeaway=r"Vertex on the $x$-axis $\Leftrightarrow$ repeated root $\Leftrightarrow$ discriminant zero - three descriptions of the same situation."),

"QUA-12": Sol(
    idea=r"'Equal roots' is the discriminant-zero condition; the twist is that it gives two values of $b$ and the question wants their sum.",
    steps=[
        (r"Write the discriminant with $a = 2$, $c = 18$: $b^2 - 4(2)(18) = b^2 - 144$.",
         r"Substitute carefully - $4ac$ is $144$, not $36$."),
        (r"Set it to zero: $b^2 = 144$, so $b = 12$ or $b = -12$.",
         r"Equal (repeated) roots means the discriminant vanishes; a square equal to a positive number always has two solutions."),
        (r"Add them: $12 + (-12) = 0$.",
         r"The two values are symmetric about zero, so the sum is $0$ without any further work."),
    ],
    pitfalls=[r"Giving only the positive root and answering $12$.",
              r"Reading 'sum of the possible values of $b$' as 'the value of $b$'."],
    takeaway=r"$b^2 = k$ always has two solutions $\pm\sqrt k$; read whether the question wants one of them, both, or a combination."),

"QUA-13": Sol(
    idea=r"A 'which one' question about vertices. Complete the square on each option - but use the sign of the $x$-coordinate to eliminate most of them first.",
    steps=[
        (r"Recall that for $y = x^2 + bx + c$ the vertex is at $x = -\frac{b}{2}$.",
         r"You only need the vertex position, not the whole completed square, to test the first condition $x < 0$."),
        (r"Second quadrant needs $x < 0$, so $-\frac b2 < 0$, i.e. $b > 0$: only $y = x^2 + 4x + 1$ and $y = x^2 + 6x + 10$ survive among the upward parabolas.",
         r"Eliminating on one condition first halves the work."),
        (r"Compute the $y$-coordinates: $x^2 + 4x + 1 = (x+2)^2 - 3$, vertex $(-2, -3)$: fails $y > 0$. $x^2 + 6x + 10 = (x+3)^2 + 1$, vertex $(-3, 1)$: passes.",
         r"Now apply the second condition to the short list."),
        (r"Check the downward ones quickly: $-x^2 - 2x - 3$ has vertex $(-1, -2)$ and $-x^2 + 2x + 1$ has vertex $(1, 2)$ - neither is in the second quadrant.",
         r"Worth 10 seconds of confirmation on a 'which one' question."),
    ],
    pitfalls=[r"Reading the vertex of $(x+3)^2 + 1$ as $(3, 1)$ - the sign flips.",
              r"Mixing up the quadrants: the second quadrant is up and to the left."],
    takeaway=r"On 'which of these' questions, test the cheapest condition first and eliminate before doing any heavy algebra."),

"QUA-14": Sol(
    idea=r"'Two distinct **positive** roots' is three conditions at once: discriminant positive, sum of roots positive, product of roots positive. All three must hold.",
    steps=[
        (r"Discriminant: $4m^2 - 4(m + 6) > 0 \Rightarrow m^2 - m - 6 > 0 \Rightarrow (m-3)(m+2) > 0$, so $m < -2$ or $m > 3$.",
         r"Distinctness and reality come from $b^2 - 4ac > 0$; this alone allows negative $m$."),
        (r"Sum of roots $= 2m > 0$, so $m > 0$.",
         r"If both roots are positive their sum is positive. This is the condition that kills the $m < -2$ branch."),
        (r"Product of roots $= m + 6 > 0$, so $m > -6$.",
         r"If both roots are positive their product is positive; this also rules out one positive and one negative root."),
        (r"Intersect all three: $(m < -2 \text{ or } m > 3)$ and $m > 0$ and $m > -6$ gives $m > 3$.",
         r"Take the overlap on a number line - the answer must satisfy every condition simultaneously."),
    ],
    pitfalls=[r"Stopping after the discriminant and choosing $m < -2$ or $m > 3$ - which is offered.",
              r"Forgetting that sum **and** product must both be positive: either one alone is not enough."],
    takeaway=r"Both roots positive $\Leftrightarrow$ discriminant $\geq 0$, sum $> 0$ and product $> 0$; sign conditions on roots always come in this package."),

"QUA-15": Sol(
    idea=r"Given the two roots, use the factorised form and the symmetry of the parabola - no expansion needed.",
    steps=[
        (r"Write the factorised form: $y = (x - 1)(x - 5)$.",
         r"Roots at $1$ and $5$ with leading coefficient $1$ (given, since the equation is $x^2 + bx + c$)."),
        (r"The vertex lies midway between the roots: $x = \frac{1 + 5}{2} = 3$.",
         r"A parabola is symmetric, so its turning point sits on the axis of symmetry, exactly halfway between the roots."),
        (r"Evaluate there: $y = (3-1)(3-5) = 2 \times (-2) = -4$.",
         r"Substituting into the factorised form is far quicker than expanding to $x^2 - 6x + 5$."),
    ],
    pitfalls=[r"Averaging the roots but then substituting into the wrong expression, e.g. getting $-9$ from $(3)^2 - 6(3) + 5$ miscomputed.",
              r"Giving the $x$-coordinate $3$ instead of the $y$-coordinate."],
    takeaway=r"Midpoint of the roots gives the axis of symmetry; substitute into the factorised form for the vertex height."),

"QUA-16": Sol(
    idea=r"A symmetric pair of equations. Expanding $(x+y)^2$ links the two given quantities to $xy$ directly.",
    steps=[
        (r"Write the identity $(x + y)^2 = x^2 + y^2 + 2xy$.",
         r"This is the only identity that connects a sum, a sum of squares and a product."),
        (r"Substitute the given values: $4^2 = 10 + 2xy$.",
         r"$x + y = 4$ and $x^2 + y^2 = 10$ are both given, so only $xy$ is unknown."),
        (r"Solve: $16 - 10 = 2xy \Rightarrow xy = 3$.",
         r"Halve at the end - forgetting to divide by $2$ gives $6$, which is offered."),
    ],
    pitfalls=[r"Answering $6$ by omitting the factor $2$ in $2xy$.",
              r"Trying to solve for $x$ and $y$ individually (they are $1$ and $3$) - slower and unnecessary."],
    takeaway=r"$(x+y)^2 = x^2 + y^2 + 2xy$ converts between the three symmetric quantities; recognise which two you are given."),

"QUA-17": Sol(
    idea=r"Three general claims about $ax^2 + bx + c = 0$. Each is a discriminant statement in disguise; the false one needs a counterexample.",
    steps=[
        (r"I: if $ac < 0$ then $-4ac > 0$, so $b^2 - 4ac \geq -4ac > 0$: two distinct real roots. **True.**",
         r"$b^2 \geq 0$ always, so a positive $-4ac$ forces the whole discriminant positive. Geometrically, $a$ and $c$ of opposite signs means the curve crosses the axis."),
        (r"II: test $b = 0$ with $x^2 - 4 = 0$, which has roots $\pm 2$. **False.**",
         r"One counterexample settles a 'for all' claim. With $b = 0$ the discriminant is $-4ac$, whose sign depends on $a$ and $c$."),
        (r"III: a repeated root means the discriminant is zero, i.e. $b^2 - 4ac = 0$, i.e. $b^2 = 4ac$. **True.**",
         r"This is the definition of the repeated-root case, just rearranged."),
        (r"I and III only.",
         r"Match the verdicts to the options."),
    ],
    pitfalls=[r"Believing II because $b = 0$ 'removes' the linear term and the graph 'sits on the axis' - it does not; $x^2 - 4$ is a counterexample.",
              r"Mis-stating III as $b^2 = -4ac$."],
    takeaway=r"Statements about roots translate into statements about $b^2 - 4ac$; to refute one, look for the simplest numbers that fit the hypothesis."),

"QUA-18": Sol(
    idea=r"Two simultaneous quadratic inequalities. Solve each separately, then intersect on a number line.",
    steps=[
        (r"First: $x^2 - 7x + 10 < 0$ factorises as $(x-2)(x-5) < 0$, giving $2 < x < 5$.",
         r"An upward parabola is **below** the axis between its roots."),
        (r"Second: $x^2 - 4 > 0$ gives $x < -2$ or $x > 2$.",
         r"Above the axis means outside the roots - two intervals."),
        (r"Intersect: $(2, 5)$ overlaps $(2, \infty)$ entirely and misses $(-\infty, -2)$ completely, so the answer is $2 < x < 5$.",
         r"'And' means intersection: a value must satisfy both, so draw both solution sets on one line and take the common part."),
    ],
    pitfalls=[r"Taking the union and including $x < -2$ - the word is 'and', not 'or'.",
              r"Getting the first inequality backwards ($x < 2$ or $x > 5$) by forgetting that $< 0$ means between the roots."],
    takeaway=r"$<0$ between the roots, $>0$ outside them (for an upward parabola); then combine solution sets on a number line."),

"QUA-19": Sol(
    idea=r"Completing the square symbolically, then imposing a relationship between the two constants. It is an equation in $c$, not in $x$.",
    steps=[
        (r"Complete the square: $x^2 + 6x + c = (x + 3)^2 - 9 + c$.",
         r"Half of $6$ is $3$; subtracting $9$ compensates for the $+9$ the square introduces."),
        (r"Identify $p = 3$ and $q = c - 9$.",
         r"Compare with the required form $(x+p)^2 + q$ term by term."),
        (r"Impose $q = -c$: $c - 9 = -c$.",
         r"The condition given in the question is a link between $q$ and $c$, so substitute your expression for $q$."),
        (r"Solve: $2c = 9$, so $c = \frac92$.",
         r"A simple linear equation - just collect the $c$ terms."),
    ],
    pitfalls=[r"Writing $q = c + 9$ (sign error) and getting $c = -\frac92$.",
              r"Solving $c - 9 = c$ and concluding there is no solution."],
    takeaway=r"Complete the square with the constant left as a letter; the extra condition then becomes an ordinary equation in that letter."),

"QUA-20": Sol(
    idea=r"Integer roots means an integer factorisation of the constant term. Count systematically and do not forget negative pairs.",
    steps=[
        (r"If the roots are integers $r$ and $s$ then $rs = 12$ and $r + s = -k$.",
         r"For a monic quadratic, product of roots $= c$ and sum $= -b$."),
        (r"List the positive factor pairs of $12$: $(1, 12), (2, 6), (3, 4)$.",
         r"Work through divisors in order so none is missed."),
        (r"Each pair also has a negative version $(-1, -12)$, $(-2, -6)$, $(-3, -4)$, since two negatives also multiply to $+12$.",
         r"The product is positive, so the roots share a sign - both positive or both negative."),
        (r"Each of the six pairs gives a different $k = -(r+s)$: $-13, -8, -7, 13, 8, 7$. So six values.",
         r"Check they are distinct before counting."),
    ],
    pitfalls=[r"Listing only the positive pairs and answering $3$.",
              r"Counting $(1,12)$ and $(12,1)$ as different, which double-counts."],
    takeaway=r"Integer-root problems become divisor-counting problems; the sign of the product tells you whether the roots share a sign."),

"QUA-21": Sol(
    idea=r"Transformations applied to a quadratic. Track what happens to the **vertex** rather than to the whole equation.",
    steps=[
        (r"Complete the square: $x^2 - 4x + 3 = (x - 2)^2 - 1$, so the minimum is $-1$ at $x = 2$.",
         r"The turning point is the only feature the transformations act on in a way that matters."),
        (r"Reflect in the $x$-axis: $y \to -y$, so the minimum $-1$ becomes a **maximum** of $1$.",
         r"Reflection in the $x$-axis flips the sign of every $y$-value, turning a minimum into a maximum."),
        (r"Translate $2$ up: the maximum becomes $1 + 2 = 3$.",
         r"A vertical translation adds to every $y$-value, including the extreme one."),
    ],
    pitfalls=[r"Forgetting that the reflection converts the minimum into a maximum and reporting $-1 + 2 = 1$.",
              r"Reflecting the $x$-coordinate as well - the turning point stays at $x = 2$ throughout."],
    takeaway=r"For transformation questions, follow one key point (usually the vertex) through each step in order."),

"QUA-22": Sol(
    idea=r"Two linked quadratics: the roots of the first give the coefficients of the second. Sum-and-product relations do all the work.",
    steps=[
        (r"For $x^2 + ax + b = 0$ with roots $3$ and $-5$: sum $= 3 + (-5) = -2 = -a$, so $a = 2$.",
         r"Sum of roots $= -b/a$; with a monic quadratic that is just $-a$ - mind the double negative."),
        (r"Product $= 3 \times (-5) = -15 = b$.",
         r"Product of roots $= c/a = b$ here."),
        (r"The second equation is $x^2 - 15x + 2 = 0$, so $p + q = 15$ and $pq = 2$.",
         r"Substitute the values found, being careful that the roles of $a$ and $b$ swap between the two equations."),
        (r"Use $p^2 + q^2 = (p+q)^2 - 2pq = 225 - 4 = 221$.",
         r"The same identity as in QUA-04."),
    ],
    pitfalls=[r"Getting $a = -2$ by forgetting the minus in 'sum $= -a$', which turns the second equation into $x^2 - 15x - 2$ and gives $229$.",
              r"Computing $(p+q)^2$ and forgetting to subtract $2pq$, giving $225$."],
    takeaway=r"Read coefficients from roots with sum $= -b/a$ and product $= c/a$, and keep track of which equation you are in."),

"QUA-23": Sol(
    idea=r"A line meeting a curve twice: substitute and demand a positive discriminant.",
    steps=[
        (r"Substitute $y = mx$ into $y = x^2 + 9$: $mx = x^2 + 9$.",
         r"Intersections are the common solutions, found by equating the two expressions for $y$."),
        (r"Rearrange: $x^2 - mx + 9 = 0$.",
         r"Standard form is needed before the discriminant can be read off."),
        (r"Two distinct intersections $\Rightarrow$ discriminant $> 0$: $m^2 - 36 > 0$.",
         r"Here $b = -m$, and $b^2 = m^2$ regardless of sign."),
        (r"Solve $m^2 > 36$: $m < -6$ or $m > 6$.",
         r"Two intervals, since $m^2 > 36$ means $|m| > 6$; geometrically, steep lines in either direction cut the parabola twice."),
    ],
    pitfalls=[r"Answering $-6 < m < 6$ (the region where the line misses the parabola entirely).",
              r"Writing the discriminant as $-m^2 - 36$ by mishandling the sign of $b$."],
    takeaway=r"$b^2$ kills the sign of $b$: conditions like this are almost always symmetric in $\pm m$."),

"QUA-24": Sol(
    idea=r"Counting **integers** in the region where a quadratic is negative. Solve the inequality, then count carefully at the ends.",
    steps=[
        (r"Factorise: $n^2 - 2n - 8 = (n - 4)(n + 2)$.",
         r"Two numbers multiplying to $-8$ and adding to $-2$: $-4$ and $+2$."),
        (r"Negative between the roots: $-2 < n < 4$.",
         r"Upward parabola, so $f < 0$ strictly between the roots."),
        (r"List the integers strictly inside: $-1, 0, 1, 2, 3$ - five of them.",
         r"The endpoints $-2$ and $4$ give $f = 0$, which is **not** less than zero, so they are excluded; and $0$ is easy to forget."),
    ],
    pitfalls=[r"Including $-2$ and $4$ and answering $7$.",
              r"Forgetting $0$ is an integer and answering $4$."],
    takeaway=r"After solving an inequality, list the integers explicitly - endpoints and zero are the two things people drop."),

}
