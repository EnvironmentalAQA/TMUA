"""Full teaching solutions: triangles, radians and sectors (TRI-xx)."""
from gen.model import Sol

SOLUTIONS = {

"TRI-01": Sol(
    idea=r"Two sides and the angle between them: that is exactly the cosine rule's input.",
    steps=[
        (r"Choose the rule: you know two sides and the **included** angle, so use the cosine rule, not the sine rule.",
         r"The sine rule needs a side opposite a known angle; here the known angle sits between the known sides."),
        (r"Write it with $BC$ opposite the known angle $A$: $BC^2 = AB^2 + AC^2 - 2(AB)(AC)\cos A$.",
         r"The side being found must be opposite the angle being used."),
        (r"Substitute, using $\cos 60^\circ = \frac12$: $BC^2 = 25 + 64 - 2(5)(8)\left(\frac12\right) = 89 - 40 = 49$.",
         r"$\cos 60^\circ = \frac12$ is one of the exact values you must recall."),
        (r"Take the square root: $BC = 7$.",
         r"Lengths are positive, so only the positive root."),
    ],
    pitfalls=[r"Forgetting the $-2bc\cos A$ term and answering $\sqrt{89}$ - which is offered.",
              r"Using $\cos 60^\circ = \frac{\sqrt3}{2}$ (that is $\cos 30^\circ$), giving $\sqrt{89 - 40\sqrt3}$."],
    takeaway=r"Two sides plus the included angle $\Rightarrow$ cosine rule; the unknown side is opposite the known angle."),

"TRI-02": Sol(
    idea=r"Three sides given, an angle wanted: the rearranged cosine rule. The word 'largest' tells you which angle.",
    steps=[
        (r"Identify the largest angle: it is opposite the longest side, $6$.",
         r"In any triangle the ordering of sides matches the ordering of opposite angles."),
        (r"Use $\cos\theta = \dfrac{a^2 + b^2 - c^2}{2ab}$ with $a = 4$, $b = 5$, $c = 6$.",
         r"The **two** sides adjacent to the angle go on the bottom; the opposite side is the one subtracted on top."),
        (r"Substitute: $\dfrac{16 + 25 - 36}{2(4)(5)} = \dfrac{5}{40} = \dfrac18$.",
         r"Positive, so the largest angle is acute - this triangle has no obtuse angle at all."),
    ],
    pitfalls=[r"Putting the longest side on the bottom, giving $\frac{9}{16}$ or similar.",
              r"Assuming the largest angle must be obtuse and choosing $-\frac18$."],
    takeaway=r"$\cos\theta = \frac{a^2+b^2-c^2}{2ab}$ with $c$ opposite $\theta$; a positive result means an acute angle."),

"TRI-03": Sol(
    idea=r"Sector area gives the angle; the angle gives the arc length. Both formulas need radians.",
    steps=[
        (r"Use the sector area formula $A = \frac12 r^2\theta$: $\frac12(36)\theta = 18\theta$.",
         r"$r = 6$, so $\frac12 r^2 = 18$. The formula is only valid with $\theta$ in radians."),
        (r"Set equal to the given area: $18\theta = 15\pi$, so $\theta = \dfrac{5\pi}{6}$.",
         r"Divide: $\frac{15\pi}{18} = \frac{5\pi}{6}$."),
        (r"Use the arc-length formula $s = r\theta = 6 \times \dfrac{5\pi}{6} = 5\pi$ cm.",
         r"The $6$ cancels neatly - a sign the angle is right."),
    ],
    pitfalls=[r"Quoting the angle $\frac{5\pi}{6}$ as the arc length - it is offered as a distractor.",
              r"Using $A = r^2\theta$ without the $\frac12$, which halves the angle and gives $\frac{5\pi}{2}$."],
    takeaway=r"$A = \frac12 r^2\theta$ and $s = r\theta$ (radians): find $\theta$ from one, then substitute into the other."),

"TRI-04": Sol(
    idea=r"Area gives $\sin P$, which has two possible angles. The word 'obtuse' picks the right one, and then the cosine rule finishes.",
    steps=[
        (r"Use area $= \frac12 ab\sin C$: $\frac12(8)(5)\sin P = 10\sqrt3$, so $20\sin P = 10\sqrt3$ and $\sin P = \dfrac{\sqrt3}{2}$.",
         r"The formula uses the angle **between** the two sides, which is $QPR$ here."),
        (r"$\sin P = \frac{\sqrt3}{2}$ gives $P = 60^\circ$ or $P = 120^\circ$; the obtuse condition selects $P = 120^\circ$.",
         r"$\sin\theta = \sin(180^\circ - \theta)$: a sine value never determines the angle by itself."),
        (r"Apply the cosine rule with $\cos 120^\circ = -\frac12$: $QR^2 = 64 + 25 - 2(8)(5)\left(-\frac12\right) = 89 + 40 = 129$.",
         r"A negative cosine turns the subtraction into an addition, making the opposite side longer - which is what an obtuse angle should do."),
        (r"So $QR = \sqrt{129}$.",
         r"Left in surd form; no calculator is available anyway."),
    ],
    pitfalls=[r"Taking $P = 60^\circ$ and answering $7$ - the value the question's 'obtuse' is designed to exclude.",
              r"Using $\cos 120^\circ = +\frac12$, giving $\sqrt{49}$."],
    takeaway=r"$\sin\theta$ always allows two angles; use any stated acute/obtuse condition, and remember $\cos$ is negative for obtuse angles."),

"TRI-05": Sol(
    idea=r"Degree-to-radian conversion: multiply by $\frac{\pi}{180}$, or spot the fraction of $180^\circ$.",
    steps=[
        (r"Express $135$ as a fraction of $180$: $\dfrac{135}{180} = \dfrac34$.",
         r"Since $180^\circ = \pi$ radians, the same fraction of $\pi$ gives the answer."),
        (r"So $135^\circ = \dfrac34 \pi = \dfrac{3\pi}{4}$.",
         r"Equivalently $135 \times \frac{\pi}{180} = \frac{3\pi}{4}$."),
    ],
    pitfalls=[r"Multiplying by $\frac{180}{\pi}$ (the reverse conversion).",
              r"Simplifying $\frac{135}{180}$ incorrectly to $\frac23$ or $\frac56$, both of which are offered."],
    takeaway=r"$180^\circ = \pi$: convert by multiplying by $\frac{\pi}{180}$, and cancel the fraction fully."),

"TRI-06": Sol(
    idea=r"Segment $=$ sector $-$ triangle. Compute the two areas and subtract; both use the same $r$ and $\theta$.",
    steps=[
        (r"Sector area: $\frac12 r^2\theta = \frac12(16)\left(\frac{\pi}{3}\right) = \dfrac{8\pi}{3}$.",
         r"$r = 4$ so $r^2 = 16$; the angle is already in radians."),
        (r"Triangle area (two radii and the chord): $\frac12 r^2\sin\theta = \frac12(16)\sin\frac{\pi}{3} = 8 \times \dfrac{\sqrt3}{2} = 4\sqrt3$.",
         r"Use $\frac12 ab\sin C$ with both sides equal to the radius."),
        (r"Subtract: segment $= \dfrac{8\pi}{3} - 4\sqrt3$.",
         r"The minor segment is the bit of the sector left over once the triangle is removed."),
    ],
    pitfalls=[r"Forgetting the $\frac12$ in the triangle area, giving $\frac{8\pi}{3} - 8\sqrt3$ (an offered option), which is negative.",
              r"Using $\sin\frac{\pi}{3} = \frac12$."],
    takeaway=r"Segment area $= \frac12 r^2(\theta - \sin\theta)$ - sector minus triangle, all in radians."),

"TRI-07": Sol(
    idea=r"Side-side-angle data: the ambiguous case. Compute $\sin C$, then decide whether both the acute and obtuse angles give a valid triangle.",
    steps=[
        (r"Apply the sine rule: $\dfrac{\sin C}{AB} = \dfrac{\sin A}{BC}$, i.e. $\dfrac{\sin C}{6} = \dfrac{\sin 30^\circ}{4}$.",
         r"Pair each angle with the side opposite it: $C$ is opposite $AB = 6$, and $A$ is opposite $BC = 4$."),
        (r"Solve: $\sin C = \dfrac{6 \times 0.5}{4} = \dfrac34$, which is less than $1$, so solutions exist.",
         r"If $\sin C$ came out greater than $1$, no triangle would exist at all."),
        (r"Both $C = \arcsin\frac34$ and $180^\circ - \arcsin\frac34$ are possible in principle; check whether the obtuse one still leaves a positive third angle.",
         r"$\arcsin\frac34 \approx 48.6^\circ$, so the obtuse option is about $131.4^\circ$; with $A = 30^\circ$ that totals under $180^\circ$ ✓."),
        (r"Equivalently: the side opposite the given angle ($4$) is shorter than the other given side ($6$) but longer than $6\sin30^\circ = 3$ - the classic two-triangle condition. So there are **2** triangles.",
         r"The condition $b\sin A < a < b$ is the standard test for the ambiguous case."),
    ],
    pitfalls=[r"Assuming one triangle because the sine rule 'gives one answer'.",
              r"Assuming two triangles always - if $a \geq b$ the obtuse option would make the angles exceed $180^\circ$."],
    takeaway=r"SSA data: with $b\sin A < a < b$ there are two triangles; with $a \geq b$ exactly one; with $a < b\sin A$ none."),

"TRI-08": Sol(
    idea=r"Two sector facts, two unknowns. Eliminate $\theta$ by substitution and solve the resulting quadratic in $r$.",
    steps=[
        (r"Perimeter of a sector $=$ two radii $+$ arc: $2r + r\theta = 20$.",
         r"Students often forget the two straight edges - the perimeter is not just the arc."),
        (r"Rearrange for the arc: $r\theta = 20 - 2r$.",
         r"Keeping the product $r\theta$ together is the key, because the area formula contains it."),
        (r"Area: $\frac12 r^2\theta = \frac12 r(r\theta) = \frac12 r(20 - 2r) = 16$.",
         r"Writing $r^2\theta$ as $r \times (r\theta)$ lets you substitute directly - no need to find $\theta$."),
        (r"Simplify and solve: $10r - r^2 = 16 \Rightarrow r^2 - 10r + 16 = 0 \Rightarrow (r-2)(r-8) = 0$, so $r = 2$ or $8$.",
         r"Both are geometrically valid: $r = 2$ gives $\theta = 8$ radians... which exceeds $2\pi$, but the question asks only for the values of $r$ from the equations."),
    ],
    pitfalls=[r"Using perimeter $= r\theta$ alone, which gives a different quadratic.",
              r"Finding only one root of the quadratic."],
    takeaway=r"Substitute the product $r\theta$ as a block; sector perimeter is $2r + r\theta$."),

"TRI-09": Sol(
    idea=r"Cosine rule with a negative cosine. The only difficulty is handling the double negative.",
    steps=[
        (r"Write the rule: $c^2 = 3^2 + 5^2 - 2(3)(5)\cos\theta$.",
         r"Two sides and the included angle again."),
        (r"Substitute $\cos\theta = -\frac15$: $c^2 = 9 + 25 - 30\left(-\frac15\right) = 34 + 6$.",
         r"Subtracting a negative adds: $-30 \times (-\frac15) = +6$."),
        (r"So $c^2 = 40$ and $c = \sqrt{40}$.",
         r"Leave it in surd form; $\sqrt{40} = 2\sqrt{10}$ if you prefer."),
    ],
    pitfalls=[r"Getting $34 - 6 = 28$ by mishandling the sign, which is offered as $\sqrt{28}$.",
              r"Forgetting the angle is obtuse, so the third side must be **longer** than $\sqrt{34}$ - a useful sanity check."],
    takeaway=r"A negative cosine makes the third side longer than Pythagoras would give; check your answer against $\sqrt{a^2+b^2}$."),

"TRI-10": Sol(
    idea=r"A ratio of sines is a ratio of sides (sine rule). Then the cosine rule finds the angle.",
    steps=[
        (r"By the sine rule, $a : b : c = \sin A : \sin B : \sin C = 3 : 5 : 7$.",
         r"$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$ means sides are proportional to the sines of opposite angles."),
        (r"Take the sides as $3k, 5k, 7k$; the $k$ will cancel, so use $3, 5, 7$.",
         r"Only the shape matters for angles, so the scale factor is irrelevant."),
        (r"Apply the cosine rule for the angle opposite $7$: $\cos C = \dfrac{9 + 25 - 49}{2(3)(5)} = \dfrac{-15}{30} = -\dfrac12$.",
         r"$C$ is opposite the largest side, so expect the largest angle."),
        (r"$\cos C = -\frac12$ gives $C = 120^\circ$.",
         r"One of the exact values: $\cos 120^\circ = -\cos 60^\circ = -\frac12$."),
    ],
    pitfalls=[r"Treating $3:5:7$ as the angles themselves, giving $84^\circ$.",
              r"Reading $\cos C = -\frac12$ as $60^\circ$ and ignoring the sign."],
    takeaway=r"Sines in ratio $\Rightarrow$ sides in the same ratio; then use the cosine rule with any convenient multiple."),

"TRI-11": Sol(
    idea=r"Equate two area expressions. The radius cancels, leaving an equation for $\theta$ alone.",
    steps=[
        (r"Segment area for a right angle at the centre: $\frac12 r^2\left(\frac{\pi}{2} - \sin\frac{\pi}{2}\right) = \frac12 r^2\left(\frac{\pi}{2} - 1\right)$.",
         r"Segment $=$ sector $-$ triangle $= \frac12 r^2\theta - \frac12 r^2\sin\theta$, and $\sin\frac\pi2 = 1$."),
        (r"Sector area for angle $\theta$: $\frac12 r^2\theta$.",
         r"Same radius, different angle."),
        (r"Set them equal: $\frac12 r^2\theta = \frac12 r^2\left(\frac\pi2 - 1\right)$.",
         r"Both areas are in the same circle, so $r$ is common."),
        (r"Cancel $\frac12 r^2$: $\theta = \dfrac{\pi}{2} - 1$.",
         r"The answer is independent of $r$, which is why the question never tells you its value."),
    ],
    pitfalls=[r"Using $\sin\frac\pi2 = 0$ and answering $\frac\pi2$.",
              r"Forgetting to cancel and leaving an $r$ in the answer."],
    takeaway=r"When two areas in the same circle are equated, $r$ cancels - the answer depends only on the angles."),

"TRI-12": Sol(
    idea=r"A condition on the sides. The cosine rule converts it into a statement about an angle; then test the third claim with a counterexample.",
    steps=[
        (r"I: $\cos C = \dfrac{a^2+b^2-c^2}{2ab}$, and $a^2 + b^2 < c^2$ makes the numerator negative, so $\cos C < 0$ and $C$ is obtuse. **True.**",
         r"The denominator $2ab$ is positive, so the sign of $\cos C$ is the sign of $a^2 + b^2 - c^2$."),
        (r"II: a triangle can have at most one obtuse angle, and the largest angle is opposite the largest side. Since $C$ is obtuse it is the largest angle, so $c$ is the longest side. **True.**",
         r"Two obtuse angles would already exceed $180^\circ$."),
        (r"III: try $a = b = 1$ and $c = 1.5$: then $a^2 + b^2 = 2 < 2.25 = c^2$ ✓ and the triangle is isosceles. **False.**",
         r"A single counterexample kills the claim. Check the triangle inequality too: $1 + 1 > 1.5$ ✓."),
        (r"I and II only.",
         r"Match to the option list."),
    ],
    pitfalls=[r"Assuming an obtuse triangle cannot be isosceles.",
              r"Forgetting to check the triangle inequality when constructing a counterexample."],
    takeaway=r"$a^2+b^2 < c^2$ $\Leftrightarrow$ the angle opposite $c$ is obtuse; obtuse triangles can still be isosceles."),

"TRI-13": Sol(
    idea=r"Distance travelled by a rotating tip is arc length. Find the fraction of a full turn, then multiply by the circumference.",
    steps=[
        (r"Find the fraction of a revolution: $\dfrac{25}{60} = \dfrac{5}{12}$.",
         r"The minute hand takes $60$ minutes for one full turn."),
        (r"Compute the full circumference: $2\pi r = 2\pi(12) = 24\pi$ cm.",
         r"The tip traces a circle of radius equal to the hand's length."),
        (r"Multiply: $\dfrac{5}{12} \times 24\pi = 10\pi$ cm.",
         r"Equivalently, $\theta = \frac{5}{12}\times 2\pi = \frac{5\pi}{6}$ and $s = r\theta = 12 \times \frac{5\pi}{6} = 10\pi$."),
    ],
    pitfalls=[r"Using the radius as the distance, or the area formula instead of arc length.",
              r"Using $\frac{25}{12}$ or $\frac{25}{60}$ of the **radius** rather than the circumference."],
    takeaway=r"Arc length $=$ (fraction of a turn) $\times 2\pi r$; a clock hand makes one turn per hour."),

"TRI-14": Sol(
    idea=r"Two right-angled triangles sharing the same height. Express both base lengths in terms of $h$ and use the given difference.",
    steps=[
        (r"From $A$: $\tan 30^\circ = \dfrac{h}{AB}$, so $AB = \dfrac{h}{\tan 30^\circ} = h\sqrt3$.",
         r"$\tan 30^\circ = \frac{1}{\sqrt3}$, so dividing by it multiplies by $\sqrt3$."),
        (r"From $C$: $\tan 60^\circ = \dfrac{h}{CB}$, so $CB = \dfrac{h}{\sqrt3}$.",
         r"$\tan 60^\circ = \sqrt3$. The steeper angle means the shorter base - a good sanity check."),
        (r"Use the $20$ m gap: $AB - CB = h\sqrt3 - \dfrac{h}{\sqrt3} = h\left(\dfrac{3 - 1}{\sqrt3}\right) = \dfrac{2h}{\sqrt3} = 20$.",
         r"Common denominator $\sqrt3$: $\sqrt3 = \frac{3}{\sqrt3}$."),
        (r"Solve: $h = \dfrac{20\sqrt3}{2} = 10\sqrt3$ m.",
         r"Multiply both sides by $\sqrt3$ and halve."),
    ],
    pitfalls=[r"Adding the bases instead of subtracting (the closer point has the **shorter** base).",
              r"Using $\tan 30^\circ = \sqrt3$, which swaps the two triangles."],
    takeaway=r"Two elevation angles to the same object: write each horizontal distance in terms of the height and use their difference."),

"TRI-15": Sol(
    idea=r"Three sides, area wanted. Find a cosine, convert to a sine, then use $\frac12 ab\sin C$ - all without a calculator.",
    steps=[
        (r"Find $\cos A$ where $A$ is between the sides $7$ and $9$: $\cos A = \dfrac{49 + 81 - 64}{2(7)(9)} = \dfrac{66}{126} = \dfrac{11}{21}$.",
         r"The side opposite $A$ is $BC = 8$, so that is the one subtracted."),
        (r"Convert to $\sin A$ using $\sin^2 + \cos^2 = 1$: $\sin A = \sqrt{1 - \frac{121}{441}} = \dfrac{\sqrt{320}}{21}$.",
         r"Keep the denominator $21$ throughout: $1 = \frac{441}{441}$."),
        (r"Simplify the surd: $\sqrt{320} = \sqrt{64 \times 5} = 8\sqrt5$, so $\sin A = \dfrac{8\sqrt5}{21}$.",
         r"Pull out the largest square factor."),
        (r"Area $= \frac12(7)(9)\sin A = \frac{63}{2} \times \dfrac{8\sqrt5}{21} = 12\sqrt5$.",
         r"$\frac{63 \times 8}{2 \times 21} = \frac{504}{42} = 12$."),
    ],
    pitfalls=[r"Taking $\sin A$ positive is right (angles in a triangle are between $0^\circ$ and $180^\circ$), but forgetting to square $\cos A$ before subtracting.",
              r"Arithmetic slips in $\sqrt{320}$, e.g. $16\sqrt5$, doubling the area."],
    takeaway=r"Three sides $\to$ $\cos$ from the cosine rule $\to$ $\sin$ from the Pythagorean identity $\to$ area from $\frac12 ab\sin C$."),

"TRI-16": Sol(
    idea=r"The overlap of two circles is two segments. The geometry of the centres gives the angle, then the segment formula applies twice.",
    steps=[
        (r"Let the circles meet at $P$ and $Q$. Each centre, together with $P$ and $Q$, forms a triangle with sides $2$, $2$ and the chord $PQ$.",
         r"Both radii are $2$ and the centres are $2$ apart, so joining a centre to $P$ and to the other centre gives an equilateral triangle of side $2$."),
        (r"That equilateral triangle shows the half-angle at a centre is $60^\circ$, so the chord subtends $\frac{2\pi}{3}$ (i.e. $120^\circ$) at each centre.",
         r"Two equilateral triangles back to back, one for $P$ and one for $Q$."),
        (r"Compute one segment: $\frac12 r^2(\theta - \sin\theta) = \frac12(4)\left(\frac{2\pi}{3} - \frac{\sqrt3}{2}\right) = \frac{4\pi}{3} - \sqrt3$.",
         r"$\sin\frac{2\pi}{3} = \frac{\sqrt3}{2}$."),
        (r"The overlap consists of two such segments (one from each circle): $2\left(\frac{4\pi}{3} - \sqrt3\right) = \dfrac{8\pi}{3} - 2\sqrt3$.",
         r"By symmetry the two segments are congruent."),
    ],
    pitfalls=[r"Counting only one segment, giving $\frac{4\pi}{3} - \sqrt3$ - an offered option.",
              r"Using $\theta = \frac{\pi}{3}$ (the half-angle) instead of $\frac{2\pi}{3}$."],
    takeaway=r"Overlapping circles: the lens is two segments; get the central angle from the triangle formed by the two centres and an intersection point."),

}
