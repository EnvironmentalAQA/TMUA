"""Identifying errors in proofs (Err1, Err2). All Paper 2."""
from gen.model import Q, ROMAN3

T = "errors"

QUESTIONS = [
    Q("ERR-01", T, "Err2", r"""A student attempts to solve the equation $\sqrt{x + 3} = x - 3$ for real $x$.

I. Squaring both sides: $x + 3 = (x - 3)^2 = x^2 - 6x + 9$.
II. So $x^2 - 7x + 6 = 0$.
III. So $(x - 1)(x - 6) = 0$.
IV. Hence the solutions are $x = 1$ and $x = 6$.

Which of the following best describes the solution?""",
      ["The solution is wrong, and the first error occurs on line IV.", "The solution is completely correct.", "The solution is wrong, and the first error occurs on line I.", "The solution is wrong, and the first error occurs on line II.", "The solution is wrong, and the first error occurs on line III."], "A",
      r"Squaring can introduce extraneous solutions, so line IV should check them: $x = 1$ gives $\sqrt4 = 2 \neq -2$. Only $x = 6$ works. Lines I-III are valid deductions.", diff=1, tags=("fixed",)),

    Q("ERR-02", T, "Err2", r"""Here is a purported proof that $1 = 2$.

I. Let $a = b$, with $a \neq 0$.
II. Then $a^2 = ab$.
III. So $a^2 - b^2 = ab - b^2$, i.e. $(a - b)(a + b) = b(a - b)$.
IV. Dividing both sides by $(a - b)$: $a + b = b$.
V. So $2b = b$, and hence $2 = 1$.

On which line does the first error occur?""",
      ["IV", "II", "III", "V", "I"], "A",
      r"Since $a = b$, $a - b = 0$ and dividing by zero is invalid.", diff=1, tags=("fixed",)),

    Q("ERR-03", T, "Err2", r"""A student tries to solve $\sin\theta = \sin 40^\circ$ for $0^\circ \leq \theta < 360^\circ$.

I. Since $\sin\theta = \sin 40^\circ$, we have $\theta = 40^\circ$.
II. The sine function has period $360^\circ$, so $\theta = 40^\circ + 360^\circ k$.
III. In the given interval the only solution is $\theta = 40^\circ$.

Which of the following is correct?""",
      [r"The first error is on line I: $\sin\theta = \sin\alpha$ does not imply $\theta = \alpha$; $\theta = 140^\circ$ is also a solution.", "The solution is completely correct.", r"The first error is on line II: the period of sine is $180^\circ$.", r"The first error is on line III: $\theta = 400^\circ$ should be included.", r"The first error is on line II: it should be $\theta = 40^\circ + 180^\circ k$."], "A",
      r"'If $\sin\alpha = \sin\beta$ then $\alpha = \beta$' is a classic invalid deduction; $\sin(180^\circ - 40^\circ) = \sin40^\circ$ too.", diff=1, tags=("fixed",)),

    Q("ERR-04", T, "Err1", r"""Claim: for all real $x$, if $x^2 > 9$ then $x > 3$.

I. Suppose $x^2 > 9$.
II. Taking square roots of both sides, $x > 3$.
III. This proves the claim.

Which of the following is true?""",
      ["The claim is false; the first error is on line II, since $x = -4$ satisfies $x^2 > 9$ but not $x > 3$.", "The claim and proof are both correct.", "The claim is true but line II should say $|x| > 3$ and then deduce $x > 3$.", "The claim is false; the first error is on line I.", "The claim is true; the first error is on line III."], "A",
      r"$x^2 > 9$ gives $|x| > 3$, i.e. $x > 3$ or $x < -3$. The claim itself is false, and line II is where the invalid deduction happens.", diff=1, tags=("fixed",)),

    Q("ERR-05", T, "Err2", r"""A student solves the inequality $\dfrac{x + 1}{x - 2} < 3$.

I. Multiply both sides by $(x - 2)$: $x + 1 < 3x - 6$.
II. So $7 < 2x$.
III. So $x > \dfrac{7}{2}$.

Which of the following is correct?""",
      ["The first error is on line I: multiplying by $x - 2$ is only valid as written when $x - 2 > 0$.", "The solution is completely correct.", "The first error is on line II: it should be $7 < 4x$.", r"The first error is on line III: it should be $x < \frac72$.", "The first error is on line I: you cannot multiply an inequality by an expression."], "A",
      r"For $x < 2$ the multiplier is negative and the inequality reverses; indeed $x = 0$ gives $-\frac12 < 3$, a solution missed by the student. The full solution set is $x < 2$ or $x > \frac72$.", diff=2, tags=("fixed",)),

    Q("ERR-06", T, "Err1", r"""Claim: the function $f(x) = x^3 - 3x^2 + 3x$ is increasing for all real $x$.

I. $f'(x) = 3x^2 - 6x + 3 = 3(x - 1)^2$.
II. So $f'(x) \geq 0$ for all $x$, with equality only at $x = 1$.
III. Since $f'(x) > 0$ for all $x$, $f$ is increasing.

Which of the following is true?""",
      ["Line III overstates what was shown: $f'(1) = 0$; but $f$ is still increasing for all $x$, so the claim is true and the proof needs a better justification.", "The proof is completely correct.", "The first error is on line I.", "The first error is on line II: $f'(x)$ can be negative.", "The claim is false: $f$ has a turning point at $x = 1$."], "A",
      r"$f$ is (strictly) increasing because $f'(x) \geq 0$ with equality only at an isolated point, so $f(a) < f(b)$ whenever $a < b$; but line III's assertion '$f'(x) > 0$ for all $x$' is false at $x = 1$. There is no turning point at $x = 1$ (the derivative does not change sign).", diff=3, tags=("fixed",)),

    Q("ERR-07", T, "Err2", r"""A student writes the following argument.

I. $0.1 > 0.01$.
II. Taking logarithms to base $10$ of both sides: $-1 > -2$.
III. Multiplying both sides by $\log_{10}\frac12$, which is negative, reverses the inequality: $-\log_{10}\frac12 < -2\log_{10}\frac12$.

Which of the following is correct?""",
      ["All three lines are correct.", "Line II is wrong: taking logarithms reverses an inequality.", r"Line III is wrong: $\log_{10}\frac12$ is positive.", r"Line II is wrong: $\log_{10} 0.1 = 1$.", "Line I is wrong."], "A",
      r"Logarithms are increasing functions, so line II is valid; $\log_{10}\frac12 < 0$, so reversing the inequality in line III is correct.", diff=2, tags=("fixed",)),

    Q("ERR-08", T, "Err1", r"""Claim: if $n$ is an integer and $n^2$ is divisible by $4$, then $n$ is divisible by $4$.

I. Suppose $n^2$ is divisible by $4$.
II. Then $n^2 = 4k$ for some integer $k$.
III. So $n = 2\sqrt{k}$, and since $n$ is an integer $\sqrt k$ is an integer.
IV. Hence $n$ is even, so $n = 2m$, and $n^2 = 4m^2$ is divisible by $4$, so $n$ is divisible by $4$.

Which of the following is true?""",
      ["The claim is false ($n = 2$ is a counterexample) and the first invalid step is on line IV.", "The claim and proof are correct.", "The claim is true but the first error is on line III.", "The claim is false and the first error is on line II.", "The claim is false and the first error is on line I."], "A",
      r"$n = 2$: $n^2 = 4$ is divisible by $4$ but $n$ is not. Lines I-III are correct deductions ($n$ even). Line IV concludes '$n$ divisible by $4$' from '$n^2$ divisible by $4$', which is exactly the unproved claim - circular and false.", diff=2, tags=("fixed",)),

    Q("ERR-09", T, "Err2", r"""A student proves that the equation $x^2 + 2x + 3 = 0$ has no real solutions.

I. Complete the square: $x^2 + 2x + 3 = (x + 1)^2 + 2$.
II. $(x + 1)^2 \geq 0$ for all real $x$.
III. So $(x + 1)^2 + 2 \geq 2 > 0$ for all real $x$.
IV. Hence the equation has no real solutions.

Which of the following is correct?""",
      ["The proof is completely correct.", "The first error is on line I.", "The first error is on line II: $(x + 1)^2$ can be negative.", "The first error is on line III.", "The first error is on line IV: a positive expression can still equal zero."], "A",
      r"Every step is valid.", diff=1, tags=("fixed",)),

    Q("ERR-10", T, "Err2", r"""Claim: if $a > b$ then $\dfrac{1}{a} < \dfrac{1}{b}$.

I. Suppose $a > b$.
II. Dividing both sides by $ab$: $\dfrac{1}{b} > \dfrac{1}{a}$.
III. So $\dfrac1a < \dfrac1b$.

Which of the following is correct?""",
      ["The claim is false in general and the first error is on line II, since $ab$ may be negative or zero.", "The claim and proof are correct.", "The first error is on line III.", "The claim is true but the first error is on line I.", "The claim is false and the first error is on line III."], "A",
      r"$a = 1$, $b = -1$: $a > b$ but $\frac1a = 1 > -1 = \frac1b$. Dividing by $ab$ without knowing its sign is invalid (and $b = 0$ would be division by zero).", diff=1, tags=("fixed",)),

    Q("ERR-11", T, "Err1", r"""Claim: $\displaystyle\int_{-1}^{1} \frac{1}{x^2}\,dx = -2$.

I. An antiderivative of $x^{-2}$ is $-x^{-1}$.
II. So the integral equals $\left[-\frac1x\right]_{-1}^{1} = -1 - 1 = -2$.
III. Hence the value is $-2$.

Which of the following is correct?""",
      ["The first error is on line II: the integrand is undefined at $x = 0$, which lies inside the interval, so the fundamental theorem cannot be applied.", "The proof is completely correct.", "The first error is on line I.", "The first error is on line II: $-1 - 1 = 0$.", "The first error is on line III: the value should be $+2$."], "A",
      r"The integrand is positive everywhere it is defined, so a negative answer is a warning sign; the function is not defined on the whole interval and the integral does not exist in the ordinary sense.", diff=2, tags=("fixed",)),

    Q("ERR-12", T, "Err2", r"""A student solves $x^2 = 4x$.

I. Divide both sides by $x$: $x = 4$.
II. So the only solution is $x = 4$.

Which of the following is correct?""",
      ["The first error is on line I: dividing by $x$ discards the solution $x = 0$.", "The solution is completely correct.", "The first error is on line II.", r"The first error is on line I: $x^2 \div x = 2x$.", "The first error is on line I: it should give $x = 2$."], "A",
      r"Factorise instead: $x(x - 4) = 0$ gives $x = 0$ or $x = 4$.", diff=1, tags=("fixed",)),

    Q("ERR-13", T, "Err1", r"""Claim: for all positive real $x$, $x + \dfrac{1}{x} \geq 2$.

I. Suppose $x + \dfrac1x \geq 2$.
II. Multiply by $x > 0$: $x^2 + 1 \geq 2x$.
III. So $x^2 - 2x + 1 \geq 0$, i.e. $(x - 1)^2 \geq 0$, which is true.
IV. Hence the claim is proved.

Which of the following best describes the argument?""",
      [r"The argument assumes what it is trying to prove (line I); it would be valid if the steps were reversed, starting from $(x - 1)^2 \geq 0$.", "The argument is completely correct as written.", "The first error is on line II: multiplying by $x$ reverses the inequality.", "The first error is on line III.", "The claim is false."], "A",
      r"Starting from the conclusion and reaching a truth does not prove the conclusion unless every step is reversible and the argument is presented in the forward direction. Here the steps are reversible, so the repair is to write it backwards.", diff=2, tags=("fixed",)),

    Q("ERR-14", T, "Err2", r"""Claim: if $x$ and $y$ are real with $x^2 = y^2$, then $x = y$.

Which of the following is a counterexample to the claim?""",
      [r"$x = 2$, $y = -2$", r"$x = 2$, $y = 2$", r"$x = 0$, $y = 0$", r"$x = 1$, $y = 2$", r"$x = -1$, $y = -1$"], "A",
      r"A counterexample must satisfy the hypothesis ($x^2 = y^2$) and fail the conclusion ($x \neq y$).", diff=1),

    Q("ERR-15", T, "Err1", r"""Claim: the sum of the first $n$ odd numbers is $n^2$.

I. The first odd number is $1 = 1^2$, so the claim holds for $n = 1$.
II. Suppose the claim holds for some $n$, i.e. $1 + 3 + \cdots + (2n - 1) = n^2$.
III. Adding the next odd number, $2n + 1$, gives $n^2 + 2n + 1 = (n + 1)^2$.
IV. So the claim holds for $n + 1$, and hence for all positive integers $n$.

Which of the following is correct?""",
      ["The proof is completely correct.", "The first error is on line II: you cannot assume the claim.", "The first error is on line III: the next odd number is $2n - 1$.", "The first error is on line IV: it only shows the claim for $n + 1$.", "The first error is on line I."], "A",
      r"This is a valid proof by induction: a base case, and a step showing that truth for $n$ implies truth for $n + 1$.", diff=2, tags=("fixed",)),

    Q("ERR-16", T, "Err2", r"""A student argues: 'Every prime number is odd, because if it were even it would be divisible by $2$ and so not prime.' Which of the following is correct?""",
      ["The argument is wrong because $2$ is even and prime: being divisible by $2$ does not stop $2$ itself being prime.", "The argument is correct.", "The argument is wrong because some odd numbers are not prime.", "The argument is wrong because $1$ is odd and not prime.", "The argument is wrong because $0$ is even."], "A",
      r"A number divisible by $2$ is not prime unless it equals $2$. The conclusion 'every prime is odd' is false.", diff=1, tags=("fixed",)),

    Q("ERR-17", T, "Err1", r"""Claim: if $f'(a) = 0$ and $f''(a) = 0$ then $f$ has a point of inflexion at $x = a$.

Which of the following shows the claim is false?""",
      [r"$f(x) = x^4$ at $a = 0$", r"$f(x) = x^3$ at $a = 0$", r"$f(x) = x^2$ at $a = 0$", r"$f(x) = x^3 - 3x$ at $a = 1$", r"$f(x) = x$ at $a = 0$"], "A",
      r"$x^4$ has $f'(0) = f''(0) = 0$ but a minimum at $0$, not an inflexion. ($x^3$ does have an inflexion; $x^2$ has $f''(0) \neq 0$.)", diff=2),

    Q("ERR-18", T, "Err2", r"""A student solves $2\cos^2 x = \cos x$ for $0 \leq x < 2\pi$.

I. Divide both sides by $\cos x$: $2\cos x = 1$.
II. So $\cos x = \dfrac12$.
III. So $x = \dfrac{\pi}{3}$ or $x = \dfrac{5\pi}{3}$.

How many solutions has the student missed, and where is the first error?""",
      ["Two solutions missed; the first error is on line I.", "No solutions missed; the working is correct.", "One solution missed; the first error is on line III.", "Two solutions missed; the first error is on line III.", "One solution missed; the first error is on line I."], "A",
      r"Dividing by $\cos x$ loses $\cos x = 0$, i.e. $x = \frac\pi2$ and $x = \frac{3\pi}{2}$: two solutions.", diff=1, tags=("fixed",)),
]
