"""Pythagoras, mensuration and 3D (M5.7, M5.11-M5.13, M5.15-M5.17)."""
from gen.model import Q, ROMAN3

T = "mensuration"

QUESTIONS = [
    Q("MEN-01", T, "M5.7", r"A cuboid measures $3$ cm by $4$ cm by $12$ cm. Find the length of its longest diagonal.",
      ["$13$ cm", "$5$ cm", r"$\sqrt{153}$ cm", "$12.5$ cm", r"$\sqrt{119}$ cm", "$15$ cm"], "A",
      r"$\sqrt{9 + 16 + 144} = \sqrt{169} = 13$.", diff=1),

    Q("MEN-02", T, "M5.16", r"A cylinder has radius $r$ and height $h$. Its volume is $54\pi$ and $h = 2r$. Find its total surface area.",
      [r"$54\pi$", r"$36\pi$", r"$27\pi$", r"$72\pi$", r"$45\pi$", r"$108\pi$"], "A",
      r"$\pi r^2 \cdot 2r = 2\pi r^3 = 54\pi \Rightarrow r = 3$, $h = 6$. Surface area $= 2\pi r^2 + 2\pi rh = 18\pi + 36\pi = 54\pi$.", diff=2),

    Q("MEN-03", T, "M5.16", r"A trapezium has parallel sides of length $8$ cm and $14$ cm and area $77$ cm$^2$. Find the perpendicular distance between the parallel sides.",
      ["$7$ cm", "$3.5$ cm", "$11$ cm", "$5.5$ cm", "$14$ cm", "$6$ cm"], "A",
      r"$\frac12(8 + 14)h = 11h = 77 \Rightarrow h = 7$.", diff=1),

    Q("MEN-04", T, "M5.16", r"A cone has base radius $6$ cm and slant height $10$ cm. Find its volume. (Volume of a cone $= \frac{1}{3}\pi r^2 h$.)",
      [r"$96\pi$ cm$^3$", r"$120\pi$ cm$^3$", r"$288\pi$ cm$^3$", r"$60\pi$ cm$^3$", r"$72\pi$ cm$^3$", r"$48\pi$ cm$^3$"], "A",
      r"Height $= \sqrt{100 - 36} = 8$. Volume $= \frac13\pi\cdot36\cdot8 = 96\pi$.", diff=1),

    Q("MEN-05", T, "M5.17", r"A sphere and a cube have the same volume. The cube has side length $a$. Find the radius of the sphere. (Volume of a sphere $= \frac{4}{3}\pi r^3$.)",
      [r"$a\sqrt[3]{\dfrac{3}{4\pi}}$", r"$a\sqrt[3]{\dfrac{4\pi}{3}}$", r"$\dfrac{a}{\sqrt[3]{\pi}}$", r"$\dfrac{3a}{4\pi}$", r"$a\sqrt{\dfrac{3}{4\pi}}$", r"$\dfrac{a}{2}$"], "A",
      r"$\frac43\pi r^3 = a^3 \Rightarrow r^3 = \frac{3a^3}{4\pi} \Rightarrow r = a\sqrt[3]{\frac{3}{4\pi}}$.", diff=1),

    Q("MEN-06", T, "M5.16", r"A square of side $10$ has a quarter-circle of radius $10$ drawn inside it, centred at one corner. Find the area of the square not covered by the quarter-circle.",
      [r"$100 - 25\pi$", r"$100 - 100\pi$", r"$25\pi$", r"$100 - 50\pi$", r"$50 - 25\pi$", r"$100\pi - 100$"], "A",
      r"$100 - \frac14\pi\cdot100 = 100 - 25\pi$.", diff=1),

    Q("MEN-07", T, "M5.7", r"A ladder of length $6.5$ m leans against a vertical wall with its foot $2.5$ m from the wall on horizontal ground. How far up the wall does it reach?",
      ["$6$ m", "$4$ m", "$5$ m", r"$\sqrt{48.5}$ m", "$7$ m", "$5.5$ m"], "A",
      r"$\sqrt{6.5^2 - 2.5^2} = \sqrt{42.25 - 6.25} = \sqrt{36} = 6$.", diff=1),

    Q("MEN-08", T, "M5.18", r"In a right-angled triangle the hypotenuse is $10$ and one angle is $30^\circ$. Find the area of the triangle.",
      [r"$\dfrac{25\sqrt{3}}{2}$", r"$25\sqrt3$", r"$25$", r"$\dfrac{25}{2}$", r"$50\sqrt3$", r"$\dfrac{25\sqrt3}{4}$"], "A",
      r"Sides $10\sin30^\circ = 5$ and $10\cos30^\circ = 5\sqrt3$. Area $= \frac12\cdot5\cdot5\sqrt3 = \frac{25\sqrt3}{2}$.", diff=1),

    Q("MEN-09", T, "M5.16", r"The volume of a cube is numerically equal to its surface area. Find the length of its side.",
      ["$6$", "$3$", "$1$", "$12$", r"$\sqrt6$", "$2$"], "A",
      r"$a^3 = 6a^2 \Rightarrow a = 6$.", diff=1),

    Q("MEN-10", T, "M5.7", r"A square-based pyramid has base side $6$ and all slant edges of length $9$. Find its height.",
      [r"$\sqrt{63}$", r"$\sqrt{72}$", r"$\sqrt{45}$", r"$3\sqrt{6}$", r"$6$", r"$\sqrt{81 - 36}$"], "A",
      r"Half the base diagonal is $3\sqrt2$, so $h^2 = 81 - 18 = 63$.", diff=2),

    Q("MEN-11", T, "M5.16", r"""Which of the following statements is/are true?

I. Doubling the radius of a circle doubles its circumference.
II. Doubling the radius of a sphere multiplies its volume by $8$.
III. Doubling the radius of a cylinder while halving its height leaves its volume unchanged.""", ROMAN3, "E",
      r"$C = 2\pi r$ is linear in $r$ (I). $V \propto r^3$ (II). $\pi(2r)^2\cdot\frac h2 = 2\pi r^2 h$: doubled, not unchanged (III false).", paper=2, tags=("roman",), diff=1),

    Q("MEN-12", T, "M5.16", r"A running track consists of two straights of length $100$ m and two semicircular ends of radius $r$. The total length of the track is $400$ m. Find $r$.",
      [r"$\dfrac{100}{\pi}$", r"$\dfrac{200}{\pi}$", r"$\dfrac{50}{\pi}$", r"$100\pi$", r"$\dfrac{400}{\pi}$", r"$\dfrac{300}{\pi}$"], "A",
      r"$200 + 2\pi r = 400 \Rightarrow r = \frac{100}{\pi}$.", diff=1),

    Q("MEN-13", T, "M5.7", r"The points $A(1, 2)$, $B(4, 6)$ and $C(k, 2)$ with $k > 1$ form a triangle with a right angle at $B$. Find $k$.",
      [r"$\dfrac{28}{3}$", r"$7$", r"$\dfrac{16}{3}$", r"$5$", r"$\dfrac{25}{3}$", r"$8$"], "A",
      r"Gradient $AB = \frac43$, so $BC$ must have gradient $-\frac34$: $\dfrac{2 - 6}{k - 4} = -\dfrac34 \Rightarrow 16 = 3(k - 4) \Rightarrow k = \dfrac{28}{3}$.", diff=2),

    Q("MEN-14", T, "M5.16", r"A cylindrical tin of radius $4$ cm and height $10$ cm is full of water. The water is poured into an empty cylindrical jug of radius $5$ cm. How deep is the water in the jug?",
      ["$6.4$ cm", "$8$ cm", "$12.5$ cm", "$5$ cm", "$6$ cm", "$7.2$ cm"], "A",
      r"$\pi\cdot16\cdot10 = \pi\cdot25\cdot h \Rightarrow h = \frac{160}{25} = 6.4$.", diff=1),

    Q("MEN-15", T, "M5.17", r"A solid consists of a hemisphere of radius $3$ on top of a cylinder of radius $3$ and height $4$. Find its volume. (Sphere volume $\frac{4}{3}\pi r^3$.)",
      [r"$54\pi$", r"$72\pi$", r"$45\pi$", r"$36\pi$", r"$63\pi$", r"$90\pi$"], "A",
      r"Cylinder $\pi\cdot9\cdot4 = 36\pi$; hemisphere $\frac12\cdot\frac43\pi\cdot27 = 18\pi$. Total $54\pi$.", diff=1),

    Q("MEN-16", T, "M5.18", r"From the top of a cliff $40$ m high, the angle of depression of a boat is $30^\circ$. How far is the boat from the foot of the cliff?",
      [r"$40\sqrt{3}$ m", r"$\dfrac{40}{\sqrt3}$ m", r"$80$ m", r"$20$ m", r"$20\sqrt3$ m", r"$40$ m"], "A",
      r"$\tan30^\circ = \frac{40}{d} \Rightarrow d = \frac{40}{1/\sqrt3} = 40\sqrt3$.", diff=1),
]
