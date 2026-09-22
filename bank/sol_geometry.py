"""Full teaching solutions: angles, polygons, congruence, transformations and vectors (GEO-xx)."""
from gen.model import Sol

SOLUTIONS = {

"GEO-01": Sol(
    idea=r"Work with the **exterior** angle: they always sum to $360^\circ$, which makes the arithmetic trivial.",
    steps=[
        (r"Exterior angle $= 180^\circ - 156^\circ = 24^\circ$.",
         r"Interior and exterior angles at a vertex lie on a straight line."),
        (r"The exterior angles of any polygon sum to $360^\circ$, and for a regular polygon they are all equal.",
         r"Walking once around the shape turns you through a full circle."),
        (r"Number of sides $= \dfrac{360}{24} = 15$.",
         r"Divide the total turn by the turn per vertex."),
    ],
    pitfalls=[r"Using $\frac{360}{156}$ or $\frac{156}{24}$.",
              r"Using the interior-angle-sum formula and then having to solve $\frac{180(n-2)}{n} = 156$ - correct but slower."],
    takeaway=r"For regular polygons, go via the exterior angle: $n = \frac{360}{\text{exterior}}$."),

"GEO-02": Sol(
    idea=r"Direct application of the interior-angle-sum formula.",
    steps=[
        (r"Recall the formula: the interior angles of an $n$-gon sum to $180(n-2)^\circ$.",
         r"The polygon splits into $n - 2$ triangles, each contributing $180^\circ$."),
        (r"Set up: $180(n - 2) = 1980$.",
         r"Substitute the given total."),
        (r"Divide: $n - 2 = 11$, so $n = 13$.",
         r"$1980 \div 180 = 11$; remember to add the $2$ back."),
    ],
    pitfalls=[r"Forgetting to add $2$ and answering $11$ - an offered option.",
              r"Using $180n$ instead of $180(n-2)$."],
    takeaway=r"Interior sum $= 180(n-2)$: divide, then add $2$."),

"GEO-03": Sol(
    idea=r"Column-vector arithmetic: operate on each component separately.",
    steps=[
        (r"Double $\mathbf a$: $2\binom{2}{-1} = \binom{4}{-2}$.",
         r"A scalar multiplies both components."),
        (r"Subtract $\mathbf b$ component by component: $\binom{4 - (-3)}{-2 - 4}$.",
         r"Subtracting a negative adds - the top component becomes $4 + 3$."),
        (r"Simplify: $\binom{7}{-6}$.",
         r"Both components computed independently."),
    ],
    pitfalls=[r"Adding $\mathbf b$ instead of subtracting, giving $\binom{1}{2}$ - an offered option.",
              r"Getting the sign of the bottom component wrong: $-2 - 4 = -6$, not $+2$."],
    takeaway=r"Vectors combine component by component; watch double negatives."),

"GEO-04": Sol(
    idea=r"Vector geometry: build a route from $A$ to $P$ out of the known vectors, using the ratio to fix the fraction.",
    steps=[
        (r"Find $\overrightarrow{OM}$: $M$ is the midpoint of $AB$, so $\overrightarrow{OM} = \frac12(\mathbf a + \mathbf b)$.",
         r"The midpoint of $AB$ is the average of the two position vectors."),
        (r"Use the ratio $OP : PM = 2 : 1$: $P$ is $\frac23$ of the way from $O$ to $M$, so $\overrightarrow{OP} = \frac23 \times \frac12(\mathbf a + \mathbf b) = \frac13(\mathbf a + \mathbf b)$.",
         r"$2 : 1$ means $2$ parts out of $3$ - convert the ratio into a fraction of the whole."),
        (r"Travel from $A$ to $P$ via $O$: $\overrightarrow{AP} = \overrightarrow{AO} + \overrightarrow{OP} = -\mathbf a + \frac13(\mathbf a + \mathbf b)$.",
         r"$\overrightarrow{AO} = -\overrightarrow{OA} = -\mathbf a$; reversing a vector negates it."),
        (r"Simplify: $-\mathbf a + \frac13\mathbf a + \frac13\mathbf b = \frac13\mathbf b - \frac23\mathbf a$.",
         r"Collect the $\mathbf a$ terms: $-1 + \frac13 = -\frac23$."),
    ],
    pitfalls=[r"Using $\frac12$ instead of $\frac23$ for the ratio point.",
              r"Forgetting the $-\mathbf a$ and giving $\overrightarrow{OP}$ instead of $\overrightarrow{AP}$ - an offered option."],
    takeaway=r"Route vectors: $\overrightarrow{XY} = \overrightarrow{XO} + \overrightarrow{OY}$, and a ratio $m : n$ means the fraction $\frac{m}{m+n}$."),

"GEO-05": Sol(
    idea=r"Similar shapes: areas scale as the **square** of the length ratio.",
    steps=[
        (r"Length scale factor: $\dfrac96 = \dfrac32$.",
         r"From the smaller to the larger, so the factor is greater than $1$."),
        (r"Area scale factor: $\left(\dfrac32\right)^2 = \dfrac94$.",
         r"Both dimensions scale, so the area scales by the square."),
        (r"Multiply: $20 \times \dfrac94 = 45$ cm$^2$.",
         r"$20 \div 4 = 5$, then $\times 9$."),
    ],
    pitfalls=[r"Using the length factor directly: $20 \times \frac32 = 30$ - an offered option.",
              r"Cubing (that would be for volumes), giving $67.5$."],
    takeaway=r"Area ratio $=$ (length ratio)$^2$; check the direction of the scale factor."),

"GEO-06": Sol(
    idea=r"A bearings problem with a right angle. Find the shape of the triangle, then work out the bearing and reverse it.",
    steps=[
        (r"The bearing changes from $060^\circ$ to $150^\circ$, a turn of $90^\circ$, so the path turns through a right angle at $Q$.",
         r"The interior angle $PQR$ is therefore $90^\circ$."),
        (r"Both legs are $10$ km, so triangle $PQR$ is right-angled **isosceles**, with the two base angles $45^\circ$ each.",
         r"Equal legs give equal base angles, each $\frac{180 - 90}{2} = 45^\circ$."),
        (r"Bearing of $R$ from $P$: the direction $PQ$ is $060^\circ$, and $PR$ is $45^\circ$ further clockwise, so $060 + 45 = 105^\circ$.",
         r"$R$ lies on the far side of $PQ$ from north, so add."),
        (r"Reverse for the bearing of $P$ from $R$: add $180^\circ$ to get $285^\circ$.",
         r"Back bearings differ by $180^\circ$ (add if under $180^\circ$, subtract if over)."),
    ],
    pitfalls=[r"Giving $105^\circ$, which is the bearing of $R$ from $P$ - the reverse of what is asked (and an offered option).",
              r"Subtracting $180^\circ$ and getting a negative, or forgetting three-figure form."],
    takeaway=r"Bearings are clockwise from north; a back bearing differs by exactly $180^\circ$."),

"GEO-07": Sol(
    idea=r"Enlargement with a negative scale factor about the origin: multiply every coordinate by that factor.",
    steps=[
        (r"With centre the origin, enlargement by $k$ sends $(x,y)$ to $(kx, ky)$.",
         r"Position vectors scale directly when the centre is the origin."),
        (r"Apply $k = -2$ to each vertex: $(1,1) \to (-2,-2)$; $(3,1) \to (-6,-2)$; $(1,4) \to (-2,-8)$.",
         r"A negative factor also rotates the shape through $180^\circ$ - the image is on the opposite side of the origin."),
        (r"Check the options: $(-2,-8)$ appears.",
         r"Match against the computed image vertices."),
    ],
    pitfalls=[r"Using $+2$ and choosing $(2,8)$ - an offered option.",
              r"Multiplying only one coordinate."],
    takeaway=r"Enlargement about the origin: multiply both coordinates by $k$; a negative $k$ flips the shape through the centre."),

"GEO-08": Sol(
    idea=r"The four congruence criteria are SSS, SAS, ASA and RHS. Anything else - notably SSA - is not sufficient.",
    steps=[
        (r"Recall the valid criteria: SSS, SAS, ASA (or AAS), RHS.",
         r"These four are the ones that fix a triangle completely."),
        (r"Consider SSA: two sides and a **non-included** angle. This is the ambiguous case of the sine rule, where two different triangles can share the same data.",
         r"The side opposite the known angle can 'swing' to two positions - exactly the situation in TRI-07."),
        (r"So SSA is the odd one out.",
         r"RHS is really a special case of SSA that works, because the right angle removes the ambiguity."),
    ],
    pitfalls=[r"Thinking RHS is invalid because it looks like SSA - the right angle makes it unambiguous.",
              r"Confusing AAA (similar but not congruent) with ASA."],
    takeaway=r"SSS, SAS, ASA, RHS prove congruence; SSA does not, and AAA gives only similarity."),

"GEO-09": Sol(
    idea=r"Co-interior (allied) angles between parallel lines add to $180^\circ$.",
    steps=[
        (r"Identify the relationship: co-interior angles lie on the same side of the transversal, between the parallel lines.",
         r"Their names matter: alternate angles are equal, corresponding angles are equal, co-interior angles are supplementary."),
        (r"Write the equation: $(3x + 10) + (2x - 5) = 180$.",
         r"Supplementary means summing to $180^\circ$."),
        (r"Simplify: $5x + 5 = 180$, so $5x = 175$ and $x = 35$.",
         r"Combine like terms, then divide."),
    ],
    pitfalls=[r"Setting the angles equal (treating them as alternate), which gives $x = 15$ - an offered option.",
              r"Arithmetic: $10 - 5 = 5$, not $15$."],
    takeaway=r"With parallel lines: alternate equal, corresponding equal, co-interior sum to $180^\circ$."),

"GEO-10": Sol(
    idea=r"Quadrilateral classification. Each claim is about whether one family is contained in another.",
    steps=[
        (r"I: a rhombus has two pairs of parallel sides, which is the definition of a parallelogram. **True.**",
         r"Rhombus $=$ parallelogram with all sides equal, so it is a special parallelogram."),
        (r"II: a rectangle has equal **angles** but not necessarily equal sides - a $2 \times 5$ rectangle is not a rhombus. **False.**",
         r"Only the square lies in both families."),
        (r"III: a kite's diagonals meet at right angles (the axis of symmetry bisects the other diagonal perpendicularly). **True.**",
         r"This is a standard kite property."),
        (r"I and III only.",
         r"Match to the option list."),
    ],
    pitfalls=[r"Reversing II: every rhombus is not a rectangle either, but the claim as stated is about rectangles.",
              r"Thinking a kite's diagonals **bisect** each other - only one bisects the other."],
    takeaway=r"Square $=$ rectangle $\cap$ rhombus; kites have perpendicular diagonals but only one is bisected."),

"GEO-11": Sol(
    idea=r"Collinear points mean one vector is a scalar multiple of the other. Compare coefficients of the two independent directions.",
    steps=[
        (r"Collinear $A$, $B$, $C$ means $\overrightarrow{BC} = \lambda\overrightarrow{AB}$ for some scalar $\lambda$.",
         r"They share the point $B$, so the two vectors must point along the same line."),
        (r"Write it out: $k\mathbf p - 4\mathbf q = \lambda(3\mathbf p + 2\mathbf q)$.",
         r"Because $\mathbf p$ and $\mathbf q$ are not parallel, coefficients can be compared independently."),
        (r"Compare $\mathbf q$: $-4 = 2\lambda$, so $\lambda = -2$.",
         r"Use the equation that contains no unknown besides $\lambda$."),
        (r"Compare $\mathbf p$: $k = 3\lambda = -6$.",
         r"Substitute the value of $\lambda$."),
    ],
    pitfalls=[r"Taking $\lambda = 2$ and answering $6$ - an offered option.",
              r"Comparing $\mathbf p$ with $\mathbf q$ coefficients."],
    takeaway=r"Non-parallel vectors are independent: equate their coefficients separately to solve for scalars."),

"GEO-12": Sol(
    idea=r"Two transformations in sequence. Apply each rule in the stated order to the coordinates.",
    steps=[
        (r"Reflection in $y = x$ swaps the coordinates: $(3,1) \to (1,3)$.",
         r"The line $y = x$ exchanges the roles of the two axes."),
        (r"Rotation $90^\circ$ anticlockwise about the origin sends $(x,y) \to (-y,x)$.",
         r"Worth memorising; check it on $(1,0) \to (0,1)$ ✓."),
        (r"Apply it: $(1,3) \to (-3,1)$.",
         r"Here $x = 1$, $y = 3$, so the image is $(-3, 1)$."),
    ],
    pitfalls=[r"Applying the transformations in the wrong order.",
              r"Using the clockwise rule $(x,y) \to (y,-x)$, giving $(3,-1)$ - an offered option."],
    takeaway=r"Anticlockwise $90^\circ$: $(x,y) \to (-y,x)$. Clockwise: $(x,y) \to (y,-x)$. Order matters."),

"GEO-13": Sol(
    idea=r"Express all three angles in terms of one, then use the angle sum of a triangle.",
    steps=[
        (r"Let angle $B = b$. Then $A = 2b$ and $C = A + 20 = 2b + 20$.",
         r"Express everything in terms of the angle being asked for."),
        (r"Angle sum: $b + 2b + (2b + 20) = 180$.",
         r"The three angles of a triangle sum to $180^\circ$."),
        (r"Simplify: $5b + 20 = 180$, so $5b = 160$ and $b = 32^\circ$.",
         r"Check: $32 + 64 + 84 = 180$ ✓."),
    ],
    pitfalls=[r"Setting $C = 2b + 20$ but forgetting that $C$ is $20$ more than $A$, not than $B$.",
              r"Arithmetic: $180 - 20 = 160$, not $200$."],
    takeaway=r"Name one angle, express the rest in terms of it, then use the $180^\circ$ sum."),

"GEO-14": Sol(
    idea=r"A line parallel to one side creates a similar triangle. Use the **full** side, not just the part.",
    steps=[
        (r"$DE \parallel BC$ makes triangles $ADE$ and $ABC$ similar (equal corresponding angles).",
         r"Parallel lines give equal corresponding angles, which is the AAA similarity condition."),
        (r"Compute the ratio: $AB = AD + DB = 4 + 6 = 10$, so $AD : AB = 4 : 10 = 2 : 5$.",
         r"The ratio must compare corresponding **whole** sides - $AD$ to $AB$, not $AD$ to $DB$."),
        (r"Scale up $DE$: $BC = 5 \times \dfrac{10}{4} = 12.5$.",
         r"Multiply by the reciprocal of the ratio to go from small to large."),
    ],
    pitfalls=[r"Using the ratio $4 : 6$ and answering $7.5$ - an offered option.",
              r"Dividing instead of multiplying, giving $2$."],
    takeaway=r"In similar triangles compare corresponding **full** sides: $\frac{AD}{AB}$, not $\frac{AD}{DB}$."),

"GEO-15": Sol(
    idea=r"Angles at a point sum to $360^\circ$. Find each polygon's interior angle and subtract.",
    steps=[
        (r"Hexagon interior angle: exterior $= \frac{360}{6} = 60^\circ$, so interior $= 120^\circ$.",
         r"Regular polygon: interior $= 180 - \frac{360}{n}$."),
        (r"Octagon interior angle: exterior $= \frac{360}{8} = 45^\circ$, so interior $= 135^\circ$.",
         r"Same formula with $n = 8$."),
        (r"At the shared vertex three angles meet and fill a full turn: $120 + 135 + x = 360$.",
         r"The two interior angles plus the gap between the outer sides make a complete revolution."),
        (r"Solve: $x = 360 - 255 = 105^\circ$.",
         r"That gap is the angle asked for."),
    ],
    pitfalls=[r"Using $180^\circ$ instead of $360^\circ$ at the vertex.",
              r"Using exterior angles in the sum, giving $255^\circ$ or similar."],
    takeaway=r"Regular $n$-gon interior angle $= 180 - \frac{360}{n}$; angles round a point total $360^\circ$."),

}
