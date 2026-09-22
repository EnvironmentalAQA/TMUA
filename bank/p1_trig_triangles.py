"""Triangles, radians and sectors (MM4.1, MM4.2, M5.16)."""
from gen.model import Q, ROMAN3

T = "trig-triangles"

QUESTIONS = [
    Q("TRI-01", T, "MM4.1", r"In triangle $ABC$, $AB = 5$, $AC = 8$ and angle $BAC = 60^\circ$. Find $BC$.",
      [r"$7$", r"$\sqrt{89}$", r"$\sqrt{129}$", r"$\sqrt{49 + 40\sqrt3}$", r"$9$", r"$\sqrt{69}$"], "A",
      r"Cosine rule: $BC^2 = 25 + 64 - 2\cdot5\cdot8\cdot\frac12 = 89 - 40 = 49$, so $BC = 7$.", diff=1),

    Q("TRI-02", T, "MM4.1", r"A triangle has sides $4$, $5$ and $6$. Find the cosine of its largest angle.",
      [r"$\dfrac{1}{8}$", r"$\dfrac{3}{4}$", r"$\dfrac{9}{16}$", r"$-\dfrac{1}{8}$", r"$\dfrac{1}{4}$", r"$\dfrac{5}{8}$"], "A",
      r"The largest angle is opposite the side $6$: $\cos\theta = \dfrac{16 + 25 - 36}{2\cdot4\cdot5} = \dfrac{5}{40} = \dfrac18$.", diff=1),

    Q("TRI-03", T, "MM4.2", r"A sector of a circle of radius $6$ cm has area $15\pi$ cm$^2$. Find the arc length of the sector.",
      [r"$5\pi$ cm", r"$\dfrac{5\pi}{2}$ cm", r"$10\pi$ cm", r"$\dfrac{5\pi}{6}$ cm", r"$3\pi$ cm", r"$15\pi$ cm"], "A",
      r"$\frac12 r^2\theta = 18\theta = 15\pi \Rightarrow \theta = \frac{5\pi}{6}$. Arc $= r\theta = 6 \cdot \frac{5\pi}{6} = 5\pi$.", diff=1),

    Q("TRI-04", T, "MM4.1", r"Triangle $PQR$ has area $10\sqrt{3}$, $PQ = 8$ and $PR = 5$. Given that angle $QPR$ is obtuse, find $QR$.",
      [r"$\sqrt{129}$", r"$7$", r"$\sqrt{89}$", r"$\sqrt{89 + 40\sqrt{3}}$", r"$13$", r"$\sqrt{109}$"], "A",
      r"$\frac12\cdot8\cdot5\sin P = 10\sqrt3 \Rightarrow \sin P = \frac{\sqrt3}{2}$, and $P$ obtuse gives $P = 120^\circ$. $QR^2 = 64 + 25 - 80\cos120^\circ = 89 + 40 = 129$.", diff=2),

    Q("TRI-05", T, "MM4.2", r"Convert $135^\circ$ to radians.",
      [r"$\dfrac{3\pi}{4}$", r"$\dfrac{2\pi}{3}$", r"$\dfrac{5\pi}{6}$", r"$\dfrac{3\pi}{8}$", r"$\dfrac{5\pi}{4}$", r"$\dfrac{4\pi}{3}$"], "A",
      r"$135 = \frac34 \times 180$, so $\frac{3\pi}{4}$.", diff=1),

    Q("TRI-06", T, "MM4.2", r"A chord of a circle of radius $4$ subtends an angle of $\dfrac{\pi}{3}$ at the centre. Find the area of the minor segment cut off by the chord.",
      [r"$\dfrac{8\pi}{3} - 4\sqrt{3}$", r"$\dfrac{8\pi}{3} - 8\sqrt{3}$", r"$\dfrac{16\pi}{3} - 4\sqrt3$", r"$\dfrac{8\pi}{3} - 4$", r"$\dfrac{4\pi}{3} - 2\sqrt3$", r"$8\pi - 4\sqrt3$"], "A",
      r"Sector area $\frac12 \cdot 16 \cdot \frac\pi3 = \frac{8\pi}{3}$. Triangle area $\frac12 \cdot 16 \sin\frac\pi3 = 4\sqrt3$. Segment $= \frac{8\pi}{3} - 4\sqrt3$.", diff=2),

    Q("TRI-07", T, "MM4.1", r"In triangle $ABC$, $AB = 6$, $BC = 4$ and angle $BAC = 30^\circ$. How many possible triangles are there?",
      ["$0$", "$1$", "$2$", "$3$", "infinitely many"], "C",
      r"Sine rule: $\dfrac{\sin C}{6} = \dfrac{\sin 30^\circ}{4}$, so $\sin C = \frac34$. Since $BC = 4 < AB = 6$ and $4 > 6\sin30^\circ = 3$, both the acute and obtuse values of $C$ give valid triangles: the ambiguous case, two triangles.", diff=2),

    Q("TRI-08", T, "MM4.2", r"The perimeter of a sector of radius $r$ and angle $\theta$ radians is $20$, and its area is $16$. Find the possible values of $r$.",
      [r"$2$ or $8$", r"$4$ only", r"$2$ or $4$", r"$4$ or $8$", r"$1$ or $16$", r"$8$ only"], "A",
      r"$2r + r\theta = 20$ and $\frac12 r^2\theta = 16$. From the first $r\theta = 20 - 2r$; then $\frac12 r(20 - 2r) = 16 \Rightarrow r^2 - 10r + 16 = 0 \Rightarrow r = 2$ or $8$.", diff=2),

    Q("TRI-09", T, "MM4.1", r"Two sides of a triangle are $3$ and $5$ and the included angle is $\theta$, where $\cos\theta = -\dfrac{1}{5}$. Find the length of the third side.",
      [r"$\sqrt{40}$", r"$\sqrt{28}$", r"$6$", r"$\sqrt{34}$", r"$\sqrt{31}$", r"$7$"], "A",
      r"$c^2 = 9 + 25 - 2\cdot3\cdot5\cdot\left(-\frac15\right) = 34 + 6 = 40$.", diff=1),

    Q("TRI-10", T, "MM4.1", r"In triangle $ABC$, $\sin A : \sin B : \sin C = 3 : 5 : 7$. Find angle $C$.",
      [r"$120^\circ$", r"$60^\circ$", r"$90^\circ$", r"$150^\circ$", r"$135^\circ$", r"$100^\circ$"], "A",
      r"By the sine rule the sides are in ratio $3 : 5 : 7$. $\cos C = \dfrac{9 + 25 - 49}{2\cdot3\cdot5} = -\dfrac{15}{30} = -\dfrac12$, so $C = 120^\circ$.", diff=2),

    Q("TRI-11", T, "MM4.2", r"A circle has radius $r$. A sector of angle $\theta$ radians has the same area as the segment cut off by a chord that subtends an angle of $\dfrac{\pi}{2}$ at the centre. Find $\theta$.",
      [r"$\dfrac{\pi}{2} - 1$", r"$\dfrac{\pi}{4} - \dfrac12$", r"$\dfrac{\pi}{2} - \dfrac12$", r"$\dfrac{\pi}{4}$", r"$\pi - 2$", r"$1$"], "A",
      r"Segment area $= \frac12 r^2\left(\frac\pi2 - \sin\frac\pi2\right) = \frac12 r^2\left(\frac\pi2 - 1\right)$. Sector area $\frac12 r^2\theta$. So $\theta = \frac\pi2 - 1$.", diff=2),

    Q("TRI-12", T, "MM4.1", r"""A triangle has sides $a$, $b$, $c$ with $a^2 + b^2 < c^2$. Which of the following statements is/are true?

I. The angle opposite $c$ is obtuse.
II. $c$ is the longest side.
III. The triangle cannot be isosceles.""", ROMAN3, "E",
      r"Cosine rule: $\cos C = \frac{a^2 + b^2 - c^2}{2ab} < 0$, so $C$ is obtuse (I). The largest angle is opposite the longest side, so $c$ is longest (II). III is false: $a = b = 1$, $c = 1.5$ works.", paper=2, tags=("roman",)),

    Q("TRI-13", T, "MM4.2", r"The minute hand of a clock is $12$ cm long. How far does its tip travel in $25$ minutes?",
      [r"$10\pi$ cm", r"$5\pi$ cm", r"$12\pi$ cm", r"$25\pi$ cm", r"$\dfrac{25\pi}{6}$ cm", r"$20\pi$ cm"], "A",
      r"$25$ minutes is $\frac{25}{60} = \frac{5}{12}$ of a revolution: $\frac{5}{12} \times 2\pi \times 12 = 10\pi$ cm.", diff=1),

    Q("TRI-14", T, "MM4.1", r"A vertical pole $BT$ stands on horizontal ground. From a point $A$ on the ground the angle of elevation of $T$ is $30^\circ$; from a point $C$ on the ground, $20$ m closer to the pole than $A$ and in line with $A$ and $B$, the angle of elevation is $60^\circ$. Find the height of the pole.",
      [r"$10\sqrt{3}$ m", r"$20\sqrt{3}$ m", r"$10$ m", r"$\dfrac{20}{\sqrt3}$ m", r"$15$ m", r"$30$ m"], "A",
      r"Let the height be $h$. $AB = h\sqrt3$ and $CB = \frac{h}{\sqrt3}$. $AB - CB = 20 \Rightarrow h\left(\sqrt3 - \frac1{\sqrt3}\right) = \frac{2h}{\sqrt3} = 20 \Rightarrow h = 10\sqrt3$.", diff=2),

    Q("TRI-15", T, "MM4.1", r"Triangle $ABC$ has $AB = 7$, $BC = 8$, $CA = 9$. Find the area of the triangle.",
      [r"$12\sqrt{5}$", r"$24\sqrt5$", r"$6\sqrt{5}$", r"$28$", r"$\sqrt{720}$", r"$30$"], "A",
      r"$\cos A = \dfrac{49 + 81 - 64}{2\cdot7\cdot9} = \dfrac{66}{126} = \dfrac{11}{21}$, so $\sin A = \dfrac{\sqrt{441 - 121}}{21} = \dfrac{\sqrt{320}}{21} = \dfrac{8\sqrt5}{21}$. Area $= \frac12\cdot7\cdot9\cdot\frac{8\sqrt5}{21} = 12\sqrt5$.", diff=2),

    Q("TRI-16", T, "MM4.2", r"Two circles of radius $2$ have their centres a distance $2$ apart. Find the area of the region common to both circles.",
      [r"$\dfrac{8\pi}{3} - 2\sqrt{3}$", r"$\dfrac{4\pi}{3} - \sqrt3$", r"$\dfrac{8\pi}{3} - 4\sqrt3$", r"$\dfrac{4\pi}{3} - 2\sqrt3$", r"$2\pi - 2\sqrt3$", r"$\dfrac{2\pi}{3}$"], "A",
      r"The common chord subtends $\frac{2\pi}{3}$ at each centre (equilateral triangles of side $2$). The overlap is two segments: $2 \times \frac12\cdot4\left(\frac{2\pi}{3} - \sin\frac{2\pi}{3}\right) = 4\left(\frac{2\pi}{3} - \frac{\sqrt3}{2}\right) = \frac{8\pi}{3} - 2\sqrt3$.", diff=3),
]
