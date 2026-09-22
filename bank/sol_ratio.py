"""Full teaching solutions: ratio, proportion and percentages (RAT-xx)."""
from gen.model import Sol

SOLUTIONS = {

"RAT-01": Sol(
    idea=r"Successive percentage changes **multiply**. Convert each to a multiplier and combine.",
    steps=[
        (r"A $20\%$ reduction multiplies by $0.8$.",
         r"You keep $80\%$ of the price: $1 - 0.20 = 0.8$."),
        (r"A further $25\%$ reduction multiplies by $0.75$ - applied to the **sale** price, not the original.",
         r"The second discount acts on whatever the price already is; that is why the changes multiply."),
        (r"Combine: $0.8 \times 0.75 = 0.6$.",
         r"Multiplying the multipliers gives the overall multiplier."),
        (r"So the final price is $60\%$ of the original.",
         r"Equivalently a $40\%$ reduction overall - not $45\%$."),
    ],
    pitfalls=[r"Adding the percentages to get $45\%$ off, hence $55\%$ - an offered option.",
              r"Applying the second reduction to the original price."],
    takeaway=r"Percentage changes compose by multiplying multipliers, never by adding percentages."),

"RAT-02": Sol(
    idea=r"A reverse-percentage problem: the given figure is the **result**, so divide by the multiplier.",
    steps=[
        (r"A $15\%$ increase means multiplying by $1.15$.",
         r"$100\% + 15\% = 115\% = 1.15$."),
        (r"Write the relation: $1.15 \times (\text{original}) = 27\,600$.",
         r"The original is the unknown; the multiplier acts on it."),
        (r"Divide: $\text{original} = \dfrac{27\,600}{1.15} = 24\,000$.",
         r"$27600 \div 115 = 240$, so dividing by $1.15$ gives $24\,000$."),
        (r"Check: $24\,000 \times 1.15 = 27\,600$ ✓.",
         r"Always multiply back - it catches the commonest error instantly."),
    ],
    pitfalls=[r"Taking $15\%$ off the new salary: $27\,600 \times 0.85 = 23\,460$ - an offered option.",
              r"Dividing by $0.15$ or by $1.5$."],
    takeaway=r"Reverse percentage: **divide** by the multiplier, then check by multiplying back."),

"RAT-03": Sol(
    idea=r"Sharing in a ratio: find the value of one part, then answer the question actually asked.",
    steps=[
        (r"Add the ratio parts: $2 + 3 + 7 = 12$.",
         r"The total is divided into this many equal parts."),
        (r"One part: $\pounds 600 \div 12 = \pounds 50$.",
         r"Divide the total by the number of parts."),
        (r"The difference between $C$ and $A$ is $7 - 2 = 5$ parts.",
         r"Work with the **difference** in parts rather than computing both shares."),
        (r"So the difference is $5 \times \pounds 50 = \pounds 250$.",
         r"Check: $A$ gets $\pounds100$, $C$ gets $\pounds350$ ✓."),
    ],
    pitfalls=[r"Giving $C$'s share ($\pounds350$) instead of the difference - an offered option.",
              r"Dividing by $3$ (the number of people) instead of $12$ (the number of parts)."],
    takeaway=r"Find the value of one part first; then read carefully whether a share, a difference or a total is wanted."),

"RAT-04": Sol(
    idea=r"Inverse proportion to a **square**. Find the constant, then substitute.",
    steps=[
        (r"Write the relationship: $y = \dfrac{k}{x^2}$.",
         r"'Inversely proportional to the square of $x$' puts $x^2$ in the denominator."),
        (r"Find $k$ from the given pair: $9 = \dfrac{k}{4}$, so $k = 36$.",
         r"Substitute $x = 2$, $y = 9$; note $x^2 = 4$, not $2$."),
        (r"Substitute $x = 6$: $y = \dfrac{36}{36} = 1$.",
         r"$6^2 = 36$."),
    ],
    pitfalls=[r"Using $y = \frac kx$ and getting $3$ - an offered option.",
              r"Reasoning '$x$ triples so $y$ thirds', which ignores the squaring (it should be a ninth)."],
    takeaway=r"Inverse square: tripling $x$ divides $y$ by $9$. Always find $k$ explicitly."),

"RAT-05": Sol(
    idea=r"Repeated doubling. Count the doublings, then raise $2$ to that power.",
    steps=[
        (r"Count the doubling periods: $24 \div 3 = 8$.",
         r"Each $3$-hour block doubles the population."),
        (r"Each doubling multiplies by $2$, so eight of them multiply by $2^8$.",
         r"Repeated multiplication is exponentiation - not multiplication by $8$."),
        (r"$2^8 = 256$.",
         r"Worth knowing the powers of $2$ up to $2^{10} = 1024$."),
    ],
    pitfalls=[r"Multiplying by $8$ or computing $2 \times 8 = 16$ - both offered.",
              r"Using $2^6 = 64$ by dividing $24$ by $4$."],
    takeaway=r"Growth factor $= (\text{factor per period})^{\text{number of periods}}$."),

"RAT-06": Sol(
    idea=r"Similar solids: areas scale as the square of lengths, volumes as the cube. Work back to the length ratio first.",
    steps=[
        (r"Areas are in ratio $4 : 9$, so the length ratio is $\sqrt4 : \sqrt9 = 2 : 3$.",
         r"Area scales with the square of length, so undo it with a square root."),
        (r"Volumes scale with the cube of length: $2^3 : 3^3$.",
         r"Every linear dimension is scaled, so three dimensions give the cube."),
        (r"So the volume ratio is $8 : 27$.",
         r"Check: the ratios $2:3$, $4:9$, $8:27$ are the classic length/area/volume triple."),
    ],
    pitfalls=[r"Cubing the **area** ratio to get $64 : 729$ - an offered option.",
              r"Leaving the answer as the length ratio $2:3$."],
    takeaway=r"Length $k$, area $k^2$, volume $k^3$: always return to the length ratio before converting."),

"RAT-07": Sol(
    idea=r"A changing ratio where one quantity stays fixed. Anchor on the unchanged amount.",
    steps=[
        (r"Split the $35$ kg in the ratio $5:2$: seven parts of $5$ kg, so $25$ kg sand and $10$ kg cement.",
         r"$35 \div 7 = 5$ kg per part."),
        (r"Only cement is added, so the sand stays at $25$ kg.",
         r"Identify what does **not** change - that is the anchor for the new ratio."),
        (r"In the new ratio $5 : 3$, the $5$ parts correspond to $25$ kg, so one part is $5$ kg and the cement must be $3 \times 5 = 15$ kg.",
         r"Scale the new ratio to the fixed quantity."),
        (r"Cement to add: $15 - 10 = 5$ kg.",
         r"The question asks for the amount added, not the final amount."),
    ],
    pitfalls=[r"Answering $15$ kg (the new total cement) - an offered option.",
              r"Rescaling the sand as well, as though both quantities changed."],
    takeaway=r"In 'add to change the ratio' problems, anchor on the quantity that stays the same."),

"RAT-08": Sol(
    idea=r"An increase then an equal-percentage decrease. The multipliers form a difference of two squares.",
    steps=[
        (r"Write the multipliers: $\left(1 + \frac{x}{100}\right)$ then $\left(1 - \frac{x}{100}\right)$.",
         r"Both act on the running value, so they multiply."),
        (r"Multiply: $\left(1 + \frac{x}{100}\right)\left(1 - \frac{x}{100}\right) = 1 - \dfrac{x^2}{10\,000}$.",
         r"Difference of two squares - which shows the result is always **less** than $1$."),
        (r"A $4\%$ overall decrease means the multiplier is $0.96$: $1 - \dfrac{x^2}{10\,000} = 0.96$.",
         r"Convert the stated overall change into a multiplier."),
        (r"Solve: $\dfrac{x^2}{10\,000} = 0.04 \Rightarrow x^2 = 400 \Rightarrow x = 20$.",
         r"Take the positive root, since $x$ is a percentage size."),
    ],
    pitfalls=[r"Assuming $x = 4$ because the net change is $4\%$ - an offered option.",
              r"Arithmetic: $0.04 \times 10\,000 = 400$, not $40$."],
    takeaway=r"Up then down by $x\%$ always loses: the net multiplier is $1 - \frac{x^2}{10\,000}$."),

"RAT-09": Sol(
    idea=r"Chaining two proportionality statements. Write each with a constant and substitute.",
    steps=[
        (r"Write them algebraically: $p = a\sqrt q$ and $q = \dfrac{b}{r}$ for constants $a, b > 0$.",
         r"'Directly proportional' means a constant multiple; 'inversely' means a constant over."),
        (r"Substitute: $p = a\sqrt{\dfrac br} = \dfrac{a\sqrt b}{\sqrt r}$.",
         r"The square root distributes over the quotient."),
        (r"Since $a\sqrt b$ is a constant, $p = \dfrac{\text{constant}}{\sqrt r}$: $p$ is inversely proportional to $\sqrt r$.",
         r"Collect all the constants into one; only the $r$-dependence matters."),
    ],
    pitfalls=[r"Forgetting the square root and concluding $p \propto \frac1r$ - an offered option.",
              r"Losing the 'inversely' and choosing $p \propto \sqrt r$."],
    takeaway=r"Chain proportionalities by substituting; the accumulated constants never affect the final relationship."),

"RAT-10": Sol(
    idea=r"Compound interest is repeated multiplication, which gives an exponential, not a linear, expression.",
    steps=[
        (r"Each year the amount is multiplied by $1 + 0.05 = 1.05$.",
         r"Interest is added to the running balance, so next year's interest is larger."),
        (r"After $n$ years the original has been multiplied $n$ times: $2000 \times 1.05^n$.",
         r"Repeated multiplication gives a power."),
    ],
    pitfalls=[r"Choosing $2000 + 100n$ or $2000(1 + 0.05n)$ - those are **simple** interest.",
              r"Choosing $2000 \times 0.05^n$, which would shrink the investment to almost nothing."],
    takeaway=r"Compound: $P(1+r)^n$. Simple: $P(1 + rn)$. The word 'compound' means the multiplier repeats."),

"RAT-11": Sol(
    idea=r"A map scale applies to **lengths**. For areas the scale factor is squared - and the unit change must be handled too.",
    steps=[
        (r"Convert the length scale: $1$ cm on the map is $25\,000$ cm in reality $= 250$ m $= 0.25$ km.",
         r"$25\,000$ cm $= 250$ m (divide by $100$), then $= 0.25$ km (divide by $1000$)."),
        (r"Square it for areas: $1$ cm$^2$ represents $(0.25)^2 = 0.0625$ km$^2$.",
         r"Area scales with the square of the length factor."),
        (r"Multiply: $8 \times 0.0625 = 0.5$ km$^2$.",
         r"$8 \times \frac{1}{16} = \frac12$."),
    ],
    pitfalls=[r"Using the length factor directly: $8 \times 0.25 = 2$ km$^2$ - an offered option.",
              r"Mishandling the cm-to-km conversion by a factor of $10$, giving $0.05$ or $5$."],
    takeaway=r"Map areas use the **square** of the linear scale; convert units before squaring."),

"RAT-12": Sol(
    idea=r"A ratio before and after a change. Introduce a multiplier $k$ so both quantities are expressed with one unknown.",
    steps=[
        (r"Let the numbers be $3k$ boys and $4k$ girls.",
         r"The ratio $3:4$ fixes only the proportion, so a scale factor $k$ is needed."),
        (r"After the change: $3k - 2$ boys and $4k + 2$ girls, with ratio $2 : 3$.",
         r"Two boys leave, two girls join."),
        (r"Write the equation: $\dfrac{3k-2}{4k+2} = \dfrac23$, so $3(3k - 2) = 2(4k + 2)$.",
         r"Cross-multiply."),
        (r"Solve: $9k - 6 = 8k + 4 \Rightarrow k = 10$, so the total is $7k = 70$.",
         r"Check: $30$ boys and $40$ girls to start; after the change, $28 : 42 = 2 : 3$ ✓."),
    ],
    pitfalls=[r"Forgetting to answer the total and giving $k$ or one of the groups.",
              r"Writing the new ratio upside down."],
    takeaway=r"Introduce $k$ for a ratio, apply the change, cross-multiply, then convert back to the quantity asked for."),

"RAT-13": Sol(
    idea=r"Repeated decay compared with a threshold. Test successive powers - no logarithms needed.",
    steps=[
        (r"Each year multiplies the value by $0.8$.",
         r"A $20\%$ fall leaves $80\%$."),
        (r"After $n$ years the multiplier is $0.8^n$; we need the first $n$ with $0.8^n < 0.5$.",
         r"'Less than half' is a condition on the multiplier."),
        (r"Compute: $0.8^2 = 0.64$, $0.8^3 = 0.512$, $0.8^4 = 0.4096$.",
         r"Multiply successively rather than using logs - three multiplications is quick."),
        (r"$0.8^3 = 0.512 > 0.5$ but $0.8^4 < 0.5$, so the answer is $4$ complete years.",
         r"Note how close year $3$ is - checking it is essential."),
    ],
    pitfalls=[r"Stopping at $3$ because $0.512$ 'is about a half'.",
              r"Reasoning '$20\%$ per year, so half gone after $2.5$ years' - decay is multiplicative."],
    takeaway=r"Test successive powers against the threshold, and always check the year before your answer."),

"RAT-14": Sol(
    idea=r"A limiting-factor problem. Work out how many each ingredient allows, then take the smaller.",
    steps=[
        (r"Flour: $1$ kg $= 1000$ g, and $150$ g makes $12$ biscuits, so flour allows $\dfrac{1000}{150} \times 12 = 80$ biscuits.",
         r"Convert to the same units first."),
        (r"Butter: $500$ g at $100$ g per $12$ biscuits allows $\dfrac{500}{100} \times 12 = 60$ biscuits.",
         r"Same method for the second ingredient."),
        (r"Take the **smaller**: butter runs out first, so $60$ biscuits.",
         r"You can only make as many as the scarcest ingredient permits."),
    ],
    pitfalls=[r"Taking the larger number ($80$) - an offered option.",
              r"Averaging the two, or adding them."],
    takeaway=r"With several ingredients, the answer is the minimum over all of them - the limiting factor."),

"RAT-15": Sol(
    idea=r"Three percentage claims. Each is settled by converting to multipliers.",
    steps=[
        (r"I: $+50\%$ then $-50\%$ gives $1.5 \times 0.5 = 0.75$, i.e. $75\%$ of the original. **False.**",
         r"The decrease acts on the larger amount, so it removes more than the increase added."),
        (r"II: $+10\%$ twice gives $1.1^2 = 1.21$, a $21\%$ increase. **True.**",
         r"The extra $1\%$ is the interest on the first year's interest."),
        (r"III: $A = 1.25B$ means $B = \dfrac{A}{1.25} = 0.8A$, which is $20\%$ less than $A$. **True.**",
         r"Percentage changes are not symmetric because the base changes."),
        (r"II and III only.",
         r"Match to the options."),
    ],
    pitfalls=[r"Accepting I because the percentages 'cancel'.",
              r"Rejecting III on the grounds that $25\%$ up should mean $25\%$ down."],
    takeaway=r"Always convert to multipliers: percentage changes are asymmetric because the base changes."),

}
