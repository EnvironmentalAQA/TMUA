"""Full teaching solutions: mathematical proof (PRF-xx)."""
from gen.model import Sol

SOLUTIONS = {

"PRF-01": Sol(
    idea=r"What makes a proof **complete**: it must cover every case in the claim with a general argument, not a sample of values.",
    steps=[
        (r"The claim is about **every** positive integer, so any valid proof must handle all $n$ at once.",
         r"Checking particular values can only ever disprove a universal claim, never prove one."),
        (r"Factorise: $n^2 + n = n(n+1)$ - the product of two **consecutive** integers.",
         r"Factorising turns a statement about a sum into one about a product, where parity is easy to control."),
        (r"Of any two consecutive integers, exactly one is even; an even factor makes the product even.",
         r"This single sentence covers both the case $n$ even and the case $n$ odd - no case-splitting needed."),
        (r"That argument is general and complete, so it is the proof.",
         r"Now examine why the others fail, which is the real content of the question."),
    ],
    pitfalls=[r"Accepting the check of $n = 1, 2, 3$: three cases out of infinitely many prove nothing.",
              r"Accepting 'if $n$ is even then $n^2+n$ is even' - true, but it leaves odd $n$ untreated, so the proof is incomplete.",
              r"Accepting 'both $n^2$ and $n$ are even' - simply false when $n$ is odd.",
              r"Accepting the contradiction attempt that ends 'unless $n$ is even' - a proof cannot end with an unresolved exception."],
    takeaway=r"A proof of 'for all $n$' must be general. Examples illustrate; only argument proves."),

"PRF-02": Sol(
    idea=r"To disprove a universal claim, find one value where the conclusion fails - so test values until one breaks.",
    steps=[
        (r"Evaluate $2^n+1$ for each candidate: $n=1 \to 3$, $n=2 \to 5$, $n=3 \to 9$, $n=4 \to 17$, $n=8 \to 257$.",
         r"Systematic evaluation is faster than trying to be clever here."),
        (r"$9 = 3 \times 3$ is **not** prime, so $n = 3$ breaks the claim.",
         r"That is the counterexample: hypothesis satisfied ($3$ is a positive integer), conclusion false."),
        (r"The others - $3, 5, 17, 257$ - are all prime, so none of them refutes anything.",
         r"($257$ is prime: it is not divisible by $2,3,5,7,11,13$, and $17^2 = 289 > 257$.)"),
    ],
    pitfalls=[r"Assuming a large value like $n = 8$ must fail because the numbers get big - size is not the issue.",
              r"Stopping at the first odd value of $2^n+1$; every one of them is odd, since $2^n$ is even."],
    takeaway=r"Notice the pattern: $2^n+1$ can only be prime when $n$ is a power of $2$ - and $3$ is not, which is exactly why it fails."),

"PRF-03": Sol(
    idea=r"Ordering a proof by contradiction. The logical skeleton is fixed: assume the opposite, deduce consequences, hit the contradiction.",
    steps=[
        (r"The assumption must come first: II sets up $\sqrt2 = \frac pq$ in lowest terms.",
         r"Nothing can be deduced before the supposition is made, and 'no common factor' is the condition that will later be contradicted."),
        (r"Next I: squaring gives $p^2 = 2q^2$, so $p^2$ is even, so $p$ is even, $p = 2k$.",
         r"It depends on II, and it introduces $k$, which IV uses."),
        (r"Then IV: substituting $p = 2k$ gives $4k^2 = 2q^2$, so $q^2 = 2k^2$ is even, so $q$ is even.",
         r"IV cannot precede I because it uses $k$, which I defines."),
        (r"Finally III: $p$ and $q$ are both even, contradicting 'no common factor'. Hence $\sqrt2$ is irrational.",
         r"The conclusion must come after **both** parities are established. Order: II, I, IV, III."),
    ],
    pitfalls=[r"Placing III before IV - the contradiction needs $q$ even too, so it cannot come earlier.",
              r"Starting with I, which refers to $p$ and $q$ before they have been introduced."],
    takeaway=r"Order a proof by dependency: each line may only use things already defined or deduced."),

"PRF-04": Sol(
    idea=r"Choosing a proof strategy. For a 'for all odd integers' claim, the standard opening is an algebraic parametrisation.",
    steps=[
        (r"Represent an arbitrary odd integer as $2k+1$, $k$ an integer.",
         r"This one expression covers **every** odd integer, which is what a universal claim needs."),
        (r"(For context, the proof then runs: $(2k+1)^2 = 4k^2+4k+1 = 4k(k+1)+1$.)",
         r"Factorising $4k^2+4k$ as $4k(k+1)$ exposes the consecutive pair."),
        (r"$k(k+1)$ is a product of consecutive integers, hence even, say $2m$, so the square is $8m+1$.",
         r"That is remainder $1$ on division by $8$, as claimed."),
    ],
    pitfalls=[r"Checking $1,3,5,7,9$ - evidence, not proof.",
              r"Writing the odd integer as $2k$, which is the form of an **even** integer.",
              r"Assuming the claim is true - circular.",
              r"Reaching for contradiction ('assume the remainder is not $1$'): legal, but here a direct proof is simpler, and the question asks for the most appropriate step."],
    takeaway=r"Universal claims about odd/even numbers start by writing the general form: $2k$ or $2k+1$."),

"PRF-05": Sol(
    idea=r"Distinguishing a justification from a pattern-spot. The valid answer must establish the formula for all $n$.",
    steps=[
        (r"The first $n$ odd numbers are $1, 3, 5, \ldots$ - an arithmetic series with $a = 1$, $d = 2$.",
         r"Recognising the structure is what lets a general formula apply."),
        (r"Apply $S_n = \frac n2\left(2a + (n-1)d\right) = \frac n2(2 + 2(n-1))$.",
         r"The standard arithmetic-series sum, valid for every $n$."),
        (r"Simplify: $\frac n2 \times 2n = n^2$.",
         r"$2 + 2n - 2 = 2n$."),
        (r"That holds for all $n$, so it justifies the conjecture.",
         r"By contrast, 'the pattern continues with $25$' checks one more case, and 'four cases is enough' explicitly is not a proof."),
    ],
    pitfalls=[r"Accepting 'four cases have been checked' - the whole point of this topic is that it is not enough.",
              r"Accepting '$n^2$ is odd when $n$ is odd' - a true but completely irrelevant statement.",
              r"Being drawn to the even-numbers argument; its calculation happens to work out, but it is presented with an unjustified aside, whereas the series argument is clean and standard."],
    takeaway=r"A justification must apply to every $n$; extending a pattern one more term never does."),

"PRF-06": Sol(
    idea=r"Only a **universal** statement that is **false** can be disproved by a counterexample. Two separate tests.",
    steps=[
        (r"I: 'every prime $> 2$ is odd' is universal - but it is **true** (any even number $>2$ has factor $2$), so no counterexample exists.",
         r"You cannot disprove a true statement."),
        (r"II: 'every integer $4k+3$ is prime' is universal and **false**: $k = 3$ gives $15 = 3 \times 5$. Disprovable. **Yes.**",
         r"One failing case is a counterexample."),
        (r"III: 'there exists an even prime' is **existential**, not universal - and it is true ($2$). A counterexample is not even the right tool.",
         r"To disprove an existential statement you would have to rule out every case, which is not a 'single counterexample'."),
        (r"So II only.",
         r"Match to the list."),
    ],
    pitfalls=[r"Including I because it is a 'for all' statement - the statement also has to be false.",
              r"Including III by confusing what disproves an existential claim."],
    takeaway=r"Counterexamples disprove false universal statements only. Existential statements are proved by example and disproved only by a general argument."),

"PRF-07": Sol(
    idea=r"Proof by exhaustive cases: the cases must cover every integer (sufficient) with none redundant (necessary), and they must be chosen to match the divisor in question.",
    steps=[
        (r"The claim is about divisibility by $3$, so split by remainder on division by $3$: $n = 3k$, $3k+1$, $3k+2$.",
         r"Every integer has exactly one of these three forms, so the cases are exhaustive and non-overlapping."),
        (r"Check each: $n^3 - n = (n-1)n(n+1)$. If $n = 3k$ the middle factor is a multiple of $3$; if $n = 3k+1$ then $n - 1 = 3k$; if $n = 3k+2$ then $n+1 = 3(k+1)$.",
         r"Three consecutive integers always include a multiple of $3$ - the case split makes that explicit."),
        (r"So the product is divisible by $3$ in every case.",
         r"The proof is complete because the cases cover all integers."),
    ],
    pitfalls=[r"Splitting into even/odd - that is the wrong modulus and tells you nothing about divisibility by $3$.",
              r"Using only $3k+1$ and $3k+2$, which omits the multiples of $3$ themselves - not exhaustive.",
              r"Splitting by sign or by primality: exhaustive, but useless for this claim."],
    takeaway=r"For divisibility by $m$, split into the $m$ residue classes $mk, mk+1, \ldots, mk+(m-1)$."),

"PRF-08": Sol(
    idea=r"Deduction from an implication. You are given information about the **conclusion**, so the contrapositive is the tool.",
    steps=[
        (r"The given rule is $f(x)>0 \Rightarrow g(x)>0$.",
         r"It lets you conclude about $g$ from $f$, not the other way round - directly, at least."),
        (r"Its contrapositive is: $g(x) \leq 0 \Rightarrow f(x) \leq 0$, which is equally valid.",
         r"Negate and swap: $\neg(g>0)$ is $g \leq 0$, $\neg(f>0)$ is $f \leq 0$."),
        (r"Apply it at $x = 2$: $g(2) = -1 \leq 0$, so $f(2) \leq 0$.",
         r"That is all that follows - $f(2)$ could be $0$ or negative."),
    ],
    pitfalls=[r"Concluding $f(2) < 0$ - too strong; the negation of $>0$ includes $=0$.",
              r"Concluding nothing, forgetting that the contrapositive is always available.",
              r"Concluding $f(2) > 0$ by using the implication backwards (affirming the consequent)."],
    takeaway=r"Information about the conclusion of an implication is used via the contrapositive - and mind the boundary: $\neg(x>0)$ is $x \leq 0$."),

"PRF-09": Sol(
    idea=r"Ordering Euclid's proof. Again the skeleton is assume-deduce-contradict, and the dependencies fix the order.",
    steps=[
        (r"II first: assume finitely many primes $p_1,\ldots,p_n$ and construct $N = p_1p_2\cdots p_n + 1$.",
         r"Everything else refers to $N$, so it must be defined first."),
        (r"Then I: each $p_i$ divides $p_1\cdots p_n$, so dividing $N$ by $p_i$ leaves remainder $1$ - no listed prime divides $N$.",
         r"This is the key property of the $+1$."),
        (r"Then IV: $N > 1$, so it has at least one prime factor.",
         r"Every integer greater than $1$ has a prime factor - a separate fact, independent of I."),
        (r"Finally III: that prime factor is not in the list, contradicting the assumption that the list was complete. Order: II, I, IV, III.",
         r"The contradiction needs **both** I (none of the listed primes works) and IV (some prime does)."),
    ],
    pitfalls=[r"Putting III immediately after II, before either supporting fact has been established.",
              r"Thinking the proof claims $N$ is prime - it need not be; it merely has a prime factor outside the list."],
    takeaway=r"In a contradiction proof, the contradiction is the last line, and it must rest on everything before it."),

"PRF-10": Sol(
    idea=r"Proving 'if $P$ then ($A$ or $B$)'. Assuming both $A$ and $B$ fail and deriving a contradiction is the natural route.",
    steps=[
        (r"Negate the conclusion: 'not ($x>5$ or $y>5$)' means $x \leq 5$ **and** $y \leq 5$ (De Morgan).",
         r"Negating an 'or' gives an 'and' - and it gives you two usable facts instead of a disjunction."),
        (r"Add the inequalities: $x + y \leq 10$.",
         r"Inequalities of the same direction may be added."),
        (r"That contradicts the hypothesis $x+y > 10$, so the conclusion must hold.",
         r"Hypothesis true and conclusion false is impossible, which is exactly what proves the implication."),
    ],
    pitfalls=[r"'If $x>5$ then the conclusion holds' - this assumes part of what is to be proved.",
              r"Testing $x = y = 6$ - a single example proves nothing about all $x, y$.",
              r"'Suppose $x > 5$, then $y > 10 - x$, so $y > 5$' - the algebra is wrong and it proves a false statement (both exceeding $5$).",
              r"'The average exceeds $5$ so both exceed $5$' - the average exceeding $5$ only forces **at least one** to."],
    takeaway=r"To prove an 'or', negate it into an 'and' and look for a contradiction - De Morgan turns a weak conclusion into strong assumptions."),

"PRF-11": Sol(
    idea=r"Describing a pattern precisely: check the start value and the two counts separately against every given line.",
    steps=[
        (r"Starting values: $1, 4, 9$ for lines $1, 2, 3$ - these are $n^2$.",
         r"Test against all three lines, not just one."),
        (r"Count the left sides: $\{1,2\}$, $\{4,5,6\}$, $\{9,10,11,12\}$ - that is $2, 3, 4$ terms, i.e. $n+1$.",
         r"Count carefully; being off by one here is the whole point of the question."),
        (r"Count the right sides: $\{3\}$, $\{7,8\}$, $\{13,14,15\}$ - that is $1, 2, 3$ terms, i.e. $n$.",
         r"Left has one more term than right, which is what makes the equality possible (the right-hand terms are larger)."),
        (r"So: starts at $n^2$, with $n+1$ terms on the left and $n$ on the right.",
         r"Check the total count: $(n+1) + n = 2n+1$, and indeed line $3$ runs from $9$ to $15$, seven numbers ✓."),
    ],
    pitfalls=[r"Swapping the counts ($n$ left, $n+1$ right) - the sides would not balance, since the right-hand numbers are bigger.",
              r"Reading the start as $2n-1$ or $n(n+1)$ - both fail at line $2$ ($3$ and $6$ rather than $4$)."],
    takeaway=r"Verify a conjectured pattern against **every** given line, and check each component (start, length) separately."),

"PRF-12": Sol(
    idea=r"Deduction from two premises. Test the strongest-looking option against premise (i) first.",
    steps=[
        (r"Suppose $n$ were a multiple of $12$. Then $12 = 4\times3$ and $12 = 6 \times 2$, so $n$ is a multiple of both $4$ and $6$.",
         r"Exploring the tempting case first often resolves the whole question."),
        (r"But (i) says a multiple of $4$ is not a multiple of $6$ - contradiction. So $n$ is **not** a multiple of $12$.",
         r"A supposition leading to a contradiction is ruled out."),
        (r"Premise (ii) offers two alternatives and the first is now impossible, so $n$ must be a multiple of $4$.",
         r"Disjunctive syllogism: '$A$ or $B$' plus 'not $A$' gives $B$."),
        (r"Then (i) applies: $n$ is a multiple of $4$ but not of $6$.",
         r"That is the full deduction."),
    ],
    pitfalls=[r"Concluding $n$ is a multiple of $12$ by picking the first branch of (ii) without testing it.",
              r"Declaring the premises inconsistent - they are perfectly consistent (e.g. $n = 4$ or $n = 8$).",
              r"Concluding nothing, missing that one branch of the 'or' is eliminated."],
    takeaway=r"With 'A or B', eliminate one branch and the other must hold; always test the branch that clashes with the other premise."),

"PRF-13": Sol(
    idea=r"Choosing the right algebraic representation is most of the work. Centre the variables on the middle term.",
    steps=[
        (r"Represent three consecutive integers as $n-1$, $n$, $n+1$.",
         r"Centring on $n$ makes the $\pm1$ cancel; $n, n+1, n+2$ also works but gives $3n+3$, needing one more line."),
        (r"Add: $(n-1) + n + (n+1) = 3n$.",
         r"The $-1$ and $+1$ cancel."),
        (r"$3n$ is $3$ times an integer, hence divisible by $3$, for every integer $n$.",
         r"General, so it is a proof."),
    ],
    pitfalls=[r"Using $n, 2n, 3n$ - those are multiples, not consecutive integers.",
              r"Checking three numerical cases.",
              r"Arguing 'any three integers include a multiple of $3$' - false for $1,2,4$, and in any case containing a multiple of $3$ would not make the **sum** a multiple of $3$.",
              r"The 'mean' argument that ends by demanding the middle integer be a multiple of $3$ - it confuses '$3 \times$ an integer' with '$3 \times$ a multiple of $3$'."],
    takeaway=r"Consecutive integers: use $n-1, n, n+1$. Their sum is $3n$, always divisible by $3$."),

"PRF-14": Sol(
    idea=r"Setting up a proof by contradiction for an implication: assume the hypothesis **and** the negated conclusion.",
    steps=[
        (r"The claim is 'if $n^2$ is even then $n$ is even': hypothesis $n^2$ even, conclusion $n$ even.",
         r"Identify both parts before negating anything."),
        (r"For contradiction, suppose the whole implication fails. An implication fails only when the hypothesis holds and the conclusion does not.",
         r"This is the one case that would make $A \Rightarrow B$ false."),
        (r"So assume: $n^2$ is even **and** $n$ is odd.",
         r"Both, not just one."),
        (r"(The proof then runs: $n = 2k+1 \Rightarrow n^2 = 4k^2+4k+1$, odd - contradicting $n^2$ even.)",
         r"The contradiction is with the retained hypothesis."),
    ],
    pitfalls=[r"Assuming only '$n$ is odd' and dropping the hypothesis - then there is nothing to contradict.",
              r"Assuming '$n^2$ is odd', which negates the hypothesis instead of the conclusion.",
              r"Assuming '$n$ even and $n^2$ odd', which negates the wrong part of each."],
    takeaway=r"To contradict $A \Rightarrow B$, assume $A$ **and** $\neg B$ - keep the hypothesis, negate only the conclusion."),

"PRF-15": Sol(
    idea=r"The classic warning about pattern-spotting: a formula can produce primes for many values and still fail.",
    steps=[
        (r"I: compute $u_1 = 41$, $u_2 = 4-2+41 = 43$, $u_3 = 9-3+41=47$, $u_4 = 16-4+41 = 53$, $u_5 = 25-5+41=61$. All prime. **True.**",
         r"Straight substitution; all five are primes (none divisible by $2,3,5$ and each is below $64$ or checkable quickly)."),
        (r"III: $u_{41} = 41^2 - 41 + 41 = 41^2$. Divisible by $41$. **True.**",
         r"The $-41$ and $+41$ cancel exactly - which is why $n = 41$ is the natural place to look for failure."),
        (r"II: since $u_{41} = 41^2 = 1681$ has factor $41$, it is not prime. **False.**",
         r"One counterexample kills the universal claim, however many earlier cases worked."),
        (r"So I and III.",
         r"Match to the list."),
    ],
    pitfalls=[r"Accepting II because the first several values are prime - this formula is famous precisely because it works for $n = 1$ to $40$ and then fails.",
              r"Trying to check $u_{41}$ by multiplying out $1681$ instead of spotting the cancellation."],
    takeaway=r"Many confirming cases never prove a universal claim; and when hunting for failure, look for the value that makes terms cancel."),

"PRF-16": Sol(
    idea=r"Direction matters. A proof should start from something known and deduce the result, not start from the result.",
    steps=[
        (r"Start with a known truth: $(\sqrt a - \sqrt b)^2 \geq 0$, valid because squares are non-negative and $\sqrt a, \sqrt b$ exist for $a, b > 0$. That is III.",
         r"Beginning from an undeniable fact is the safe way round."),
        (r"Expand it: $a - 2\sqrt{ab} + b \geq 0$. That is II.",
         r"$(\sqrt a)^2 = a$, $(\sqrt b)^2 = b$, and the cross term is $-2\sqrt a\sqrt b = -2\sqrt{ab}$."),
        (r"Rearrange: $a + b \geq 2\sqrt{ab}$, then divide by $2$. That is I.",
         r"Dividing by the positive number $2$ preserves the inequality."),
        (r"Order: III, II, I.",
         r"Known truth $\to$ algebra $\to$ required result."),
    ],
    pitfalls=[r"Choosing I, II, III - that starts by assuming the result. Working backwards is a legitimate way to **find** a proof, but to **present** one every step must be reversed.",
              r"Starting with II, whose inequality has not yet been justified."],
    takeaway=r"Present proofs forwards, from an established fact to the conclusion. This one proves AM $\geq$ GM."),

"PRF-17": Sol(
    idea=r"Scan the claims for the one that squaring breaks - negative numbers are where inequalities misbehave.",
    steps=[
        (r"'$a>b \Rightarrow a^2 > b^2$ for all real $a,b$': try $a = 1$, $b = -2$. Then $1 > -2$ but $1 < 4$. **False.**",
         r"Squaring reverses order once negatives with larger magnitude are involved."),
        (r"'$a > b > 0 \Rightarrow a^2 > b^2$' is **true** - the positivity condition is exactly what the first claim lacked.",
         r"Comparing the two shows precisely which hypothesis does the work."),
        (r"'$a>b \Rightarrow a+c > b+c$' is **true**: adding the same number to both sides preserves order.",
         r"Valid for every real $c$, positive or negative."),
        (r"'$a>b \Rightarrow a^3>b^3$' is **true**: cubing is strictly increasing for every real number, unlike squaring.",
         r"$x^3$ keeps the sign of $x$, so no reversal occurs."),
        (r"'$a>b \Rightarrow -a < -b$' is **true**: multiplying by $-1$ reverses the inequality.",
         r"The standard sign rule."),
    ],
    pitfalls=[r"Thinking the cubing claim fails - it does not; only **even** powers destroy order.",
              r"Thinking multiplying by $-1$ keeps the direction."],
    takeaway=r"Squaring preserves order only for non-negative numbers; cubing, adding and negating (with a flip) always behave."),

"PRF-18": Sol(
    idea=r"'Must be true' with a concrete object given. Some claims follow from the given element; others need a counterexample set.",
    steps=[
        (r"I: $10 \in S$ and $10 = 2 \times 5$ is a positive multiple of $5$. **Must be true.**",
         r"The element is handed to you; nothing more is needed."),
        (r"II: the second condition says every multiple of $3$ in $S$ is negative, so none can be positive. **Must be true.**",
         r"Note this is vacuously fine even if $S$ contains no multiples of $3$ at all."),
        (r"III: must $S$ contain a negative number? Try $S = \{10\}$: every element is a multiple of $3$ or $5$ ✓, there are no multiples of $3$ to be negative ✓, and $10 \in S$ ✓. No negative number. **Not necessarily true.**",
         r"A single valid $S$ with no negative element refutes 'must be true'."),
        (r"So I and II.",
         r"Match to the list."),
    ],
    pitfalls=[r"Reading 'every multiple of $3$ in $S$ is negative' as promising that $S$ **has** a multiple of $3$ - a universal statement can be true with nothing to apply it to.",
              r"Confusing 'could be true' with 'must be true' for III."],
    takeaway=r"A conditional statement about members of a set is vacuously true when no member qualifies; to refute 'must be true', build a legal example that fails it."),

"PRF-19": Sol(
    idea=r"Diagnosing why a proof technique fails when transplanted. Follow the argument line by line and find the step that no longer bites.",
    steps=[
        (r"Suppose $\sqrt4 = \frac pq$ in lowest terms; then $p^2 = 4q^2$, so $p^2$ is even, so $p$ is even - this much is **fine**.",
         r"$4q^2$ is certainly even, and an odd number squared is odd, so $p$ must be even."),
        (r"Substituting $p = 2k$: $4k^2 = 4q^2$, i.e. $k^2 = q^2$.",
         r"Here the $4$ cancels entirely, because the constant was $4$ and not $2$."),
        (r"Compare with $\sqrt2$: there $p^2 = 2q^2$ gives $4k^2 = 2q^2$, i.e. $q^2 = 2k^2$ - a spare factor of $2$ forcing $q$ even.",
         r"That leftover factor of $2$ is the whole engine of the classical proof."),
        (r"With $\sqrt4$ no factor is left over, so $k^2 = q^2$ tells you nothing about the parity of $q$, and no contradiction ever appears.",
         r"Correctly so: $\sqrt4 = 2$ is rational, so no proof of irrationality could possibly succeed."),
    ],
    pitfalls=[r"Claiming $p^2 = 4q^2$ fails to make $p$ even - it does not fail; that step is valid.",
              r"Claiming the 'lowest terms' assumption is illegitimate - every rational can be written that way.",
              r"Accepting the argument and concluding $\sqrt4$ is irrational, when $\sqrt4 = 2$."],
    takeaway=r"The $\sqrt2$ proof works because $2$ is prime; the leftover prime factor is what forces the second parity. Check where an adapted proof loses its engine."),

"PRF-20": Sol(
    idea=r"Proving a conjecture about a sequence: substitute the formula and simplify algebraically to a general result.",
    steps=[
        (r"Write both terms: $T_n = \dfrac{n(n+1)}{2}$ and $T_{n+1} = \dfrac{(n+1)(n+2)}{2}$.",
         r"Replace $n$ by $n+1$ throughout the given formula."),
        (r"Add over the common denominator: $\dfrac{n(n+1) + (n+1)(n+2)}{2}$.",
         r"Same denominator, so just add numerators."),
        (r"Factor out $(n+1)$: $\dfrac{(n+1)\left[n + (n+2)\right]}{2} = \dfrac{(n+1)(2n+2)}{2}$.",
         r"Spotting the common factor avoids expanding and re-factorising."),
        (r"$2n+2 = 2(n+1)$, so the expression is $(n+1)^2$ - a perfect square for every $n$. **Proved.**",
         r"The $2$ cancels the denominator."),
    ],
    pitfalls=[r"Checking $T_4 + T_5 = 25$ and stopping - one more case is still not a proof.",
              r"'Triangular numbers are always squares' - plainly false ($T_2 = 3$).",
              r"'$T_n + T_{n+1} = 2T_n + (n+1)$, which is a square' - the identity is right but the conclusion is asserted, not shown.",
              r"Quoting the difference $T_{n+1} - T_n = n+1$, which is true but says nothing about the sum."],
    takeaway=r"Substitute the general formula and simplify; consecutive triangular numbers sum to $(n+1)^2$."),

}
