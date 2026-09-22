"""Angles, polygons, congruence, similarity, transformations and vectors (M5.1-M5.6, M5.10, M5.14, M5.18, M5.19)."""
from gen.model import Q, ROMAN3

T = "geometry"

QUESTIONS = [
    Q("GEO-01", T, "M5.2", r"The interior angle of a regular polygon is $156^\circ$. How many sides does it have?",
      ["$15$", "$12$", "$18$", "$20$", "$24$", "$10$"], "A",
      r"Exterior angle $24^\circ$; $360/24 = 15$ sides.", diff=1),

    Q("GEO-02", T, "M5.2", r"A polygon has interior angles that sum to $1980^\circ$. How many sides does it have?",
      ["$13$", "$11$", "$12$", "$14$", "$10$", "$15$"], "A",
      r"$180(n - 2) = 1980 \Rightarrow n - 2 = 11 \Rightarrow n = 13$.", diff=1),

    Q("GEO-03", T, "M5.19", r"$\mathbf{a} = \binom{2}{-1}$ and $\mathbf{b} = \binom{-3}{4}$. Find $2\mathbf{a} - \mathbf{b}$.",
      [r"$\binom{7}{-6}$", r"$\binom{1}{2}$", r"$\binom{-7}{6}$", r"$\binom{7}{-2}$", r"$\binom{-1}{3}$", r"$\binom{5}{-5}$"], "A",
      r"$\binom{4}{-2} - \binom{-3}{4} = \binom{7}{-6}$.", diff=1),

    Q("GEO-04", T, "M5.19", r"In triangle $OAB$, $\overrightarrow{OA} = \mathbf{a}$ and $\overrightarrow{OB} = \mathbf{b}$. $M$ is the midpoint of $AB$ and $P$ is the point on $OM$ with $OP : PM = 2 : 1$. Express $\overrightarrow{AP}$ in terms of $\mathbf{a}$ and $\mathbf{b}$.",
      [r"$\dfrac{1}{3}\mathbf{b} - \dfrac{2}{3}\mathbf{a}$", r"$\dfrac{1}{3}\mathbf{a} + \dfrac{1}{3}\mathbf{b}$", r"$\dfrac{2}{3}\mathbf{b} - \dfrac{1}{3}\mathbf{a}$", r"$\dfrac{1}{3}(\mathbf{b} - \mathbf{a})$", r"$\dfrac{1}{2}\mathbf{b} - \dfrac{1}{2}\mathbf{a}$", r"$\dfrac{2}{3}(\mathbf{a} + \mathbf{b})$"], "A",
      r"$\overrightarrow{OM} = \frac12(\mathbf a + \mathbf b)$, $\overrightarrow{OP} = \frac23\overrightarrow{OM} = \frac13(\mathbf a + \mathbf b)$. $\overrightarrow{AP} = \overrightarrow{OP} - \mathbf a = \frac13\mathbf b - \frac23\mathbf a$.", diff=2),

    Q("GEO-05", T, "M5.5", r"Two similar triangles have corresponding sides of length $6$ cm and $9$ cm. The smaller triangle has area $20$ cm$^2$. Find the area of the larger triangle.",
      ["$45$ cm$^2$", "$30$ cm$^2$", "$40$ cm$^2$", "$60$ cm$^2$", "$67.5$ cm$^2$", "$27$ cm$^2$"], "A",
      r"Area scale factor $\left(\frac96\right)^2 = \frac94$: $20 \times \frac94 = 45$.", diff=1),

    Q("GEO-06", T, "M5.14", r"A ship sails from $P$ on a bearing of $060^\circ$ for $10$ km to $Q$, then on a bearing of $150^\circ$ for $10$ km to $R$. What is the bearing of $P$ from $R$?",
      [r"$285^\circ$", r"$105^\circ$", r"$255^\circ$", r"$315^\circ$", r"$195^\circ$", r"$075^\circ$"], "A",
      r"The turn at $Q$ is $90^\circ$ and $PQ = QR$, so triangle $PQR$ is right-angled isosceles and $PR$ makes $45^\circ$ with $QR$. Bearing of $R$ from $P$ is $060 + 45 = 105^\circ$; the back bearing is $105 + 180 = 285^\circ$.", diff=2),

    Q("GEO-07", T, "M5.6", r"The triangle with vertices $(1, 1)$, $(3, 1)$, $(1, 4)$ is enlarged with scale factor $-2$, centre the origin. Which of the following is a vertex of the image?",
      [r"$(-2, -8)$", r"$(2, 8)$", r"$(-6, -8)$", r"$(6, 2)$", r"$(-3, -1)$", r"$(-1, -4)$"], "A",
      r"Multiply each coordinate by $-2$: $(-2, -2)$, $(-6, -2)$, $(-2, -8)$.", diff=1),

    Q("GEO-08", T, "M5.4", r"Which of the following sets of information is NOT sufficient to prove that two triangles are congruent?",
      [r"two sides and a non-included angle equal (SSA)", r"three sides equal (SSS)", r"two sides and the included angle equal (SAS)", r"two angles and a corresponding side equal (ASA)", r"right angle, hypotenuse and one other side equal (RHS)"], "A",
      r"SSA is not a congruence condition (it is the ambiguous case of the sine rule); the other four are the standard criteria.", diff=1),

    Q("GEO-09", T, "M5.2", r"In the diagram (not shown), $AB$ is parallel to $CD$. A transversal makes an angle of $(3x + 10)^\circ$ with $AB$ and the co-interior angle with $CD$ is $(2x - 5)^\circ$. Find $x$.",
      ["$35$", "$15$", "$25$", "$45$", "$55$", "$30$"], "A",
      r"Co-interior angles sum to $180^\circ$: $5x + 5 = 180 \Rightarrow x = 35$.", diff=1),

    Q("GEO-10", T, "M5.3", r"""Which of the following statements is/are true?

I. Every rhombus is a parallelogram.
II. Every rectangle is a rhombus.
III. The diagonals of a kite are perpendicular.""", ROMAN3, "F",
      r"A rhombus has two pairs of parallel sides (I). A rectangle need not have equal sides (II false). The diagonals of a kite cross at right angles (III).", paper=2, tags=("roman",), diff=1),

    Q("GEO-11", T, "M5.19", r"$\overrightarrow{AB} = 3\mathbf{p} + 2\mathbf{q}$ and $\overrightarrow{BC} = k\mathbf{p} - 4\mathbf{q}$, where $\mathbf{p}$ and $\mathbf{q}$ are not parallel. Given that $A$, $B$ and $C$ are collinear, find $k$.",
      ["$-6$", "$6$", "$-4$", "$2$", "$-3$", r"$\dfrac{3}{2}$"], "A",
      r"Collinear means $\overrightarrow{BC} = \lambda\overrightarrow{AB}$: $-4 = 2\lambda \Rightarrow \lambda = -2$, so $k = 3\lambda = -6$.", diff=2),

    Q("GEO-12", T, "M5.6", r"A shape is reflected in the line $y = x$ and then rotated $90^\circ$ anticlockwise about the origin. The point $(3, 1)$ ends up at",
      [r"$(-3, 1)$", r"$(1, 3)$", r"$(-1, 3)$", r"$(3, -1)$", r"$(-1, -3)$", r"$(1, -3)$"], "A",
      r"Reflection in $y = x$: $(3, 1) \to (1, 3)$. Rotation $90^\circ$ anticlockwise: $(x, y) \to (-y, x)$, so $(1, 3) \to (-3, 1)$.", diff=1),

    Q("GEO-13", T, "M5.2", r"In triangle $ABC$, angle $A$ is twice angle $B$, and angle $C$ is $20^\circ$ more than angle $A$. Find angle $B$.",
      [r"$32^\circ$", r"$40^\circ$", r"$64^\circ$", r"$36^\circ$", r"$28^\circ$", r"$30^\circ$"], "A",
      r"$B + 2B + (2B + 20) = 180 \Rightarrow 5B = 160 \Rightarrow B = 32^\circ$.", diff=1),

    Q("GEO-14", T, "M5.5", r"In triangle $ABC$, $D$ lies on $AB$ and $E$ lies on $AC$ with $DE$ parallel to $BC$. $AD = 4$, $DB = 6$ and $DE = 5$. Find $BC$.",
      [r"$12.5$", r"$7.5$", r"$10$", r"$15$", r"$8$", r"$12$"], "A",
      r"Triangles $ADE$ and $ABC$ are similar with ratio $AD : AB = 4 : 10$. $BC = 5 \times \frac{10}{4} = 12.5$.", diff=1),

    Q("GEO-15", T, "M5.2", r"A regular hexagon and a regular octagon share a common side. What is the size of the angle between their two other sides that meet at one end of the common side (the angle outside both polygons)?",
      [r"$105^\circ$", r"$120^\circ$", r"$135^\circ$", r"$95^\circ$", r"$115^\circ$", r"$75^\circ$"], "A",
      r"Angles at the shared vertex: $120^\circ$ (hexagon) $+ 135^\circ$ (octagon) $+ x = 360^\circ$, so $x = 105^\circ$.", diff=2),
]
