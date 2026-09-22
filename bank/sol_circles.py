"""Full teaching solutions: circles and circle theorems (CIR-xx)."""
from gen.model import Sol

SOLUTIONS = {

"CIR-01": Sol(
    idea=r"The expanded form of a circle. Complete the square in $x$ and in $y$ to recover the centre-radius form.",
    steps=[
        (r"Group the terms: $(x^2 - 6x) + (y^2 + 4y) = 12$.",
         r"Move the constant to the right first so the completed squares have somewhere to go."),
        (r"Complete each square: $x^2 - 6x = (x-3)^2 - 9$ and $y^2 + 4y = (y+2)^2 - 4$.",
         r"Halve each coefficient ($-6 \to -3$, $4 \to 2$) and subtract its square."),
        (r"Substitute: $(x-3)^2 + (y+2)^2 - 13 = 12$, so $(x-3)^2 + (y+2)^2 = 25$.",
         r"The $-9$ and $-4$ move across to the right, **adding** to the constant."),
        (r"Read off $r^2 = 25$, so $r = 5$.",
         r"The right-hand side is $r^2$, not $r$."),
    ],
    pitfalls=[r"Answering $25$ - that is $r^2$.",
              r"Subtracting the $9$ and $4$ on the right instead of adding, giving $r^2 = 12$ or similar."],
    takeaway=r"$x^2+y^2+cx+dy+e=0$ has centre $\left(-\frac c2, -\frac d2\right)$ and $r^2 = \frac{c^2}{4}+\frac{d^2}{4}-e$."),

"CIR-02": Sol(
    idea=r"An equation of circle form only **is** a circle when the resulting $r^2$ is positive. That gives an inequality in $k$.",
    steps=[
        (r"Complete both squares: $(x + k)^2 - k^2 + (y - 2)^2 - 4 + 3k + 4 = 0$.",
         r"Treat $k$ as a constant: half of $2k$ is $k$, half of $-4$ is $-2$."),
        (r"Rearrange: $(x+k)^2 + (y-2)^2 = k^2 - 3k$.",
         r"The $-4$ and $+4$ cancel, leaving $r^2 = k^2 - 3k$."),
        (r"A genuine circle needs $r^2 > 0$: $k^2 - 3k > 0$, i.e. $k(k - 3) > 0$.",
         r"If $r^2 = 0$ the 'circle' is a single point; if $r^2 < 0$ there are no real points at all."),
        (r"Solve the quadratic inequality: $k < 0$ or $k > 3$.",
         r"Roots $0$ and $3$, upward parabola, positive outside the roots."),
    ],
    pitfalls=[r"Choosing $0 < k < 3$ - that is where $r^2$ is negative and there is no circle.",
              r"Forgetting the sign change when moving $-k^2$ across."],
    takeaway=r"Complete the square and demand $r^2 > 0$; the shape only exists when the right-hand side is positive."),

"CIR-03": Sol(
    idea=r"A tangent is perpendicular to the radius at the point of contact. Find the radius gradient, invert, and write the line.",
    steps=[
        (r"Vector from centre $(2,-1)$ to the point $(5,3)$: $(3, 4)$, so the radius has gradient $\frac43$.",
         r"Differences of coordinates give the direction; no need for the circle's equation."),
        (r"The tangent is perpendicular, so its gradient is $-\dfrac34$.",
         r"Tangent $\perp$ radius is the key circle fact here."),
        (r"Line through $(5,3)$: $y - 3 = -\frac34(x - 5)$.",
         r"The tangent touches at the given point, so use it in the point-gradient form."),
        (r"Clear fractions: $4y - 12 = -3x + 15 \Rightarrow 3x + 4y = 27$.",
         r"Multiply by $4$, then collect."),
    ],
    pitfalls=[r"Using the radius gradient $\frac43$ for the tangent, giving $4x - 3y = 11$ - an offered option.",
              r"Arithmetic slip on the constant, giving $3x + 4y = 15$."],
    takeaway=r"Tangent gradient $= -1 \div$ (radius gradient); the point of contact is on both the circle and the tangent."),

"CIR-04": Sol(
    idea=r"A diameter's endpoints give the centre (midpoint) and the radius (half the distance) in one move.",
    steps=[
        (r"Centre $=$ midpoint $= \left(\frac{1+5}{2}, \frac{7 + (-1)}{2}\right) = (3, 3)$.",
         r"The centre is the midpoint of any diameter."),
        (r"Radius$^2$: distance from the centre to $(1,7)$ squared $= (3-1)^2 + (3-7)^2 = 4 + 16 = 20$.",
         r"Going from centre to an endpoint is one radius; squaring avoids surds entirely."),
        (r"Write the equation: $(x-3)^2 + (y-3)^2 = 20$.",
         r"The right-hand side is $r^2$."),
    ],
    pitfalls=[r"Using the full diameter length squared ($80$) as $r^2$.",
              r"Writing $r^2 = \sqrt{20}$ - the square root is already undone by squaring."],
    takeaway=r"From a diameter: centre is the midpoint, and $r^2$ is the squared distance from centre to either end."),

"CIR-05": Sol(
    idea=r"Tangency means the perpendicular distance from the centre to the line equals the radius. Faster than substituting and using the discriminant.",
    steps=[
        (r"Identify centre $(1,2)$ and radius $\sqrt8 = 2\sqrt2$.",
         r"Read them straight from the centre-radius form."),
        (r"Write the line in the form $x - y + c = 0$ and apply the distance formula: $\dfrac{|1 - 2 + c|}{\sqrt{1^2 + (-1)^2}} = \dfrac{|c - 1|}{\sqrt2}$.",
         r"Rearranging $y = x + c$ to $x - y + c = 0$ gives $a = 1$, $b = -1$."),
        (r"Set it equal to the radius: $\dfrac{|c-1|}{\sqrt2} = 2\sqrt2$, so $|c - 1| = 4$.",
         r"Multiply both sides by $\sqrt2$: $2\sqrt2 \times \sqrt2 = 4$."),
        (r"Solve the modulus: $c - 1 = \pm 4$, so $c = 5$ or $c = -3$.",
         r"Two tangents with that gradient exist - one on each side of the circle."),
    ],
    pitfalls=[r"Dropping the modulus and finding only $c = 5$.",
              r"Using $r = 8$ instead of $\sqrt8$."],
    takeaway=r"Tangency $\Leftrightarrow$ distance from centre to line $=$ radius; the modulus always gives two answers."),

"CIR-06": Sol(
    idea=r"The angle at the centre is twice the angle at the circumference on the same arc - provided you use the right arc.",
    steps=[
        (r"Identify the arc: angle $AOB = 100^\circ$ at the centre stands on the **minor** arc $AB$.",
         r"The reflex angle at the centre ($260^\circ$) would correspond to the other arc - which arc you use decides the answer."),
        (r"$C$ is on the major arc, so it sees the same minor arc $AB$.",
         r"The circumference angle must be on the opposite arc from the one it stands on."),
        (r"Apply the theorem: angle $ACB = \frac12 \times 100^\circ = 50^\circ$.",
         r"Centre angle is double the circumference angle on the same arc."),
    ],
    pitfalls=[r"Doubling instead of halving, giving $200^\circ$ - impossible for an angle in a triangle.",
              r"Using the reflex angle $260^\circ$ and answering $130^\circ$ (which would be right if $C$ were on the minor arc)."],
    takeaway=r"Angle at centre $= 2 \times$ angle at circumference **on the same arc**; check which side of the chord the point lies."),

"CIR-07": Sol(
    idea=r"Cyclic quadrilateral: opposite angles are supplementary. That gives a linear equation immediately.",
    steps=[
        (r"Identify the opposite pair: in $PQRS$ the vertices go round in order, so $P$ and $R$ are opposite.",
         r"Opposite means separated by one vertex on each side - reading the labelling order matters."),
        (r"Apply the theorem: $3x + (x + 40) = 180$.",
         r"Opposite angles of a cyclic quadrilateral sum to $180^\circ$."),
        (r"Solve: $4x = 140$, so $x = 35^\circ$.",
         r"Check: angles $105^\circ$ and $75^\circ$ sum to $180^\circ$ ✓."),
    ],
    pitfalls=[r"Setting the angles equal (that is a parallelogram property, not a cyclic one).",
              r"Using $360^\circ$ and getting $x = 80^\circ$."],
    takeaway=r"Cyclic quadrilateral: opposite angles sum to $180^\circ$; adjacent ones have no such relation."),

"CIR-08": Sol(
    idea=r"The perpendicular from the centre bisects the chord, creating a right-angled triangle with the radius as hypotenuse.",
    steps=[
        (r"Draw the radius to one end of the chord and the perpendicular from the centre: they form a right-angled triangle.",
         r"The perpendicular distance, half the chord and the radius are the three sides."),
        (r"Apply Pythagoras: half-chord $= \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12$.",
         r"The radius $13$ is the hypotenuse because it is the longest side."),
        (r"Double it: the chord is $24$.",
         r"The perpendicular **bisects** the chord, so the triangle gives only half of it."),
    ],
    pitfalls=[r"Answering $12$ by forgetting to double.",
              r"Adding instead of subtracting inside the square root."],
    takeaway=r"Perpendicular from centre to chord: it bisects the chord, so use Pythagoras and then double."),

"CIR-09": Sol(
    idea=r"The tangent, radius and line to the external point form a right-angled triangle. Pythagoras gives the tangent length.",
    steps=[
        (r"Put the circle in centre-radius form: $(x-1)^2 + (y-2)^2 = 4 + 1 + 4 = 9$, so centre $(1,2)$, radius $3$.",
         r"Complete the square in $x$ and $y$; the constant $-4$ moves across."),
        (r"Distance from $(7,1)$ to the centre: $\sqrt{(7-1)^2 + (1-2)^2} = \sqrt{36 + 1} = \sqrt{37}$.",
         r"This is the hypotenuse of the right-angled triangle (the tangent meets the radius at $90^\circ$)."),
        (r"Tangent length $= \sqrt{PC^2 - r^2} = \sqrt{37 - 9} = \sqrt{28}$.",
         r"Subtract the squares, not the lengths - the right angle is at the point of contact."),
    ],
    pitfalls=[r"Answering $\sqrt{37}$ (that is the distance to the centre) or $\sqrt{37} - 3$.",
              r"Getting $r = 9$ instead of $3$ from the completed square."],
    takeaway=r"Tangent length from $P$: $\sqrt{PC^2 - r^2}$, because tangent $\perp$ radius makes a right-angled triangle."),

"CIR-10": Sol(
    idea=r"The alternate segment theorem, stated almost word for word. The work is in identifying which angle is 'in the alternate segment'.",
    steps=[
        (r"$TA$ is tangent at $A$ and $AB$ is a chord, so the angle $TAB$ between them is the tangent-chord angle.",
         r"The theorem applies exactly to this configuration."),
        (r"The alternate segment is the one on the other side of $AB$ from $T$ - which is where $C$ lies.",
         r"The question places $C$ deliberately; the angle used must be in the segment **away** from the tangent's side."),
        (r"Therefore angle $TAB$ = angle $ACB = 65^\circ$.",
         r"Alternate segment theorem: the tangent-chord angle equals the inscribed angle in the alternate segment."),
    ],
    pitfalls=[r"Using $180^\circ - 65^\circ = 115^\circ$, which is the angle on the other side of the tangent.",
              r"Halving to $32.5^\circ$ by confusing this with the centre-circumference theorem."],
    takeaway=r"Tangent-chord angle $=$ angle in the alternate segment - the segment on the far side of the chord."),

"CIR-11": Sol(
    idea=r"Two circles: compare the distance between centres with the sum and difference of the radii.",
    steps=[
        (r"Read off centres and radii: $(0,0)$ with $r = 5$; $(8,0)$ with $r = 3$.",
         r"Both are already in centre-radius form."),
        (r"Distance between centres: $8$. Compare with $r_1 + r_2 = 8$.",
         r"Equal to the sum means the circles touch externally - exactly one common point."),
        (r"I is therefore true, and II (two intersection points) is false.",
         r"Two intersections would need $|r_1 - r_2| < d < r_1 + r_2$, i.e. $2 < d < 8$ strictly."),
        (r"III: check $(5,0)$ in both: $25 + 0 = 25$ ✓ and $(5-8)^2 + 0 = 9$ ✓. **True.**",
         r"The touching point lies on the line joining the centres, $5$ from one and $3$ from the other."),
        (r"I and III only.",
         r"Match to the options."),
    ],
    pitfalls=[r"Assuming circles that 'meet' must meet twice.",
              r"Forgetting to test III in **both** equations."],
    takeaway=r"$d = r_1 + r_2$: touch externally; $d = |r_1 - r_2|$: touch internally; strictly between: two points."),

"CIR-12": Sol(
    idea=r"Which line misses the circle: compare each line's distance from the centre with the radius. Horizontal and vertical lines make this trivial.",
    steps=[
        (r"Complete the square: $(x-2)^2 + (y-3)^2 = -9 + 4 + 9 = 4$, so centre $(2,3)$ and radius $2$.",
         r"Always convert to centre-radius form first."),
        (r"The circle therefore spans $x$ from $0$ to $4$ and $y$ from $1$ to $5$.",
         r"Centre $\pm$ radius in each direction gives the bounding box, whose edges are tangent lines."),
        (r"Check each line: $x = 0$, $x = 4$ and $y = 5$ are tangents (distance exactly $2$); $x = 2$ passes through the centre.",
         r"For a vertical line $x = k$, the distance from the centre is $|k - 2|$."),
        (r"$y = 0$ is at distance $|0 - 3| = 3 > 2$, so it misses the circle.",
         r"Distance greater than the radius means no intersection."),
    ],
    pitfalls=[r"Assuming a tangent line 'does not meet' the circle - touching counts as meeting.",
              r"Getting $r^2 = 9$ by mishandling the $+9$ constant."],
    takeaway=r"For horizontal/vertical lines just compare the centre coordinate with the radius; tangency still counts as meeting."),

"CIR-13": Sol(
    idea=r"One common point means tangency, so the radius equals the distance from the centre to the line.",
    steps=[
        (r"The circle is centred at the origin, so compute the distance from $(0,0)$ to $3x + 4y = 20$.",
         r"Centre-at-origin makes the distance formula especially clean."),
        (r"Distance $= \dfrac{|3(0) + 4(0) - 20|}{\sqrt{3^2+4^2}} = \dfrac{20}{5} = 4$.",
         r"$\sqrt{9+16} = 5$ - the familiar 3-4-5 triple."),
        (r"Tangency requires $r$ equal to this distance: $r = 4$.",
         r"If $r$ were larger the line would cut the circle twice; smaller, and it would miss."),
    ],
    pitfalls=[r"Dividing by $\sqrt{20}$ or by $7$ instead of $5$.",
              r"Answering $20$ or $\sqrt{20}$ by stopping too early."],
    takeaway=r"Distance from the origin to $ax+by=c$ is $\frac{|c|}{\sqrt{a^2+b^2}}$; tangency sets it equal to $r$."),

"CIR-14": Sol(
    idea=r"The angle in a semicircle is a right angle, so $AB$ is the hypotenuse of a right-angled triangle.",
    steps=[
        (r"$AB$ is a diameter and $C$ is on the circle, so angle $ACB = 90^\circ$.",
         r"The angle in a semicircle is a right angle - the key theorem here."),
        (r"Apply Pythagoras: $AB = \sqrt{6^2 + 8^2} = \sqrt{100} = 10$.",
         r"The right angle is at $C$, so the diameter $AB$ is the hypotenuse."),
        (r"Radius $= \frac{10}{2} = 5$.",
         r"The question asks for the radius, not the diameter."),
    ],
    pitfalls=[r"Answering $10$ (the diameter).",
              r"Assuming the right angle is at $A$ or $B$."],
    takeaway=r"A triangle inscribed with one side a diameter is right-angled at the third vertex."),

"CIR-15": Sol(
    idea=r"Three points determine a circle, but here two of the chords are along the axes - and the right angle at the origin gives the centre instantly.",
    steps=[
        (r"Notice the triangle $(0,0)$, $(6,0)$, $(0,8)$ has a right angle at the origin.",
         r"The two legs lie along the axes, so the angle between them is $90^\circ$."),
        (r"A right angle inscribed in a circle stands on a diameter, so the hypotenuse from $(6,0)$ to $(0,8)$ is a diameter.",
         r"This is the converse of the angle-in-a-semicircle theorem."),
        (r"The centre is the midpoint of that diameter: $\left(\frac{6+0}{2}, \frac{0+8}{2}\right) = (3, 4)$.",
         r"Centre is the midpoint of any diameter."),
    ],
    pitfalls=[r"Averaging all three points to get $(2, \frac83)$ - that is the centroid, not the circumcentre.",
              r"Taking the midpoint of the wrong pair, e.g. $(3,0)$."],
    takeaway=r"If three given points form a right angle, the hypotenuse is a diameter and its midpoint is the centre."),

"CIR-16": Sol(
    idea=r"A locus defined by a distance ratio. Write the condition algebraically, square to remove roots, and complete the square.",
    steps=[
        (r"Write the condition: $\sqrt{(x-3)^2 + y^2} = 2\sqrt{x^2 + y^2}$.",
         r"'Distance from $A$ is twice the distance from $B$' - write both distances with the formula."),
        (r"Square both sides: $(x-3)^2 + y^2 = 4(x^2 + y^2)$.",
         r"Squaring is safe because both sides are non-negative; and it removes both roots at once. Note the right-hand side gains a factor $4$, not $2$."),
        (r"Expand and collect: $x^2 - 6x + 9 + y^2 = 4x^2 + 4y^2 \Rightarrow 3x^2 + 3y^2 + 6x - 9 = 0$.",
         r"Bring everything to one side."),
        (r"Divide by $3$ and complete the square: $x^2 + 2x + y^2 = 3 \Rightarrow (x+1)^2 + y^2 = 4$, so $r = 2$.",
         r"Dividing by the common factor first makes the coefficients of $x^2$ and $y^2$ equal to $1$ - necessary before completing the square."),
    ],
    pitfalls=[r"Squaring the right side as $2(x^2+y^2)$ instead of $4(x^2+y^2)$.",
              r"Forgetting to divide by $3$ before completing the square, which corrupts the radius."],
    takeaway=r"Distance-ratio loci (Apollonius circles): square the condition, divide so $x^2$ and $y^2$ have coefficient $1$, then complete the square."),

}
