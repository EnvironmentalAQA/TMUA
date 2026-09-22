"""Circles and circle theorems (MM3.2, MM3.3, M5.8, M5.9)."""
from gen.model import Q, ROMAN3

T = "circles"

QUESTIONS = [
    Q("CIR-01", T, "MM3.2", r"Find the radius of the circle $x^2 + y^2 - 6x + 4y - 12 = 0$.",
      ["$5$", r"$\sqrt{12}$", "$25$", "$1$", r"$\sqrt{13}$", "$4$"], "A",
      r"$(x-3)^2 + (y+2)^2 = 12 + 9 + 4 = 25$, so $r = 5$.", diff=1),

    Q("CIR-02", T, "MM3.2", r"Find the complete set of values of $k$ for which $x^2 + y^2 + 2kx - 4y + 3k + 4 = 0$ represents a circle.",
      [r"$k < 0$ or $k > 3$", r"$0 < k < 3$", r"$k < -3$ or $k > 0$", r"$-3 < k < 0$", r"all real $k$", r"$k > 3$"], "A",
      r"$(x + k)^2 + (y - 2)^2 = k^2 + 4 - 3k - 4 = k^2 - 3k = k(k - 3)$. A circle needs a positive right-hand side: $k < 0$ or $k > 3$.", diff=2),

    Q("CIR-03", T, "MM3.2", r"The circle with centre $(2, -1)$ passes through $(5, 3)$. Find the equation of the tangent to the circle at $(5, 3)$.",
      [r"$3x + 4y = 27$", r"$4x - 3y = 11$", r"$3x - 4y = 3$", r"$4x + 3y = 29$", r"$3x + 4y = 15$", r"$x + y = 8$"], "A",
      r"Radius direction $(3, 4)$ has gradient $\frac43$, so the tangent has gradient $-\frac34$: $y - 3 = -\frac34(x - 5) \Rightarrow 4y - 12 = -3x + 15 \Rightarrow 3x + 4y = 27$.", diff=1),

    Q("CIR-04", T, "MM3.2", r"The points $(1, 7)$ and $(5, -1)$ are the ends of a diameter of a circle. Find the equation of the circle.",
      [r"$(x-3)^2 + (y-3)^2 = 20$", r"$(x-3)^2 + (y-3)^2 = 80$", r"$(x-3)^2 + (y-3)^2 = 40$", r"$(x-2)^2 + (y-4)^2 = 20$", r"$(x-3)^2 + (y-3)^2 = \sqrt{20}$", r"$(x+3)^2 + (y+3)^2 = 20$"], "A",
      r"Centre is the midpoint $(3, 3)$; radius$^2$ $= (3-1)^2 + (3-7)^2 = 4 + 16 = 20$.", diff=1),

    Q("CIR-05", T, "MM3.2", r"The line $y = x + c$ is a tangent to the circle $(x-1)^2 + (y-2)^2 = 8$. Find the possible values of $c$.",
      [r"$c = -3$ or $c = 5$", r"$c = -5$ or $c = 3$", r"$c = 1 \pm 2\sqrt{2}$", r"$c = -1$ or $c = 3$", r"$c = \pm 4$", r"$c = 1$ or $c = 5$"], "A",
      r"The distance from $(1, 2)$ to $x - y + c = 0$ is $\frac{|1 - 2 + c|}{\sqrt2} = \sqrt8 = 2\sqrt2$, so $|c - 1| = 4$: $c = 5$ or $c = -3$.", diff=2),

    Q("CIR-06", T, "MM3.3", r"$A$, $B$ and $C$ lie on a circle with centre $O$. Angle $AOB = 100^\circ$ and $C$ lies on the major arc $AB$. Find angle $ACB$.",
      [r"$50^\circ$", r"$100^\circ$", r"$130^\circ$", r"$80^\circ$", r"$40^\circ$", r"$200^\circ$"], "A",
      r"The angle at the centre is twice the angle at the circumference subtended by the same arc: $ACB = 50^\circ$.", diff=1),

    Q("CIR-07", T, "MM3.3", r"$PQRS$ is a cyclic quadrilateral with angle $P = 3x$, angle $R = x + 40^\circ$. Find $x$.",
      [r"$35^\circ$", r"$40^\circ$", r"$45^\circ$", r"$30^\circ$", r"$50^\circ$", r"$25^\circ$"], "A",
      r"Opposite angles of a cyclic quadrilateral sum to $180^\circ$: $4x + 40 = 180$, $x = 35^\circ$.", diff=1),

    Q("CIR-08", T, "MM3.3", r"A chord of a circle of radius $13$ is at perpendicular distance $5$ from the centre. Find the length of the chord.",
      ["$24$", "$12$", "$18$", "$26$", "$10$", r"$\sqrt{144}$"], "A",
      r"The perpendicular from the centre bisects the chord: half-length $= \sqrt{13^2 - 5^2} = 12$, so the chord is $24$.", diff=1),

    Q("CIR-09", T, "MM3.2", r"Find the length of the tangent from the point $(7, 1)$ to the circle $x^2 + y^2 - 2x - 4y - 4 = 0$.",
      [r"$\sqrt{28}$", "$5$", r"$\sqrt{37}$", "$3$", r"$\sqrt{26}$", "$6$"], "A",
      r"Centre $(1, 2)$, radius $3$. Distance from $(7, 1)$ to centre: $\sqrt{36 + 1} = \sqrt{37}$. Tangent length $= \sqrt{37 - 9} = \sqrt{28}$.", diff=2),

    Q("CIR-10", T, "MM3.3", r"$TA$ is a tangent to a circle at $A$, and $AB$ is a chord. $C$ is a point on the circle on the opposite side of $AB$ from $T$, with angle $ACB = 65^\circ$. Find angle $TAB$.",
      [r"$65^\circ$", r"$115^\circ$", r"$25^\circ$", r"$130^\circ$", r"$32.5^\circ$", r"$50^\circ$"], "A",
      r"Alternate segment theorem: the angle between tangent and chord equals the angle in the alternate segment, so $TAB = 65^\circ$.", diff=1),

    Q("CIR-11", T, "MM3.2", r"""Two circles have equations $x^2 + y^2 = 25$ and $(x - 8)^2 + y^2 = 9$. Which of the following statements is/are true?

I. The circles touch externally.
II. The circles intersect at exactly two points.
III. The point $(5, 0)$ lies on both circles.""", ROMAN3, "F",
      r"Radii $5$ and $3$, centres $8$ apart $= 5 + 3$, so the circles touch externally at one point (I true, II false). That point is $(5, 0)$: $25 = 25$ and $9 + 0 = 9$ (III true).", paper=2, tags=("roman",)),

    Q("CIR-12", T, "MM3.2", r"The circle $C$ has equation $x^2 + y^2 - 4x - 6y + 9 = 0$. Which of the following lines does not meet $C$?",
      [r"$x = 0$", r"$y = 0$", r"$x = 4$", r"$y = 5$", r"$x = 2$"], "B",
      r"Centre $(2, 3)$, radius $2$, so the circle spans $0 \leq x \leq 4$ and $1 \leq y \leq 5$. The line $y = 0$ is $3$ from the centre, more than the radius, so it misses; $x = 0$, $x = 4$ and $y = 5$ touch and $x = 2$ passes through the centre.", diff=1),

    Q("CIR-13", T, "MM3.2", r"The circle $x^2 + y^2 = r^2$ and the line $3x + 4y = 20$ have exactly one point in common. Find $r$.",
      ["$4$", "$5$", r"$\sqrt{20}$", "$20$", r"$\dfrac{20}{7}$", "$2$"], "A",
      r"Distance from origin to the line $= \frac{20}{\sqrt{9 + 16}} = 4$. Tangency means $r = 4$.", diff=1),

    Q("CIR-14", T, "MM3.3", r"$AB$ is a diameter of a circle and $C$ is a point on the circle with $AC = 6$ and $BC = 8$. Find the radius of the circle.",
      ["$5$", "$10$", "$7$", r"$\sqrt{50}$", "$4$", "$14$"], "A",
      r"The angle in a semicircle is a right angle, so $AB = \sqrt{36 + 64} = 10$ and the radius is $5$.", diff=1),

    Q("CIR-15", T, "MM3.2", r"A circle passes through $(0, 0)$, $(6, 0)$ and $(0, 8)$. Find the coordinates of its centre.",
      [r"$(3, 4)$", r"$(6, 8)$", r"$(2, 3)$", r"$(4, 3)$", r"$(3, 3)$", r"$(5, 5)$"], "A",
      r"The triangle has a right angle at the origin, so $(6, 0)$-$(0, 8)$ is a diameter; the centre is its midpoint $(3, 4)$.", diff=1),

    Q("CIR-16", T, "MM3.2", r"The point $P(x, y)$ moves so that its distance from $(3, 0)$ is twice its distance from $(0, 0)$. The locus of $P$ is a circle. Find its radius.",
      ["$2$", "$1$", "$3$", r"$\sqrt{3}$", "$4$", r"$\sqrt{2}$"], "A",
      r"$(x-3)^2 + y^2 = 4(x^2 + y^2) \Rightarrow 3x^2 + 3y^2 + 6x - 9 = 0 \Rightarrow x^2 + 2x + y^2 = 3 \Rightarrow (x+1)^2 + y^2 = 4$. Radius $2$.", diff=2),
]

