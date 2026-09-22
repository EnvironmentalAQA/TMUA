"""Statistics (M6.1-M6.4) and probability (M7.1-M7.7)."""
from gen.model import Q, ROMAN3

S = "statistics"
P = "probability"

QUESTIONS = [
    # ---------------- statistics ----------------
    Q("STA-01", S, "M6.3", r"The mean of five numbers is $12$. When a sixth number is added the mean becomes $14$. What is the sixth number?",
      ["$24$", "$14$", "$20$", "$26$", "$16$", "$84$"], "A",
      r"Total goes from $60$ to $84$: the sixth number is $24$.", diff=1),

    Q("STA-02", S, "M6.3", r"A histogram has a bar for the class $10 \leq x < 15$ of height (frequency density) $3.2$ and a bar for $15 \leq x < 25$ of height $1.5$. What is the total frequency of these two classes?",
      ["$31$", "$4.7$", "$23.5$", "$16$", "$47$", "$15$"], "A",
      r"Frequency $=$ density $\times$ width: $3.2 \times 5 + 1.5 \times 10 = 16 + 15 = 31$.", diff=1),

    Q("STA-03", S, "M6.3", r"The numbers $3, 7, x, 12, 18$ (with $7 \leq x \leq 12$) have mean equal to median. Find $x$.",
      ["$8$", "$9$", "$10$", "$7$", "$11$", "$12$"], "C",
      r"The median is $x$ and the mean is $\frac{40 + x}{5}$. Setting them equal: $40 + x = 5x$, so $x = 10$.", diff=1),

    Q("STA-04", S, "M6.3", r"The table shows grouped data: $0 \leq t < 10$: frequency $4$; $10 \leq t < 20$: frequency $10$; $20 \leq t < 40$: frequency $6$. Estimate the mean.",
      ["$18$", "$16$", "$20$", "$15$", "$17.5$", "$22$"], "E",
      r"Use the midpoints $5, 15, 30$: $\dfrac{4\cdot5 + 10\cdot15 + 6\cdot30}{20} = \dfrac{20 + 150 + 180}{20} = \dfrac{350}{20} = 17.5$.", diff=1),

    Q("STA-05", S, "M6.4", r"""Which of the following statements about a scatter graph showing strong positive correlation between hours of revision and exam mark is/are valid?

I. Students who revised more tended to score higher.
II. Revising more causes a higher mark.
III. A line of best fit could be used to estimate the mark of a student who revised for a number of hours within the range of the data.""", ROMAN3, "F",
      r"Correlation describes a tendency (I) and supports interpolation within the data range (III), but does not by itself establish causation (II).", paper=2, tags=("roman",), diff=1),

    Q("STA-06", S, "M6.3", r"A set of $n$ numbers has mean $m$. Each number is doubled and then $3$ is added. Which of the following is the new mean, and which the new range (if the original range was $R$)?",
      [r"mean $2m + 3$, range $2R$", r"mean $2m + 3$, range $2R + 3$", r"mean $2m$, range $2R$", r"mean $m + 3$, range $R$", r"mean $2m + 3$, range $R$"], "A",
      r"Mean transforms with the data: $2m + 3$. The range is unaffected by adding a constant but doubles with the scaling: $2R$.", diff=1),

    Q("STA-07", S, "M6.3", r"The median of $7$ distinct integers is $10$ and the mean is $12$. The smallest number is increased by $20$. Which of the following must be true?",
      [r"The mean increases and the median does not change.", r"The mean and median both increase.", r"The median increases and the mean does not change.", r"Neither the mean nor the median changes.", r"The mean increases and the median may or may not change."], "E",
      r"The mean rises by $\frac{20}{7}$. The smallest number plus $20$ could exceed the median (e.g. if the smallest is $1$ and it becomes $21$ the middle value changes), or it could stay below it. So the median may or may not change.", diff=2),

    Q("STA-08", S, "M6.3", r"A cumulative frequency graph for $80$ observations passes through $(20, 20)$, $(30, 40)$ and $(45, 60)$. Estimate the interquartile range.",
      ["$25$", "$40$", "$10$", "$15$", "$20$", "$30$"], "A",
      r"Lower quartile at cumulative frequency $20$: value $20$. Upper quartile at $60$: value $45$. IQR $= 25$.", diff=1),

    Q("STA-09", S, "M6.3", r"Class A has $20$ students with mean mark $60$; class B has $30$ students with mean mark $70$. What is the mean mark of all $50$ students?",
      ["$66$", "$65$", "$64$", "$67$", "$68$", "$62$"], "A",
      r"$\frac{1200 + 2100}{50} = \frac{3300}{50} = 66$.", diff=1),

    Q("STA-10", S, "M6.3", r"For which of the following data sets is the mean greater than the median?",
      [r"$1, 2, 3, 4, 20$", r"$1, 2, 3, 4, 5$", r"$1, 10, 11, 12, 13$", r"$5, 5, 5, 5, 5$", r"$2, 4, 6, 8, 10$"], "A",
      r"A large outlier pulls the mean above the median: mean $6 > $ median $3$. In B, D, E the mean equals the median; in C the mean $9.4 <$ median $11$.", diff=1),

    # ---------------- probability ----------------
    Q("PRO-01", P, "M7.7", r"A bag contains $4$ red and $6$ blue counters. Two counters are taken at random without replacement. Find the probability that they are different colours.",
      [r"$\dfrac{8}{15}$", r"$\dfrac{4}{15}$", r"$\dfrac{12}{25}$", r"$\dfrac{7}{15}$", r"$\dfrac{2}{5}$", r"$\dfrac{24}{100}$"], "A",
      r"$P(RB) + P(BR) = \frac{4}{10}\cdot\frac{6}{9} + \frac{6}{10}\cdot\frac{4}{9} = \frac{48}{90} = \frac{8}{15}$.", diff=1),

    Q("PRO-02", P, "M7.6", r"Two fair dice are thrown. Find the probability that the product of the two scores is odd.",
      [r"$\dfrac{1}{4}$", r"$\dfrac{1}{2}$", r"$\dfrac{3}{4}$", r"$\dfrac{1}{3}$", r"$\dfrac{1}{6}$", r"$\dfrac{2}{3}$"], "A",
      r"The product is odd only if both scores are odd: $\frac12 \times \frac12 = \frac14$.", diff=1),

    Q("PRO-03", P, "M7.7", r"""$P(A) = 0.6$, $P(B) = 0.5$ and $P(A \text{ and } B) = 0.3$. Which of the following statements is/are true?

I. $A$ and $B$ are independent.
II. $A$ and $B$ are mutually exclusive.
III. $P(A \text{ or } B) = 0.8$""", ROMAN3, "F",
      r"$P(A)P(B) = 0.3 = P(A \text{ and } B)$, so independent (I). Not mutually exclusive since they can both happen (II false). $P(A \text{ or } B) = 0.6 + 0.5 - 0.3 = 0.8$ (III).", paper=2, tags=("roman",), diff=1),

    Q("PRO-04", P, "M7.7", r"A biased coin has probability $p$ of landing heads. It is tossed twice. The probability of exactly one head is $\dfrac{3}{8}$. Find the possible values of $p$.",
      [r"$\dfrac{1}{4}$ or $\dfrac{3}{4}$", r"$\dfrac{3}{8}$ only", r"$\dfrac{1}{2}$ only", r"$\dfrac{1}{3}$ or $\dfrac{2}{3}$", r"$\dfrac{3}{16}$ only", r"$\dfrac{1}{8}$ or $\dfrac{7}{8}$"], "A",
      r"$2p(1 - p) = \frac38 \Rightarrow 16p^2 - 16p + 3 = 0 \Rightarrow (4p - 1)(4p - 3) = 0$.", diff=2),

    Q("PRO-05", P, "M7.2", r"A spinner has probability $0.15$ of landing on red. It is spun $200$ times. What is the expected number of times it lands on red?",
      ["$30$", "$15$", "$25$", "$20$", "$35$", "$40$"], "A",
      r"$0.15 \times 200 = 30$.", diff=1),

    Q("PRO-06", P, "M7.7", r"In a class of $30$, $18$ study French, $12$ study German and $5$ study both. A student is chosen at random. Given that the student studies French, what is the probability that they also study German?",
      [r"$\dfrac{5}{18}$", r"$\dfrac{5}{12}$", r"$\dfrac{1}{6}$", r"$\dfrac{5}{30}$", r"$\dfrac{13}{18}$", r"$\dfrac{5}{25}$"], "A",
      r"Conditional on French ($18$ students), $5$ also study German: $\frac{5}{18}$.", diff=1),

    Q("PRO-07", P, "M7.6", r"Three fair coins are tossed. Find the probability of getting more heads than tails.",
      [r"$\dfrac{1}{2}$", r"$\dfrac{3}{8}$", r"$\dfrac{1}{4}$", r"$\dfrac{5}{8}$", r"$\dfrac{1}{8}$", r"$\dfrac{3}{4}$"], "A",
      r"Need $2$ or $3$ heads: $\frac{3 + 1}{8} = \frac12$ (by symmetry between heads and tails).", diff=1),

    Q("PRO-08", P, "M7.7", r"A box contains $n$ white balls and $3$ black balls. Two balls are drawn without replacement. The probability that both are white is $\dfrac{5}{12}$. Find $n$.",
      ["$6$", "$5$", "$4$", "$7$", "$9$", "$3$"], "A",
      r"$\dfrac{n}{n+3}\cdot\dfrac{n-1}{n+2} = \dfrac{5}{12} \Rightarrow 12n^2 - 12n = 5n^2 + 25n + 30 \Rightarrow 7n^2 - 37n - 30 = 0 \Rightarrow (7n + 5)(n - 6) = 0$, so $n = 6$.", diff=2),

    Q("PRO-09", P, "M7.4", r"The probabilities that a train is early, on time or late are $0.1$, $x$ and $2x$ respectively. Find the probability that the train is not late.",
      ["$0.4$", "$0.6$", "$0.3$", "$0.7$", "$0.9$", "$0.5$"], "A",
      r"$0.1 + 3x = 1 \Rightarrow x = 0.3$; not late $= 0.1 + 0.3 = 0.4$.", diff=1),

    Q("PRO-10", P, "M7.7", r"A fair die is thrown repeatedly until a six appears. Find the probability that the first six appears on the third throw.",
      [r"$\dfrac{25}{216}$", r"$\dfrac{1}{216}$", r"$\dfrac{1}{6}$", r"$\dfrac{5}{36}$", r"$\dfrac{91}{216}$", r"$\dfrac{125}{216}$"], "A",
      r"$\left(\frac56\right)^2 \cdot \frac16 = \frac{25}{216}$.", diff=1),

    Q("PRO-11", P, "M7.6", r"Two cards are drawn at random from a standard pack of $52$ without replacement. Which of the following expressions is the probability that both are aces?",
      [r"$\dfrac{4}{52} \times \dfrac{3}{51}$", r"$\dfrac{4}{52} \times \dfrac{4}{52}$", r"$\dfrac{4}{52} \times \dfrac{3}{52}$", r"$\dfrac{4}{52} + \dfrac{3}{51}$", r"$\dfrac{1}{13} \times \dfrac{1}{13}$", r"$\dfrac{2}{52}$"], "A",
      r"Without replacement the second draw has $3$ aces among $51$ cards.", diff=1),

    Q("PRO-12", P, "M7.7", r"Events $A$ and $B$ are mutually exclusive with $P(A) = 0.3$ and $P(B) = 0.4$. Find $P(\text{neither } A \text{ nor } B)$.",
      ["$0.3$", "$0.7$", "$0.42$", "$0.12$", "$0.58$", "$0.1$"], "A",
      r"$P(A \text{ or } B) = 0.7$, so neither $= 0.3$.", diff=1),
]
