"""Revision notes for the Section 1 Part 2 topics (M1-M7, Higher GCSE) and Section 2 (Paper 2 reasoning)."""

NOTES = {
"number": {
    "summary": r"GCSE number skills appear in TMUA as fast mental arithmetic under pressure: prime factorisation for HCF/LCM and divisor counts, standard form, bounds, recurring decimals and systematic counting. The traps are careless ones - keep the working tidy.",
    "sections": [
        {"h": "Primes, factors and multiples (M2.3)", "body": r"""- Prime factorise: $360 = 2^3\cdot3^2\cdot5$. HCF = lowest powers of common primes; LCM = highest powers of all primes.
- Number of divisors of $p^a q^b r^c$ is $(a + 1)(b + 1)(c + 1)$.
- $\text{lcm}(1, \ldots, 10) = 2^3\cdot3^2\cdot5\cdot7 = 2520$.
- Among any three numbers $n, n + 2, n + 4$ one is a multiple of $3$ - so $3, 5, 7$ is the only prime triple of that form."""},
        {"h": "Decimals, standard form, bounds (M2.8, M2.9, M2.13, M2.14)", "body": r"""- Recurring decimal: $x = 0.\dot2\dot7$, $100x = 27.\dot2\dot7$, $99x = 27$, $x = \frac{3}{11}$. A fraction terminates iff its lowest-terms denominator has only the prime factors $2$ and $5$.
- Standard form $a \times 10^n$ with $1 \leq a < 10$: multiply the $a$'s, add the powers, then renormalise.
- Bounds: a value $4.6$ to 1 d.p. lies in $[4.55, 4.65)$. Upper bound of a quotient = upper/lower; lower bound = lower/upper.
- Truncated (not rounded) to $3.14$: $3.14 \leq x < 3.15$.
- Estimation: round each number to 1 s.f. before calculating."""},
        {"h": "Units and counting (M1, M2.5)", "body": r"""- $90$ km/h $= 90000/3600 = 25$ m/s. $1$ m$^3 = 1000$ litres; $1$ m$^2 = 10^4$ cm$^2$.
- Product rule for counting: $m$ ways then $n$ ways gives $mn$. Without repetition the choices shrink: $5 \times 4 \times 3$."""},
    ],
    "key": [r"divisors of $p^aq^b = (a+1)(b+1)$", r"terminating $\Leftrightarrow$ denominator $2^a5^b$", r"$x$ to 1 d.p. $= 4.6 \Rightarrow 4.55 \leq x < 4.65$", r"km/h $\div 3.6 = $ m/s"],
    "traps": [r"The upper bound of an interval is not attainable: write $< 4.65$, not $\leq$.",
              r"Adding in standard form needs equal powers of $10$ first.",
              r"Codes with 'different digits' use $9 \times 8$, not $9 \times 9$."],
    "worked": [{"q": r"How many positive divisors has $360$?", "a": r"$360 = 2^3\cdot3^2\cdot5$, so $(3+1)(2+1)(1+1) = 24$."}],
},
"ratio-proportion": {
    "summary": r"Think multiplicatively: a $20\%$ decrease is $\times 0.8$, successive changes multiply, and reverse-percentage problems divide by the multiplier. Direct and inverse proportion are equations with a constant $k$; similar shapes scale lengths by $k$, areas by $k^2$ and volumes by $k^3$.",
    "sections": [
        {"h": "Ratio and percentages (M3.1-M3.8)", "body": r"""- Share in the ratio $2 : 3 : 7$: each part is total $\div 12$.
- Changing a ratio: express amounts, add to one part, solve. Mixtures: track the pure quantity (e.g. grams of red paint).
- Percentage multipliers: $+15\% \to \times1.15$; $-25\% \to \times 0.75$. Original value $= $ final $\div$ multiplier.
- $+x\%$ then $-x\%$ is $\times(1 - \frac{x^2}{10000})$: a net decrease. $A$ is $25\%$ more than $B$ $\Leftrightarrow$ $B$ is $20\%$ less than $A$.
- Map scale $1 : 25000$: $1$ cm $= 0.25$ km, so $1$ cm$^2 = 0.0625$ km$^2$."""},
        {"h": "Proportion, growth and similarity (M3.9-M3.11)", "body": r"""- $y \propto x^n$ means $y = kx^n$; inverse proportion $y = \frac{k}{x^n}$. Find $k$ from the given pair, then substitute.
- Chains: $p \propto \sqrt q$ and $q \propto \frac1r$ give $p \propto \frac{1}{\sqrt r}$.
- Compound growth: amount $= P(1 + r)^n$; decay: $P(1 - r)^n$. 'First below half' means find the least $n$ with $0.8^n < 0.5$ by trial ($0.8^4 = 0.4096$).
- Similar solids: areas in ratio $4 : 9$ means lengths $2 : 3$ and volumes $8 : 27$."""},
    ],
    "key": [r"$\times(1 \pm \frac{p}{100})$", r"original $=$ final $\div$ multiplier", r"length $k$, area $k^2$, volume $k^3$", r"$P(1+r)^n$"],
    "traps": [r"Two successive $10\%$ rises are $21\%$, not $20\%$.",
              r"'Increase by $50\%$ then decrease by $50\%$' gives $75\%$ of the start.",
              r"Compound interest is not simple interest: $2000 \times 1.05^n$, not $2000 + 100n$."],
    "worked": [{"q": r"After a $15\%$ rise a salary is $27\,600$. Original?", "a": r"$27600 \div 1.15 = 24000$."}],
},
"gcse-algebra": {
    "summary": r"Fluency topics: expanding, factorising (including $ax^2 + bx + c$), rearranging formulae where the subject appears twice, simplifying algebraic fractions, identities versus equations, and $n$th terms of linear and quadratic sequences. Kinematics graphs (area under speed-time = distance) are also here.",
    "sections": [
        {"h": "Manipulation (M4.1-M4.8)", "body": r"""- Rearranging when the subject appears twice: collect the subject terms on one side and factorise: $y(x - 1) = 2x + 3 \Rightarrow x(y - 2) = y + 3$.
- Algebraic fractions: factorise numerator and denominator fully, cancel common factors; add with a common denominator.
- Identity ($\equiv$): true for all $x$, e.g. $(x + 3)^2 - (x - 3)^2 \equiv 12x$. Equation: true for particular $x$.
- Factorise $6x^2 - 7x - 20$: find two numbers with product $-120$ and sum $-7$ ($-15, 8$), split the middle term.
- Substitution into formulae: $v^2 = u^2 + 2as$ with care over signs and squares."""},
        {"h": "Sequences and graphs in context (M4.18, M4.19)", "body": r"""- Linear sequence: $n$th term $= dn + (a - d)$. Quadratic sequence: second difference $2a$; fit $an^2 + bn + c$ from the first terms.
- Term-to-term rules can be constant or cyclic: $x \to x^2 - 2$ from $2$ stays at $2$.
- Speed-time graph: area = distance; gradient = acceleration. Distance-time graph: gradient = speed; average speed = total distance $\div$ total time (not displacement)."""},
    ],
    "key": [r"$n$th term of a quadratic sequence: second difference $= 2a$", r"area under $v$-$t$ = distance", r"identity: true for all $x$"],
    "traps": [r"Cancelling: only common **factors** cancel, never terms ($\frac{x^2 - 9}{x - 3} = x + 3$ but $\frac{x + 9}{x + 3}$ does not simplify).",
              r"$(n + 1)^2 - 1 = n^2 + 2n$: two option forms can be the same expression.",
              r"'For how long is the ball above 15 m' is the length of the interval between the two times."],
    "worked": [{"q": r"$n$th term of $3, 8, 15, 24, 35$?", "a": r"Differences $5, 7, 9, 11$; second difference $2$, so $n^2 + bn + c$; $n = 1, 2$ give $b = 2$, $c = 0$: $n^2 + 2n$."}],
},
"geometry": {
    "summary": r"Angle facts (parallel lines, polygons), the properties of special quadrilaterals, congruence criteria (SSS, SAS, ASA, RHS - not SSA), similarity, transformations and column vectors. TMUA uses these for short 'which statement must be true' or 'which condition is necessary and sufficient' questions.",
    "sections": [
        {"h": "Angles and polygons (M5.1-M5.3)", "body": r"""- Angles on a line $180^\circ$, at a point $360^\circ$, vertically opposite equal; with parallel lines: alternate equal, corresponding equal, co-interior sum to $180^\circ$.
- Interior angles of an $n$-gon sum to $180(n - 2)^\circ$; exterior angles sum to $360^\circ$; regular $n$-gon exterior angle $\frac{360}{n}$.
- Quadrilaterals: parallelogram (opposite sides parallel and equal), rhombus (parallelogram with equal sides, perpendicular diagonals), rectangle (equal diagonals), square (both), kite (perpendicular diagonals, one line of symmetry), trapezium (one pair of parallel sides)."""},
        {"h": "Congruence, similarity, transformations, vectors (M5.4-M5.6, M5.14, M5.18, M5.19)", "body": r"""- Congruence: SSS, SAS, ASA (or AAS), RHS. Two sides and a non-included angle (SSA) is **not** enough.
- Similar shapes: equal angles, sides in the same ratio; a line parallel to one side of a triangle creates a similar triangle.
- Transformations: enlargement with negative scale factor inverts through the centre; rotation $90^\circ$ anticlockwise about $O$: $(x, y) \to (-y, x)$; reflection in $y = x$: $(x, y) \to (y, x)$.
- Bearings: measured clockwise from north, three figures; the back bearing differs by $180^\circ$.
- Vectors: $\overrightarrow{AB} = \mathbf b - \mathbf a$; parallel vectors are multiples; collinear points have parallel joining vectors; midpoint $\frac12(\mathbf a + \mathbf b)$; ratio point $OP : PM = 2 : 1$ gives $\overrightarrow{OP} = \frac23\overrightarrow{OM}$."""},
    ],
    "key": [r"interior sum $180(n-2)$", r"exterior angle of regular $n$-gon $= 360/n$", r"congruence: SSS, SAS, ASA, RHS", r"$(x,y) \to (-y,x)$ for $90^\circ$ anticlockwise", r"$\overrightarrow{AB} = \mathbf b - \mathbf a$"],
    "traps": [r"Every square is a rhombus and a rectangle; the converses fail.",
              r"Bearings less than $100^\circ$ still need three figures ($075^\circ$).",
              r"For collinearity with vectors, compare the ratios of coefficients of $\mathbf p$ and $\mathbf q$."],
    "worked": [{"q": r"Interior angle $156^\circ$: how many sides?", "a": r"Exterior $24^\circ$; $360/24 = 15$."}],
},
"mensuration": {
    "summary": r"Pythagoras in 2D and 3D (the space diagonal $\sqrt{a^2 + b^2 + c^2}$), areas of composite shapes, volumes and surface areas of prisms and cylinders (must be known) and of cones, spheres and pyramids (formulas given if needed), and right-angled trigonometry with exact values.",
    "sections": [
        {"h": "Formulas to know (M5.7, M5.16)", "body": r"""- Pythagoras $a^2 + b^2 = c^2$; cuboid diagonal $\sqrt{a^2 + b^2 + c^2}$; pyramid height from a slant edge via half the base diagonal.
- Triangle $\frac12 bh$; parallelogram $bh$; trapezium $\frac12(a + b)h$; circle $\pi r^2$, circumference $2\pi r$; sector $\frac{\theta}{360}\pi r^2$.
- Prism volume = cross-section $\times$ length; cylinder $\pi r^2 h$, curved surface $2\pi rh$, total $2\pi r^2 + 2\pi rh$.
- Given if needed: cone $\frac13\pi r^2h$ (curved surface $\pi rl$), sphere $\frac43\pi r^3$ (surface $4\pi r^2$), pyramid $\frac13 \times$ base $\times$ height."""},
        {"h": "Trigonometry in right-angled triangles (M5.17, M5.18)", "body": r"""- $\sin = \frac{\text{opp}}{\text{hyp}}$, $\cos = \frac{\text{adj}}{\text{hyp}}$, $\tan = \frac{\text{opp}}{\text{adj}}$; exact values for $30^\circ, 45^\circ, 60^\circ$ from the $1, 1, \sqrt2$ and $1, \sqrt3, 2$ triangles.
- Angles of elevation/depression are measured from the horizontal; the angle of depression from the top equals the angle of elevation from the bottom.
- Similar solids: if lengths scale by $k$, areas scale by $k^2$ and volumes by $k^3$.
- Plans and elevations: reason about the minimum and maximum number of cubes consistent with all three views."""},
    ],
    "key": [r"diagonal of cuboid $\sqrt{a^2+b^2+c^2}$", r"cylinder $V = \pi r^2 h$", r"trapezium $\frac12(a+b)h$", r"$\tan 30^\circ = \frac{1}{\sqrt3}$, $\tan 60^\circ = \sqrt3$"],
    "traps": [r"Doubling a radius while halving the height doubles a cylinder's volume; it does not keep it constant.",
              r"Surface area of a solid made of two parts: subtract the hidden joining faces.",
              r"'Cube volume equals surface area numerically': $a^3 = 6a^2$ gives $a = 6$, not $a = \sqrt6$."],
    "worked": [{"q": r"Cone: $r = 6$, slant $10$. Volume?", "a": r"$h = 8$; $V = \frac13\pi\cdot36\cdot8 = 96\pi$."}],
},
"statistics": {
    "summary": r"Averages and spread, grouped-data estimates, histograms (frequency density), cumulative frequency and quartiles, and scatter graphs. TMUA questions are reasoning questions about what **must** happen to a mean or median when the data change.",
    "sections": [
        {"h": "Averages and spread (M6.3)", "body": r"""- Mean $= \frac{\sum x}{n}$; combined mean $= \frac{n_1\bar x_1 + n_2\bar x_2}{n_1 + n_2}$; adding a value changes the total, so a new mean fixes the new value.
- Median: middle value of ordered data (mean of the two middle values when $n$ is even). Mode: most frequent.
- Transforming every value by $ax + b$: mean $\to a\bar x + b$; range and IQR $\to |a| \times$ (unchanged by $b$).
- Grouped data: use midpoints for an estimated mean; the modal class is the one with the greatest frequency density.
- An outlier pulls the mean towards it but usually leaves the median alone; changing the smallest value may or may not change the median."""},
        {"h": "Diagrams (M6.1, M6.2, M6.4)", "body": r"""- Histogram: area = frequency; frequency density $= \frac{\text{frequency}}{\text{class width}}$.
- Cumulative frequency graph: read the lower quartile at $\frac n4$, median at $\frac n2$, upper quartile at $\frac{3n}{4}$; IQR $= Q_3 - Q_1$.
- Scatter graphs: correlation describes a trend, not a cause; interpolation within the data range is reasonable, extrapolation is risky."""},
    ],
    "key": [r"frequency $=$ density $\times$ width", r"combined mean $= \frac{n_1\bar x_1 + n_2 \bar x_2}{n_1+n_2}$", r"IQR $= Q_3 - Q_1$", r"correlation $\neq$ causation"],
    "traps": [r"Doubling then adding $3$: the mean becomes $2m + 3$ but the range becomes $2R$ (no $+3$).",
              r"Estimated means from grouped data are estimates because the exact values are unknown.",
              r"The median of an even-sized list need not be a member of the list."],
    "worked": [{"q": r"Mean of five numbers is $12$; adding a sixth makes it $14$. Sixth number?", "a": r"$84 - 60 = 24$."}],
},
"probability": {
    "summary": r"Probabilities of an exhaustive set of outcomes sum to $1$; multiply along branches of a tree (adjusting for 'without replacement'), add across mutually exclusive branches. Conditional probability is best handled with counts (two-way tables, Venn diagrams) rather than formulas.",
    "sections": [
        {"h": "Rules (M7.1-M7.7)", "body": r"""- $P(\text{not } A) = 1 - P(A)$. $P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)$; for mutually exclusive events the last term is $0$.
- Independent: $P(A \text{ and } B) = P(A)P(B)$. Test independence by checking this product.
- Without replacement: the second probability uses the reduced totals ($\frac{4}{10}\cdot\frac{6}{9} + \frac{6}{10}\cdot\frac{4}{9}$).
- Conditional: $P(B \mid A) = \frac{P(A \text{ and } B)}{P(A)}$ - with counts, restrict to the $A$ group.
- Expected frequency $= n \times p$. Relative frequency approaches the theoretical probability as trials increase, but any single run can differ."""},
        {"h": "Techniques", "body": r"""- Possibility spaces: two dice give $36$ equally likely outcomes; 'product odd' needs both odd: $\frac14$.
- 'At least one' = $1 - P(\text{none})$. 'First success on the third go' $= q^2 p$.
- Unknown probabilities: set up an equation, e.g. $2p(1 - p) = \frac38$ gives a quadratic with two valid roots.
- Symmetry: with three fair coins, $P(\text{more heads than tails}) = \frac12$."""},
    ],
    "key": [r"$P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)$", r"independent: $P(A)P(B)$", r"$P(B|A) = \frac{P(A \text{ and } B)}{P(A)}$", r"at least one $= 1 - P(\text{none})$"],
    "traps": [r"Mutually exclusive and independent are different: exclusive events with non-zero probabilities are never independent.",
              r"Without replacement the denominators change on the second draw.",
              r"'Given that' fixes the denominator to the given group's size."],
    "worked": [{"q": r"$P(A) = 0.6$, $P(B) = 0.5$, $P(A \text{ and } B) = 0.3$. Independent?", "a": r"$0.6 \times 0.5 = 0.3$: yes. $P(A \text{ or } B) = 0.8$."}],
},
"logic": {
    "summary": r"Paper 2 lives here. 'If $A$ then $B$' has converse 'if $B$ then $A$' (not equivalent) and contrapositive 'if not $B$ then not $A$' (equivalent). '$A$ only if $B$' means $A \Rightarrow B$; '$A$ if $B$' means $B \Rightarrow A$. $P$ is sufficient for $Q$ when $P \Rightarrow Q$ and necessary when $Q \Rightarrow P$. Negate quantifiers by swapping 'for all' and 'there exists' and negating the inside.",
    "sections": [
        {"h": "Implications (Arg1, Arg2)", "body": r"""- Statement $A \Rightarrow B$. Converse $B \Rightarrow A$. Inverse (not $A$) $\Rightarrow$ (not $B$). Contrapositive (not $B$) $\Rightarrow$ (not $A$). Statement $\equiv$ contrapositive; converse $\equiv$ inverse; the two pairs are independent of each other.
- '$A$ if and only if $B$' = both directions.
- $P$ sufficient for $Q$: $P \Rightarrow Q$. $P$ necessary for $Q$: $Q \Rightarrow P$ (you cannot have $Q$ without $P$). Decide each direction separately and look for a counterexample to the one that fails.
- $A \Rightarrow B$ is equivalent to '(not $A$) or $B$'.
- Truth of a conditional: 'if $x > 2$ then $x^2 > 4$' is judged for **all** $x$; one counterexample makes it false."""},
        {"h": "Quantifiers and negation (Arg3, Arg4)", "body": r"""- 'For all $x$, $P(x)$' is refuted by one counterexample; 'there exists $x$ with $P(x)$' is proved by one example.
- Negations: not(for all $x$, $P$) = there exists $x$ with not $P$; not(exists $x$ with $P$) = for all $x$, not $P$; not($A$ and $B$) = (not $A$) or (not $B$); not($A$ or $B$) = (not $A$) and (not $B$); not($x > 3$) is $x \leq 3$.
- Order of quantifiers matters: 'for every $x$ there is $y > x$' is true; 'there is $y$ greater than every $x$' is false.
- Nested negation: 'for every $n$ there is a prime $p$ with $n < p < 2n$' negates to 'there is an $n$ for which no prime $p$ satisfies $n < p < 2n$'."""},
    ],
    "key": [r"contrapositive $\equiv$ original", r"converse $\not\equiv$ original", r"$P$ sufficient: $P \Rightarrow Q$; $P$ necessary: $Q \Rightarrow P$", r"$A$ only if $B$: $A \Rightarrow B$", r"not(for all) = exists not"],
    "traps": [r"'$P$ is necessary and sufficient' needs both implications; check for a counterexample in each direction (e.g. $4 \mid n$ vs $8 \mid n^2$ really is both).",
              r"'Not more than 50' is '50 or less', not 'less than 50'.",
              r"A true statement can have a false converse (equilateral $\Rightarrow$ isosceles)."],
    "worked": [{"q": r"Negate 'every student scored more than 50'.", "a": r"'At least one student scored 50 or less.'"}],
},
"proof": {
    "summary": r"Recognise the four proof types the spec names - direct deduction, cases, contradiction, disproof by counterexample - and be able to reorder a scrambled proof, spot a circular argument, and justify a conjecture made from small cases with a general argument.",
    "sections": [
        {"h": "Proof types (Prf1)", "body": r"""- Direct: start from what is given and deduce step by step ('$n(n + 1)$ is a product of consecutive integers, so it is even').
- Cases: split by parity, by remainder mod $3$, by sign; the cases must cover everything.
- Contradiction: assume the statement is false (the hypothesis true **and** the conclusion false), derive an impossibility. Classic: $\sqrt2$ irrational, infinitely many primes.
- Counterexample: one instance with the hypothesis true and the conclusion false disproves a 'for all' claim; it says nothing about an 'exists' claim.
- Checking small cases ($n^2 - n + 41$ is prime for $n = 1, \ldots, 40$ but not $41$) is evidence, not proof."""},
        {"h": "Working with proofs (Prf2-Prf4)", "body": r"""- Ordering steps: the assumption comes first, the contradiction last; each line must use only earlier lines.
- Deducing from given implications: use the contrapositive ('$f(x) > 0 \Rightarrow g(x) > 0$ and $g(2) = -1$' gives $f(2) \leq 0$).
- Backwards working (start from the result, reach a truth) is valid only if every step is reversible and the proof is then presented forwards.
- Conjecture from a pattern, then justify algebraically: $T_n + T_{n+1} = (n + 1)^2$ by expanding.
- A proof for $\sqrt2$ copied for $\sqrt4$ breaks where the parity argument no longer applies - identify **which** step fails."""},
    ],
    "key": [r"counterexample: hypothesis true, conclusion false", r"contradiction: assume not-conclusion", r"cases must be exhaustive", r"small cases $\neq$ proof"],
    "traps": [r"'If $x^2 > 9$ then $x > 3$' is false: $x = -4$. Taking square roots loses the negative branch.",
              r"Assuming the claim to prove the claim is circular even if every step 'works'.",
              r"An 'exists' statement cannot be disproved by a counterexample; it needs a proof that no example exists."],
    "worked": [{"q": r"Prove: if $n^2$ is even then $n$ is even.", "a": r"Contrapositive: if $n$ is odd, $n = 2k + 1$, then $n^2 = 4k^2 + 4k + 1$ is odd."}],
},
"reasoning": {
    "summary": r"Multi-step problems that combine small facts: parity, pigeonhole, extremal cases, counting by complementary sets, and 'must be true / could be true' logic. Work systematically, test the extreme or boundary case, and build a counterexample before trusting an intuition.",
    "sections": [
        {"h": "Standard tools", "body": r"""- Pigeonhole: to force two numbers differing by $10$ from $\{1, \ldots, 20\}$, pair them up; $n = $ pairs $+ 1$.
- Parity: the sum of degrees in a handshake graph is even; the sum of five consecutive odd numbers is $5 \times$ the middle one.
- Factor pairs: $x^2 - y^2 = 45$, $(x - y)(x + y) = 45$ with matching parity; $\frac1m + \frac1n = \frac14 \Rightarrow (m - 4)(n - 4) = 16$.
- Inclusion-exclusion: numbers up to $999$ divisible by $2$ or $5$: $499 + 199 - 99$.
- Invariants: every match eliminates one player, so $37$ players need $36$ matches whatever the draw."""},
        {"h": "Must / could / cannot", "body": r"""- 'Must be true': try to build a counterexample; if none exists, prove it. 'Could be true': one example suffices. 'Cannot': show a contradiction.
- Exactly-one-true puzzles: assume each candidate is the truthful one and check consistency.
- Order/inequality statements: test negative values and values between $0$ and $1$ ($ab < bc$ fails for negative $b$).
- Sequences with block conditions: overlapping sums (three-term sums positive, five-term sums negative) - combine blocks to compare."""},
    ],
    "key": [r"pigeonhole: $n$ boxes, $n + 1$ objects", r"$(x-y)(x+y)$ factor pairs", r"inclusion-exclusion $|A \cup B| = |A| + |B| - |A \cap B|$", r"test negatives, zero and fractions"],
    "traps": [r"A sum of two primes is odd only if one of them is $2$.",
              r"'Exactly two of three statements are true' - a number making all three true is excluded.",
              r"Counting ordered pairs: $(2, 8)$ and $(8, 2)$ are different."],
    "worked": [{"q": r"Smallest $n$ so that $n$ numbers from $1$-$20$ must include two differing by $10$?", "a": r"Ten pairs $\{k, k + 10\}$; $n = 11$."}],
},
"errors": {
    "summary": r"Every year Paper 2 shows a student's argument and asks for the first wrong line. The spec names the classics: '$x^2 = y^2$ so $x = y$', '$\sin\alpha = \sin\beta$ so $\alpha = \beta$'. Add: dividing by something that may be zero, multiplying an inequality by a quantity of unknown sign, squaring without checking, assuming the conclusion, and applying a theorem outside its conditions.",
    "sections": [
        {"h": "The catalogue of invalid steps (Err2)", "body": r"""- $x^2 = y^2 \Rightarrow x = \pm y$, not $x = y$. $x^2 > 9 \Rightarrow |x| > 3$.
- $\sin\alpha = \sin\beta \Rightarrow \alpha = \beta$ or $\alpha = 180^\circ - \beta$ (plus periods). Same for $\cos$ and $\tan$.
- Dividing by $x$, $a - b$ or $\cos x$ loses the case where it is zero (the '$1 = 2$' proof; $x^2 = 4x$; $2\cos^2 x = \cos x$).
- Multiplying an inequality by $x - 2$ or $ab$ without knowing the sign.
- Squaring both sides can create extraneous roots: substitute back ($\sqrt{x + 3} = x - 3$ gives only $x = 6$).
- Starting from the statement to be proved and reaching a true statement (needs reversibility and reversed presentation).
- Applying the FTC or an integral across a point where the function is undefined ($\int_{-1}^1 x^{-2}\,dx$).
- Proving the converse instead of the statement; checking cases instead of proving generally; using a result that is exactly the claim (circularity)."""},
        {"h": "How to attack an 'identify the error' question (Err1)", "body": r"""- Read each line as a claimed deduction from the previous ones; ask 'is this always valid?' not 'is it true here?'.
- Test the claim itself with a quick counterexample first ($n = 2$ for '$4 \mid n^2 \Rightarrow 4 \mid n$'); if the claim is false, the error is at the step that is not a valid deduction.
- The first error is usually where a hidden assumption enters (sign, non-zero, domain).
- 'Completely correct' is a genuine option: valid inductions and completed-square arguments do appear."""},
    ],
    "key": [r"$x^2 = y^2 \Rightarrow x = \pm y$", r"never divide by a possible zero", r"inequality $\times$ negative flips", r"squaring: check solutions", r"backwards proof needs reversibility"],
    "traps": [r"'$f'(x) \geq 0$ with equality at one point' still gives an increasing function; the error is in claiming $f' > 0$ everywhere, not in the conclusion.",
              r"Two even primes? No - but '$2$ is even and prime' breaks 'every prime is odd'.",
              r"$f'(a) = f''(a) = 0$ does not force an inflexion ($x^4$)."],
    "worked": [{"q": r"Where is the first error in: $a = b$; $a^2 = ab$; $a^2 - b^2 = ab - b^2$; divide by $a - b$: $a + b = b$?", "a": r"Dividing by $a - b = 0$."}],
},
}
