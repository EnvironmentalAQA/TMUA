"""Answer keys and score conversions for the published TMUA papers, transcribed from the
official answer-key PDFs in official-papers/ (TMUA-<series>-KEY.pdf).

KEYS[series][paper] = 20-letter string (question 1 first).
GRADES[series] = {"p1": [grade for raw 0..20], "p2": [...], "overall": [grade for raw 0..40]} where published.
"""

SERIES = [
    # (series id, label, year for sorting, notes)
    ("Specimen", "Specimen papers", 2016, "Specimen papers published before the first sitting."),
    ("Practice", "Practice papers", 2016, "Practice papers published by the test provider."),
    ("2017", "November 2017", 2017, "First live sitting."),
    ("2018", "October 2018", 2018, ""),
    ("2019", "2019", 2019, ""),
    ("2020", "2020", 2020, ""),
    ("2021", "2021", 2021, ""),
    ("2022", "2022", 2022, ""),
    ("2023", "2023", 2023, "The last paper-based sitting run by Cambridge; no grade conversion was published with the key."),
]

KEYS = {
    "Specimen": {1: "DDBEDDCFADEDCDAEDBDG", 2: "BBCAAFCCEEDACBEAEEBD"},
    "Practice": {1: "HECBCCBFDEEECDCCDABD", 2: "ABDCCCCBDEDFEBDCHDFE"},
    "2017":     {1: "CCABCBBAFEABCFBEDADE", 2: "AEGBBAEEDDBCBFDCFBEB"},
    "2018":     {1: "DCEGDEADBECFCBEFABDE", 2: "CBFDACBDFBAFFEGFCCCB"},
    "2019":     {1: "AAECECFEDFHCBBACCBCE", 2: "ECADBDBEDAAFDBBFDEEB"},
    "2020":     {1: "CCBDACADCAEDFECCAAEC", 2: "EFCGAAHEFFGDDADDEGEC"},
    "2021":     {1: "FFGBFDGACBAECBCBABBD", 2: "DECCBDBCCECBACBEFCFE"},
    "2022":     {1: "CDFCHFEBECADADHBDBFB", 2: "BECBFCFCAGCFEDFDEEBE"},
    "2023":     {1: "FACCFEFBEBBFFAFEEEDF", 2: "HFCGAFEDDAGCCFBBFDHD"},
}

# grade for raw score 0, 1, 2, ..., 20 (papers) or 0..40 (overall)
GRADES = {
    "2017": {
        "p1": [1, 1, 1, 1, 1.6, 2.3, 2.9, 3.5, 4, 4.5, 5, 5.5, 6, 6.6, 7.1, 7.8, 8.4, 9, 9, 9, 9],
        "p2": [1, 1, 1, 1.4, 2.1, 2.8, 3.4, 4, 4.5, 5, 5.4, 5.9, 6.4, 6.9, 7.4, 8, 8.6, 9, 9, 9, 9],
        "overall": [1, 1, 1, 1, 1, 1, 1, 1, 1.5, 1.9, 2.2, 2.6, 3, 3.3, 3.6, 3.9, 4.2, 4.5, 4.8, 5.1, 5.4,
                    5.6, 5.9, 6.2, 6.5, 6.8, 7.1, 7.4, 7.7, 8, 8.4, 8.8, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    },
    "2018": {
        "p1": [1, 1, 1, 1, 1, 1.7, 2.4, 3, 3.6, 4.1, 4.7, 5.3, 5.8, 6.4, 7, 7.7, 8.5, 9, 9, 9, 9],
        "p2": [1, 1, 1, 1.2, 2.2, 3, 3.6, 4.3, 4.9, 5.5, 6, 6.5, 7.1, 7.7, 8.3, 9, 9, 9, 9, 9, 9],
        "overall": [1, 1, 1, 1, 1, 1, 1, 1, 1.5, 1.9, 2.3, 2.6, 3, 3.3, 3.6, 3.9, 4.2, 4.5, 4.8, 5.1, 5.4,
                    5.6, 5.9, 6.2, 6.5, 6.8, 7.1, 7.4, 7.7, 8, 8.4, 8.8, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    },
    "2019": {
        "p1": [1, 1, 1, 1.1, 2, 2.8, 3.5, 4.2, 4.8, 5.3, 5.9, 6.5, 6.7, 6.9, 7.2, 7.4, 7.7, 8, 8.5, 9, 9],
        "p2": [1, 1, 1, 1, 1, 1.8, 2.5, 3.1, 3.7, 4.3, 4.8, 5.4, 5.9, 6.5, 6.8, 7, 7.3, 7.6, 8.1, 8.8, 9],
        "overall": [1, 1, 1, 1, 1, 1, 1, 1.1, 1.5, 1.9, 2.3, 2.6, 3, 3.3, 3.6, 3.9, 4.2, 4.5, 4.8, 5.1, 5.4,
                    5.7, 5.9, 6.2, 6.5, 6.6, 6.7, 6.8, 7, 7.1, 7.2, 7.4, 7.5, 7.7, 7.9, 8.1, 8.3, 8.6, 9, 9, 9],
    },
    "2020": {
        "p1": [1, 1, 1, 1, 1.6, 2.3, 3, 3.6, 4.2, 4.7, 5.3, 5.8, 6.4, 6.7, 6.9, 7.1, 7.4, 7.8, 8.2, 8.9, 9],
        "p2": [1, 1, 1, 1, 1.3, 2.2, 2.9, 3.6, 4.2, 4.8, 5.4, 6, 6.5, 6.8, 7, 7.3, 7.6, 7.9, 8.4, 9, 9],
        "overall": [1, 1, 1, 1, 1, 1, 1, 1, 1.4, 1.8, 2.2, 2.6, 2.9, 3.3, 3.6, 3.9, 4.2, 4.5, 4.8, 5.1, 5.3,
                    5.6, 5.9, 6.2, 6.5, 6.6, 6.7, 6.8, 7, 7.1, 7.2, 7.4, 7.5, 7.7, 7.8, 8.1, 8.3, 8.6, 9, 9, 9],
    },
    "2021": {
        "p1": [1, 1, 1, 1, 1.9, 2.6, 3.3, 3.9, 4.5, 5, 5.6, 6.1, 6.6, 6.8, 7, 7.3, 7.6, 7.9, 8.3, 9, 9],
        "p2": [1, 1, 1, 1, 1.1, 1.9, 2.7, 3.3, 3.9, 4.5, 5.1, 5.7, 6.3, 6.7, 6.9, 7.2, 7.5, 7.8, 8.3, 9, 9],
        "overall": [1, 1, 1, 1, 1, 1, 1, 1.1, 1.5, 1.9, 2.3, 2.6, 3, 3.3, 3.6, 3.9, 4.2, 4.5, 4.8, 5.1, 5.4,
                    5.6, 5.9, 6.2, 6.5, 6.6, 6.7, 6.8, 7, 7.1, 7.2, 7.4, 7.5, 7.7, 7.9, 8.1, 8.3, 8.6, 9, 9, 9],
    },
    "2022": {
        "p1": [1, 1, 1, 2.1, 3, 3.8, 4.4, 5, 5.6, 6.1, 6.5, 6.7, 6.9, 7.1, 7.3, 7.5, 7.8, 8.1, 8.5, 9, 9],
        "p2": [1, 1, 1, 1, 1.3, 2.1, 2.8, 3.4, 4, 4.6, 5.2, 5.8, 6.4, 6.7, 6.9, 7.2, 7.4, 7.8, 8.2, 8.9, 9],
        "overall": [1, 1, 1, 1, 1, 1, 1.2, 1.6, 2.1, 2.5, 2.9, 3.2, 3.6, 3.9, 4.2, 4.5, 4.8, 5.1, 5.4, 5.7, 5.9,
                    6.2, 6.5, 6.6, 6.7, 6.8, 6.9, 7, 7.1, 7.2, 7.4, 7.5, 7.6, 7.8, 8, 8.1, 8.4, 8.6, 9, 9, 9],
    },
    "Practice": {
        "p1": [1, 1, 1, 1, 1.8, 2.7, 3.4, 4.2, 4.8, 5.5, 6.1, 6.7, 7.3, 7.9, 8.6, 9, 9, 9, 9, 9, 9],
        "p2": [1, 1, 1, 1.4, 2.5, 3.4, 4.2, 4.9, 5.6, 6.2, 6.8, 7.4, 8.1, 8.7, 9, 9, 9, 9, 9, 9, 9],
        "overall": [1, 1, 1, 1, 1, 1, 1, 1.6, 2.1, 2.6, 3, 3.4, 3.8, 4.2, 4.5, 4.8, 5.2, 5.5, 5.8, 6.1, 6.4,
                    6.7, 7.1, 7.4, 7.7, 8, 8.3, 8.7, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    },
}

# Series used for the site's default grade estimate (most recent published conversion).
DEFAULT_GRADE_SERIES = "2022"


def grade_for(series, which, raw):
    """which in ('p1', 'p2', 'overall'). Returns None if no table."""
    t = GRADES.get(series, {}).get(which)
    if t is None:
        return None
    raw = max(0, min(raw, len(t) - 1))
    return t[raw]
