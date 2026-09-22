"""Straight lines (MM3.1, M4.9, M4.10)."""
from gen.model import Q, ROMAN3

T = "straight-lines"

QUESTIONS = [
    Q("LIN-01", T, "MM3.1", r"Find the equation of the line through $(2, -3)$ that is perpendicular to $3x - 2y + 5 = 0$.",
      [r"$2x + 3y + 5 = 0$", r"$2x + 3y - 5 = 0$", r"$3x - 2y - 12 = 0$", r"$2x - 3y - 13 = 0$", r"$3x + 2y = 0$", r"$2x + 3y - 13 = 0$"], "A",
      r"The given line has gradient $\frac32$, so the perpendicular has gradient $-\frac23$: $y + 3 = -\frac23(x - 2) \Rightarrow 3y + 9 = -2x + 4 \Rightarrow 2x + 3y + 5 = 0$.", diff=1),

    Q("LIN-02", T, "MM3.1", r"The points $A(1, 2)$, $B(5, 4)$ and $C(k, 8)$ are collinear. Find $k$.",
      ["$13$", "$9$", "$11$", "$7$", "$12$", "$10$"], "A",
      r"Gradient $AB = \frac{2}{4} = \frac12$. Gradient $AC = \frac{6}{k-1} = \frac12 \Rightarrow k - 1 = 12 \Rightarrow k = 13$.", diff=1),

    Q("LIN-03", T, "MM3.1", r"The line $L$ passes through $(4, 0)$ and $(0, 6)$. Find the perpendicular distance from the origin to $L$.",
      [r"$\dfrac{12}{\sqrt{13}}$", r"$\dfrac{24}{13}$", r"$\sqrt{13}$", r"$\dfrac{12}{13}$", r"$2\sqrt{13}$", r"$5$"], "A",
      r"Area of triangle $= \frac12 \cdot 4 \cdot 6 = 12$. Hypotenuse $= \sqrt{16 + 36} = \sqrt{52} = 2\sqrt{13}$. Distance $d$ satisfies $\frac12 \cdot 2\sqrt{13} \cdot d = 12$, so $d = \frac{12}{\sqrt{13}}$.", diff=2),

    Q("LIN-04", T, "MM3.1", r"The lines $y = 2x + 1$, $y = -x + 7$ and the $x$-axis enclose a triangle. Find its area.",
      [r"$\dfrac{75}{4}$", r"$\dfrac{25}{2}$", r"$\dfrac{15}{2}$", r"$\dfrac{45}{4}$", r"$15$", r"$\dfrac{35}{2}$"], "A",
      r"Intersection: $2x + 1 = 7 - x \Rightarrow x = 2$, $y = 5$. $x$-intercepts: $-\frac12$ and $7$, base $= \frac{15}{2}$. Area $= \frac12 \cdot \frac{15}{2} \cdot 5 = \frac{75}{4}$.", diff=2),

    Q("LIN-05", T, "MM3.1", r"Which of the following lines is parallel to $4x + 6y = 9$?",
      [r"$2x + 3y = 1$", r"$3x - 2y = 4$", r"$4x - 6y = 9$", r"$6x + 4y = 9$", r"$y = \frac{3}{2}x + 1$"], "A",
      r"$4x + 6y = 9$ has gradient $-\frac23$; so does $2x + 3y = 1$.", diff=1),

    Q("LIN-06", T, "MM3.1", r"The perpendicular bisector of the line segment joining $(1, 5)$ and $(7, 1)$ has equation",
      [r"$3x - 2y = 6$", r"$2x + 3y = 17$", r"$3x - 2y = 18$", r"$2x - 3y = -1$", r"$3x + 2y = 18$", r"$y = \frac32 x - 3$"], "A",
      r"Midpoint $(4, 3)$; gradient of segment $\frac{-4}{6} = -\frac23$, so the bisector has gradient $\frac32$: $y - 3 = \frac32(x - 4) \Rightarrow 2y - 6 = 3x - 12 \Rightarrow 3x - 2y = 6$.", diff=1),

    Q("LIN-07", T, "MM3.1", r"The line $ax + by = 12$ has $x$-intercept $3$ and $y$-intercept $-4$. Find $a - b$.",
      ["$7$", "$1$", "$-7$", "$-1$", "$12$", "$0$"], "A",
      r"$(3, 0)$: $3a = 12 \Rightarrow a = 4$. $(0, -4)$: $-4b = 12 \Rightarrow b = -3$. $a - b = 7$.", diff=1),

    Q("LIN-08", T, "MM3.1", r"For which value of $k$ are the lines $kx + 3y = 2$ and $2x - (k-1)y = 5$ perpendicular?",
      ["$-3$", "$3$", "$1$", r"$\dfrac{3}{2}$", "$-1$", "$6$"], "B",
      r"Gradients $-\frac k3$ and $\frac{2}{k-1}$. Perpendicular when the product is $-1$: $\frac{-2k}{3(k-1)} = -1 \Rightarrow 2k = 3k - 3 \Rightarrow k = 3$.", diff=2),

    Q("LIN-09", T, "MM3.1", r"The point $P$ lies on the line $y = 2x - 1$ and is equidistant from $(0, 0)$ and $(4, 2)$. Find the coordinates of $P$.",
      [r"$(2, 3)$", r"$(1, 1)$", r"$\left(\dfrac{5}{4}, \dfrac{3}{2}\right)$", r"$(3, 5)$", r"$\left(\dfrac32, 2\right)$", r"$(2, 1)$"], "E",
      r"Equidistant means $P$ is on the perpendicular bisector of $(0,0)$-$(4,2)$: midpoint $(2, 1)$, gradient $-2$: $y = -2x + 5$. With $y = 2x - 1$: $4x = 6$, $x = \frac32$, $y = 2$. So $P = (\frac32, 2)$.", diff=2),

    Q("LIN-10", T, "MM3.1", r"""The line through $(a, 0)$ and $(0, b)$, with $a, b > 0$, passes through $(2, 3)$. Which of the following statements is/are true?

I. $\dfrac{2}{a} + \dfrac{3}{b} = 1$
II. $a > 2$ and $b > 3$
III. The smallest possible value of $ab$ is $24$""", ROMAN3, "H",
      r"The line is $\frac xa + \frac yb = 1$, so I holds. Since $\frac2a < 1$ and $\frac3b < 1$, II holds. $b = \frac{3a}{a-2}$, so $ab = \frac{3a^2}{a-2}$; setting $a = 2 + t$ gives $\frac{3(2+t)^2}{t} = 3\left(\frac4t + 4 + t\right) \geq 3(4 + 4) = 24$ by AM-GM (equality at $t = 2$, $a = 4$, $b = 6$). III holds.", paper=2, tags=("roman",), diff=3),

    Q("LIN-11", T, "MM3.1", r"The vertices of a triangle are $A(0, 0)$, $B(6, 0)$ and $C(2, 4)$. Find the equation of the line through $C$ that bisects the area of the triangle.",
      [r"$y = 4x - 4$", r"$y = -4x + 12$", r"$y = 2x$", r"$y = x + 2$", r"$y = -2x + 8$", r"$x = 2$"], "B",
      r"A line through a vertex bisects the area iff it passes through the midpoint of the opposite side, $(3, 0)$. Through $(2, 4)$ and $(3, 0)$: gradient $-4$, $y = -4x + 12$.", diff=2),

    Q("LIN-12", T, "MM3.1", r"The lines $y = mx + 4$ and $y = 3x - 2$ intersect at a point with positive $x$- and $y$-coordinates. Find the complete set of values of $m$.",
      [r"$-6 < m < 3$", r"$m < 3$", r"$m > -6$", r"$m < -6$ or $m > 3$", r"$0 < m < 3$", r"$-6 < m < 0$"], "A",
      r"$mx + 4 = 3x - 2 \Rightarrow x = \frac{6}{3 - m}$, which is positive iff $m < 3$. Then $y = 3x - 2 > 0$ iff $x > \frac23$, i.e. $\frac{6}{3-m} > \frac23$; with $3 - m > 0$ this is $18 > 6 - 2m$, i.e. $m > -6$. So $-6 < m < 3$.", diff=2),

    Q("LIN-13", T, "MM3.1", r"The distance between the parallel lines $3x + 4y = 5$ and $3x + 4y = 20$ is",
      ["$3$", "$15$", "$5$", "$4$", r"$\dfrac{15}{7}$", "$1$"], "A",
      r"The lines are $3x + 4y = c$; the perpendicular direction is $(3, 4)$ of length $5$. Distance $= \frac{|20 - 5|}{5} = 3$. (Alternatively, the point $(0, \frac54)$ on the first line is $3$ from the second.)", diff=2),

    Q("LIN-14", T, "MM3.1", r"A line passes through $(1, 2)$ with gradient $m$. It crosses the $x$-axis at $A$ and the $y$-axis at $B$, and the midpoint of $AB$ is $(1, 2)$. Find $m$.",
      ["$-2$", "$2$", r"$-\dfrac12$", r"$\dfrac12$", "$-1$", "$-4$"], "A",
      r"Midpoint $(1, 2)$ means $A = (2, 0)$ and $B = (0, 4)$. Gradient $= \frac{4 - 0}{0 - 2} = -2$.", diff=1),
]
