"""Trigonometric functions and equations (MM4.3-MM4.6)."""
from gen.model import Q, ROMAN3

T = "trig-functions"

QUESTIONS = [
    Q("TRG-01", T, "MM4.6", r"How many solutions does $\sin 2x = \dfrac{1}{2}$ have for $0 \leq x < 2\pi$?",
      ["$2$", "$3$", "$4$", "$6$", "$8$", "$1$"], "C",
      r"$2x$ runs over $[0, 4\pi)$, which contains two full periods of $\sin$, each giving two solutions: $4$ in total.", diff=1),

    Q("TRG-02", T, "MM4.5", r"Solve $2\cos^2 x + 3\sin x - 3 = 0$ for $0^\circ \leq x \leq 360^\circ$. How many solutions are there?",
      ["$1$", "$2$", "$3$", "$4$", "$0$", "$5$"], "C",
      r"$2(1 - \sin^2 x) + 3\sin x - 3 = 0 \Rightarrow 2\sin^2 x - 3\sin x + 1 = 0 \Rightarrow (2\sin x - 1)(\sin x - 1) = 0$. $\sin x = \frac12$: $30^\circ, 150^\circ$; $\sin x = 1$: $90^\circ$. Three solutions.", diff=2),

    Q("TRG-03", T, "MM4.3", r"Find the exact value of $\sin 60^\circ \cos 30^\circ + \cos 60^\circ \sin 30^\circ$.",
      ["$1$", r"$\dfrac{\sqrt3}{2}$", r"$\dfrac12$", r"$\dfrac{\sqrt3}{4}$", "$0$", r"$\dfrac{3}{4}$"], "A",
      r"$\frac{\sqrt3}{2}\cdot\frac{\sqrt3}{2} + \frac12\cdot\frac12 = \frac34 + \frac14 = 1$.", diff=1),

    Q("TRG-04", T, "MM4.6", r"Find the sum of all solutions of $\tan x = \sqrt{3}$ in the interval $0 \leq x \leq 2\pi$.",
      [r"$\dfrac{5\pi}{3}$", r"$\dfrac{4\pi}{3}$", r"$\pi$", r"$\dfrac{2\pi}{3}$", r"$\dfrac{7\pi}{3}$", r"$2\pi$"], "A",
      r"$x = \frac\pi3$ and $x = \frac\pi3 + \pi = \frac{4\pi}{3}$. Sum $\frac{5\pi}{3}$.", diff=1),

    Q("TRG-05", T, "MM4.4", r"""Which of the following statements about the graph of $y = \cos x$ is/are true?

I. It is symmetric about the $y$-axis.
II. It is a translation of the graph of $y = \sin x$ by $\dfrac{\pi}{2}$ in the negative $x$-direction.
III. It has period $\pi$.""", ROMAN3, "E",
      r"$\cos(-x) = \cos x$ so I is true. $\sin\left(x + \frac\pi2\right) = \cos x$, so II is true. The period of $\cos$ is $2\pi$, so III is false.", paper=2, tags=("roman",)),

    Q("TRG-06", T, "MM4.5", r"Given that $\sin\theta = \dfrac{3}{5}$ and $\theta$ is obtuse, find $\tan\theta$.",
      [r"$-\dfrac{3}{4}$", r"$\dfrac{3}{4}$", r"$-\dfrac{4}{3}$", r"$\dfrac{4}{3}$", r"$-\dfrac{3}{5}$", r"$-\dfrac{4}{5}$"], "A",
      r"$\cos\theta = -\frac45$ (negative in the second quadrant), so $\tan\theta = \frac{3/5}{-4/5} = -\frac34$.", diff=1),

    Q("TRG-07", T, "MM4.6", r"Solve $\sin^2 x = \dfrac{3}{4}$ for $0 \leq x < 2\pi$. How many solutions are there?",
      ["$4$", "$2$", "$1$", "$3$", "$6$", "$8$"], "A",
      r"$\sin x = \pm\frac{\sqrt3}{2}$: $x = \frac\pi3, \frac{2\pi}{3}, \frac{4\pi}{3}, \frac{5\pi}{3}$. Four solutions.", diff=1),

    Q("TRG-08", T, "MM4.6", r"Find the smallest positive solution of $\cos\left(x - \dfrac{\pi}{6}\right) = -\dfrac{1}{2}$.",
      [r"$\dfrac{5\pi}{6}$", r"$\dfrac{2\pi}{3}$", r"$\dfrac{\pi}{2}$", r"$\dfrac{3\pi}{2}$", r"$\dfrac{7\pi}{6}$", r"$\pi$"], "A",
      r"$x - \frac\pi6 = \frac{2\pi}{3}$ gives $x = \frac{5\pi}{6}$ (the other solution $x - \frac\pi6 = \frac{4\pi}{3}$ gives $\frac{3\pi}{2}$, larger).", diff=1),

    Q("TRG-09", T, "MM4.5", r"Simplify $\dfrac{1 - \cos^2\theta}{\cos\theta \tan\theta}$ for values of $\theta$ where the expression is defined.",
      [r"$\sin\theta$", r"$\cos\theta$", r"$\tan\theta$", r"$\sin^2\theta$", r"$1$", r"$\dfrac{\sin\theta}{\cos\theta}$"], "A",
      r"$\cos\theta\tan\theta = \sin\theta$, and $1 - \cos^2\theta = \sin^2\theta$. So the expression is $\sin\theta$.", diff=1),

    Q("TRG-10", T, "MM4.6", r"How many solutions does the equation $\sin x = \dfrac{x}{10}$ have?",
      ["$5$", "$6$", "$7$", "$3$", "$1$", "$9$"], "C",
      r"Solutions need $|x| \leq 10$. Both sides are odd functions, so count $x > 0$ and double, then add $x = 0$. On $(0, \pi)$ the curve starts above the line (since $\sin x \approx x$) and ends below it: one crossing. On $(\pi, 2\pi)$, $\sin x < 0$: none. On $(2\pi, 3\pi)$ the line is between $0.63$ and $0.94$ while $\sin x$ rises to $1$: two crossings ($3\pi \approx 9.42 < 10$). Beyond $4\pi > 10$ the line exceeds $1$. So $3$ positive, $3$ negative and $0$: seven solutions.", diff=3),

    Q("TRG-11", T, "MM4.4", r"The function $f(x) = 3\sin(2x) - 1$ is defined for all real $x$. Find the difference between its maximum and minimum values.",
      ["$6$", "$3$", "$4$", "$2$", "$7$", "$1$"], "A",
      r"Range is $[-4, 2]$; the difference is $6$.", diff=1),

    Q("TRG-12", T, "MM4.6", r"Find the number of solutions of $\tan^2 x = 3$ for $0 \leq x < 2\pi$.",
      ["$4$", "$2$", "$1$", "$3$", "$6$", "$8$"], "A",
      r"$\tan x = \pm\sqrt3$: $x = \frac\pi3, \frac{2\pi}{3}, \frac{4\pi}{3}, \frac{5\pi}{3}$. Four solutions.", diff=1),

    Q("TRG-13", T, "MM4.5", r"For all $\theta$ where the expressions are defined, $(\sin\theta + \cos\theta)^2 + (\sin\theta - \cos\theta)^2$ equals",
      ["$2$", "$1$", r"$2\sin^2\theta$", r"$2\cos^2\theta$", r"$2 + 2\sin\theta\cos\theta$", "$0$"], "A",
      r"Expanding: $(1 + 2\sin\theta\cos\theta) + (1 - 2\sin\theta\cos\theta) = 2$.", diff=1),

    Q("TRG-14", T, "MM4.6", r"Solve $12\cos^2 x + 6\sin x - 10 = 2$ for $0^\circ < x < 360^\circ$. Which of the following is the complete set of solutions?",
      [r"$30^\circ, 150^\circ, 180^\circ$", r"$30^\circ, 150^\circ, 210^\circ, 330^\circ$", r"$30^\circ, 150^\circ$", r"$30^\circ, 150^\circ, 270^\circ$", r"$0^\circ, 30^\circ, 150^\circ, 180^\circ$", r"$210^\circ, 330^\circ$"], "A",
      r"$12(1 - \sin^2x) + 6\sin x - 12 = 0 \Rightarrow 12\sin^2 x - 6\sin x = 0 \Rightarrow 6\sin x(2\sin x - 1) = 0$. $\sin x = 0$ gives $180^\circ$ (the endpoints $0^\circ$ and $360^\circ$ are excluded); $\sin x = \frac12$ gives $30^\circ$ and $150^\circ$.", diff=2),

    Q("TRG-15", T, "MM4.4", r"The graph of $y = \sin x$ (with $x$ in radians) crosses the line $y = x$ at how many points?",
      ["$1$", "$2$", "$3$", "$0$", "infinitely many"], "A",
      r"$|\sin x| < |x|$ for all $x \neq 0$, so the only intersection is at the origin.", diff=2),

    Q("TRG-16", T, "MM4.6", r"Given that $\sin x + \cos x = 0$ and $0 \leq x < 2\pi$, find the sum of all possible values of $x$.",
      [r"$\dfrac{5\pi}{2}$", r"$\dfrac{3\pi}{2}$", r"$\pi$", r"$2\pi$", r"$\dfrac{3\pi}{4}$", r"$\dfrac{7\pi}{4}$"], "A",
      r"$\tan x = -1$: $x = \frac{3\pi}{4}$ or $\frac{7\pi}{4}$. Sum $= \frac{10\pi}{4} = \frac{5\pi}{2}$.", diff=1),

    Q("TRG-17", T, "MM4.5", r"""Which of the following is/are true for all real $x$?

I. $\sin^2 x + \cos^2 x = 1$
II. $\sin(2x) = 2\sin x$
III. $\sin(x + \pi) = -\sin x$""", ROMAN3, "F",
      r"I is the Pythagorean identity. II is false (e.g. $x = \frac\pi2$: $0 \neq 2$). III: translating $\sin$ by half a period negates it, so III is true.", paper=2, tags=("roman",)),

    Q("TRG-18", T, "MM4.3", r"Find the value of $\tan 30^\circ \tan 60^\circ + \sin^2 45^\circ$.",
      [r"$\dfrac{3}{2}$", r"$1$", r"$\dfrac{1}{2}$", r"$2$", r"$1 + \sqrt3$", r"$\dfrac{\sqrt2}{2}$"], "A",
      r"$\tan30^\circ\tan60^\circ = \frac{1}{\sqrt3}\cdot\sqrt3 = 1$, $\sin^2 45^\circ = \frac12$. Total $\frac32$.", diff=1),
]
