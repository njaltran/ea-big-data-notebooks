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
        # 03 — Banko & Brill (2001): Learning curves at scale

        Paired with [`resources/03-banko-brill-2001.md`](../resources/03-banko-brill-2001.md).

        The paper's punchline: on NLP disambiguation (e.g. *principle* vs *principal*), four different
        learners all keep improving **log-linearly** from 10⁶ to 10⁹ words — none plateaus.

        > *"Reconsider the trade-off between investing in better algorithms vs. investing in more data."*

        Three interactive tools:

        1. **Curve reproduction** — shape of `accuracy ≈ a + b·log₁₀(n)` per learner
        2. **Committee voting** — agreement level → accuracy (paper's Table)
        3. **Active vs sequential sampling** — budget split at fixed labels
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## 1. Learning curves

        We model each learner with `accuracy(n) = min(1, a + b · log₁₀(n / 10⁶))` where `a` is the
        starting accuracy at 1M words and `b` is the per-decade slope. Drag the sliders to see how
        slope and ceiling interact.
        """
    )
    return


@app.cell
def _(mo):
    slope_mult = mo.ui.slider(0.5, 2.0, value=1.0, step=0.05, label="slope multiplier")
    max_exp = mo.ui.slider(6, 11, value=9, label="max training size (10^x words)")
    mo.hstack([slope_mult, max_exp])
    return max_exp, slope_mult


@app.cell
def _(alt, max_exp, np, pd, slope_mult):
    # Base shapes approximated from Figure 1 of the paper.
    _learners = {
        "Winnow":        {"a": 0.745, "b": 0.018},
        "Perceptron":    {"a": 0.740, "b": 0.017},
        "Naïve Bayes":   {"a": 0.730, "b": 0.016},
        "Memory-based":  {"a": 0.720, "b": 0.020},
    }
    _ns = np.logspace(6, max_exp.value, 60)
    _rows = []
    for _name, _p in _learners.items():
        _b_eff = _p["b"] * slope_mult.value
        _accs = np.minimum(1.0, _p["a"] + _b_eff * np.log10(_ns / 1e6))
        for _n_, _a_ in zip(_ns, _accs):
            _rows.append({"words": float(_n_), "accuracy": float(_a_), "learner": _name})
    _df = pd.DataFrame(_rows)
    _chart = (
        alt.Chart(_df)
        .mark_line()
        .encode(
            x=alt.X("words:Q", scale=alt.Scale(type="log"), title="training words (log)"),
            y=alt.Y("accuracy:Q", scale=alt.Scale(domain=[0.70, 1.0])),
            color="learner:N",
            tooltip=["learner", alt.Tooltip("words:Q", format=".2e"), alt.Tooltip("accuracy:Q", format=".3f")],
        )
        .properties(width=620, height=320, title="Accuracy vs training corpus size (log-linear)")
    )
    _chart
    return


@app.cell
def _(mo):
    mo.md(
        """
        Notice two things:

        - The lines stay straight on a **log-x** axis through 10⁹ words → **log-linear** growth, no asymptote.
        - Differences between learners shrink as `n` grows — more data compresses the algorithmic gap.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## 2. Committee voting (§5.2)

        Ten Naïve Bayes classifiers trained on bootstrap samples. Auto-label only instances where `k`
        of them agree. Higher agreement = more confident = higher accuracy.

        The paper reports (exact values):
        """
    )
    return


@app.cell
def _(mo):
    agree_threshold = mo.ui.slider(5, 10, value=10, label="# classifiers that must agree")
    agree_threshold
    return (agree_threshold,)


@app.cell
def _(agree_threshold, alt, pd):
    _voting = pd.DataFrame(
        [
            (10, 0.8734),
            (9, 0.6892),
            (8, 0.6286),
            (7, 0.6027),
            (6, 0.5497),
            (5, 0.5000),
        ],
        columns=["agree", "accuracy"],
    )
    _voting["selected"] = _voting["agree"] >= agree_threshold.value
    _chart = (
        alt.Chart(_voting)
        .mark_bar()
        .encode(
            x=alt.X("agree:O", title="classifiers agreeing (of 10)"),
            y=alt.Y("accuracy:Q", scale=alt.Scale(domain=[0.4, 1.0])),
            color=alt.Color("selected:N", scale=alt.Scale(range=["#ccc", "#3b82f6"]),
                            legend=None),
            tooltip=["agree", "accuracy"],
        )
        .properties(width=520, height=260)
    )
    _chart
    return


@app.cell
def _(agree_threshold, mo):
    insight = {
        10: "Only ~unanimity is safe — 87% accurate auto-labels, but you label few instances.",
        9:  "One dissenter drops you from 87% to 69% — sharp confidence cliff.",
        8:  "Already noisy: 63%. Auto-labeling at this threshold pollutes the training set.",
        7:  "60% — barely above chance on balanced sets. Don't auto-label.",
        6:  "55% — basically a coin flip.",
        5:  "Majority vote = 50% = random.",
    }
    mo.md(f"**At threshold ≥ {agree_threshold.value}:** {insight[agree_threshold.value]}")
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## 3. Active learning vs sequential sampling (§5.1)

        Budget `M` labels. Split them:

        - `M · u` on the **most-uncertain** instances (highest vote-entropy under bagging)
        - `M · (1 − u)` on **random** instances

        Paper finding: pure uncertainty sampling (u = 1) biases the training set toward hard cases.
        Mixing half-and-half beats both extremes. Sliding `u`:
        """
    )
    return


@app.cell
def _(mo):
    budget = mo.ui.slider(100, 5000, value=1000, step=100, label="label budget M")
    mix = mo.ui.slider(0.0, 1.0, value=0.5, step=0.05, label="fraction uncertain (u)")
    mo.hstack([budget, mix])
    return budget, mix


@app.cell
def _(alt, budget, mix, mo, np, pd):
    # Simulated: sequential baseline climbs slowly; active with mix=0.5 gets ~10-15% more accuracy
    # per label; pure uncertainty (u=1) actually degrades because of hard-case bias.
    _M = budget.value
    _labels = np.linspace(10, _M, 40)
    _baseline = 0.72 + 0.04 * np.log10(_labels / 10)          # random sampling
    # Peak gain at u=0.5; quadratic penalty for u=0 or u=1
    _active_gain = 0.05 * (1 - 4 * (mix.value - 0.5) ** 2)
    _active = _baseline + _active_gain * np.log10(_labels / 10)

    _df = pd.DataFrame(
        {
            "labels": np.concatenate([_labels, _labels]),
            "accuracy": np.concatenate([_baseline, _active]),
            "strategy": ["sequential (random)"] * len(_labels) + [f"active (u = {mix.value:.2f})"] * len(_labels),
        }
    )
    _chart = (
        alt.Chart(_df)
        .mark_line()
        .encode(
            x=alt.X("labels:Q", scale=alt.Scale(type="log"), title="labeled examples"),
            y=alt.Y("accuracy:Q", scale=alt.Scale(domain=[0.7, 0.95])),
            color="strategy:N",
        )
        .properties(width=560, height=260)
    )
    _caption = "Best mix sits near u = 0.5. Pure uncertainty (u → 1) hurts — too many hard cases, no class balance."
    mo.vstack([_chart, mo.md(f"_{_caption}_")])
    return


@app.cell
def _(mo):
    mo.md(
        """
        ---

        **Takeaway:** Banko & Brill reframed the field — given free labels, **ship more data** instead of
        a cleverer model. [Notebook 04](04_unreasonable_effectiveness.py) stretches this even further.
        """
    )
    return


if __name__ == "__main__":
    app.run()
