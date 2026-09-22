"""Full teaching solutions: the logic of arguments (LGC-xx)."""
from gen.model import Sol

SOLUTIONS = {

"LGC-01": Sol(
    idea=r"The four relatives of an implication. Given $A \Rightarrow B$, you must be able to write the converse, inverse and contrapositive without hesitating.",
    steps=[
        (r"Name the parts: $A$ is '$n$ is a multiple of $6$', $B$ is '$n$ is a multiple of $3$'.",
         r"Always label before manipulating - most errors here are bookkeeping errors."),
        (r"The contrapositive is 'if not $B$ then not $A$': **if $n$ is not a multiple of $3$, then $n$ is not a multiple of $6$**.",
         r"Negate both parts **and** swap them. Doing only one of the two gives the wrong relative."),
        (r"Sanity-check the meaning: if $3$ does not divide $n$, then $6$ certainly cannot, since every multiple of $6$ is a multiple of $3$.",
         r"The contrapositive is logically **equivalent** to the original, so it must also be true - a free check."),
    ],
    pitfalls=[r"Choosing 'if $n$ is a multiple of $3$ then $n$ is a multiple of $6$' - that is the **converse** (swap only), and it is false ($n=9$).",
              r"Choosing 'if $n$ is not a multiple of $6$ then $n$ is not a multiple of $3$' - the **inverse** (negate only), also false ($n=9$)."],
    takeaway=r"Converse: swap. Inverse: negate. Contrapositive: swap **and** negate - and only the contrapositive is equivalent to the original."),

"LGC-02": Sol(
    idea=r"Necessary/sufficient questions are two separate yes-no checks: does $P \Rightarrow Q$? does $Q \Rightarrow P$?",
    steps=[
        (r"Test sufficiency ($P \Rightarrow Q$): if $x > 2$ then $x^2 > 4$. **True**, so $P$ is sufficient.",
         r"Squaring preserves the inequality for positive numbers."),
        (r"Test necessity ($Q \Rightarrow P$): try to break it. $x = -3$ gives $x^2 = 9 > 4$ but $x \not> 2$.",
         r"One counterexample is enough to destroy an implication; negative numbers are the obvious place to look when squaring."),
        (r"So $P$ is sufficient but not necessary.",
         r"Sufficient $=$ 'enough to guarantee'; necessary $=$ 'can't do without'."),
    ],
    pitfalls=[r"Getting the direction backwards: '$P$ is necessary for $Q$' means $Q \Rightarrow P$, not $P \Rightarrow Q$.",
              r"Only checking positive $x$ and concluding the two are equivalent."],
    takeaway=r"$P$ sufficient for $Q$ means $P \Rightarrow Q$; $P$ necessary for $Q$ means $Q \Rightarrow P$. Check each direction separately, hunting for counterexamples."),

"LGC-03": Sol(
    idea=r"Negating a universal statement. 'All' flips to 'at least one', and the property inside flips too.",
    steps=[
        (r"Write it formally: 'for all students $s$, mark$(s) > 50$'.",
         r"Formalising stops the English from misleading you."),
        (r"Negate: 'there exists a student $s$ with mark$(s) \not> 50$'.",
         r"$\neg \forall x\, P(x) \equiv \exists x\, \neg P(x)$: the quantifier flips and the inside is negated."),
        (r"Translate $\not> 50$ into '$\leq 50$', i.e. **$50$ or less**.",
         r"The negation of 'greater than' is 'less than **or equal to**' - the boundary belongs to the negation."),
        (r"So: at least one student scored $50$ or less.",
         r"One failure is all it takes to make 'every' false."),
    ],
    pitfalls=[r"Over-negating to 'every student scored $50$ or less' - that is far stronger than the negation and is not implied.",
              r"Writing 'less than $50$' and losing the case of exactly $50$."],
    takeaway=r"Negating 'all ... are' gives 'at least one ... is not' - and remember $\neg(x > a)$ is $x \leq a$."),

"LGC-04": Sol(
    idea=r"Judge a statement and its converse separately. Each needs either a proof or a counterexample.",
    steps=[
        (r"The statement: if $x^2 = x$ then $x = 1$. Solve $x^2 = x$: $x(x-1) = 0$, so $x = 0$ or $x = 1$.",
         r"Never divide by $x$ - that is exactly how the root $x = 0$ gets lost."),
        (r"$x = 0$ satisfies the hypothesis but not the conclusion, so the statement is **false**.",
         r"A single counterexample settles it."),
        (r"The converse: if $x = 1$ then $x^2 = x$. Substituting gives $1 = 1$. **True.**",
         r"Verifying one value is enough because the hypothesis pins $x$ down completely."),
        (r"So: false statement, true converse.",
         r"Match to the option list."),
    ],
    pitfalls=[r"Dividing $x^2 = x$ by $x$, getting only $x = 1$, and wrongly declaring the statement true.",
              r"Assuming a false statement must have a false converse - the two are independent."],
    takeaway=r"A statement and its converse have no logical connection; test each on its own, and never divide an equation by a variable."),

"LGC-05": Sol(
    idea=r"Quantifier **order** matters. '$\forall x \exists y$' and '$\exists y \forall x$' say completely different things.",
    steps=[
        (r"I: for each $x$, can I find a bigger $y$? Take $y = x + 1$. **True.**",
         r"$y$ is allowed to depend on $x$, because $x$ is chosen first."),
        (r"II: is there a single $y$ bigger than **every** real $x$? That would be a largest real number. Taking $x = y$ contradicts $y > x$. **False.**",
         r"Here $y$ is fixed **before** $x$, so it must work for all $x$ at once - including $x = y$."),
        (r"III: for each $x$ is there $y$ with $xy = 1$? For $x = 0$, $0 \cdot y = 0 \neq 1$. **False.**",
         r"'For every $x$' includes the awkward cases; zero has no reciprocal."),
        (r"So I only.",
         r"Match to the list."),
    ],
    pitfalls=[r"Reading I and II as the same statement - the difference is the order of the quantifiers, nothing else.",
              r"Forgetting $x = 0$ in III and accepting $y = \frac1x$ uncritically."],
    takeaway=r"In $\forall x \exists y$ the $y$ may depend on $x$; in $\exists y \forall x$ one $y$ must serve every $x$. And 'for every' always includes the edge cases."),

"LGC-06": Sol(
    idea=r"The phrase 'only if' is the one piece of logical English almost everyone mistranslates. '$A$ only if $B$' means $A \Rightarrow B$.",
    steps=[
        (r"Let $A$ = 'you pass', $B$ = 'you revise'. The sentence is '$A$ only if $B$'.",
         r"Label first."),
        (r"'$A$ only if $B$' says that $A$ can happen **only** in the case that $B$ holds - so $A$ forces $B$: $A \Rightarrow B$.",
         r"Compare with '$A$ if $B$', which is the other direction $B \Rightarrow A$. 'Only if' and 'if' point opposite ways."),
        (r"Translate back: **if you pass, then you revised**.",
         r"Revising is necessary for passing, but the teacher promises no guarantee that it is enough."),
    ],
    pitfalls=[r"Reading it as 'if you revise, you will pass' - the converse, and a much stronger promise than the teacher made.",
              r"Reading it as 'if and only if'; 'only if' gives one direction only.",
              r"Choosing 'if you do not pass then you did not revise' - the inverse, not equivalent (the correct contrapositive is 'if you did not revise, you did not pass')."],
    takeaway=r"'$A$ if $B$' means $B \Rightarrow A$; '$A$ only if $B$' means $A \Rightarrow B$. 'Only if' marks the **necessary** condition."),

"LGC-07": Sol(
    idea=r"The same two-direction test, now in geometry. Look for a shape satisfying one condition but not the other.",
    steps=[
        (r"Sufficiency: every square has four equal sides, so $P \Rightarrow Q$. **True.**",
         r"Straight from the definition of a square."),
        (r"Necessity: does four equal sides force a square? A rhombus with angles $60^\circ$ and $120^\circ$ has four equal sides and is not a square.",
         r"A square also needs right angles; equal sides alone do not fix the angles."),
        (r"So $P$ is sufficient but not necessary for $Q$.",
         r"$P$ is the stronger condition, so it implies the weaker one but not conversely."),
    ],
    pitfalls=[r"Confusing which is the stronger condition: the more demanding property (square) is sufficient for the less demanding one (four equal sides).",
              r"Failing to produce a concrete counterexample and guessing."],
    takeaway=r"A stronger condition is sufficient for a weaker one; the weaker is necessary for the stronger. Name a counterexample to confirm."),

"LGC-08": Sol(
    idea=r"Negating an existential statement whose inside is already a negation - so two flips happen.",
    steps=[
        (r"Formalise: '$\exists n$ such that $n^2+n+41$ is **not** prime'.",
         r"Note the inner 'not'."),
        (r"Negate the quantifier: $\neg\exists n\, P(n) \equiv \forall n\, \neg P(n)$.",
         r"'There is one' becomes 'there is none', i.e. 'every one fails'."),
        (r"Negate the inside: 'not (not prime)' $=$ 'prime'.",
         r"Double negation cancels."),
        (r"Result: **for every positive integer $n$, $n^2+n+41$ is prime**.",
         r"Exactly one of the original and this is true; in fact this one is false, since $n = 41$ gives $41^2+41+41 = 41 \times 43$."),
    ],
    pitfalls=[r"Leaving the inner 'not' in place: 'for every $n$, $n^2+n+41$ is not prime' - that negates the quantifier but not the property.",
              r"Keeping 'there exists' and only flipping the property."],
    takeaway=r"$\neg\exists x\,\neg P(x) \equiv \forall x\, P(x)$: flip the quantifier **and** the statement inside."),

"LGC-09": Sol(
    idea=r"One inequality, examined three ways. The contrapositive is free once the statement is settled; the converse must be tested separately.",
    steps=[
        (r"I: for $x > 0$, write $x + \dfrac1x - 2 = \dfrac{x^2 - 2x + 1}{x} = \dfrac{(x-1)^2}{x}$.",
         r"Put over a common denominator - the numerator turns out to be a perfect square."),
        (r"Since $(x-1)^2 \geq 0$ and $x > 0$, the fraction is $\geq 0$, so $x + \frac1x \geq 2$. **True.**",
         r"A non-negative numerator over a positive denominator is non-negative. Equality at $x = 1$."),
        (r"III: the contrapositive of a true statement is automatically **true**.",
         r"No work needed - contrapositive and original are logically equivalent."),
        (r"II (the converse): suppose $x + \frac1x \geq 2$; must $x > 0$? If $x < 0$ then both $x$ and $\frac1x$ are negative, so $x + \frac1x < 0 < 2$ - the hypothesis fails. And $x = 0$ is not allowed. So $x > 0$. **True.**",
         r"Proved by eliminating the alternatives, which is itself a contrapositive argument."),
        (r"So all three.",
         r"Match to the list."),
    ],
    pitfalls=[r"Assuming the converse is false because converses 'usually' are - here it genuinely holds.",
              r"Multiplying the inequality $x + \frac1x \geq 2$ by $x$ without knowing the sign of $x$; that is precisely what is in question."],
    takeaway=r"$x + \frac1x \geq 2$ for $x>0$ is worth knowing; and a statement always shares its truth value with its contrapositive, never necessarily with its converse."),

"LGC-10": Sol(
    idea=r"The squaring trap again, in its purest form.",
    steps=[
        (r"Sufficiency: if $a = b$ then squaring both sides gives $a^2 = b^2$. **True.**",
         r"Doing the same thing to equal quantities keeps them equal."),
        (r"Necessity: does $a^2 = b^2$ force $a = b$? Take $a = 1$, $b = -1$: $1 = 1$ but $a \neq b$.",
         r"$a^2 = b^2$ only gives $a = \pm b$."),
        (r"So $P$ is sufficient but not necessary.",
         r"Squaring loses sign information, so it cannot be reversed."),
    ],
    pitfalls=[r"Treating squaring as reversible - it is exactly this that makes squaring an equation introduce extra solutions.",
              r"Only trying positive values."],
    takeaway=r"$a = b \Rightarrow a^2 = b^2$, but $a^2 = b^2 \Rightarrow a = \pm b$. Squaring is a one-way street."),

"LGC-11": Sol(
    idea=r"Given a true implication, only one of the three relatives is guaranteed. Identify which of I, II, III is the contrapositive.",
    steps=[
        (r"I is 'isosceles $\Rightarrow$ equilateral' - the **converse**. Not guaranteed, and here false (a $3,3,5$ triangle).",
         r"Swapped but not negated."),
        (r"II is 'not isosceles $\Rightarrow$ not equilateral' - the **contrapositive**. Always guaranteed. **True.**",
         r"Swapped and negated; logically equivalent to the original."),
        (r"III is 'not equilateral $\Rightarrow$ not isosceles' - the **inverse**. Not guaranteed, and here false (the same $3,3,5$ triangle).",
         r"Negated but not swapped - and the inverse is just the contrapositive of the converse, so it carries the converse's truth value, not the original's."),
        (r"So II only.",
         r"Match to the list."),
    ],
    pitfalls=[r"Accepting III because both its parts are negated - negation alone is not enough; the parts must also swap.",
              r"Accepting I because equilateral triangles are also isosceles - that supports the original, not the converse."],
    takeaway=r"From $A \Rightarrow B$ you get exactly one free statement: $\neg B \Rightarrow \neg A$."),

"LGC-12": Sol(
    idea=r"An $\exists \forall$ statement: you only need to produce **one** $k$ that works for **all** $x$. Then check why the offered reasons are right or wrong.",
    steps=[
        (r"Try $k = 0$: $x^2 + 1 > 0$ for every real $x$, since $x^2 \geq 0$.",
         r"One successful witness proves an existential statement."),
        (r"So the statement is true. Now check the reason offered with each claim.",
         r"In a 'true because...' question both the verdict **and** the justification must be right."),
        (r"Is it true for **every** $k$? No: the condition is discriminant $< 0$, i.e. $k^2 - 4 < 0$, so only $-2 < k < 2$.",
         r"A positive quadratic with no real roots never crosses the axis."),
        (r"And $k = 2$ gives $(x+1)^2$, which equals $0$ at $x = -1$ - so that witness fails the strict inequality.",
         r"The boundary case of the discriminant gives $\geq 0$, not $> 0$."),
        (r"So: true, with $k = 0$ as the witness.",
         r"Match to the list."),
    ],
    pitfalls=[r"Claiming it holds for all $k$ - $k = 5$ gives $x^2+5x+1$, which is negative at $x = -1$.",
              r"Offering $k = 2$ as the witness, which fails only at the single point $x = -1$ - easy to miss.",
              r"Thinking a quadratic with a positive $x^2$ coefficient must eventually be negative; it is large **positive** for large $|x|$."],
    takeaway=r"To prove $\exists$, exhibit one witness - but check the witness satisfies the condition **strictly** where required."),

"LGC-13": Sol(
    idea=r"De Morgan's law: negating an 'and' turns it into an 'or', with both parts negated.",
    steps=[
        (r"$\neg(A \text{ and } B) \equiv (\neg A) \text{ or } (\neg B)$.",
         r"For the conjunction to fail, it is enough that **one** part fails."),
        (r"Negate the first part: $\neg(x > 3)$ is $x \leq 3$.",
         r"The boundary $x = 3$ satisfies the negation, since $3 > 3$ is false."),
        (r"Negate the second: $\neg(y \leq 5)$ is $y > 5$.",
         r"Strict inequality, because $y = 5$ satisfied the original."),
        (r"Combine with 'or': $x \leq 3$ **or** $y > 5$.",
         r"The joining word flips too - this is the half most often forgotten."),
    ],
    pitfalls=[r"Keeping 'and': '$x \leq 3$ and $y > 5$' is far too strong - it demands both failures.",
              r"Getting the boundaries wrong: writing $x < 3$ or $y \geq 5$, which mishandles $x = 3$ and $y = 5$."],
    takeaway=r"De Morgan: not(A and B) $=$ notA or notB; not(A or B) $=$ notA and notB. Negate the connective as well as the parts."),

"LGC-14": Sol(
    idea=r"Statement and converse again, with the classic $n = 2$ counterexample.",
    steps=[
        (r"Statement: primes are odd? $n = 2$ is prime and even. **False.**",
         r"$2$ is the only even prime - it is the standard counterexample and worth memorising."),
        (r"Converse: odd numbers are prime? $n = 9 = 3 \times 3$ is odd and composite. **False.**",
         r"Also $n = 1$, which is odd and not prime by definition."),
        (r"So both are false.",
         r"Match to the option list."),
    ],
    pitfalls=[r"Forgetting that $2$ is prime and declaring the statement true.",
              r"Forgetting that $1$ is **not** prime when hunting counterexamples."],
    takeaway=r"$2$ is the even prime and $1$ is not prime - the two facts behind most prime-related counterexamples."),

"LGC-15": Sol(
    idea=r"A genuine 'necessary **and** sufficient' case, dressed to look like the usual 'sufficient only'. You must prove both directions rather than assume a counterexample exists.",
    steps=[
        (r"Sufficiency: if $4 \mid n$, write $n = 4k$. Then $n^2 = 16k^2$, which is divisible by $8$. **True.**",
         r"$16$ is a multiple of $8$, so divisibility by $8$ follows immediately."),
        (r"Necessity: suppose $8 \mid n^2$. Then $n^2$ is even, so $n$ is even - write $n = 2m$.",
         r"An odd number squared is odd, so $n$ cannot be odd."),
        (r"Then $n^2 = 4m^2$, and $8 \mid 4m^2$ forces $2 \mid m^2$, so $m$ is even, say $m = 2j$.",
         r"Divide the divisibility through by the common factor $4$."),
        (r"So $n = 4j$, i.e. $4 \mid n$. Both directions hold: necessary **and** sufficient.",
         r"No counterexample exists, which is what distinguishes this from the usual pattern."),
    ],
    pitfalls=[r"Answering 'sufficient but not necessary' out of habit, without actually hunting for a counterexample. Test $n = 2$: $n^2 = 4$, not divisible by $8$ - so it is not a counterexample; $n = 6$: $36$, not divisible by $8$. The hunt keeps failing, which is the clue.",
              r"Assuming $8 \mid n^2 \Rightarrow 8 \mid n$ - false ($n = 4$ gives $n^2 = 16$)."],
    takeaway=r"Before declaring a condition 'not necessary', actually look for a counterexample; repeated failure to find one is a signal to prove the converse instead."),

"LGC-16": Sol(
    idea=r"Three quantified statements about squaring and ordering. Negative numbers decide all three.",
    steps=[
        (r"I: $x < y \Rightarrow x^2 < y^2$ for all reals? Take $x = -2$, $y = 1$: $-2 < 1$ but $4 > 1$. **False.**",
         r"Squaring is only order-preserving for non-negative numbers."),
        (r"II: for each $x$, is there $y$ with $x < y$ and $x^2 < y^2$? Take $y = |x| + 1$: then $y > x$ and $y > |x|$ so $y^2 > x^2$. **True.**",
         r"Choosing $y$ larger than $|x|$ guarantees both conditions at once - and $y$ may depend on $x$."),
        (r"III: do some $x < y$ have $x^2 > y^2$? The counterexample from I works: $x = -2$, $y = 1$. **True.**",
         r"Reuse the work - the same pair settles both."),
        (r"So II and III.",
         r"Match to the list."),
    ],
    pitfalls=[r"Accepting I by testing only positive numbers.",
              r"Rejecting II by picking a bad $y$; you get to choose $y$, so choose a helpful one."],
    takeaway=r"$x<y \Rightarrow x^2<y^2$ needs $0 \leq x$; and to prove $\forall x \exists y$, construct $y$ as a formula in $x$."),

"LGC-17": Sol(
    idea=r"Unpacking 'if and only if' into its two implications.",
    steps=[
        (r"'$A$ if and only if $B$' means both '$A$ if $B$' ($B \Rightarrow A$) and '$A$ only if $B$' ($A \Rightarrow B$).",
         r"The phrase is literally built from 'if' and 'only if' - each supplies one direction."),
        (r"With $A$: $x \geq 2$ and $B$: $x^3 \geq 8$, that is $(x \geq 2 \Rightarrow x^3 \geq 8)$ **and** $(x^3 \geq 8 \Rightarrow x \geq 2)$.",
         r"The conjunction of the implication and its converse."),
        (r"(Both happen to be true here, since cubing is increasing - but the question only asks for the equivalent form.)",
         r"Read what is asked: the structure, not the truth value."),
    ],
    pitfalls=[r"Giving only one implication - that is half the statement.",
              r"Joining the two with 'or' instead of 'and'."],
    takeaway=r"$A \Leftrightarrow B$ is exactly $(A \Rightarrow B)$ **and** $(B \Rightarrow A)$."),

"LGC-18": Sol(
    idea=r"Negating a nested $\forall \exists$ statement: work from the outside in, flipping one quantifier at a time.",
    steps=[
        (r"Formalise: $\forall n\ \exists p$ (prime) with $n < p < 2n$.",
         r"Two quantifiers, so two flips."),
        (r"Flip the outer: $\exists n$ such that $\neg[\exists p$ with $n<p<2n]$.",
         r"'For all' fails exactly when one case fails."),
        (r"Flip the inner: $\exists n$ such that $\forall$ primes $p$, $\neg(n<p<2n)$ - i.e. **no** prime lies strictly between $n$ and $2n$.",
         r"'There exists' fails exactly when every candidate fails."),
        (r"So: there is a positive integer $n$ for which no prime $p$ satisfies $n < p < 2n$.",
         r"(The original is Bertrand's postulate and is in fact true, so this negation is false - but the question is about form.)"),
    ],
    pitfalls=[r"Keeping 'for every $n$' and only negating the inside - that is a much stronger claim, not the negation.",
              r"Turning it into '$\exists n$ and $\exists p$ with $p \leq n$ or $p \geq 2n$', which is trivially true and says nothing: the inner quantifier must become **for all** primes."],
    takeaway=r"Negate nested quantifiers outside-in: each $\forall$ becomes $\exists$, each $\exists$ becomes $\forall$, and the innermost statement is negated once."),

"LGC-19": Sol(
    idea=r"Sometimes the two statements are the same by **definition** - recognise that and both directions are immediate.",
    steps=[
        (r"Recall the definition: $f$ has a stationary point at $x = a$ precisely when $f'(a) = 0$.",
         r"That is what 'stationary' means - the rate of change is zero."),
        (r"So $P \Rightarrow Q$ and $Q \Rightarrow P$ both hold trivially.",
         r"Definitions are biconditional."),
        (r"Hence $P$ is necessary and sufficient for $Q$.",
         r"Match to the option list."),
    ],
    pitfalls=[r"Confusing this with 'turning point': $f'(a) = 0$ does **not** guarantee a maximum or minimum ($y = x^3$ at $x=0$). But the question says stationary point, not turning point.",
              r"Worrying about functions that are not differentiable - the question states $f$ is defined and $f'(a)$ is referred to, so differentiability is assumed."],
    takeaway=r"A definition gives both implications at once; but stationary $\neq$ turning - the extra condition is a **sign change** in $f'$."),

"LGC-20": Sol(
    idea=r"Two standard equivalents of $A \Rightarrow B$: the contrapositive, and the disjunctive form 'not $A$, or $B$'.",
    steps=[
        (r"I: 'not $A$ or $B$'. An implication only fails when $A$ is true and $B$ false - exactly when '$\neg A$ or $B$' fails. **Equivalent.**",
         r"Check the one bad case: raining and ground dry makes both statements false; every other case makes both true."),
        (r"II: 'if the ground is not wet, it is not raining' - the contrapositive. **Equivalent.**",
         r"Swap and negate."),
        (r"III: 'if the ground is wet, it is raining' - the converse. **Not equivalent**; the ground could be wet from a burst pipe.",
         r"A concrete alternative cause is the cleanest refutation."),
        (r"So I and II.",
         r"Match to the list."),
    ],
    pitfalls=[r"Rejecting I because it looks nothing like an implication - test it against the single case that breaks an implication.",
              r"Accepting III because wet ground is evidence of rain; evidence is not implication."],
    takeaway=r"$A \Rightarrow B$ is equivalent both to 'not $A$, or $B$' and to $\neg B \Rightarrow \neg A$. The converse is never among the equivalents."),

"LGC-21": Sol(
    idea=r"A universal claim about a quadratic. Completing the square settles it, and the question also tests whether the **reason** given is sound.",
    steps=[
        (r"Complete the square: $x^2 - 6x + 10 = (x-3)^2 - 9 + 10 = (x-3)^2 + 1$.",
         r"Halve the coefficient of $x$ to get $-3$, then correct by $-(-3)^2 = -9$."),
        (r"$(x-3)^2 \geq 0$, so the expression is $\geq 1 > 0$ for every real $x$. **True.**",
         r"A square is never negative; the minimum value is $1$ at $x = 3$."),
        (r"Check the false reasons: $x = 3$ gives $9 - 18 + 10 = 1$, not $0$; and the discriminant $36 - 40 = -4 < 0$, so there are **no** real roots.",
         r"The claim that it has two real roots is simply wrong, and would in any case not prove positivity."),
    ],
    pitfalls=[r"Assuming any quadratic takes negative values - one with a positive leading coefficient and negative discriminant never does.",
              r"Mis-completing the square as $(x-3)^2 + 10$ or $(x-6)^2+1$."],
    takeaway=r"Completing the square proves positivity outright: $a(x-h)^2 + k$ with $a>0, k>0$ is always positive."),

"LGC-22": Sol(
    idea=r"This one reverses the usual direction - the check must be done carefully rather than by pattern-matching.",
    steps=[
        (r"Test '$P$ sufficient for $Q$', i.e. $ab = 0 \Rightarrow a = 0$: take $a = 5$, $b = 0$. Then $ab = 0$ but $a \neq 0$. **Not sufficient.**",
         r"The zero-product rule gives $a = 0$ **or** $b = 0$, not $a = 0$."),
        (r"Test '$P$ necessary for $Q$', i.e. $Q \Rightarrow P$: if $a = 0$ then $ab = 0 \cdot b = 0$. **True, so necessary.**",
         r"Anything times zero is zero."),
        (r"So $P$ is necessary but not sufficient for $Q$.",
         r"Note the direction: the **weaker** condition ($ab=0$) is necessary for the stronger one ($a=0$)."),
    ],
    pitfalls=[r"Answering 'sufficient but not necessary' by reflex - in this question the roles are swapped from the common pattern.",
              r"Thinking $ab = 0$ requires both to be zero."],
    takeaway=r"$ab = 0 \Rightarrow a = 0$ or $b = 0$; and always check both directions explicitly rather than assuming the familiar answer."),

"LGC-23": Sol(
    idea=r"A counterexample must make the hypothesis **true** and the conclusion **false**. Check both halves for each candidate.",
    steps=[
        (r"Hypothesis: both $a$ and $b$ irrational. Conclusion to break: $a + b$ irrational - so we need $a+b$ **rational**.",
         r"Only a case satisfying the hypothesis can refute the statement."),
        (r"$a = \sqrt2$, $b = -\sqrt2$: both irrational ✓, and $a + b = 0$, which is rational ✓. **Counterexample.**",
         r"$-\sqrt2$ is irrational: if it were rational, so would its negative be."),
        (r"Reject $a = 1, b = -1$: these are rational, so the hypothesis fails and nothing is refuted.",
         r"A case that does not satisfy the hypothesis says nothing about the implication."),
        (r"Reject $\sqrt2 + \sqrt3$, $\sqrt2 + 2\sqrt2 = 3\sqrt2$ and $\pi + \sqrt2$: each sum is irrational, so the conclusion holds and the statement is not broken.",
         r"These are examples **of** the statement, not against it."),
    ],
    pitfalls=[r"Picking rational numbers whose sum is rational - the hypothesis is not satisfied.",
              r"Picking irrationals whose sum is irrational - the conclusion is not broken."],
    takeaway=r"A counterexample satisfies the 'if' and violates the 'then'. Check both halves every time."),

"LGC-24": Sol(
    idea=r"What it takes to refute a universal statement - and what it takes to refute *this* one in particular.",
    steps=[
        (r"The statement has the form 'for all even $n > 2$, $P(n)$'.",
         r"Identify the quantifier and the domain: even numbers greater than $2$."),
        (r"Its negation is 'there exists an even $n > 2$ with $P(n)$ false'.",
         r"One failure suffices; you do not have to show the property fails often."),
        (r"So a counterexample is a single even number greater than $2$ that cannot be written as a sum of two primes.",
         r"It must lie in the stated domain **and** fail the property."),
        (r"(This is Goldbach's conjecture - no counterexample is known, which is why it remains a conjecture.)",
         r"Verifying billions of cases is not a proof; one counterexample would be a disproof."),
    ],
    pitfalls=[r"Offering an **odd** number that is not a sum of two primes - outside the stated domain, so irrelevant.",
              r"Offering an even number that **is** a sum of two primes - that confirms the statement, it does not refute it.",
              r"Thinking many confirming examples add up to a proof."],
    takeaway=r"To disprove 'for all', produce one object **in the domain** for which the property fails; confirming instances never prove it."),

}
