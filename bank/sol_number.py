"""Full teaching solutions: number, units and estimation (NUM-xx)."""
from gen.model import Sol

SOLUTIONS = {

"NUM-01": Sol(
    idea=r"HCF from prime factorisations: take each **common** prime to its **lower** power.",
    steps=[
        (r"List the primes in each: $2^3 \times 3^2 \times 5$ and $2^2 \times 3^3 \times 7$.",
         r"Both are already factorised, which is the form the rule needs."),
        (r"Take the common primes only: $2$ and $3$ appear in both; $5$ and $7$ do not.",
         r"A prime missing from one number cannot divide both."),
        (r"Take the lower power of each: $2^{\min(3,2)} = 2^2$ and $3^{\min(2,3)} = 3^2$.",
         r"The HCF must divide both, so it cannot use more copies of a prime than the smaller number has."),
        (r"Multiply: $4 \times 9 = 36$.",
         r"Check: $36$ divides $360$ and $756$ ✓."),
    ],
    pitfalls=[r"Taking the higher powers (that gives the LCM contribution, not the HCF).",
              r"Including $5$ or $7$, which gives a number dividing only one of them."],
    takeaway=r"HCF: common primes, lowest powers. LCM: all primes, highest powers."),

"NUM-02": Sol(
    idea=r"An LCM condition. Work out what the other two numbers already supply, then see what $n$ must add - and must not exceed.",
    steps=[
        (r"Factorise: $12 = 2^2 \times 3$, $18 = 2 \times 3^2$, so $\text{lcm}(12,18) = 2^2 \times 3^2 = 36$.",
         r"LCM takes the highest power of each prime."),
        (r"The target is $180 = 2^2 \times 3^2 \times 5$, so $n$ must supply the factor $5$.",
         r"$36$ has no factor $5$, so $n$ is the only possible source."),
        (r"$n$ must also **divide** $180$: it cannot contain $2^3$, $3^3$ or $5^2$, or the LCM would be larger than $180$.",
         r"The LCM is at least $n$, so $n$ must divide the target exactly."),
        (r"Check the options: $20 = 2^2 \times 5$ divides $180$ and supplies the $5$ ✓. The others either lack a factor $5$ ($24$, $8$, $27$) or do not divide $180$ ($50 = 2\times5^2$, $40 = 2^3\times5$).",
         r"Test both conditions on each candidate."),
    ],
    pitfalls=[r"Choosing $50$ or $40$ because they contain a $5$, forgetting they must divide $180$.",
              r"Assuming $n$ must equal $180 \div 36 = 5$."],
    takeaway=r"For $\text{lcm}(a,b,n) = L$: $n$ must divide $L$ and supply any prime powers $a$ and $b$ lack."),

"NUM-03": Sol(
    idea=r"The standard algebraic trick for recurring decimals: multiply by a power of $10$ that shifts one full period, then subtract.",
    steps=[
        (r"Let $x = 0.272727\ldots$ The repeating block has **two** digits, so multiply by $10^2 = 100$: $100x = 27.272727\ldots$",
         r"Shifting by exactly one period makes the decimal tails identical, so they cancel."),
        (r"Subtract: $100x - x = 27.2727\ldots - 0.2727\ldots = 27$, so $99x = 27$.",
         r"The infinite tails cancel exactly - this is the whole method."),
        (r"Solve: $x = \dfrac{27}{99}$.",
         r"The denominator is always $10^k - 1$, i.e. a string of nines matching the period length."),
        (r"Simplify by $9$: $\dfrac{3}{11}$.",
         r"The question demands lowest terms, and $\frac{27}{99}$ is offered as a trap."),
    ],
    pitfalls=[r"Choosing $\frac{27}{99}$ - correct in value but not in lowest terms.",
              r"Multiplying by $10$ instead of $100$, which does not align the tails."],
    takeaway=r"Multiply by $10^{(\text{period length})}$, subtract, then simplify fully."),

"NUM-04": Sol(
    idea=r"Bounds: each measurement is an interval. For a maximum product, take the top of each interval.",
    steps=[
        (r"Length $4.6$ to 1 d.p. means $4.55 \leq \ell < 4.65$, so the upper bound is $4.65$.",
         r"Rounding to 1 d.p. means the true value is within $0.05$ either side."),
        (r"Width $3$ to the nearest cm means $2.5 \leq w < 3.5$, so the upper bound is $3.5$.",
         r"Nearest whole number means within $0.5$ either side - a different half-width from the length."),
        (r"Both factors are positive, so the area is largest when both are largest: $4.65 \times 3.5$.",
         r"Products of positive numbers increase with each factor."),
        (r"Compute: $4.65 \times 3.5 = 16.275$ cm$^2$.",
         r"$4.65 \times 3 = 13.95$, plus $4.65 \times 0.5 = 2.325$."),
    ],
    pitfalls=[r"Using $4.65 \times 3.0 = 13.95$ by forgetting the width also has a bound.",
              r"Using half-widths of $0.05$ for both, giving $3.05$ for the width."],
    takeaway=r"Each measurement has its own accuracy: 1 d.p. gives $\pm0.05$, nearest whole gives $\pm0.5$."),

"NUM-05": Sol(
    idea=r"Standard-form arithmetic: handle the numbers and the powers of ten separately, then renormalise.",
    steps=[
        (r"Multiply the numerator: $(3 \times 8) \times 10^{4 + (-2)} = 24 \times 10^{2}$.",
         r"Multiply the leading numbers, add the indices."),
        (r"Divide by $6 \times 10^{-3}$: $\dfrac{24}{6} \times 10^{2 - (-3)} = 4 \times 10^{5}$.",
         r"Divide the numbers, subtract the indices - and subtracting $-3$ adds $3$."),
        (r"Check the form: $1 \leq 4 < 10$ ✓, so no renormalising is needed.",
         r"Standard form requires the leading number to be between $1$ and $10$."),
    ],
    pitfalls=[r"Getting $10^{-1}$ by adding instead of subtracting the $-3$.",
              r"Leaving $24 \times 10^{2}$, which is not in standard form."],
    takeaway=r"Numbers multiply/divide; indices add/subtract. Then check $1 \leq a < 10$."),

"NUM-06": Sol(
    idea=r"The product rule for counting, with one part allowing repeats and the other not.",
    steps=[
        (r"Letters: $5$ choices for the first and, since repeats are allowed, $5$ again for the second: $5 \times 5$.",
         r"'May be repeated' means the second choice is unaffected by the first."),
        (r"Digits: $9$ choices for the first, but only $8$ for the second because they must differ: $9 \times 8$.",
         r"'Must be different' removes exactly one option from the second slot."),
        (r"Multiply all the stages: $5 \times 5 \times 9 \times 8 = 1800$.",
         r"The product rule: independent stages multiply."),
    ],
    pitfalls=[r"Using $9 \times 9 = 81$ for the digits, giving $2025$ - an offered option.",
              r"Using $5 \times 4$ for the letters, giving $1440$."],
    takeaway=r"Multiply the number of choices at each stage, reducing by one only where repetition is forbidden."),

"NUM-07": Sol(
    idea=r"A compound-unit conversion: convert distance and time separately.",
    steps=[
        (r"$90$ km $= 90 \times 1000 = 90\,000$ m.",
         r"Convert the distance unit first."),
        (r"$1$ hour $= 60 \times 60 = 3600$ s.",
         r"Convert the time unit."),
        (r"Divide: $\dfrac{90\,000}{3600} = 25$ m/s.",
         r"Equivalently, divide km/h by $3.6$ - worth memorising."),
    ],
    pitfalls=[r"Multiplying by $3.6$ instead of dividing, giving $324$ - an offered option.",
              r"Converting only one of the two units."],
    takeaway=r"km/h $\div 3.6 = $ m/s; convert numerator and denominator units separately."),

"NUM-08": Sol(
    idea=r"Estimation by rounding to one significant figure, choosing roundings that make the arithmetic exact.",
    steps=[
        (r"Round each: $4.92 \approx 5$, $99.3 \approx 100$, $0.198 \approx 0.2$.",
         r"One significant figure; $99.3$ rounds to $100$, which is also a perfect square - convenient."),
        (r"Take the root: $\sqrt{100} = 10$.",
         r"Choosing $100$ rather than $99$ is what makes the root exact."),
        (r"Compute: $\dfrac{5 \times 10}{0.2} = \dfrac{50}{0.2} = 250$.",
         r"Dividing by $0.2$ is multiplying by $5$."),
    ],
    pitfalls=[r"Dividing by $0.2$ as if it were $2$, giving $25$.",
              r"Forgetting the square root and using $100$ directly, giving $2500$."],
    takeaway=r"Round to 1 s.f., but choose the rounding that makes roots and divisions exact; dividing by $0.2$ multiplies by $5$."),

"NUM-09": Sol(
    idea=r"Counting divisors from the prime factorisation: each prime's exponent can be chosen independently.",
    steps=[
        (r"Factorise: $360 = 8 \times 45 = 2^3 \times 3^2 \times 5$.",
         r"Split into convenient factors and factorise each."),
        (r"A divisor has the form $2^a 3^b 5^c$ with $0 \leq a \leq 3$, $0 \leq b \leq 2$, $0 \leq c \leq 1$.",
         r"Any such combination divides $360$, and every divisor has this form uniquely."),
        (r"Count the choices: $4 \times 3 \times 2 = 24$.",
         r"Each exponent has (power $+ 1$) possible values, because $0$ is allowed."),
    ],
    pitfalls=[r"Multiplying the exponents ($3 \times 2 \times 1 = 6$) instead of (exponent $+1$).",
              r"Forgetting that $1$ and $360$ are themselves divisors - the '$+1$'s account for them."],
    takeaway=r"Number of divisors of $p^aq^br^c$ is $(a+1)(b+1)(c+1)$."),

"NUM-10": Sol(
    idea=r"Truncation, not rounding. Truncating throws away everything after the cut, so the value can only be **above** the stated one.",
    steps=[
        (r"Truncating to $2$ d.p. means simply deleting the third and later decimals.",
         r"No rounding up ever happens, which makes the interval one-sided."),
        (r"The smallest such $x$ is $3.14$ itself (with nothing after it).",
         r"$3.14$ truncates to $3.14$, so equality is allowed at the bottom."),
        (r"The largest is anything below $3.15$: at $3.15$ the truncation would read $3.15$.",
         r"Strict inequality at the top."),
        (r"So $3.14 \leq x < 3.15$.",
         r"Contrast with rounding, which would give $3.135 \leq x < 3.145$ - an offered distractor."),
    ],
    pitfalls=[r"Using the rounding interval $3.135 \leq x < 3.145$.",
              r"Making the lower end strict, excluding $3.14$ itself."],
    takeaway=r"Truncation: $[a, a + 10^{-n})$. Rounding: $[a - \frac12 10^{-n}, a + \frac12 10^{-n})$."),

"NUM-11": Sol(
    idea=r"Mixed numbers and division of fractions. Convert to improper fractions, subtract, then multiply by the reciprocal.",
    steps=[
        (r"Convert: $2\frac13 = \frac73$ and $1\frac34 = \frac74$.",
         r"Whole part times denominator plus numerator."),
        (r"Subtract with a common denominator $12$: $\dfrac{28}{12} - \dfrac{21}{12} = \dfrac{7}{12}$.",
         r"$\frac73 = \frac{28}{12}$ and $\frac74 = \frac{21}{12}$."),
        (r"Divide by $\frac76$ means multiply by $\frac67$: $\dfrac{7}{12} \times \dfrac{6}{7}$.",
         r"Dividing by a fraction is multiplying by its reciprocal."),
        (r"Cancel and multiply: the $7$s cancel and $\frac{6}{12} = \frac12$.",
         r"Cancel before multiplying to keep numbers small."),
    ],
    pitfalls=[r"Multiplying by $\frac76$ instead of its reciprocal, giving $\frac{49}{72}$ - an offered option.",
              r"Subtracting the whole parts and fractions separately and mishandling the borrow."],
    takeaway=r"Improper fractions, common denominator, then multiply by the reciprocal - and cancel before multiplying."),

"NUM-12": Sol(
    idea=r"A prime-triple question. One observation about remainders on division by $3$ settles all three statements.",
    steps=[
        (r"III: among $n$, $n+2$, $n+4$, the remainders on division by $3$ are all different (they differ by $2$ and $4$, i.e. by $2$ and $1$ modulo $3$), so one of them is a multiple of $3$. **True.**",
         r"Three numbers hitting all three remainder classes must include one divisible by $3$."),
        (r"I: that multiple of $3$ can only be prime if it **equals** $3$. Checking the possibilities gives $n = 3$ ($3,5,7$ are all prime); $n = 1$ fails ($1$ is not prime) and larger cases contain a composite multiple of $3$. **True.**",
         r"So the triple is unique - this is why $3,5,7$ is famous as the only 'prime triplet' of this form."),
        (r"II: $n = 3$ is odd. (Also, any even $n > 2$ would not be prime.) **True.**",
         r"Both routes give the same verdict."),
        (r"All three.",
         r"Match to the option list."),
    ],
    pitfalls=[r"Testing a few values, finding only $3,5,7$, and still doubting uniqueness - the mod-3 argument proves it.",
              r"Thinking $n$ could be $2$: then $4$ is not prime."],
    takeaway=r"Any three numbers spaced $2$ apart cover all remainders mod $3$, so one is divisible by $3$."),

"NUM-13": Sol(
    idea=r"Everything is a power of $2$. Convert and use the index laws.",
    steps=[
        (r"Convert: $8 = 2^3$ so $8^4 = 2^{12}$; $4 = 2^2$ so $4^3 = 2^6$.",
         r"A common base turns the whole expression into index arithmetic."),
        (r"Numerator: $2^{12} \times 2^{-5} = 2^{7}$.",
         r"Multiplying adds indices."),
        (r"Divide: $2^{7-6} = 2^1 = 2$.",
         r"Dividing subtracts indices."),
    ],
    pitfalls=[r"Using $8^4 = 2^{7}$ (adding instead of multiplying the indices).",
              r"Sign slip on the $-5$, giving $2^{11-6} = 32$."],
    takeaway=r"Rewrite every number as a power of the same base, then just add and subtract indices."),

"NUM-14": Sol(
    idea=r"Simplify each surd first; they all reduce to multiples of $\sqrt3$, so the expression collapses.",
    steps=[
        (r"Simplify: $\sqrt{48} = \sqrt{16 \times 3} = 4\sqrt3$, $\sqrt{27} = 3\sqrt3$, $\sqrt{12} = 2\sqrt3$.",
         r"Take out the largest square factor each time."),
        (r"Multiply the first two: $4\sqrt3 \times 3\sqrt3 = 12 \times 3 = 36$.",
         r"$\sqrt3 \times \sqrt3 = 3$ - the surd disappears."),
        (r"Divide: $\dfrac{36}{2\sqrt3} = \dfrac{18}{\sqrt3}$.",
         r"Only one surd remains, in the denominator."),
        (r"Rationalise: $\dfrac{18}{\sqrt3} \times \dfrac{\sqrt3}{\sqrt3} = \dfrac{18\sqrt3}{3} = 6\sqrt3$.",
         r"Multiply top and bottom by $\sqrt3$."),
    ],
    pitfalls=[r"Answering $18$ by forgetting to rationalise (or by cancelling the $\sqrt3$ incorrectly).",
              r"Combining under one root: $\sqrt{48 \times 27 \div 12} = \sqrt{108}$ - correct but then needing simplification to $6\sqrt3$ anyway."],
    takeaway=r"Simplify each surd, do the arithmetic, then rationalise any surd left in a denominator."),

"NUM-15": Sol(
    idea=r"Counting with two restrictions: digits from a fixed set, and all different.",
    steps=[
        (r"List the allowed digits: $1, 3, 5, 7, 9$ - five odd digits.",
         r"'All odd' restricts the pool; note $0$ is even so no leading-zero problem arises."),
        (r"First digit: $5$ choices. Second: $4$ (one used). Third: $3$.",
         r"'All different' removes one option at each stage."),
        (r"Multiply: $5 \times 4 \times 3 = 60$.",
         r"The product rule."),
    ],
    pitfalls=[r"Using $5^3 = 125$ by ignoring 'all different' - an offered option.",
              r"Worrying about leading zeros, which cannot occur here."],
    takeaway=r"Count position by position, reducing the pool by one each time when repetition is banned."),

"NUM-16": Sol(
    idea=r"A rate problem with a unit conversion. Convert the volume to litres, divide by the rate, then convert the time.",
    steps=[
        (r"Convert the volume: $3.6$ m$^3 = 3.6 \times 1000 = 3600$ litres.",
         r"The conversion is given in the question."),
        (r"Divide by the rate: $\dfrac{3600}{1.2} = 3000$ seconds.",
         r"Volume divided by volume-per-second gives seconds."),
        (r"Convert to minutes: $\dfrac{3000}{60} = 50$ minutes.",
         r"The options are in minutes, so finish the conversion."),
    ],
    pitfalls=[r"Leaving the answer as $3000$ seconds and picking $500$ seconds by a slip.",
              r"Dividing by $1.2$ as if it were $12$, giving $5$ minutes."],
    takeaway=r"Make the units match before dividing, and convert the answer into the units the options use."),

"NUM-17": Sol(
    idea=r"Bounds for a quotient: smallest over largest gives the smallest result.",
    steps=[
        (r"$a = 5.0$ to 2 s.f. means $4.95 \leq a < 5.05$.",
         r"The last significant figure is in the first decimal place, so the half-width is $0.05$."),
        (r"$b = 2.0$ to 2 s.f. means $1.95 \leq b < 2.05$.",
         r"Same reasoning."),
        (r"For the **smallest** quotient, make the numerator as small as possible and the denominator as large as possible.",
         r"Increasing the denominator decreases a positive fraction - this is the key insight."),
        (r"So the lower bound is $\dfrac{4.95}{2.05}$.",
         r"Left in fraction form, which is what the options offer."),
    ],
    pitfalls=[r"Pairing both lower bounds as $\frac{4.95}{1.95}$: a smaller denominator makes the fraction **bigger**, so that is not the lower bound.",
              r"Using $\pm 0.5$ instead of $\pm 0.05$ - for these numbers, 2 significant figures means one decimal place."],
    takeaway=r"Quotients: lower bound $= \frac{\text{lower}}{\text{upper}}$, upper bound $= \frac{\text{upper}}{\text{lower}}$."),

"NUM-18": Sol(
    idea=r"The smallest number divisible by all of $1$ to $10$ is their LCM: take the highest power of each prime up to $10$.",
    steps=[
        (r"List the primes up to $10$: $2, 3, 5, 7$.",
         r"Only primes matter; composite numbers are built from them."),
        (r"Take the highest power of each that is at most $10$: $2^3 = 8$, $3^2 = 9$, $5$, $7$.",
         r"$8$ needs three $2$s and $9$ needs two $3$s - the largest demands from any single number."),
        (r"Multiply: $8 \times 9 \times 5 \times 7 = 2520$.",
         r"$72 \times 35 = 2520$."),
        (r"Check: $2520$ is divisible by $4$, $6$, $10$ automatically, since those are built from the primes included.",
         r"Covering the highest prime powers covers every composite too."),
    ],
    pitfalls=[r"Multiplying all the numbers $1$ to $10$ ($3628800$) - divisible, but far from smallest.",
              r"Using $2^2$ instead of $2^3$, giving $1260$, which is not divisible by $8$."],
    takeaway=r"LCM of a range: each prime to the highest power that appears within the range."),

"NUM-19": Sol(
    idea=r"A fraction terminates exactly when its lowest-terms denominator is built only from $2$s and $5$s.",
    steps=[
        (r"Check each denominator is in lowest terms with the numerator.",
         r"A shared factor could change the denominator - here none do."),
        (r"Factorise: $40 = 2^3 \times 5$ ✓; $12 = 2^2\times3$ ✗; $15 = 3\times5$ ✗; $14 = 2\times7$ ✗; $9 = 3^2$ ✗; $22 = 2\times11$ ✗.",
         r"Any prime other than $2$ or $5$ forces a recurring expansion."),
        (r"So only $\dfrac{7}{40}$ terminates (it is $0.175$).",
         r"Because $10 = 2\times5$, only these primes can divide a power of ten."),
    ],
    pitfalls=[r"Assuming a 'nice-looking' denominator like $12$ terminates.",
              r"Forgetting to reduce a fraction first in questions where the numerator shares a factor."],
    takeaway=r"Terminating $\Leftrightarrow$ denominator (in lowest terms) is $2^a 5^b$."),

"NUM-20": Sol(
    idea=r"A sum of conjugate squares. The surd terms cancel, so the answer is rational.",
    steps=[
        (r"Expand the first: $(\sqrt5 - 1)^2 = 5 - 2\sqrt5 + 1 = 6 - 2\sqrt5$.",
         r"$(a-b)^2 = a^2 - 2ab + b^2$ with $(\sqrt5)^2 = 5$."),
        (r"Expand the second: $(\sqrt5 + 1)^2 = 6 + 2\sqrt5$.",
         r"Only the middle sign differs."),
        (r"Add: the $\mp2\sqrt5$ terms cancel, leaving $12$.",
         r"Conjugates always cancel their surd parts when added."),
    ],
    pitfalls=[r"Dropping the cross terms: here it happens to give $12$ anyway, but the same slip fails whenever the two brackets are not conjugates.",
              r"Adding the surd terms instead of cancelling, giving $12 + 4\sqrt5$ - an offered option."],
    takeaway=r"$(a+b)^2 + (a-b)^2 = 2(a^2+b^2)$: here $2(5 + 1) = 12$, with no surds surviving."),

}
