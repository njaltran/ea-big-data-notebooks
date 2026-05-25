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

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import altair as alt
    import math

    return alt, math, mo, np, pd


@app.cell
def _(mo):
    mo.md("""
    # 02 — Time & Space Complexity

    Paired with [`resources/02-time-space-complexity.md`](../resources/02-time-space-complexity.md).

    Three interactive tools:

    1. **Growth plotter** — draw any subset of O(1) … O(n!) on one axis
    2. **Crossover explorer** — at what `n` does `a·n²` overtake `b·n`?
    3. **Data-structure matrix** — pick operations, see the trade-off
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 1. Growth plotter
    """)
    return


@app.cell
def _(mo):
    max_n = mo.ui.slider(10, 200, value=50, step=5, label="max n")
    log_scale = mo.ui.switch(value=False, label="log-y")
    classes = mo.ui.multiselect(
        options=["O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n²)", "O(n³)", "O(2ⁿ)", "O(n!)"],
        value=["O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n²)"],
        label="classes",
    )
    mo.vstack([max_n, log_scale, classes])
    return classes, log_scale, max_n


@app.cell
def _(alt, classes, log_scale, math, max_n, np, pd):
    formulas = {
        "O(1)":      lambda n: np.ones_like(n, dtype=float),
        "O(log n)":  lambda n: np.log2(np.clip(n, 1, None)),
        "O(n)":      lambda n: n.astype(float),
        "O(n log n)": lambda n: n * np.log2(np.clip(n, 1, None)),
        "O(n²)":     lambda n: n.astype(float) ** 2,
        "O(n³)":     lambda n: n.astype(float) ** 3,
        "O(2ⁿ)":     lambda n: np.power(2.0, np.clip(n, 0, 60)),  # cap to avoid overflow
        "O(n!)":     lambda n: np.array([math.factorial(min(int(x), 20)) for x in n], dtype=float),
    }
    ns = np.arange(1, max_n.value + 1)
    rows = []
    for name in classes.value:
        ys = formulas[name](ns)
        for n_, y_ in zip(ns, ys):
            rows.append({"n": int(n_), "ops": float(y_), "class": name})
    _df = pd.DataFrame(rows)
    _y_scale = alt.Scale(type="log") if log_scale.value else alt.Scale(type="linear")
    _chart = (
        alt.Chart(_df)
        .mark_line(point=False)
        .encode(
            x=alt.X("n:Q"),
            y=alt.Y("ops:Q", scale=_y_scale, title="operations"),
            color=alt.Color("class:N", sort=list(formulas.keys())),
            tooltip=["class", "n", "ops"],
        )
        .properties(width=620, height=320)
    )
    _chart
    return


@app.cell
def _(mo):
    mo.md("""
    ## 2. Crossover explorer

    Algorithm A does `a · n` work. Algorithm B does `b · n²` work. At small `n`, A's constant can be
    huge and B wins. At some crossover `n*`, they meet, then B's quadratic term runs away.

    This is Banko & Brill in miniature: *constant-factor elegance matters less than the asymptotic class.*
    """)
    return


@app.cell
def _(mo):
    a = mo.ui.slider(1, 500, value=100, label="a (constant on n)")
    b = mo.ui.slider(1, 50, value=1, label="b (constant on n²)")
    mo.hstack([a, b])
    return a, b


@app.cell
def _(a, alt, b, mo, np, pd):
    _ns = np.arange(1, 2001)
    _a_vals = a.value * _ns
    _b_vals = b.value * _ns**2
    _crossover = a.value / b.value  # a·n = b·n²  →  n = a/b

    _df = pd.DataFrame(
        {"n": np.concatenate([_ns, _ns]),
         "ops": np.concatenate([_a_vals, _b_vals]),
         "alg": ["A: a·n"] * len(_ns) + ["B: b·n²"] * len(_ns)}
    )
    _chart = (
        alt.Chart(_df)
        .mark_line()
        .encode(
            x=alt.X("n:Q"),
            y=alt.Y("ops:Q", scale=alt.Scale(type="log"), title="operations (log)"),
            color="alg:N",
        )
        .properties(width=560, height=260)
    )
    _rule = (
        alt.Chart(pd.DataFrame({"n": [_crossover]}))
        .mark_rule(color="red", strokeDash=[4, 4])
        .encode(x="n:Q")
    )
    mo.vstack([
        mo.md(f"**Crossover:** A beats B for `n > {_crossover:.1f}`."),
        _chart + _rule,
    ])
    return


@app.cell
def _(a, b, pd):
    sizes = [10, 100, 1_000, 10_000]
    tbl = pd.DataFrame(
        {
            "n": sizes,
            "A: a·n": [a.value * n for n in sizes],
            "B: b·n²": [b.value * n**2 for n in sizes],
            "winner": ["A" if a.value * n < b.value * n**2 else "B" for n in sizes],
        }
    )
    tbl
    return


@app.cell
def _(mo):
    mo.md("""
    ## 3. Data-structure trade-offs

    Pick operations you care about — the table sorts structures by total cost. `O(1)` rows go first.
    """)
    return


@app.cell
def _(mo):
    ops = mo.ui.multiselect(
        options=["access", "search", "insert", "delete"],
        value=["access", "search", "insert"],
        label="operations you care about",
    )
    ops
    return (ops,)


@app.cell
def _(ops, pd):
    # Average-case Big-O encoded as a weight so we can rank.
    weight = {"O(1)": 1, "O(log n)": 2, "O(n)": 3, "O(n log n)": 4, "O(n²)": 5}
    data = pd.DataFrame(
        [
            ("Array",             "O(1)", "O(n)",     "O(n)",     "O(n)"),
            ("Sorted array",      "O(1)", "O(log n)", "O(n)",     "O(n)"),
            ("Linked list",       "O(n)", "O(n)",     "O(1)",     "O(1)"),
            ("Stack (LIFO)",      "O(n)", "O(n)",     "O(1)",     "O(1)"),
            ("Queue (FIFO)",      "O(n)", "O(n)",     "O(1)",     "O(1)"),
            ("Hash table",        "O(1)", "O(1)",     "O(1)",     "O(1)"),
            ("Binary search tree","O(log n)", "O(log n)", "O(log n)", "O(log n)"),
            ("Balanced BST",      "O(log n)", "O(log n)", "O(log n)", "O(log n)"),
        ],
        columns=["structure", "access", "search", "insert", "delete"],
    )
    chosen = ops.value or ["access", "search", "insert", "delete"]
    data["cost"] = data[chosen].apply(lambda row: sum(weight[c] for c in row), axis=1)
    data.sort_values("cost").drop(columns=["cost"])
    return


@app.cell
def _(mo):
    mo.md("""
    ---

    **Takeaway:** the Big-O class beats the constant every time — but only once `n` is big enough.
    That threshold is often the hidden design decision.
    """)
    return


if __name__ == "__main__":
    app.run()
