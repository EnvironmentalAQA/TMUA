"""The TMUA topic tree, taken directly from the UAT-UK TMUA Content Specification
(for assessment in October 2026 and January 2027).

Section 1 Part 1 (MM1-MM8) = AS-level pure maths; Section 1 Part 2 (M1-M7) = Higher GCSE;
Section 2 (Arg / Prf / Err) = the logic-and-proof content examined only in Paper 2.

Paper 1 (Applications of Mathematical Knowledge) draws on Section 1.
Paper 2 (Mathematical Reasoning) draws on Sections 1 and 2.
"""

TEST = {
    "name": "Test of Mathematics for University Admission (TMUA)",
    "papers": {
        1: {"title": "Paper 1: Applications of Mathematical Knowledge", "minutes": 75, "questions": 20,
            "blurb": "Tests your ability to apply mathematical knowledge (Section 1 of the specification) in a variety of contexts."},
        2: {"title": "Paper 2: Mathematical Reasoning", "minutes": 75, "questions": 20,
            "blurb": "Tests your ability to apply conceptual knowledge to constructing and analysing mathematical arguments (Sections 1 and 2)."},
    },
    "rules": ["Two 75-minute papers of 20 multiple-choice questions, taken one after the other.",
              "Every question carries one mark; no penalty for wrong answers - attempt all 20.",
              "No calculator, no dictionary and no formulae booklet - you must know every formula.",
              "Answers are recorded on a separate answer sheet in soft pencil."],
}

# Each group is one spec heading; each topic (slug) is the unit the site is organised around.
GROUPS = [
    {"slug": "part1", "name": "Section 1 Part 1: AS-level pure mathematics", "paper": "Papers 1 and 2", "topics": [
        {"slug": "indices-surds", "name": "Indices and surds", "spec": "MM1.1, MM1.2, M2.7, M2.11, M2.12",
         "desc": "Laws of indices for rational exponents; simplifying surds and rationalising denominators."},
        {"slug": "quadratics", "name": "Quadratic functions", "spec": "MM1.3, M4.5, M4.11-M4.14",
         "desc": "Graphs, the discriminant, completing the square, solving quadratic equations, roots and turning points."},
        {"slug": "simultaneous-inequalities", "name": "Simultaneous equations and inequalities", "spec": "MM1.4, MM1.5, M4.16, M4.17",
         "desc": "Linear/quadratic simultaneous equations by substitution; linear and quadratic inequalities."},
        {"slug": "polynomials", "name": "Polynomials, factor and remainder theorems", "spec": "MM1.6",
         "desc": "Expanding, factorising, algebraic division by linear and quadratic divisors, the Factor and Remainder Theorems."},
        {"slug": "functions", "name": "Functions and transformations", "spec": "MM1.7, MM8.2, MM8.3, MM8.4",
         "desc": "One-to-one and many-to-one mappings, square-root and modulus functions, af(x), f(x)+a, f(x+a), f(ax) and compositions."},
        {"slug": "sequences-series", "name": "Sequences and series", "spec": "MM2.1, MM2.2, MM2.3, M4.19",
         "desc": "nth-term and recurrence sequences; arithmetic series; finite and infinite geometric series."},
        {"slug": "binomial", "name": "Binomial expansion", "spec": "MM2.4",
         "desc": "Expanding (1+x)^n and (a+f(x))^n for positive integer n; n! and nCr notation."},
        {"slug": "straight-lines", "name": "Straight lines", "spec": "MM3.1, M4.9, M4.10",
         "desc": "Equations of lines, gradients, parallel and perpendicular lines, distances and midpoints."},
        {"slug": "circles", "name": "Circles and circle theorems", "spec": "MM3.2, MM3.3, M5.8, M5.9",
         "desc": "Equation of a circle in both forms, tangents and chords, and the seven circle theorems."},
        {"slug": "trig-triangles", "name": "Triangles, radians and sectors", "spec": "MM4.1, MM4.2, M5.16",
         "desc": "Sine and cosine rules (including the ambiguous case), area = 1/2 ab sin C, radians, arc length, sector and segment area."},
        {"slug": "trig-functions", "name": "Trigonometric functions and equations", "spec": "MM4.3-MM4.6",
         "desc": "Exact values, graphs and periodicity of sin, cos, tan; tan = sin/cos and sin^2 + cos^2 = 1; solving equations in an interval."},
        {"slug": "exp-logs", "name": "Exponentials and logarithms", "spec": "MM5.1-MM5.3",
         "desc": "y = a^x, the laws of logarithms, and solving a^x = b and equations that reduce to it."},
        {"slug": "differentiation", "name": "Differentiation", "spec": "MM6.1-MM6.3, MM8.5",
         "desc": "Derivatives of x^n, gradients, tangents and normals, stationary points, increasing and decreasing functions, second derivatives."},
        {"slug": "integration", "name": "Integration", "spec": "MM7.1-MM7.6",
         "desc": "Integrals of x^n, areas between curves and axes, the Fundamental Theorem of Calculus, combining integrals, the trapezium rule and dy/dx = f(x)."},
        {"slug": "graphs", "name": "Graphs of functions", "spec": "MM8.1, MM8.5-MM8.7, M4.15",
         "desc": "Sketching lines, quadratics, cubics, trig, log, exponential, root and modulus graphs; intersections with axes; roots and intersections of graphs."},
    ]},
    {"slug": "part2", "name": "Section 1 Part 2: Higher GCSE mathematics", "paper": "Papers 1 and 2", "topics": [
        {"slug": "number", "name": "Number, units and estimation", "spec": "M1.1, M1.2, M2.1-M2.14",
         "desc": "Units and compound measures, primes, HCF/LCM, index laws, standard form, recurring decimals, bounds, rounding and estimation, systematic counting."},
        {"slug": "ratio-proportion", "name": "Ratio, proportion and percentages", "spec": "M3.1-M3.11",
         "desc": "Ratio and scale, percentage change and reverse percentages, direct and inverse proportion, growth and decay, similarity of lengths, areas and volumes."},
        {"slug": "gcse-algebra", "name": "GCSE algebra", "spec": "M4.1-M4.8, M4.18, M4.19",
         "desc": "Algebraic manipulation, rearranging formulae, identities, rational expressions, nth terms of linear and quadratic sequences, kinematics graphs."},
        {"slug": "geometry", "name": "Angles, polygons, congruence and vectors", "spec": "M5.1-M5.6, M5.10, M5.14, M5.18, M5.19",
         "desc": "Angle facts, interior and exterior angles, special quadrilaterals, congruence criteria, similarity, transformations, bearings and vectors."},
        {"slug": "mensuration", "name": "Pythagoras, mensuration and 3D", "spec": "M5.7, M5.11-M5.13, M5.15-M5.17",
         "desc": "Pythagoras in 2D and 3D, areas of composite shapes, volumes and surface areas of prisms, cylinders, cones, spheres and pyramids, trig ratios in right-angled triangles."},
        {"slug": "statistics", "name": "Statistics", "spec": "M6.1-M6.4",
         "desc": "Mean, median, mode and range (including grouped estimates), histograms and frequency density, cumulative frequency, quartiles, scatter graphs."},
        {"slug": "probability", "name": "Probability", "spec": "M7.1-M7.7",
         "desc": "Possibility spaces, tree diagrams, Venn diagrams, mutually exclusive and independent events, conditional probability, expected frequency."},
    ]},
    {"slug": "section2", "name": "Section 2: Mathematical reasoning (Paper 2 only)", "paper": "Paper 2", "topics": [
        {"slug": "logic", "name": "The logic of arguments", "spec": "Arg1-Arg4",
         "desc": "If/then, A if B, A only if B, if and only if; converse and contrapositive; necessary and sufficient; for all / for some / there exists; negating statements."},
        {"slug": "proof", "name": "Mathematical proof", "spec": "Prf1-Prf4",
         "desc": "Direct proof, proof by cases, proof by contradiction, disproof by counterexample; deducing implications; conjectures from small cases; ordering the steps of a proof."},
        {"slug": "reasoning", "name": "Chains of reasoning", "spec": "Prf2, Prf3, Prf5",
         "desc": "Problems needing a sophisticated chain of reasoning: which statements must / could be true, extremal arguments, pigeonhole-style counting, working systematically."},
        {"slug": "errors", "name": "Identifying errors in proofs", "spec": "Err1, Err2",
         "desc": "Spotting the first wrong line in a purported proof; the classic invalid deductions (x^2 = y^2 so x = y, sin a = sin b so a = b, dividing by zero, squaring inequalities)."},
    ]},
]

# The two papers described by which topics they draw on.
PAPER_TOPICS = {
    1: [t["slug"] for g in GROUPS if g["slug"] in ("part1", "part2") for t in g["topics"]],
    2: [t["slug"] for g in GROUPS for t in g["topics"]],
}


def topic_index():
    """slug -> dict(name, spec, desc, group, group_slug)."""
    out = {}
    for g in GROUPS:
        for t in g["topics"]:
            d = dict(t)
            d["group"] = g["name"]
            d["group_slug"] = g["slug"]
            out[t["slug"]] = d
    return out


ALL_SLUGS = [t["slug"] for g in GROUPS for t in g["topics"]]
