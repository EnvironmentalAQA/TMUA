"""Full teaching solutions: statistics (STA-xx) and probability (PRO-xx)."""
from gen.model import Sol

SOLUTIONS = {

# ---------------- statistics ----------------

"STA-01": Sol(
    idea=r"Means questions are almost always really about **totals**. Convert each mean into a total before doing anything else.",
    steps=[
        (r"Original total $= 5 \times 12 = 60$.",
         r"mean $=\dfrac{\text{total}}{\text{how many}}$, so total $=$ mean $\times$ how many."),
        (r"New total $= 6 \times 14 = 84$.",
         r"There are now six numbers, and their mean is $14$."),
        (r"The sixth number is the difference: $84 - 60 = 24$.",
         r"Nothing else changed, so the whole increase in the total is the new number."),
    ],
    pitfalls=[r"Answering $14$ - the new **mean**, not the new **number**.",
              r"Answering $84$, the new total rather than the added value.",
              r"Thinking the new number must be $2$ more than the old mean; the mean rose by $2$ for **all six**, so the newcomer must carry $6 \times 2 = 12$ extra above the old mean of $12$, giving $24$."],
    takeaway=r"Turn means into totals; the added value is the change in total."),

"STA-02": Sol(
    idea=r"On a histogram the **area** of a bar is the frequency, not its height. Height is frequency density.",
    steps=[
        (r"Read the first bar: width $15 - 10 = 5$, height $3.2$.",
         r"Class widths on a histogram are usually unequal - that is why density is used."),
        (r"Frequency $=$ density $\times$ width $= 3.2 \times 5 = 16$.",
         r"Rearranging density $=\dfrac{\text{frequency}}{\text{width}}$."),
        (r"Second bar: width $25 - 15 = 10$, so frequency $= 1.5 \times 10 = 15$.",
         r"Same rule, wider class."),
        (r"Add: $16 + 15 = 31$.",
         r"Total frequency of the two classes."),
    ],
    pitfalls=[r"Adding the heights: $3.2 + 1.5 = 4.7$ - an offered option.",
              r"Using the same width for both bars; the second is twice as wide even though it is shorter."],
    takeaway=r"Histogram: frequency $=$ density $\times$ class width (area of the bar)."),

"STA-03": Sol(
    idea=r"Write expressions for the mean and the median, then equate. The given range for $x$ tells you where it sits in the order.",
    steps=[
        (r"Since $7 \leq x \leq 12$, the sorted list is $3, 7, x, 12, 18$, so the median is $x$.",
         r"With five values the median is the third; the constraint is there precisely to fix $x$'s position."),
        (r"Mean $= \dfrac{3 + 7 + x + 12 + 18}{5} = \dfrac{40 + x}{5}$.",
         r"Sum the known values first: $3+7+12+18 = 40$."),
        (r"Set mean $=$ median: $\dfrac{40+x}{5} = x$.",
         r"That is the condition stated."),
        (r"Solve: $40 + x = 5x \Rightarrow 4x = 40 \Rightarrow x = 10$.",
         r"And $10$ does lie in $[7, 12]$, so the assumed ordering holds."),
    ],
    pitfalls=[r"Taking the median to be $12$ (the middle of the numbers as originally listed without $x$).",
              r"Forgetting to check that the answer is consistent with the assumed position in the order."],
    takeaway=r"Order first, then write the median; always check the solution respects the ordering you assumed."),

"STA-04": Sol(
    idea=r"Grouped data: you cannot know the individual values, so **estimate** using class midpoints.",
    steps=[
        (r"Find midpoints: $\frac{0+10}{2} = 5$, $\frac{10+20}{2} = 15$, $\frac{20+40}{2} = 30$.",
         r"The midpoint is the best single representative of a class."),
        (r"Multiply each by its frequency: $4(5) = 20$, $10(15) = 150$, $6(30) = 180$.",
         r"This estimates the total of all the values in each class."),
        (r"Total $= 350$; total frequency $= 4 + 10 + 6 = 20$.",
         r"Add both columns."),
        (r"Mean $= \dfrac{350}{20} = 17.5$.",
         r"Divide estimated total by the number of observations."),
    ],
    pitfalls=[r"Using the midpoint $25$ for the last class by assuming equal widths - it runs from $20$ to $40$, so its midpoint is $30$.",
              r"Dividing by $3$ (the number of classes) instead of $20$."],
    takeaway=r"Grouped mean $\approx \dfrac{\sum f x_{\text{mid}}}{\sum f}$ - and read each class width individually."),

"STA-05": Sol(
    idea=r"A correlation-and-causation statement test. Decide what correlation does and does not licence.",
    steps=[
        (r"I: strong positive correlation means higher revision went with higher marks. **True** - that is exactly what correlation describes.",
         r"'Tended to' is a statement about the trend, not about every student."),
        (r"II: correlation does not establish causation. **False.**",
         r"A hidden variable (motivation, prior ability) could drive both, so the data alone cannot prove cause."),
        (r"III: using a line of best fit **within** the data range is interpolation. **True.**",
         r"Interpolation is legitimate; extrapolation beyond the data is what is unreliable."),
        (r"So I and III only.",
         r"Match to the list."),
    ],
    pitfalls=[r"Accepting II because the causal story sounds plausible - plausibility is not evidence.",
              r"Rejecting III by confusing interpolation with extrapolation."],
    takeaway=r"Correlation licenses description and interpolation; it never licenses a causal claim on its own."),

"STA-06": Sol(
    idea=r"Coding: see separately how a linear transformation affects a measure of **location** (the mean) and a measure of **spread** (the range).",
    steps=[
        (r"Each value $x$ becomes $2x + 3$.",
         r"Read the transformation carefully: double, then add."),
        (r"The mean follows the same transformation: new mean $= 2m + 3$.",
         r"Because $\overline{2x+3} = 2\bar x + 3$ - the mean is linear."),
        (r"The range is a **difference**: $(2x_{\max}+3) - (2x_{\min}+3) = 2(x_{\max} - x_{\min}) = 2R$.",
         r"The $+3$ cancels in the subtraction; only the scaling survives."),
        (r"So mean $2m+3$, range $2R$.",
         r"Location shifts and scales; spread only scales."),
    ],
    pitfalls=[r"Giving range $2R + 3$ - the offered trap; adding a constant to every value shifts the data but does not stretch it.",
              r"Leaving the range unchanged as $R$, forgetting the doubling."],
    takeaway=r"Under $x \to ax + b$: mean $\to a\bar x + b$, but spread (range, IQR, SD) $\to |a| \times$ spread - the $+b$ never affects spread."),

"STA-07": Sol(
    idea=r"A 'must be true' question. Test each claim by trying to construct a counterexample.",
    steps=[
        (r"The mean: the total rises by $20$, so the mean rises by $\frac{20}{7}$ - it **definitely** increases.",
         r"Nothing else changed, so the total change is $+20$ across $7$ values."),
        (r"The median: try the smallest $= 1$ becoming $21$. That value jumps past the middle, so the values shift along and the median changes.",
         r"Moving a value from below the median to above it pushes the middle value up one place."),
        (r"Now try the smallest $= -15$ becoming $5$, still below the median $10$. The ordering of the middle is untouched, so the median is unchanged.",
         r"A value that stays on the same side of the median cannot move it."),
        (r"Both are possible, so the median **may or may not** change while the mean definitely rises.",
         r"That is precisely the statement offered."),
    ],
    pitfalls=[r"Claiming the median never changes - true only if the increased value stays below the median.",
              r"Claiming both must increase, which would need the smallest to always overtake the middle."],
    takeaway=r"'Must be true' means no counterexample exists; hunt for one before agreeing."),

"STA-08": Sol(
    idea=r"On a cumulative frequency graph, quartiles are read by going **in** from the cumulative frequency axis at $\frac n4$, $\frac n2$, $\frac{3n}{4}$.",
    steps=[
        (r"With $n = 80$: the lower quartile is at cumulative frequency $\frac{80}{4} = 20$, the upper at $\frac{3 \times 80}{4} = 60$.",
         r"Cumulative frequency graphs use $\frac n4$ and $\frac{3n}{4}$ directly (no $+1$, unlike a raw list)."),
        (r"The point $(20, 20)$ gives $Q_1 = 20$.",
         r"Read across at CF $= 20$ and down to the value axis."),
        (r"The point $(45, 60)$ gives $Q_3 = 45$.",
         r"Read across at CF $= 60$."),
        (r"IQR $= Q_3 - Q_1 = 45 - 20 = 25$.",
         r"The interquartile range is a difference of **values**, not of frequencies."),
    ],
    pitfalls=[r"Subtracting the cumulative frequencies, $60 - 20 = 40$ - an offered option.",
              r"Using the median point $(30, 40)$ as a quartile."],
    takeaway=r"Go in from the frequency axis at $\frac n4$ and $\frac{3n}{4}$, read off values, then subtract the **values**."),

"STA-09": Sol(
    idea=r"A combined mean is a **weighted** average: go back to totals, since the classes are different sizes.",
    steps=[
        (r"Class A total $= 20 \times 60 = 1200$.",
         r"Total $=$ mean $\times$ number."),
        (r"Class B total $= 30 \times 70 = 2100$.",
         r"Same again for the larger class."),
        (r"Combined mean $= \dfrac{1200 + 2100}{50} = \dfrac{3300}{50} = 66$.",
         r"Divide the grand total by the grand number of students."),
    ],
    pitfalls=[r"Averaging the means: $\frac{60+70}{2} = 65$ - an offered option, and wrong because class B has more students.",
              r"A quick check: the answer must lie **closer to $70$** than to $60$, which $66$ does."],
    takeaway=r"Never average averages; weight by group size - or just work with totals."),

"STA-10": Sol(
    idea=r"The mean is pulled by extreme values; the median is not. Look for skew rather than computing everything.",
    steps=[
        (r"Check $1, 2, 3, 4, 20$: median $= 3$, mean $= \frac{30}{5} = 6$. Mean $>$ median. **Yes.**",
         r"The single large outlier $20$ drags the mean far above the middle."),
        (r"$1,2,3,4,5$ and $2,4,6,8,10$ and $5,5,5,5,5$ are symmetric, so mean $=$ median.",
         r"For symmetric data the two coincide - no need to compute."),
        (r"$1, 10, 11, 12, 13$: median $= 11$, mean $= \frac{47}{5} = 9.4$, so mean $<$ median.",
         r"Here the outlier is small, so it drags the mean **down** - the mirror image."),
        (r"So only $1, 2, 3, 4, 20$ works.",
         r"One high outlier gives positive skew."),
    ],
    pitfalls=[r"Assuming any outlier raises the mean - a low outlier lowers it, as in $1, 10, 11, 12, 13$.",
              r"Computing all five means when symmetry settles three of them instantly."],
    takeaway=r"Mean $>$ median signals a tail to the **right** (a high outlier); mean $<$ median signals a tail to the left."),

# ---------------- probability ----------------

"PRO-01": Sol(
    idea=r"'Different colours' happens in two orders. Either add the two ordered cases or use the complement.",
    steps=[
        (r"Red then blue: $\dfrac{4}{10} \times \dfrac{6}{9}= \dfrac{24}{90}$.",
         r"After removing a red, $9$ counters remain and all $6$ blues are still there - **without replacement**."),
        (r"Blue then red: $\dfrac{6}{10} \times \dfrac{4}{9} = \dfrac{24}{90}$.",
         r"The same product, but the orders are distinct outcomes so both count."),
        (r"Add: $\dfrac{48}{90} = \dfrac{8}{15}$.",
         r"Mutually exclusive cases add; then cancel by $6$."),
        (r"Check by complement: $P(\text{same}) = \frac{4}{10}\frac{3}{9} + \frac{6}{10}\frac{5}{9} = \frac{12+30}{90} = \frac{42}{90}$, and $1 - \frac{42}{90} = \frac{48}{90}$ ✓.",
         r"Two routes agreeing is strong confirmation."),
    ],
    pitfalls=[r"Counting only one order, giving $\frac{4}{15}$ - an offered option.",
              r"Keeping the denominator at $10$ for the second draw ($\frac{12}{25}$), which is the **with replacement** answer."],
    takeaway=r"Without replacement: reduce both the relevant colour count and the total; and count both orders unless the question fixes one."),

"PRO-02": Sol(
    idea=r"A product is odd only when **every** factor is odd - so this is an 'and' of two independent events.",
    steps=[
        (r"Odd $\times$ odd $=$ odd; any even factor makes the product even.",
         r"Recognising this converts the question into a much simpler one."),
        (r"$P(\text{first die odd}) = \frac36 = \frac12$; same for the second.",
         r"Three odd faces out of six: $1, 3, 5$."),
        (r"Independent dice, so multiply: $\frac12 \times \frac12 = \frac14$.",
         r"One die's outcome has no effect on the other."),
    ],
    pitfalls=[r"Answering $\frac12$ by thinking 'half of all products are odd' - in fact only $9$ of the $36$ outcomes are.",
              r"Treating it as a **sum** (where odd $+$ odd $=$ even), a different and much more common question."],
    takeaway=r"Product odd $\iff$ all factors odd; product even $\iff$ at least one even."),

"PRO-03": Sol(
    idea=r"Three definitions to test: independence, mutual exclusivity and the addition rule.",
    steps=[
        (r"I: independence means $P(A \cap B) = P(A)P(B)$. Here $0.6 \times 0.5 = 0.3$, which matches. **True.**",
         r"Independence is a numerical condition, not something you can eyeball."),
        (r"II: mutually exclusive means $P(A \cap B) = 0$. It is $0.3 \neq 0$. **False.**",
         r"They overlap, so they can happen together."),
        (r"III: $P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.6 + 0.5 - 0.3 = 0.8$. **True.**",
         r"Subtract the overlap or you count it twice."),
        (r"So I and III only.",
         r"Match to the list."),
    ],
    pitfalls=[r"Treating independent and mutually exclusive as the same thing - they are near-opposites: two events with non-zero probabilities cannot be both.",
              r"Forgetting the $-P(A\cap B)$ and answering $1.1$, which is impossible for a probability."],
    takeaway=r"Independent: $P(A\cap B) = P(A)P(B)$. Mutually exclusive: $P(A\cap B) = 0$. Check the numbers, not the words."),

"PRO-04": Sol(
    idea=r"'Exactly one head' in two tosses happens in two orders; that gives a quadratic in $p$ with two valid roots.",
    steps=[
        (r"$P(\text{exactly one head}) = P(HT) + P(TH) = p(1-p) + (1-p)p = 2p(1-p)$.",
         r"The factor $2$ is the number of orders - equivalently $\binom21$."),
        (r"Set $2p(1-p) = \frac38$ and clear fractions: $16p(1-p) = 3$, so $16p - 16p^2 = 3$.",
         r"Multiply through by $8$."),
        (r"Rearrange and factorise: $16p^2 - 16p + 3 = 0 \Rightarrow (4p-1)(4p-3) = 0$.",
         r"Check: $4 \times 4 = 16$, $-1 \times -3 = 3$, and $-12p - 4p = -16p$ ✓."),
        (r"So $p = \frac14$ or $p = \frac34$; both lie in $[0,1]$, so both are valid.",
         r"They are mirror images - swapping heads and tails leaves 'exactly one head' unchanged, so the symmetry is expected."),
    ],
    pitfalls=[r"Omitting the factor $2$, which gives $p^2 - p + \frac38 = 0$ with no real roots.",
              r"Discarding one root; a biased coin can favour either face, and the symmetry $p \leftrightarrow 1-p$ guarantees a pair."],
    takeaway=r"'Exactly one' needs the count of orders; and check **both** roots against $0 \leq p \leq 1$ rather than assuming one is spurious."),

"PRO-05": Sol(
    idea=r"Expected number of successes in repeated independent trials is simply $n \times p$.",
    steps=[
        (r"Identify $n = 200$ spins and $p = 0.15$.",
         r"Each spin is an independent trial with the same probability."),
        (r"Expected number $= 200 \times 0.15 = 30$.",
         r"$0.15 = \frac{15}{100}$, and $15\%$ of $200$ is $30$."),
    ],
    pitfalls=[r"Answering $15$ by reading the percentage as the answer.",
              r"Expecting the answer to be a whole number in general - expectations often are not, and that is fine."],
    takeaway=r"Expected frequency $= n \times p$."),

"PRO-06": Sol(
    idea=r"The words 'given that' signal **conditional** probability: the sample space shrinks to the condition.",
    steps=[
        (r"Restrict attention to the $18$ French students - they are now the whole universe.",
         r"'Given that the student studies French' means we only consider those students."),
        (r"Of those $18$, the number who also study German is $5$.",
         r"The overlap is stated directly in the question."),
        (r"$P(\text{German} \mid \text{French}) = \dfrac{5}{18}$.",
         r"Equivalently $\dfrac{P(F \cap G)}{P(F)} = \dfrac{5/30}{18/30} = \dfrac{5}{18}$ - the $30$s cancel."),
    ],
    pitfalls=[r"Using $\frac{5}{30}$ - the unconditional probability of studying both, ignoring the condition.",
              r"Using $\frac{5}{12}$, which conditions on **German** instead - the wrong way round."],
    takeaway=r"Conditioning replaces the denominator: divide by the size of the group you are told you are in."),

"PRO-07": Sol(
    idea=r"Either count the favourable outcomes out of $8$, or exploit the symmetry between heads and tails.",
    steps=[
        (r"With three coins there are $2^3 = 8$ equally likely outcomes.",
         r"Each coin independently doubles the number of outcomes."),
        (r"'More heads than tails' means $2$ or $3$ heads: $\binom32 + \binom33 = 3 + 1 = 4$ outcomes.",
         r"With an odd number of coins there is no tie, so every outcome has a strict majority."),
        (r"$P = \dfrac48 = \dfrac12$.",
         r"Or instantly: heads and tails are symmetric and a tie is impossible, so each must have probability $\frac12$."),
    ],
    pitfalls=[r"Answering $\frac38$ - the probability of exactly $2$ heads, forgetting the all-heads case.",
              r"Trying the symmetry argument with an **even** number of coins, where ties break it."],
    takeaway=r"An odd number of fair coins: $P(\text{more heads}) = \frac12$ by symmetry, since ties cannot occur."),

"PRO-08": Sol(
    idea=r"Set up the without-replacement probability in terms of $n$, then solve the resulting quadratic.",
    steps=[
        (r"There are $n + 3$ balls in total. $P(\text{both white}) = \dfrac{n}{n+3} \times \dfrac{n-1}{n+2}$.",
         r"After one white is removed, $n-1$ whites remain out of $n+2$."),
        (r"Set equal to $\frac{5}{12}$ and cross-multiply: $12n(n-1) = 5(n+3)(n+2)$.",
         r"Cross-multiplying is safe since all denominators are positive."),
        (r"Expand: $12n^2 - 12n = 5(n^2 + 5n + 6) = 5n^2 + 25n + 30$.",
         r"Expand the right side carefully: $(n+3)(n+2) = n^2 + 5n + 6$."),
        (r"Collect: $7n^2 - 37n - 30 = 0$, which factorises as $(7n + 5)(n - 6) = 0$.",
         r"Check the middle term: $-42n + 5n = -37n$ ✓."),
        (r"$n = -\frac57$ is impossible for a count, so $n = 6$.",
         r"Verify: $\frac{6}{9}\times\frac58 = \frac{30}{72} = \frac{5}{12}$ ✓."),
    ],
    pitfalls=[r"Writing $\left(\frac{n}{n+3}\right)^2$, the with-replacement version.",
              r"Accepting the negative root instead of rejecting it on contextual grounds."],
    takeaway=r"Model without replacement by decreasing both numerator and denominator, then reject roots that cannot be counts."),

"PRO-09": Sol(
    idea=r"The probabilities of an exhaustive set of outcomes sum to $1$. Use that to find $x$ first.",
    steps=[
        (r"Early, on time, late are the only possibilities, so $0.1 + x + 2x = 1$.",
         r"Exhaustive and mutually exclusive outcomes have total probability $1$."),
        (r"Solve: $3x = 0.9$, so $x = 0.3$ and late $= 0.6$.",
         r"Subtract $0.1$, then divide by $3$."),
        (r"Not late $=$ early $+$ on time $= 0.1 + 0.3 = 0.4$.",
         r"Or use the complement: $1 - 0.6 = 0.4$ - quicker and a useful check."),
    ],
    pitfalls=[r"Stopping at $x = 0.3$ and answering that, or answering $0.6$, the probability of being late.",
              r"Forgetting 'early' counts as 'not late'."],
    takeaway=r"Probabilities of all outcomes sum to $1$; 'not late' is the complement of 'late'."),

"PRO-10": Sol(
    idea=r"'First success on the $k$th trial' means failure, failure, ..., then success - a chain of independent events.",
    steps=[
        (r"The first two throws must be non-sixes: probability $\frac56$ each.",
         r"'First six on the third' forbids a six on throws one and two."),
        (r"The third throw must be a six: probability $\frac16$.",
         r"Exactly one way to succeed on that throw."),
        (r"Multiply: $\left(\frac56\right)^2 \times \frac16 = \dfrac{25}{216}$.",
         r"Independent throws, so probabilities multiply."),
    ],
    pitfalls=[r"Answering $\frac16$ by ignoring the first two throws.",
              r"Using $\left(\frac16\right)^3 = \frac{1}{216}$, which is the probability of **three** sixes."],
    takeaway=r"First success on trial $k$: $(1-p)^{k-1}p$ - failures first, then the one success."),

"PRO-11": Sol(
    idea=r"The question asks for the **expression**, so the reasoning is entirely about how the second draw changes.",
    steps=[
        (r"First card an ace: $\dfrac{4}{52}$ - four aces in the pack.",
         r"All $52$ cards are equally likely."),
        (r"Given that, one ace and one card overall have gone: $3$ aces remain among $51$ cards.",
         r"Without replacement, **both** numbers drop by one."),
        (r"Multiply: $\dfrac{4}{52} \times \dfrac{3}{51}$.",
         r"This is $P(A) \times P(B \mid A)$, the multiplication rule for dependent events."),
    ],
    pitfalls=[r"$\frac{4}{52} \times \frac{4}{52}$ - that is with replacement.",
              r"$\frac{4}{52} \times \frac{3}{52}$ - reducing the aces but forgetting the total also falls to $51$.",
              r"Adding rather than multiplying: 'and' means multiply."],
    takeaway=r"Without replacement, reduce numerator **and** denominator; 'and' $\Rightarrow$ multiply."),

"PRO-12": Sol(
    idea=r"'Neither' is the complement of 'at least one'. Mutual exclusivity makes the addition rule simple.",
    steps=[
        (r"Mutually exclusive means $P(A \cap B) = 0$, so $P(A \cup B) = 0.3 + 0.4 = 0.7$.",
         r"No overlap to subtract."),
        (r"'Neither' is the complement of 'A or B': $1 - 0.7 = 0.3$.",
         r"Everything not in $A \cup B$."),
    ],
    pitfalls=[r"Answering $0.7$, the probability that one of them **does** happen.",
              r"Computing $0.7 \times 0.6 = 0.42$ by treating them as independent - they are explicitly not, and independent events with these probabilities could not be mutually exclusive."],
    takeaway=r"Neither $= 1 - P(A \cup B)$; and for mutually exclusive events $P(A\cup B)$ is just the sum."),

}
