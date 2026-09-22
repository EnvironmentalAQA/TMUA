"""Revision notes for the Section 1 Part 1 topics (MM1-MM8). Same markup as questions."""

NOTES = {
"indices-surds": {
    "summary": r"Everything here is mechanical once the laws are automatic. TMUA questions hide these skills inside bigger problems (solving $4^x = 8^{2x-3}$, simplifying an integrand before integrating, or checking whether a surd expression is rational), so aim for speed and accuracy rather than depth.",
    "sections": [
        {"h": "Laws of indices (MM1.1)", "body": r"""- $a^m \times a^n = a^{m+n}$, $\quad a^m \div a^n = a^{m-n}$, $\quad (a^m)^n = a^{mn}$, $\quad (ab)^n = a^n b^n$
- $a^0 = 1$, $\quad a^{-n} = \dfrac{1}{a^n}$, $\quad a^{1/n} = \sqrt[n]{a}$, $\quad a^{m/n} = \left(\sqrt[n]{a}\right)^m$
- For fractional powers of fractions, take the root first: $\left(\frac{27}{8}\right)^{-2/3} = \left(\frac{8}{27}\right)^{2/3} = \left(\frac{2}{3}\right)^2 = \frac{4}{9}$.
- Equations like $4^{x+1} = 8^{2x-3}$: write everything as a power of one base ($2^{2x+2} = 2^{6x-9}$) and equate indices.
- 'Hidden quadratics': $9^x - 4\cdot3^x + 3 = 0$ is $y^2 - 4y + 3 = 0$ with $y = 3^x$. Reject any root with $y \leq 0$."""},
        {"h": "Surds (MM1.2, M2.12)", "body": r"""- $\sqrt{ab} = \sqrt a\sqrt b$ and $\sqrt{\frac ab} = \frac{\sqrt a}{\sqrt b}$ for $a, b \geq 0$; but $\sqrt{a + b} \neq \sqrt a + \sqrt b$.
- Simplify by extracting square factors: $\sqrt{75} = \sqrt{25 \times 3} = 5\sqrt3$.
- Rationalise with the conjugate: $\dfrac{5}{3 + 2\sqrt5} = \dfrac{5(3 - 2\sqrt5)}{9 - 20} = \dfrac{-15 + 10\sqrt5}{11}$.
- $(a + \sqrt b)(a - \sqrt b) = a^2 - b$ is the difference of two squares; use it to compare or telescope surd sums, e.g. $\frac{1}{\sqrt2 + 1} = \sqrt2 - 1$.
- $\sqrt{x^2} = |x|$, never just $x$: the symbol $\sqrt{}$ always means the non-negative root (MM1.7)."""},
    ],
    "key": [r"$a^{m/n} = (\sqrt[n]{a})^m$", r"$a^{-n} = 1/a^n$", r"$\sqrt{ab} = \sqrt a \sqrt b$", r"$(a+\sqrt b)(a-\sqrt b) = a^2 - b$", r"$\sqrt{x^2} = |x|$"],
    "traps": [r"Do not add exponents when multiplying different bases: $2^3 \times 3^2$ is not $6^5$.",
              r"$(x + y)^{1/2}$ cannot be split; only products and quotients split.",
              r"When comparing surds like $\sqrt2 + \sqrt7$ and $2 + \sqrt5$, square them (both positive) instead of estimating."],
    "worked": [{"q": r"Solve $2^{x^2} = 16 \times 2^{-3x}$.", "a": r"$2^{x^2} = 2^{4-3x}$, so $x^2 + 3x - 4 = 0$, $(x + 4)(x - 1) = 0$: $x = -4$ or $x = 1$."}],
},
"quadratics": {
    "summary": r"The quadratic is the most examined object in Paper 1: completing the square gives the vertex and the range, the discriminant decides how many roots (and whether a line is a tangent), and the relations between roots and coefficients give quick routes to 'find $\alpha^2 + \beta^2$' questions.",
    "sections": [
        {"h": "Three forms of a quadratic (MM1.3, M4.11-M4.13)", "body": r"""- Standard $ax^2 + bx + c$: $y$-intercept $c$; the graph opens up if $a > 0$ and down if $a < 0$.
- Factorised $a(x - p)(x - q)$: roots $p$, $q$; the axis of symmetry is $x = \frac{p + q}{2}$.
- Completed square $a(x - h)^2 + k$: vertex $(h, k)$, which is the minimum (if $a > 0$) or maximum (if $a < 0$). For $x^2 + bx + c$: $h = -\frac b2$, $k = c - \frac{b^2}{4}$.
- The quadratic formula $x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ must be recalled (no formula booklet)."""},
        {"h": "The discriminant $b^2 - 4ac$", "body": r"""- $> 0$: two distinct real roots; $= 0$: one repeated root (the graph touches the axis); $< 0$: no real roots.
- 'The line meets the curve at exactly one point' means: substitute, form a quadratic in $x$, set the discriminant to zero.
- '$f(x) > 0$ for all $x$' means $a > 0$ **and** discriminant $< 0$.
- Conditions on roots: both roots positive needs discriminant $\geq 0$, sum $-\frac ba > 0$ and product $\frac ca > 0$."""},
        {"h": "Roots and coefficients", "body": r"""- If the roots are $\alpha, \beta$: $\alpha + \beta = -\dfrac ba$ and $\alpha\beta = \dfrac ca$.
- $\alpha^2 + \beta^2 = (\alpha + \beta)^2 - 2\alpha\beta$ and $(\alpha - \beta)^2 = (\alpha + \beta)^2 - 4\alpha\beta = \dfrac{b^2 - 4ac}{a^2}$.
- Disguised quadratics: $x^4 - 5x^2 + 4$, $(x^2 - 3x)^2 - 2(x^2 - 3x) - 8$, $9^x - 4\cdot 3^x + 3$ - substitute and remember to translate back (and to count the solutions correctly)."""},
    ],
    "key": [r"$x^2 + bx + c = (x + \frac b2)^2 + c - \frac{b^2}{4}$", r"$b^2 - 4ac$: $>0$, $=0$, $<0$", r"$\alpha + \beta = -b/a$, $\alpha\beta = c/a$", r"vertex of $a(x-h)^2 + k$ is $(h, k)$"],
    "traps": [r"When $a$ is negative, completing the square gives a maximum, not a minimum.",
              r"'No real roots' for $kx^2 + 4x + k = 0$: check whether $k = 0$ makes the equation linear.",
              r"Counting solutions of $x^4 - 5x^2 + 4 = 0$: each positive value of $x^2$ gives two values of $x$."],
    "worked": [{"q": r"For which $k$ does $x^2 + (k - 2)x + (k + 1) = 0$ have distinct real roots?", "a": r"$(k-2)^2 - 4(k+1) = k^2 - 8k = k(k - 8) > 0$, so $k < 0$ or $k > 8$."}],
},
"simultaneous-inequalities": {
    "summary": r"Substitution turns a linear/quadratic pair into a single quadratic; the discriminant of that quadratic then tells you how many intersection points the line and curve have. Inequalities are best solved by sketching the sign of a factorised expression rather than by manipulating symbols.",
    "sections": [
        {"h": "Simultaneous equations (MM1.4)", "body": r"""- Make one variable the subject of the linear equation and substitute into the quadratic one.
- The number of solutions equals the number of intersection points of the line and the curve; use the discriminant of the resulting quadratic.
- Symmetric tricks: from $x + y$ and $xy$ (or $x^2 + y^2$) you can find $(x - y)^2 = (x + y)^2 - 4xy$ without solving.
- $x^2 = y^2$ means $y = x$ **or** $y = -x$: two cases."""},
        {"h": "Inequalities (MM1.5, M4.17)", "body": r"""- Linear: as equations, but multiplying or dividing by a negative reverses the sign.
- Quadratic: factorise, find the roots, sketch, read off where the graph is above or below the axis. $(x - 2)(x - 5) < 0$ gives $2 < x < 5$; $\geq 0$ gives the two outer regions.
- Products of three or more factors: use a sign chart (the sign changes at each simple root).
- Never multiply an inequality by an expression whose sign is unknown ($x$, $x - 2$); either split into cases or bring everything to one side and study the sign of a fraction.
- Modulus: $|x - a| < r$ means $a - r < x < a + r$; $|x| > r$ means $x < -r$ or $x > r$.
- 'Both inequalities': intersect the solution sets on a number line; 'either': take the union."""},
    ],
    "key": [r"$(x - p)(x - q) < 0 \Leftrightarrow p < x < q$ (for $p < q$)", r"$|x - a| < r \Leftrightarrow a - r < x < a + r$", r"one line-curve intersection $\Leftrightarrow$ discriminant $= 0$"],
    "traps": [r"$\frac1x > 2$ is not $1 > 2x$: for $x < 0$ the inequality flips. Solution: $0 < x < \frac12$.",
              r"Replacing $x$ by $-x$ in $ax^2 + bx + c < 0$ reflects the solution set, so $-2 < x < 5$ becomes $-5 < x < 2$.",
              r"Count integers in an interval carefully: $2 < n < 8$ contains five integers."],
    "worked": [{"q": r"Solve $x + 2y = 7$, $x^2 + y^2 = 10$.", "a": r"$x = 7 - 2y$: $5y^2 - 28y + 39 = 0$, $(5y - 13)(y - 3) = 0$, giving $(1, 3)$ and $(\frac95, \frac{13}{5})$."}],
},
"polynomials": {
    "summary": r"The Factor Theorem and Remainder Theorem convert 'is $(x - a)$ a factor?' into 'is $f(a) = 0$?'. Combined with comparing coefficients this handles almost every TMUA polynomial question, including those with divisors of the form $ax + b$ or a quadratic.",
    "sections": [
        {"h": "Factor and Remainder Theorems (MM1.6)", "body": r"""- Remainder Theorem: when $f(x)$ is divided by $(x - a)$ the remainder is $f(a)$; for $(ax - b)$ it is $f\!\left(\frac ba\right)$.
- Factor Theorem: $(x - a)$ is a factor of $f(x)$ if and only if $f(a) = 0$.
- Dividing by a quadratic leaves a remainder of degree at most $1$: write $f(x) = (x^2 - 1)q(x) + Ax + B$ and substitute the roots $x = \pm1$ to find $A$ and $B$.
- To find a quotient quickly, compare coefficients: $2x^3 - 3x^2 + 4x - 5 = (x - 1)(2x^2 + px + q) + r$."""},
        {"h": "Factorising and roots", "body": r"""- A cubic $x^3 + ax^2 + bx + c$ with roots $p, q, r$ equals $(x - p)(x - q)(x - r)$, so $p + q + r = -a$, $pq + qr + rp = b$, $pqr = -c$.
- $f(1)$ is the sum of the coefficients; $f(-1)$ is the alternating sum.
- Useful identities: $x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2)$ (add and subtract $4x^2$); $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$.
- A repeated factor $(x - a)^2$ means $f(a) = 0$ and $f'(a) = 0$ (the graph touches the axis)."""},
    ],
    "key": [r"remainder on dividing by $(ax - b)$ is $f(b/a)$", r"$(x - a)$ factor $\Leftrightarrow f(a) = 0$", r"degree of remainder $<$ degree of divisor", r"$f(1) = $ sum of coefficients"],
    "traps": [r"For divisor $(2x - 1)$ substitute $x = \frac12$, not $x = 1$ or $x = 2$.",
              r"Not every cubic factorises over the integers - test $\pm$ factors of the constant term systematically.",
              r"Comparing coefficients needs the same number of equations as unknowns; a leftover equation is a check, not a contradiction."],
    "worked": [{"q": r"$x^3 + px + q$ is divisible by $(x - 2)^2$. Find $q$.", "a": r"$x^3 + px + q = (x - 2)^2(x - r)$; the $x^2$ coefficient gives $-4 - r = 0$, so $r = -4$ and $q = (4)(4) = 16$."}],
},
"functions": {
    "summary": r"A function is a rule that sends each input to exactly one output; 'one-to-one' means different inputs give different outputs. Transformations are tested constantly: know exactly which way $f(x + a)$ and $f(ax)$ move the graph and what happens when transformations are combined.",
    "sections": [
        {"h": "Mappings and common functions (MM1.7)", "body": r"""- Many-to-one: $x^2$, $|x|$, $\sin x$ (a horizontal line can cut the graph more than once). One-to-one: $x^3$, $2^x$, $\log x$, $x^3 + x$.
- $f(x) = \sqrt x$ is defined for $x \geq 0$ and always non-negative; $f(x) = |x|$ is $x$ for $x \geq 0$ and $-x$ for $x < 0$.
- Composition: $f(g(x))$ means apply $g$ first. $f(g(x))$ and $g(f(x))$ are usually different.
- $\sqrt{x^2} = |x|$, so $\sqrt{g(x)}$ with $g(x) = x^2 + 3$ ... care: $\sqrt{x^2} = x$ only when $x \geq 0$."""},
        {"h": "Transformations (MM8.2-MM8.4)", "body": r"""- $y = f(x) + a$: translate $a$ up. $y = f(x + a)$: translate $a$ to the **left**. $y = af(x)$: stretch vertically by $a$. $y = f(ax)$: stretch horizontally by factor $\frac1a$ (squash if $a > 1$).
- $y = -f(x)$ reflects in the $x$-axis; $y = f(-x)$ reflects in the $y$-axis.
- Order matters for combinations: $y = 2f(x - 3)$ is 'translate then stretch'; $y = f(2x - 2) = f(2(x - 1))$ is 'stretch by $\frac12$ then translate $1$ right'.
- Track a point: if $(4, 6)$ is on $y = f(x)$ then $(2, 17)$ is on $y = 3f(2x) - 1$ (halve $x$, then $3y - 1$).
- For $y = a(x + b)^2 + c$ the vertex is $(-b, c)$; for $y = mx + c$, $m$ is the gradient and $c$ the intercept.
- An exponential translation is a stretch in disguise: $2^{x-3} = \frac18\cdot 2^x$; a stretch of $\log$ is a translation: $\log(kx) = \log k + \log x$."""},
    ],
    "key": [r"$f(x + a)$: left by $a$", r"$f(ax)$: horizontal factor $1/a$", r"$af(x)$: vertical factor $a$", r"$f(-x)$: reflect in $y$-axis", r"$\sqrt{x^2} = |x|$"],
    "traps": [r"$f(x + 3)$ moves the graph to the left, not the right.",
              r"For $y = f(2x + 6)$ factorise first: $f(2(x + 3))$ - translate 3 left, then squash by $\frac12$ (or squash then translate 3 left if you translate by 6 first - do not mix the orders).",
              r"Two transformations that look different can give the same graph (e.g. reflecting $x^2$ in the $y$-axis does nothing)."],
    "worked": [{"q": r"The maximum of $y = f(x)$ is at $(3, 8)$. Where is the maximum of $y = f(x - a) + b$?", "a": r"At $(3 + a, 8 + b)$: the translation moves every point by $a$ right and $b$ up."}],
},
"sequences-series": {
    "summary": r"Arithmetic series (constant difference) and geometric series (constant ratio) each have two formulas you must know by heart, plus the condition $|r| < 1$ for a geometric series to have a sum to infinity. Recurrence sequences are examined by computing a few terms and spotting a pattern or a cycle.",
    "sections": [
        {"h": "Arithmetic (MM2.2)", "body": r"""- $u_n = a + (n - 1)d$; $\quad S_n = \frac n2\left[2a + (n - 1)d\right] = \frac n2(a + l)$ where $l$ is the last term.
- $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$.
- $u_n = S_n - S_{n-1}$ recovers a term from a sum formula.
- Three numbers are in arithmetic progression iff the middle one is the mean of the other two."""},
        {"h": "Geometric (MM2.3)", "body": r"""- $u_n = ar^{n-1}$; $\quad S_n = \dfrac{a(r^n - 1)}{r - 1} = \dfrac{a(1 - r^n)}{1 - r}$.
- $S_\infty = \dfrac{a}{1 - r}$ exists only when $|r| < 1$.
- The sum of the squares of a geometric series is another geometric series with first term $a^2$ and ratio $r^2$.
- Three numbers $p, q, r$ are in geometric progression iff $q^2 = pr$."""},
        {"h": "Recurrences (MM2.1)", "body": r"""- $x_{n+1} = f(x_n)$: just iterate. Look for cycles ($x_{n+1} = \frac{1}{1 - x_n}$ has period $3$) and use $n \bmod$ period for $x_{100}$.
- To prove a sequence is increasing and bounded, show $x_{n+1} - x_n > 0$ and use the bound in the recurrence.
- A sequence given by a formula in $n$ may be a quadratic; its minimum is found by completing the square in $n$ (remember $n$ is an integer)."""},
    ],
    "key": [r"$S_n = \frac n2[2a + (n-1)d]$", r"$S_n = \frac{a(r^n - 1)}{r - 1}$", r"$S_\infty = \frac{a}{1 - r}$, $|r| < 1$", r"$\sum_{k=1}^n k = \frac{n(n+1)}{2}$"],
    "traps": [r"'Sum of the first $n$ terms exceeds 500' needs the first $n$ that works, so check $n$ and $n - 1$.",
              r"A bouncing ball travels up **and** down: double the geometric series for the rises and add the initial drop.",
              r"$r = -1$ gives a series that does not converge even though it stays bounded."],
    "worked": [{"q": r"A geometric series has $S_\infty = 8$ and the sum of the squares of its terms is $\frac{64}{3}$. Find $r$.", "a": r"$\frac{a}{1-r} = 8$, $\frac{a^2}{1-r^2} = \frac{64}{3}$; dividing, $\frac{1 - r}{1 + r} = \frac13$, so $r = \frac12$."}],
},
"binomial": {
    "summary": r"For positive integer $n$, $(a + b)^n = \sum \binom nr a^{n-r} b^r$. TMUA questions ask for one coefficient, a term independent of $x$, the sum of coefficients, or an unknown $n$ or $k$ from a given coefficient - always identify the general term first.",
    "sections": [
        {"h": "The expansion (MM2.4)", "body": r"""- $\binom nr = \dfrac{n!}{r!(n - r)!}$; the first few rows of Pascal's triangle ($1\ 4\ 6\ 4\ 1$, $1\ 5\ 10\ 10\ 5\ 1$, $1\ 6\ 15\ 20\ 15\ 6\ 1$) save time.
- $(1 + x)^n = 1 + nx + \binom n2 x^2 + \cdots$; $(a + bx)^n$: general term $\binom nr a^{n-r}(bx)^r$.
- Symmetry $\binom nr = \binom n{n-r}$; Pascal's rule $\binom nr + \binom n{r+1} = \binom{n+1}{r+1}$; $\sum_r \binom nr = 2^n$.
- Sum of coefficients: put $x = 1$. Alternating sum: put $x = -1$."""},
        {"h": "Techniques", "body": r"""- Term independent of $x$ in $\left(x^2 + \frac2x\right)^6$: the power of $x$ is $2(6 - r) - r = 12 - 3r$; set it to $0$.
- Products such as $(1 + 3x)(1 - 2x)^4$: collect the two ways of making $x^2$.
- Unknown $n$ from two coefficients: divide the equations to eliminate the unknown constant, e.g. $na = 12$, $\binom n2 a^2 = 54$ gives $\frac{n - 1}{2n} = \frac{54}{144}$.
- Approximations like $1.01^5$: use the first few terms of $(1 + 0.01)^5$."""},
    ],
    "key": [r"$\binom nr = \frac{n!}{r!(n-r)!}$", r"general term $\binom nr a^{n-r} b^r$", r"$\binom nr = \binom n{n-r}$", r"$x = 1$ gives the sum of the coefficients"],
    "traps": [r"In $(2 + 3x)^5$ the coefficient of $x^3$ includes $2^2$ from the other term: $\binom53 2^2 3^3 = 1080$.",
              r"A negative sign inside the bracket alternates the signs of the terms.",
              r"'Coefficient' means the number in front; 'term' includes the $x^r$."],
    "worked": [{"q": r"Find the coefficient of $x^2$ in $(1 + 3x)(1 - 2x)^4$.", "a": r"$(1 - 2x)^4 = 1 - 8x + 24x^2 - \ldots$; the $x^2$ coefficient is $24 + 3(-8) = 0$."}],
},
"straight-lines": {
    "summary": r"Gradient, intercepts, parallel/perpendicular conditions and the distance and midpoint formulas cover the content; the exam skill is choosing the right form ($y - y_1 = m(x - x_1)$ or $ax + by + c = 0$) and using geometry (perpendicular bisectors, areas of triangles) rather than heavy algebra.",
    "sections": [
        {"h": "Equations and gradients (MM3.1, M4.10)", "body": r"""- Gradient $m = \dfrac{y_2 - y_1}{x_2 - x_1}$; line through $(x_1, y_1)$: $y - y_1 = m(x - x_1)$.
- $ax + by + c = 0$ has gradient $-\frac ab$, $x$-intercept $-\frac ca$ and $y$-intercept $-\frac cb$; the intercept form is $\frac xp + \frac yq = 1$.
- Parallel: equal gradients. Perpendicular: $m_1 m_2 = -1$ (a line of gradient $\frac ab$ has perpendicular gradient $-\frac ba$).
- Three points are collinear if two of the pairwise gradients agree.
- Midpoint $\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$; distance $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$."""},
        {"h": "Useful geometry", "body": r"""- Perpendicular bisector of $AB$: through the midpoint with the negative reciprocal gradient. Points equidistant from $A$ and $B$ lie on it.
- Distance from a point to a line $ax + by + c = 0$: $\dfrac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}}$ - or use 'area of triangle two ways'.
- Distance between parallel lines $ax + by = c_1$ and $ax + by = c_2$: $\dfrac{|c_1 - c_2|}{\sqrt{a^2 + b^2}}$.
- Area of a triangle with a horizontal or vertical base is $\frac12 \times$ base $\times$ height; a line through a vertex bisects the area iff it passes through the midpoint of the opposite side."""},
    ],
    "key": [r"$y - y_1 = m(x - x_1)$", r"perpendicular: $m_1 m_2 = -1$", r"$ax + by + c = 0$ has gradient $-a/b$", r"distance from $(x_0,y_0)$ to $ax+by+c=0$ is $|ax_0+by_0+c|/\sqrt{a^2+b^2}$"],
    "traps": [r"A vertical line $x = k$ has no gradient; do not divide by zero when points share an $x$-coordinate.",
              r"When finding where $y = mx + 4$ and $y = 3x - 2$ meet 'in the first quadrant', both coordinates must be positive - two conditions on $m$.",
              r"Perpendicular to $3x - 2y + 5 = 0$: gradient $-\frac23$, not $\frac23$ or $-\frac32$."],
    "worked": [{"q": r"Find the perpendicular bisector of $(1, 5)$ and $(7, 1)$.", "a": r"Midpoint $(4, 3)$; segment gradient $-\frac23$; bisector gradient $\frac32$: $y - 3 = \frac32(x - 4)$, i.e. $3x - 2y = 6$."}],
},
"circles": {
    "summary": r"Two skills: the algebra of $(x - a)^2 + (y - b)^2 = r^2$ (complete the square to find centre and radius, use the distance from the centre to a line for tangency) and the seven circle theorems, which are examined as short reasoning questions rather than long proofs.",
    "sections": [
        {"h": "Coordinate geometry of the circle (MM3.2)", "body": r"""- $x^2 + y^2 + cx + dy + e = 0$ is $(x + \frac c2)^2 + (y + \frac d2)^2 = \frac{c^2}{4} + \frac{d^2}{4} - e$; it is a real circle only when the right-hand side is positive.
- Tangent at a point: perpendicular to the radius there. Length of the tangent from an external point $P$: $\sqrt{PC^2 - r^2}$.
- A line is a tangent iff its distance from the centre equals $r$ (or the substituted quadratic has discriminant $0$).
- Two circles with radii $r_1, r_2$ and centres $d$ apart: touch externally if $d = r_1 + r_2$, internally if $d = |r_1 - r_2|$, intersect twice if $|r_1 - r_2| < d < r_1 + r_2$.
- A right angle in a triangle inscribed in a circle sits opposite a diameter, so the hypotenuse is a diameter and its midpoint is the centre."""},
        {"h": "Circle theorems (MM3.3, M5.9)", "body": r"""- The perpendicular from the centre to a chord bisects the chord.
- The tangent is perpendicular to the radius at the point of contact.
- Angle at the centre $= 2 \times$ angle at the circumference (same arc).
- The angle in a semicircle is $90^\circ$.
- Angles in the same segment are equal.
- Opposite angles of a cyclic quadrilateral sum to $180^\circ$.
- Alternate segment theorem: the angle between a tangent and a chord equals the angle in the alternate segment."""},
    ],
    "key": [r"$(x-a)^2 + (y-b)^2 = r^2$", r"tangent $\perp$ radius", r"centre angle $= 2\times$ circumference angle", r"cyclic quadrilateral: opposite angles sum to $180^\circ$", r"tangent length $= \sqrt{PC^2 - r^2}$"],
    "traps": [r"Halve $c$ and $d$ when completing the square: centre $(-c/2, -d/2)$, not $(-c, -d)$.",
              r"'Represents a circle' needs $r^2 > 0$; equality gives a single point.",
              r"The locus 'distance from $A$ is twice the distance from $B$' is a circle - expand and complete the square."],
    "worked": [{"q": r"Find $c$ so that $y = x + c$ touches $(x - 1)^2 + (y - 2)^2 = 8$.", "a": r"Distance from $(1, 2)$ to $x - y + c = 0$ is $\frac{|c - 1|}{\sqrt2} = 2\sqrt2$, so $|c - 1| = 4$: $c = 5$ or $-3$."}],
},
"trig-triangles": {
    "summary": r"Sine rule, cosine rule and $\frac12 ab\sin C$ solve any triangle; radians make arc length and sector area simple ($r\theta$ and $\frac12 r^2\theta$). The 'ambiguous case' - two triangles from side-side-angle data - is a TMUA favourite.",
    "sections": [
        {"h": "Triangles (MM4.1)", "body": r"""- Sine rule: $\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C}$. Cosine rule: $a^2 = b^2 + c^2 - 2bc\cos A$, i.e. $\cos A = \dfrac{b^2 + c^2 - a^2}{2bc}$.
- Area $= \frac12 ab\sin C$. Heron-style: find $\cos$ from the cosine rule, then $\sin$ from $\sin^2 + \cos^2 = 1$.
- Ambiguous case: given sides $a, b$ and angle $A$ (opposite $a$) with $b\sin A < a < b$, there are two triangles (an acute and an obtuse value of $B$). If $a \geq b$ or $a = b\sin A$ there is one; if $a < b\sin A$, none.
- Largest angle is opposite the longest side; $a^2 + b^2 < c^2$ means the angle opposite $c$ is obtuse."""},
        {"h": "Radians, arcs and sectors (MM4.2)", "body": r"""- $\pi$ radians $= 180^\circ$; $30^\circ = \frac\pi6$, $45^\circ = \frac\pi4$, $60^\circ = \frac\pi3$, $90^\circ = \frac\pi2$.
- Arc length $s = r\theta$; sector area $\frac12 r^2\theta$; segment area $\frac12 r^2(\theta - \sin\theta)$ ($\theta$ in radians).
- Perimeter of a sector $= 2r + r\theta$.
- Overlapping circles: the common region is two segments; the chord subtends $2\theta$ at each centre."""},
    ],
    "key": [r"$a^2 = b^2 + c^2 - 2bc\cos A$", r"$\frac{a}{\sin A} = \frac{b}{\sin B}$", r"area $= \frac12 ab\sin C$", r"$s = r\theta$, $A = \frac12 r^2\theta$", r"segment $= \frac12 r^2(\theta - \sin\theta)$"],
    "traps": [r"$\cos 120^\circ = -\frac12$: the cosine rule with an obtuse angle **adds** the last term.",
              r"Sector formulas need radians; convert first.",
              r"An area of $10\sqrt3$ with $\sin P = \frac{\sqrt3}{2}$ gives $P = 60^\circ$ or $120^\circ$ - read whether the angle is obtuse."],
    "worked": [{"q": r"Sector: perimeter $20$, area $16$. Find $r$.", "a": r"$r\theta = 20 - 2r$ and $\frac12 r(20 - 2r) = 16$, so $r^2 - 10r + 16 = 0$: $r = 2$ or $8$."}],
},
"trig-functions": {
    "summary": r"Know the exact values, the shapes and symmetries of the three graphs, and the two identities $\tan\theta = \frac{\sin\theta}{\cos\theta}$ and $\sin^2\theta + \cos^2\theta = 1$. Most equation questions ask 'how many solutions' - a sketch of the graph in the given interval is faster and safer than listing them all.",
    "sections": [
        {"h": "Exact values and graphs (MM4.3, MM4.4)", "body": r"""- $\sin$: $0, \frac12, \frac{\sqrt2}{2}, \frac{\sqrt3}{2}, 1$ for $0^\circ, 30^\circ, 45^\circ, 60^\circ, 90^\circ$; $\cos$ runs the same list backwards; $\tan$: $0, \frac{1}{\sqrt3}, 1, \sqrt3$, undefined.
- $\sin$ and $\cos$ have period $360^\circ$ ($2\pi$), range $[-1, 1]$; $\tan$ has period $180^\circ$ ($\pi$) and asymptotes at $90^\circ + 180^\circ k$.
- $\cos$ is even ($\cos(-x) = \cos x$), $\sin$ and $\tan$ are odd. $\cos x = \sin(x + 90^\circ)$. $\sin(180^\circ - x) = \sin x$, $\cos(360^\circ - x) = \cos x$, $\tan(x + 180^\circ) = \tan x$.
- $y = a\sin(bx) + c$ has amplitude $|a|$, period $\frac{360^\circ}{b}$ and midline $y = c$."""},
        {"h": "Identities and equations (MM4.5, MM4.6)", "body": r"""- $\tan\theta = \dfrac{\sin\theta}{\cos\theta}$; $\sin^2\theta + \cos^2\theta = 1$ (so $\cos^2\theta = 1 - \sin^2\theta$ turns $2\cos^2x + 3\sin x - 3 = 0$ into a quadratic in $\sin x$).
- Solving $\sin(kx + a) = c$: find the solutions for $u = kx + a$ over the stretched interval, then convert. The number of solutions is usually $k$ times what it would be for $\sin u = c$.
- Sign check with CAST or the graph: $\sin x = \frac12$ has $30^\circ$ and $150^\circ$; $\cos x = -\frac12$ has $120^\circ$ and $240^\circ$; $\tan x = -1$ has $135^\circ$ and $315^\circ$.
- $\sin x = \sin\alpha$ does **not** imply $x = \alpha$; it gives $x = \alpha$ or $180^\circ - \alpha$ (plus multiples of $360^\circ$).
- Never divide by $\cos x$ or $\sin x$: factorise instead, or you lose the solutions where it is zero."""},
    ],
    "key": [r"$\sin 30^\circ = \frac12$, $\cos 30^\circ = \frac{\sqrt3}{2}$, $\tan 60^\circ = \sqrt3$", r"$\sin^2 x + \cos^2 x = 1$", r"period of $\sin(kx)$ is $360^\circ/k$", r"$\sin(180^\circ - x) = \sin x$"],
    "traps": [r"Check the interval's endpoints: $0 < x < 360^\circ$ excludes $0^\circ$ and $360^\circ$ but includes $180^\circ$.",
              r"$\sin^2 x = \frac34$ has four solutions in a full turn, not two.",
              r"Radians vs degrees: $\sin x = \frac{x}{10}$ only makes sense in radians."],
    "worked": [{"q": r"How many solutions has $\sin 2x = \frac12$ for $0 \leq x < 2\pi$?", "a": r"$2x$ runs over $[0, 4\pi)$ - two periods, two solutions each: four."}],
},
"exp-logs": {
    "summary": r"$y = a^x$ and $y = \log_a x$ are inverses (reflections in $y = x$). The three log laws plus $\log_a a = 1$ and $\log_a 1 = 0$ let you solve $a^x = b$ and equations that reduce to it; the change-of-base formula is not required, but $\log_4 x = \frac12\log_2 x$ style relations are.",
    "sections": [
        {"h": "Exponentials (MM5.1, MM5.3)", "body": r"""- $y = a^x$ ($a > 1$): through $(0, 1)$, increasing, asymptote $y = 0$; for $0 < a < 1$ it decreases. $a^{-x} = \left(\frac1a\right)^x$.
- Compare growth by finding when curves cross: $2^x$ and $x^2$ meet at $x = 2, 4$ and once for negative $x$.
- $a^x = b \Leftrightarrow x = \log_a b$. Equations like $25^x - 3\cdot5^x + 2 = 0$ are quadratics in $5^x$; keep only positive roots.
- Halving/doubling: $\left(\frac12\right)^{t/5} = \frac{1}{10} \Rightarrow t = \frac{5}{\log_{10} 2}$."""},
        {"h": "Logarithms (MM5.2)", "body": r"""- $\log_a(xy) = \log_a x + \log_a y$; $\log_a\frac xy = \log_a x - \log_a y$; $k\log_a x = \log_a x^k$; $\log_a\frac1x = -\log_a x$; $\log_a a = 1$, $\log_a 1 = 0$.
- $\log_a x$ is only defined for $x > 0$: after solving $\log_3(x + 6) + \log_3(x - 2) = 2$, reject any $x$ that makes an argument non-positive.
- Chains: $\log_a b = 2$ and $\log_b c = 3$ give $c = b^3 = a^6$, so $\log_a c = 6$.
- $\frac{\log 27}{\log 3} = 3$ because $27 = 3^3$ (no change of base needed).
- Sums of logs telescope: $\sum \log\frac{n+1}{n} = \log(N + 1)$."""},
    ],
    "key": [r"$\log_a(xy) = \log_a x + \log_a y$", r"$k\log_a x = \log_a x^k$", r"$a^x = b \Leftrightarrow x = \log_a b$", r"$\log_a a = 1$, $\log_a 1 = 0$", r"$y = a^x$ and $y = \log_a x$ are reflections in $y = x$"],
    "traps": [r"$\log(x + y)$ has no expansion; $\log x - \log y$ is $\log\frac xy$, not $\frac{\log x}{\log y}$.",
              r"Extraneous solutions: $\log$ of a negative number is undefined even if the algebra 'works'.",
              r"A translation of $y = 2^x$ by $3$ to the right is the same as a vertical stretch by $\frac18$."],
    "worked": [{"q": r"Solve $2^{2x} - 3\cdot2^{x+2} + 32 = 0$.", "a": r"With $y = 2^x$: $y^2 - 12y + 32 = (y - 4)(y - 8) = 0$, so $x = 2$ or $3$."}],
},
"differentiation": {
    "summary": r"Differentiate powers of $x$ after rewriting the expression as a sum of terms $ax^n$ (expand brackets, split fractions, convert roots). Then apply: gradient of tangent/normal, stationary points and their nature, increasing/decreasing intervals, and optimisation.",
    "sections": [
        {"h": "Derivatives (MM6.1, MM6.2)", "body": r"""- $\dfrac{d}{dx}x^n = nx^{n-1}$ for any rational $n$; constants differentiate to $0$; sums term by term.
- Rewrite first: $\dfrac{(3x - 2)^2}{x^2} = 9 - 12x^{-1} + 4x^{-2}$; $\sqrt x = x^{1/2}$; $\dfrac{1}{\sqrt x} = x^{-1/2}$.
- $f'(a)$ is the gradient of the tangent at $x = a$ and the rate of change there; velocity is $\frac{ds}{dt}$.
- Second derivative $f''(x)$: positive at a stationary point means a minimum, negative means a maximum, zero is inconclusive (check the sign change of $f'$)."""},
        {"h": "Applications (MM6.3, MM8.5)", "body": r"""- Tangent at $(a, f(a))$: $y - f(a) = f'(a)(x - a)$; normal: gradient $-\frac{1}{f'(a)}$.
- Stationary points: solve $f'(x) = 0$. Increasing where $f'(x) > 0$, decreasing where $f'(x) < 0$.
- A cubic $ax^3 + bx^2 + cx + d$ has two turning points iff $b^2 > 3ac$; it has three real roots iff the local max is above the axis and the local min below.
- Optimisation: express the quantity in one variable, differentiate, solve, confirm max/min, then evaluate.
- $f'(x) = (x - 2)^2(x + 1)$: the squared factor does not change sign, so $x = 2$ is a stationary point but not a turning point."""},
    ],
    "key": [r"$\frac{d}{dx}x^n = nx^{n-1}$", r"tangent: $y - y_1 = f'(x_1)(x - x_1)$", r"normal gradient $= -1/f'(x_1)$", r"$f'' > 0$ min, $f'' < 0$ max", r"increasing $\Leftrightarrow f' > 0$"],
    "traps": [r"Differentiate the whole expression, not a bracket 'in place': $\frac{d}{dx}(3x - 2)^2 \neq 2(3x - 2)$ without the chain rule (not in the spec - expand instead).",
              r"A local minimum need not be the global minimum: $x^3 - 3x$ has local min $-2$ but is unbounded below.",
              r"Minimum distance from a point to a curve: minimise the **squared** distance to avoid square roots."],
    "worked": [{"q": r"Find the stationary points of $y = x^3 - 3x^2 - 9x + 5$.", "a": r"$y' = 3(x - 3)(x + 1)$; $y'' = 6x - 6$: maximum $(-1, 10)$, minimum $(3, -22)$."}],
},
"integration": {
    "summary": r"Integration reverses differentiation: $\int x^n\,dx = \frac{x^{n+1}}{n+1} + c$ for $n \neq -1$. Definite integrals give signed areas - regions below the axis count negative - and the Fundamental Theorem of Calculus links $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$. The trapezium rule and its over/under-estimate are examined every year.",
    "sections": [
        {"h": "Indefinite and definite integrals (MM7.2, MM7.4)", "body": r"""- Rewrite before integrating: $\dfrac{3x^2 - 5}{\sqrt x} = 3x^{3/2} - 5x^{-1/2}$.
- $\int_a^b f(x)\,dx = F(b) - F(a)$; $\int_b^a = -\int_a^b$; $\int_a^b + \int_b^c = \int_a^c$; $\int (f \pm g) = \int f \pm \int g$; constants come out.
- $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$ (FTC): if $F(x) = \int_2^x (t^2 - 3t)\,dt$ then $F'(x) = x^2 - 3x$.
- Odd functions integrate to $0$ over symmetric intervals; even functions give twice the integral from $0$.
- $\frac{dy}{dx} = f(x)$ with a point on the curve: integrate, then find $c$."""},
        {"h": "Areas and the trapezium rule (MM7.1, MM7.3, MM7.5)", "body": r"""- Area between a curve and the axis: split at the roots and add the absolute values of the pieces.
- Area between two curves: $\int (\text{upper} - \text{lower})\,dx$ between the intersection points.
- Trapezium rule with strips of width $h$: $\frac h2\left[y_0 + 2(y_1 + \cdots + y_{n-1}) + y_n\right]$.
- Overestimate when the curve is convex (bends upwards, chords above the curve, e.g. $x^2$, $2^x$); underestimate when concave ($\sqrt x$, $\log x$, $-x^2$).
- Symmetry shortcuts: $y = x(x - 1)(x - 2)$ is odd about $(1, 0)$, so the two enclosed regions are equal."""},
    ],
    "key": [r"$\int x^n dx = \frac{x^{n+1}}{n+1} + c$", r"$\int_a^b f = F(b) - F(a)$", r"$\frac{d}{dx}\int_a^x f(t)dt = f(x)$", r"trapezium: $\frac h2[y_0 + 2(\ldots) + y_n]$", r"convex $\Rightarrow$ overestimate"],
    "traps": [r"A definite integral can be negative or zero while the **area** is positive.",
              r"$\int (x + \frac1x)^2 dx$: expand first; you cannot integrate a bracket by raising the power.",
              r"$\int_{-1}^{1} x^{-2}dx$ is not $-2$: the integrand is undefined at $0$, inside the interval."],
    "worked": [{"q": r"Area between $y = x^2$ and $y = 2x + 3$.", "a": r"Meet at $x = -1, 3$. $\int_{-1}^{3}(2x + 3 - x^2)\,dx = \frac{32}{3}$."}],
},
"graphs": {
    "summary": r"Sketching is a reasoning tool: the number of solutions of $f(x) = g(x)$ is the number of intersections of the graphs, and the sign of a function is read from a sketch. Know the standard shapes and how roots, repeated roots and the leading coefficient control a polynomial's picture.",
    "sections": [
        {"h": "Standard graphs (MM8.1, M4.15)", "body": r"""- Lines, parabolas, cubics (an S-shape; $+x^3$ rises to the right), $y = \frac1x$ (two branches, asymptotes both axes), $y = a^x$ (through $(0, 1)$), $y = \log_a x$ (through $(1, 0)$, only $x > 0$), $y = \sqrt x$ (only $x \geq 0$), $y = |x|$ (V-shape), $\sin$, $\cos$, $\tan$.
- $y = |f(x)|$: reflect the parts below the axis upwards. $|x^2 - 4|$ is a W with minima $0$ at $\pm2$ and a local maximum $4$ at $0$.
- Reflection in $y = x$ gives the inverse: $\log_2 x \leftrightarrow 2^x$."""},
        {"h": "Roots and intersections (MM8.6, MM8.7)", "body": r"""- A polynomial of degree $n$ has at most $n$ real roots; an odd degree guarantees at least one.
- A factor $(x - a)^2$ makes the graph touch the axis at $a$; $(x - a)^3$ crosses with a flat point.
- $y$-intercept: put $x = 0$. The sign of the leading coefficient fixes the behaviour as $x \to \pm\infty$.
- Solutions of $f(x) = k$ = intersections with the horizontal line $y = k$: slide the line to count how the number changes (e.g. exactly three solutions of $|x^2 - 4| = k$ only when $k = 4$).
- Line meets curve: substitute and use the discriminant (or a sketch when no algebra is possible, e.g. $\sin x = \frac{x}{10}$)."""},
    ],
    "key": [r"degree $n$: at most $n$ roots; odd degree: at least $1$", r"$(x-a)^2$ factor: touches", r"intersections of $y = f(x)$ and $y = g(x)$ = solutions of $f(x) = g(x)$", r"$y = |f(x)|$ reflects negative parts up"],
    "traps": [r"$x^2 + cx - 1 = 0$ always has two roots (discriminant $c^2 + 4 > 0$): $y = x + c$ always meets $y = \frac1x$ twice.",
              r"$\sqrt{4 - x} = \sqrt{-(x - 4)}$: reflect first, then translate $4$ right (the other order gives $\sqrt{-x - 4}$).",
              r"A cubic with three real roots must have two turning points, but two turning points do not guarantee three roots."],
    "worked": [{"q": r"How many real solutions has $x^3 = 3x + 1$?", "a": r"$y = x^3 - 3x - 1$ has turning values $y(-1) = 1 > 0$ and $y(1) = -3 < 0$, so three crossings."}],
},
}
