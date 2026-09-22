"""Ratio, proportion and percentages (M3.1-M3.11)."""
from gen.model import Q, ROMAN3

T = "ratio-proportion"

QUESTIONS = [
    Q("RAT-01", T, "M3.8", r"The price of a coat is reduced by $20\%$ in a sale, and then the sale price is reduced by a further $25\%$. The final price is what percentage of the original price?",
      [r"$60\%$", r"$55\%$", r"$45\%$", r"$65\%$", r"$50\%$", r"$40\%$"], "A",
      r"$0.8 \times 0.75 = 0.6$, so $60\%$.", diff=1),

    Q("RAT-02", T, "M3.8", r"After a $15\%$ increase, a salary is $\pounds 27\,600$. What was the original salary?",
      [r"$\pounds 24\,000$", r"$\pounds 23\,460$", r"$\pounds 24\,500$", r"$\pounds 23\,000$", r"$\pounds 25\,000$", r"$\pounds 31\,740$"], "A",
      r"$1.15 \times S = 27600 \Rightarrow S = 24000$.", diff=1),

    Q("RAT-03", T, "M3.4", r"$\pounds 600$ is divided between $A$, $B$ and $C$ in the ratio $2 : 3 : 7$. How much more does $C$ receive than $A$?",
      [r"$\pounds 250$", r"$\pounds 350$", r"$\pounds 100$", r"$\pounds 200$", r"$\pounds 300$", r"$\pounds 150$"], "A",
      r"Each part is $\pounds 50$; $C - A = 5$ parts $= \pounds 250$.", diff=1),

    Q("RAT-04", T, "M3.9", r"$y$ is inversely proportional to the square of $x$. When $x = 2$, $y = 9$. Find $y$ when $x = 6$.",
      ["$1$", "$3$", "$27$", "$81$", r"$\dfrac{1}{3}$", "$4$"], "A",
      r"$y = \frac{k}{x^2}$, $k = 36$. $y = \frac{36}{36} = 1$.", diff=1),

    Q("RAT-05", T, "M3.11", r"A bacteria population doubles every $3$ hours. By what factor does it grow in $24$ hours?",
      ["$256$", "$16$", "$8$", "$48$", "$128$", "$64$"], "A",
      r"$24/3 = 8$ doublings: $2^8 = 256$.", diff=1),

    Q("RAT-06", T, "M3.10", r"Two similar solids have surface areas in the ratio $4 : 9$. Find the ratio of their volumes.",
      [r"$8 : 27$", r"$4 : 9$", r"$16 : 81$", r"$2 : 3$", r"$64 : 729$", r"$12 : 27$"], "A",
      r"Length ratio $2 : 3$, so volume ratio $2^3 : 3^3 = 8 : 27$.", diff=1),

    Q("RAT-07", T, "M3.5", r"A mixture contains sand and cement in the ratio $5 : 2$. How much cement must be added to $35$ kg of the mixture to make the ratio $5 : 3$?",
      ["$5$ kg", "$10$ kg", "$3$ kg", "$15$ kg", "$7$ kg", "$2.5$ kg"], "A",
      r"$35$ kg contains $25$ kg sand and $10$ kg cement. For $5 : 3$ with $25$ kg sand, cement must be $15$ kg: add $5$ kg.", diff=1),

    Q("RAT-08", T, "M3.8", r"A quantity increases by $x\%$ and then decreases by $x\%$. The overall change is a decrease of $4\%$. Find $x$.",
      ["$20$", "$4$", "$2$", "$10$", "$40$", "$25$"], "A",
      r"$(1 + \frac{x}{100})(1 - \frac{x}{100}) = 1 - \frac{x^2}{10000} = 0.96 \Rightarrow x^2 = 400 \Rightarrow x = 20$.", diff=2),

    Q("RAT-09", T, "M3.9", r"$p$ is directly proportional to $\sqrt{q}$, and $q$ is inversely proportional to $r$. Which of the following is true?",
      [r"$p$ is inversely proportional to $\sqrt{r}$", r"$p$ is inversely proportional to $r$", r"$p$ is directly proportional to $\sqrt{r}$", r"$p$ is inversely proportional to $r^2$", r"$p$ is directly proportional to $r$"], "A",
      r"$p = a\sqrt q$ and $q = \frac{b}{r}$, so $p = a\sqrt{\frac br} = \frac{a\sqrt b}{\sqrt r}$.", diff=2),

    Q("RAT-10", T, "M3.11", r"$\pounds 2000$ is invested at $5\%$ compound interest per year. Which expression gives the amount after $n$ years?",
      [r"$2000 \times 1.05^{n}$", r"$2000 + 100n$", r"$2000 \times 0.05^{n}$", r"$2000 \times 1.5^{n}$", r"$2000(1 + 0.05n)$", r"$2000 \times 5^{n}$"], "A",
      r"Compound growth multiplies by $1.05$ each year.", diff=1),

    Q("RAT-11", T, "M3.1", r"On a map with scale $1 : 25\,000$, a lake has area $8$ cm$^2$. What is the actual area of the lake in km$^2$?",
      [r"$0.5$ km$^2$", r"$2$ km$^2$", r"$5$ km$^2$", r"$0.2$ km$^2$", r"$50$ km$^2$", r"$0.05$ km$^2$"], "A",
      r"$1$ cm represents $25\,000$ cm $= 0.25$ km, so $1$ cm$^2$ represents $0.0625$ km$^2$. $8 \times 0.0625 = 0.5$ km$^2$.", diff=2),

    Q("RAT-12", T, "M3.6", r"In a year group the ratio of boys to girls is $3 : 4$. Two boys leave and two girls join, and the ratio becomes $2 : 3$. How many students are in the year group?",
      ["$70$", "$35$", "$42$", "$56$", "$63$", "$84$"], "A",
      r"With $3k$ boys and $4k$ girls: $\dfrac{3k - 2}{4k + 2} = \dfrac23 \Rightarrow 9k - 6 = 8k + 4 \Rightarrow k = 10$. Total $7k = 70$.", diff=2),

    Q("RAT-13", T, "M3.8", r"The value of a car falls by $20\%$ each year. After how many complete years is it first worth less than half its original value?",
      ["$4$", "$3$", "$2$", "$5$", "$6$", "$10$"], "A",
      r"$0.8^3 = 0.512 > 0.5$, $0.8^4 = 0.4096 < 0.5$. So $4$ years.", diff=1),

    Q("RAT-14", T, "M3.5", r"A recipe for $12$ biscuits uses $150$ g of flour and $100$ g of butter. Ann has $1$ kg of flour and $500$ g of butter. What is the greatest number of biscuits she can make?",
      ["$60$", "$80$", "$72$", "$48$", "$66$", "$50$"], "A",
      r"Flour allows $\frac{1000}{150} \times 12 = 80$; butter allows $\frac{500}{100} \times 12 = 60$. Butter is the limit: $60$.", diff=1),

    Q("RAT-15", T, "M3.8", r"""Which of the following statements is/are true?

I. Increasing a quantity by $50\%$ and then decreasing the result by $50\%$ returns it to its original value.
II. A $10\%$ increase followed by a $10\%$ increase is a $21\%$ increase overall.
III. If $A$ is $25\%$ more than $B$, then $B$ is $20\%$ less than $A$.""", ROMAN3, "G",
      r"I is false: $1.5 \times 0.5 = 0.75$. II: $1.1^2 = 1.21$, true. III: $A = 1.25B \Rightarrow B = 0.8A$, true.", paper=2, tags=("roman",), diff=1),
]
