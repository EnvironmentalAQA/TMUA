"""Full teaching solutions: Pythagoras, mensuration and 3D (MEN-xx)."""
from gen.model import Sol

SOLUTIONS = {

"MEN-01": Sol(
    idea=r"The space diagonal of a cuboid: Pythagoras applied twice, which gives the three-dimensional formula.",
    steps=[
        (r"First find the diagonal of the base: $\sqrt{3^2 + 4^2} = 5$.",
         r"That is a 3-4-5 triangle - the base diagonal lies in a horizontal plane."),
        (r"Now use that with the height: $\sqrt{5^2 + 12^2} = \sqrt{169} = 13$.",
         r"The space diagonal, the base diagonal and the vertical edge form a second right-angled triangle. This is a 5-12-13 triple."),
        (r"Equivalently, $\sqrt{a^2+b^2+c^2} = \sqrt{9 + 16 + 144} = 13$ cm.",
         r"The two applications of Pythagoras combine into one formula."),
    ],
    pitfalls=[r"Using only two of the three dimensions, giving $5$ or $\sqrt{153}$.",
              r"Adding the lengths: $3 + 4 + 12 = 19$."],
    takeaway=r"Space diagonal $= \sqrt{a^2+b^2+c^2}$ - Pythagoras twice in one step."),

"MEN-02": Sol(
    idea=r"Use the volume condition to find $r$, then substitute into the surface-area formula. Both formulas must be recalled.",
    steps=[
        (r"Write the volume with $h = 2r$: $V = \pi r^2 h = \pi r^2 (2r) = 2\pi r^3$.",
         r"Substituting the relationship immediately reduces to one unknown."),
        (r"Solve $2\pi r^3 = 54\pi$: $r^3 = 27$, so $r = 3$ and $h = 6$.",
         r"The $\pi$ cancels, which is a good sign."),
        (r"Total surface area $= 2\pi r^2$ (two circular ends) $+\ 2\pi r h$ (curved surface).",
         r"'Total' means include both ends; 'curved surface area' would be just $2\pi rh$."),
        (r"Substitute: $2\pi(9) + 2\pi(3)(6) = 18\pi + 36\pi = 54\pi$.",
         r"Coincidentally equal to the volume's numerical value - a deliberate touch."),
    ],
    pitfalls=[r"Giving only the curved surface $36\pi$ - an offered option.",
              r"Forgetting that there are **two** circular ends."],
    takeaway=r"Cylinder: $V = \pi r^2h$, curved surface $2\pi rh$, total surface $2\pi r^2 + 2\pi rh$."),

"MEN-03": Sol(
    idea=r"Trapezium area formula, rearranged for the height.",
    steps=[
        (r"Write the formula: area $= \frac12(a + b)h$ where $a, b$ are the parallel sides.",
         r"The height is the **perpendicular** distance between the parallel sides."),
        (r"Substitute: $\frac12(8 + 14)h = 11h$.",
         r"$\frac12 \times 22 = 11$."),
        (r"Solve: $11h = 77$, so $h = 7$ cm.",
         r"Divide both sides by $11$."),
    ],
    pitfalls=[r"Forgetting the $\frac12$ and answering $3.5$ - an offered option.",
              r"Using the difference of the parallel sides instead of the sum."],
    takeaway=r"Trapezium: average the parallel sides, then multiply by the perpendicular height."),

"MEN-04": Sol(
    idea=r"The cone's slant height, radius and vertical height form a right-angled triangle. Find the height, then use the volume formula.",
    steps=[
        (r"Use Pythagoras: $h = \sqrt{l^2 - r^2} = \sqrt{100 - 36} = 8$ cm.",
         r"The slant height is the **hypotenuse**, so subtract; this is another 6-8-10 triangle."),
        (r"Apply the given formula: $V = \frac13\pi r^2 h = \frac13\pi(36)(8)$.",
         r"The formula is provided in the question, as the specification promises."),
        (r"Compute: $\frac13 \times 288 = 96$, so $V = 96\pi$ cm$^3$.",
         r"$36 \times 8 = 288$."),
    ],
    pitfalls=[r"Using the slant height as the vertical height, giving $120\pi$ - an offered option.",
              r"Forgetting the $\frac13$ and answering $288\pi$."],
    takeaway=r"Cone: slant$^2 = r^2 + h^2$; and the volume carries a factor of $\frac13$ compared with a cylinder."),

"MEN-05": Sol(
    idea=r"Equate the two volumes and solve for $r$ - an algebraic rearrangement with a cube root.",
    steps=[
        (r"Set the volumes equal: $\frac43\pi r^3 = a^3$.",
         r"The sphere's formula is given; the cube's is $a^3$."),
        (r"Isolate $r^3$: $r^3 = \dfrac{3a^3}{4\pi}$.",
         r"Multiply both sides by $\frac{3}{4\pi}$."),
        (r"Take the cube root: $r = a\sqrt[3]{\dfrac{3}{4\pi}}$.",
         r"The cube root of $a^3$ is $a$, and the constant keeps its cube root."),
    ],
    pitfalls=[r"Inverting the fraction, giving $a\sqrt[3]{\frac{4\pi}{3}}$ - an offered option.",
              r"Taking a square root instead of a cube root."],
    takeaway=r"Equate volumes, isolate $r^3$, then cube-root everything including the constant."),

"MEN-06": Sol(
    idea=r"A composite area: subtract the quarter-circle from the square.",
    steps=[
        (r"Square area: $10^2 = 100$.",
         r"Side squared."),
        (r"Quarter-circle area: $\frac14\pi r^2 = \frac14\pi(100) = 25\pi$.",
         r"The radius equals the side, and a quarter of a circle is $\frac14$ of $\pi r^2$."),
        (r"Subtract: $100 - 25\pi$.",
         r"Leave $\pi$ exact - no calculator is available anyway."),
    ],
    pitfalls=[r"Forgetting the quarter and subtracting $100\pi$, which would give a negative area.",
              r"Using $\frac14 \pi r$ (circumference) instead of area."],
    takeaway=r"Composite areas: subtract the parts, and check the answer is positive ($25\pi \approx 78.5 < 100$ ✓)."),

"MEN-07": Sol(
    idea=r"A ladder against a wall is a right-angled triangle with the ladder as hypotenuse.",
    steps=[
        (r"Identify the hypotenuse: the ladder, $6.5$ m - the longest side, opposite the right angle at the base of the wall.",
         r"The wall and ground are perpendicular."),
        (r"Apply Pythagoras: height $= \sqrt{6.5^2 - 2.5^2} = \sqrt{42.25 - 6.25}$.",
         r"Subtract, because we want a shorter side."),
        (r"Compute: $\sqrt{36} = 6$ m.",
         r"Decimals chosen to give a whole number - a sign the working is right."),
    ],
    pitfalls=[r"Adding the squares, giving $\sqrt{48.5}$ - an offered option.",
              r"Arithmetic: $6.5^2 = 42.25$, not $36.25$."],
    takeaway=r"Hypotenuse known $\Rightarrow$ subtract squares; hypotenuse unknown $\Rightarrow$ add them."),

"MEN-08": Sol(
    idea=r"Right-angled trigonometry to get the two legs, then the standard triangle area.",
    steps=[
        (r"The side opposite the $30^\circ$ angle: $10\sin 30^\circ = 10 \times \frac12 = 5$.",
         r"$\sin = \frac{\text{opposite}}{\text{hypotenuse}}$, so opposite $=$ hypotenuse $\times \sin$."),
        (r"The adjacent side: $10\cos 30^\circ = 10 \times \frac{\sqrt3}{2} = 5\sqrt3$.",
         r"Exact values must be recalled: $\cos 30^\circ = \frac{\sqrt3}{2}$."),
        (r"Area $= \frac12 \times$ base $\times$ height $= \frac12(5)(5\sqrt3) = \dfrac{25\sqrt3}{2}$.",
         r"The two legs are perpendicular, so they serve as base and height."),
    ],
    pitfalls=[r"Forgetting the $\frac12$, giving $25\sqrt3$ - an offered option.",
              r"Using the hypotenuse as one of the perpendicular sides."],
    takeaway=r"In a right-angled triangle the two legs are base and height; get them from $\sin$ and $\cos$ of the hypotenuse."),

"MEN-09": Sol(
    idea=r"Set the two expressions equal and solve. The equation is cubic but factorises immediately.",
    steps=[
        (r"Write both: volume $= a^3$, surface area $= 6a^2$ (six square faces).",
         r"A cube has six identical faces of area $a^2$."),
        (r"Set them equal: $a^3 = 6a^2$.",
         r"'Numerically equal' means the numbers match, though the units differ."),
        (r"Factorise rather than divide: $a^2(a - 6) = 0$, so $a = 0$ or $a = 6$. A cube must have $a > 0$, so $a = 6$.",
         r"Dividing by $a^2$ is fine here (a side length is non-zero), but factorising is the safer habit."),
    ],
    pitfalls=[r"Taking a square root somewhere and answering $\sqrt6$ - an offered option.",
              r"Using $4a^2$ or $a^2$ for the surface area."],
    takeaway=r"Cube: $V = a^3$, $S = 6a^2$; equate and factorise rather than dividing by a variable."),

"MEN-10": Sol(
    idea=r"The height of a pyramid, a slant edge and half the base diagonal form a right-angled triangle.",
    steps=[
        (r"Find the base diagonal: a square of side $6$ has diagonal $6\sqrt2$.",
         r"Pythagoras on the square base: $\sqrt{36 + 36} = 6\sqrt2$."),
        (r"Half of it is $3\sqrt2$ - the horizontal distance from the centre to a corner.",
         r"The apex sits above the centre of the base, so this is the horizontal leg."),
        (r"Apply Pythagoras with the slant edge as hypotenuse: $h^2 = 9^2 - (3\sqrt2)^2 = 81 - 18 = 63$.",
         r"$(3\sqrt2)^2 = 9 \times 2 = 18$ - square the coefficient too."),
        (r"So $h = \sqrt{63}$.",
         r"$= 3\sqrt7$, if you prefer it simplified."),
    ],
    pitfalls=[r"Using half the **side** ($3$) instead of half the diagonal, giving $\sqrt{72}$ - an offered option.",
              r"Computing $(3\sqrt2)^2$ as $6$ or $9$."],
    takeaway=r"For a slant **edge**, use half the base diagonal; for a slant **face height**, use half the base side."),

"MEN-11": Sol(
    idea=r"Three scaling claims. Each is checked by substituting the new dimensions into the formula.",
    steps=[
        (r"I: $C = 2\pi r$ is linear in $r$, so doubling $r$ doubles $C$. **True.**",
         r"Circumference scales with the first power of the radius."),
        (r"II: $V = \frac43\pi r^3$, so doubling $r$ multiplies the volume by $2^3 = 8$. **True.**",
         r"Volume scales with the cube."),
        (r"III: new volume $= \pi(2r)^2\left(\frac h2\right) = \pi(4r^2)\left(\frac h2\right) = 2\pi r^2 h$ - **double**, not unchanged. **False.**",
         r"The radius is squared, so doubling it quadruples that factor; halving the height only removes a factor of $2$."),
        (r"I and II only.",
         r"Match to the option list."),
    ],
    pitfalls=[r"Assuming the doubling and halving in III cancel - the radius is squared, so they do not.",
              r"Confusing area and volume scaling in II."],
    takeaway=r"Substitute the new dimensions into the formula; squared quantities change faster than linear ones."),

"MEN-12": Sol(
    idea=r"The two semicircular ends together make one full circle. Write the perimeter and solve.",
    steps=[
        (r"Total length $=$ two straights $+$ two semicircles $= 2(100) + 2\left(\pi r\right)$.",
         r"A semicircular arc has length $\pi r$; two of them make a full circumference $2\pi r$."),
        (r"Set up: $200 + 2\pi r = 400$.",
         r"Substitute the given total."),
        (r"Solve: $2\pi r = 200$, so $r = \dfrac{100}{\pi}$.",
         r"Divide by $2\pi$."),
    ],
    pitfalls=[r"Using $\pi r$ for both ends together, giving $\frac{200}{\pi}$ - an offered option.",
              r"Using the area formula instead of arc length."],
    takeaway=r"Two semicircles of the same radius make one circle: total arc $= 2\pi r$."),

"MEN-13": Sol(
    idea=r"A right angle in coordinate geometry means perpendicular gradients - the vertex of the right angle is the shared point.",
    steps=[
        (r"Compute the gradient of $AB$: $\dfrac{6-2}{4-1} = \dfrac43$.",
         r"The right angle is at $B$, so the two sides meeting there are $BA$ and $BC$."),
        (r"Perpendicular gradient for $BC$: $-\dfrac34$.",
         r"Negative reciprocal."),
        (r"Write the gradient of $BC$ using $C(k,2)$: $\dfrac{2 - 6}{k - 4} = \dfrac{-4}{k-4}$, and set it equal to $-\frac34$.",
         r"Keep the subtraction order consistent: from $B$ to $C$ in both coordinates."),
        (r"Solve: $\dfrac{-4}{k-4} = -\dfrac34 \Rightarrow 16 = 3(k-4) \Rightarrow k = 4 + \dfrac{16}{3} = \dfrac{28}{3}$.",
         r"Cross-multiply; both sides are negative so the signs cancel."),
    ],
    pitfalls=[r"Assuming the right angle is at $A$ or $C$.",
              r"Dropping the $+4$ at the end and answering $\frac{16}{3}$ - an offered option."],
    takeaway=r"Right angle at a named vertex: use the two sides **through that vertex** and set the gradient product to $-1$."),

"MEN-14": Sol(
    idea=r"Conservation of volume: the water keeps its volume, so equate the two cylinder volumes.",
    steps=[
        (r"Volume in the tin: $\pi r^2 h = \pi(16)(10) = 160\pi$.",
         r"$r = 4$ so $r^2 = 16$."),
        (r"In the jug the same volume occupies $\pi(25)h$.",
         r"Radius $5$, unknown depth $h$; the $\pi$ will cancel."),
        (r"Equate and solve: $160\pi = 25\pi h \Rightarrow h = \dfrac{160}{25} = 6.4$ cm.",
         r"The wider jug means a shallower depth - a good sanity check."),
    ],
    pitfalls=[r"Using the radii rather than their squares, giving $8$ cm - an offered option.",
              r"Expecting the depth to increase because the jug is 'bigger'."],
    takeaway=r"Pouring conserves volume: equate $\pi r_1^2h_1 = \pi r_2^2h_2$; a wider container gives a shallower depth."),

"MEN-15": Sol(
    idea=r"A composite solid: add the two volumes, halving the sphere formula for the hemisphere.",
    steps=[
        (r"Cylinder: $\pi r^2 h = \pi(9)(4) = 36\pi$.",
         r"$r = 3$, $h = 4$."),
        (r"Hemisphere: half a sphere, $\frac12 \times \frac43\pi r^3 = \frac23\pi(27) = 18\pi$.",
         r"$\frac23 \times 27 = 18$; the sphere formula is given if needed."),
        (r"Add: $36\pi + 18\pi = 54\pi$.",
         r"The solids sit on top of each other, so volumes simply add."),
    ],
    pitfalls=[r"Using the full sphere, giving $72\pi$ - an offered option.",
              r"Computing $r^3$ as $9$ instead of $27$."],
    takeaway=r"Composite solids: compute each piece separately and add; a hemisphere is exactly half a sphere."),

"MEN-16": Sol(
    idea=r"An angle of depression from the top equals the angle of elevation from the boat. Then it is right-angled trigonometry.",
    steps=[
        (r"Draw the triangle: the cliff is vertical ($40$ m), the sea horizontal, and the angle at the boat is $30^\circ$.",
         r"The angle of depression from the cliff top equals the angle of elevation from the boat (alternate angles with the horizontal)."),
        (r"Relative to the $30^\circ$ angle, the cliff is opposite and the distance $d$ is adjacent: $\tan 30^\circ = \dfrac{40}{d}$.",
         r"$\tan = \frac{\text{opposite}}{\text{adjacent}}$."),
        (r"Solve: $d = \dfrac{40}{\tan 30^\circ} = \dfrac{40}{1/\sqrt3} = 40\sqrt3$ m.",
         r"Dividing by $\frac{1}{\sqrt3}$ multiplies by $\sqrt3$."),
    ],
    pitfalls=[r"Multiplying by $\tan 30^\circ$ instead of dividing, giving $\frac{40}{\sqrt3}$ - an offered option.",
              r"Placing the $30^\circ$ angle at the top of the cliff inside the triangle, which would swap opposite and adjacent."],
    takeaway=r"Depression from the top $=$ elevation from the bottom; a shallow angle means a large horizontal distance."),

}
