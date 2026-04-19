# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "altair",
#     "pandas",
#     "numpy",
# ]
# ///

import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import altair as alt
    return alt, mo, np, pd


@app.cell
def _(mo):
    mo.md(
        """
        # 04 — The Unreasonable Effectiveness of Data (Halevy, Norvig, Pereira 2009)

        Paired with [`resources/04-halevy-unreasonable-effectiveness.md`](../resources/04-halevy-unreasonable-effectiveness.md).

        Thesis: for human-behavior problems (language, vision), theory bends the knee to **web-scale data**.
        > "Simple models and a lot of data trump more elaborate models based on less data."

        Three interactive tools:

        1. **Corpus scale ladder** — Brown (1M) → Google (1T) words
        2. **Long-tail distribution** — Zipf-generated; watch rare events emerge
        3. **Web-table attributes** — Paşca-style schema autocomplete
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## 1. Corpus scale ladder

        Drag the slider up the orders of magnitude. Every decade of data buys roughly a fixed chunk of
        accuracy — the line is straight on a log-x axis, just like Banko & Brill.
        """
    )
    return


@app.cell
def _(mo):
    log_words = mo.ui.slider(6, 12, value=9, step=0.25, label="corpus size (10^x words)")
    log_words
    return (log_words,)


@app.cell
def _(alt, log_words, mo, np, pd):
    _corpora = [
        (6,  "Brown Corpus (1967)"),
        (8,  "Wikipedia dump"),
        (10, "Common Crawl snapshot"),
        (12, "Google n-grams (1T)"),
    ]
    _xs = np.linspace(6, 12, 50)
    _ys = 0.60 + 0.035 * (_xs - 6)  # accuracy per decade; pure illustration

    _df = pd.DataFrame({"log_n": _xs, "accuracy": _ys})
    _markers = pd.DataFrame(
        [{"log_n": e, "label": name, "accuracy": 0.60 + 0.035 * (e - 6)} for e, name in _corpora]
    )
    _user = pd.DataFrame(
        [{"log_n": log_words.value, "accuracy": 0.60 + 0.035 * (log_words.value - 6)}]
    )

    _line = alt.Chart(_df).mark_line().encode(x="log_n:Q", y=alt.Y("accuracy:Q", scale=alt.Scale(domain=[0.55, 1.0])))
    _dots = alt.Chart(_markers).mark_point(size=80, color="black").encode(x="log_n:Q", y="accuracy:Q", tooltip=["label"])
    _labels = alt.Chart(_markers).mark_text(dy=-12, fontSize=10).encode(x="log_n:Q", y="accuracy:Q", text="label")
    _me = alt.Chart(_user).mark_point(size=200, color="red", shape="diamond").encode(x="log_n:Q", y="accuracy:Q")

    _chart = (_line + _dots + _labels + _me).properties(width=620, height=300,
        title="Synthetic: accuracy ≈ 0.60 + 0.035 · log₁₀(N). Red = your slider.")
    mo.vstack([
        _chart,
        mo.md(f"**You picked:** ~10^{log_words.value:.2f} words → simulated accuracy ≈ "
              f"{0.60 + 0.035 * (log_words.value - 6):.3f}"),
    ])
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## 2. The long tail — don't throw away rare events

        Zipf's law: the `k`-th most-common word has frequency ∝ `1/k`. Most of the mass is in the head,
        but the **tail is enormous**. Halevy: *"Web data = individually rare but collectively frequent."*
        """
    )
    return


@app.cell
def _(mo):
    corpus_log = mo.ui.slider(3, 9, value=6, label="corpus size (10^x tokens)")
    vocab_log = mo.ui.slider(2, 7, value=5, label="vocabulary size (10^x words)")
    mo.hstack([corpus_log, vocab_log])
    return corpus_log, vocab_log


@app.cell
def _(alt, corpus_log, mo, np, pd, vocab_log):
    _V = int(10 ** vocab_log.value)
    _N = int(10 ** corpus_log.value)
    _ranks = np.arange(1, _V + 1)
    # Zipf: freq(k) ∝ 1/k ; normalize then scale to corpus
    _weights = 1.0 / _ranks
    _weights /= _weights.sum()
    _counts = _weights * _N

    # Bucket counts by observability tiers
    _tiers = pd.DataFrame(
        [
            ("seen ≥100 times", int((_counts >= 100).sum())),
            ("seen 10–99 times", int(((_counts >= 10) & (_counts < 100)).sum())),
            ("seen 1–9 times",  int(((_counts >= 1) & (_counts < 10)).sum())),
            ("unseen (<1)",     int((_counts < 1).sum())),
        ],
        columns=["tier", "words"],
    )
    _chart = (
        alt.Chart(_tiers)
        .mark_bar()
        .encode(
            x=alt.X("words:Q", scale=alt.Scale(type="symlog"), title="vocabulary words (symlog)"),
            y=alt.Y("tier:N", sort=["seen ≥100 times", "seen 10–99 times", "seen 1–9 times", "unseen (<1)"]),
            color=alt.Color("tier:N", legend=None),
            tooltip=["tier", "words"],
        )
        .properties(width=560, height=180)
    )
    mo.vstack([
        _chart,
        mo.md(
            f"At **10^{corpus_log.value} tokens** across a **10^{vocab_log.value}-word vocab**: "
            f"{_tiers.loc[0, 'words']:,} words are well-sampled, "
            f"{_tiers.loc[3, 'words']:,} are **unseen**. Scale the corpus up and the unseen bar shrinks."
        ),
    ])
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## 3. Web-table attribute autocomplete (Paşca)

        Halevy et al. mention extracting 2.5M distinct schemata from 150M web tables. Given a *class*,
        you can propose its top attributes with ~90% precision. Pick a class and see synthetic
        suggestions:
        """
    )
    return


@app.cell
def _(mo):
    seed = mo.ui.dropdown(
        options=["Company", "Car", "Country", "Movie", "Drug"],
        value="Company",
        label="class",
    )
    seed
    return (seed,)


@app.cell
def _(pd, seed):
    attrs = {
        "Company": [("CEO", 0.96), ("Headquarters", 0.94), ("Founded", 0.93), ("Stock price", 0.90),
                    ("Employees", 0.88), ("Industry", 0.87), ("Revenue", 0.85), ("Logo", 0.82),
                    ("Website", 0.80), ("Products", 0.78)],
        "Car":     [("Make", 0.97), ("Model", 0.96), ("Year", 0.95), ("Price", 0.93),
                    ("Mileage", 0.91), ("Color", 0.89), ("Transmission", 0.86), ("Fuel type", 0.84),
                    ("Engine", 0.82), ("VIN", 0.80)],
        "Country": [("Capital", 0.97), ("Population", 0.96), ("Area", 0.94), ("Currency", 0.93),
                    ("Language", 0.90), ("GDP", 0.89), ("Continent", 0.87), ("Flag", 0.85),
                    ("President", 0.83), ("Time zone", 0.81)],
        "Movie":   [("Director", 0.96), ("Year", 0.95), ("Runtime", 0.93), ("Genre", 0.92),
                    ("Cast", 0.90), ("Rating", 0.89), ("Budget", 0.86), ("Box office", 0.84),
                    ("Studio", 0.82), ("Language", 0.80)],
        "Drug":    [("Generic name", 0.95), ("Brand name", 0.94), ("Dosage", 0.92), ("Route", 0.90),
                    ("Manufacturer", 0.88), ("Side effects", 0.87), ("Indication", 0.85),
                    ("ATC code", 0.83), ("Half-life", 0.81), ("Pregnancy category", 0.79)],
    }
    pd.DataFrame(attrs[seed.value], columns=["suggested attribute", "precision"])
    return


@app.cell
def _(mo):
    mo.md(
        """
        The numbers are illustrative, but the pattern is real: the **top-10 attributes per class hit
        ~90%** precision because the same schemas recur across millions of tables. Data at scale
        becomes its own ontology — no hand-curated Semantic Web needed.

        ---

        **Takeaway:** Halevy's thesis is operational — *choose a representation that exploits unlabeled
        data at web scale*. [Notebook 05](05_big_data_analytics.py) grounds this in the platforms that
        make it possible.
        """
    )
    return


if __name__ == "__main__":
    app.run()
