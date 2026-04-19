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
        # 05 — Big Data Analytics (Watson 2014)

        Paired with [`resources/05-watson-tutorial.md`](../resources/05-watson-tutorial.md).

        Four interactive tools:

        1. **Analytics maturity** — Descriptive → Predictive → Prescriptive, with real cases
        2. **Platform decision tree** — V/V/V profile → recommended platform
        3. **Cloud warehouse cost** — Redshift $1K/TB/year model
        4. **MapReduce speedup** — Amdahl's Law on a synthetic job
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## 1. Analytics maturity

        Watson: most organizations mature **descriptive → predictive → prescriptive**. Each step adds
        a different question and a different case study.
        """
    )
    return


@app.cell
def _(mo):
    stage = mo.ui.radio(
        options=["Descriptive", "Predictive", "Prescriptive"],
        value="Descriptive",
        label="stage",
    )
    stage
    return (stage,)


@app.cell
def _(mo, stage):
    content = {
        "Descriptive": (
            "**What happened?** — Rear-view mirror.\n\n"
            "Reports, OLAP cubes, dashboards, data viz over a clean warehouse.\n\n"
            "**Case: Starbucks** — monitored blogs / Twitter / forums during a coffee launch. "
            "Sentiment said *too expensive* within hours; price dropped; negative sentiment disappeared "
            "by end of day."
        ),
        "Predictive": (
            "**What will happen?** — Windshield.\n\n"
            "Regression, ML, neural nets, 'golden-path' analysis.\n\n"
            "**Case: Chevron** — each Gulf-of-Mexico drilling miss costs ~$100M. Analyzing **50 TB of "
            "seismic data** lifted strike odds from **1-in-5 to ~1-in-3**.\n\n"
            "**Case: Target** — 25-variable pregnancy-prediction model (unscented lotion, supplements, "
            "cotton balls, etc). Backlash forced them to interleave unrelated coupons."
        ),
        "Prescriptive": (
            "**What should we do?** — GPS.\n\n"
            "Optimization, revenue management, math programming.\n\n"
            "**Case: U.S. Xpress** — trucks stream **900+ sensor fields**. Distinguishing avoidable "
            "idle from traffic idle saved millions in fuel. Output isn't a prediction — it's a "
            "routing action."
        ),
    }
    mo.md(content[stage.value])
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## 2. Platform decision tree

        Watson: *"There is no formula. Consider volume, velocity, variety, users, batch vs real-time, cost."*
        This is a simplified rules-of-thumb picker.
        """
    )
    return


@app.cell
def _(mo):
    v_vol = mo.ui.slider(1, 3, value=2, label="Volume (1=low, 3=high)")
    v_vel = mo.ui.slider(1, 3, value=1, label="Velocity (1=batch, 3=streaming)")
    v_var = mo.ui.slider(1, 3, value=1, label="Variety (1=structured, 3=unstructured)")
    mo.vstack([v_vol, v_vel, v_var])
    return v_var, v_vel, v_vol


@app.cell
def _(mo, v_var, v_vel, v_vol):
    vol, vel, var = v_vol.value, v_vel.value, v_var.value

    if vel == 3:
        rec = ("Streaming / CEP", "Tibco StreamBase, Flink, Kafka Streams",
               "Low-latency events — fraud, trading, IoT.")
    elif vol == 3 and var >= 2:
        rec = ("Hadoop / Spark on HDFS", "Cloudera, Hortonworks, Databricks",
               "PB-scale, mixed-format batch workloads.")
    elif var == 3:
        rec = ("NoSQL", "Cassandra, Mongo, Couchbase",
               "Schema-flexible, high write throughput, semi-structured docs.")
    elif vol == 3:
        rec = ("Columnar cloud warehouse", "Redshift, BigQuery, Snowflake",
               "TB–PB structured analytics, ad-hoc SQL.")
    else:
        rec = ("Classic data warehouse", "Teradata, Oracle, SAP HANA",
               "Descriptive analytics on clean structured data.")

    name, vendors, why = rec
    mo.md(
        f"### → {name}\n\n"
        f"**Typical vendors:** {vendors}\n\n"
        f"**Why:** {why}"
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## 3. Cloud warehouse cost

        Amazon Redshift, circa 2013, priced at **$1,000 / TB / year**. A sanity check on "can we just
        throw it in a warehouse?"
        """
    )
    return


@app.cell
def _(mo):
    tb = mo.ui.slider(1, 500, value=50, label="data volume (TB)")
    years = mo.ui.slider(1, 7, value=3, label="retention (years)")
    growth = mo.ui.slider(0, 100, value=20, step=5, label="annual growth (%)")
    mo.vstack([tb, years, growth])
    return growth, tb, years


@app.cell
def _(alt, growth, mo, pd, tb, years):
    _rate = 1000  # $/TB/year
    _g = growth.value / 100
    _rows = []
    for _y in range(1, years.value + 1):
        _size = tb.value * (1 + _g) ** (_y - 1)
        _rows.append({"year": _y, "TB": _size, "cost_usd": _size * _rate})
    _df = pd.DataFrame(_rows)
    _total = _df["cost_usd"].sum()

    _chart = (
        alt.Chart(_df)
        .mark_bar()
        .encode(
            x=alt.X("year:O"),
            y=alt.Y("cost_usd:Q", title="annual cost (USD)"),
            tooltip=["year", alt.Tooltip("TB:Q", format=".1f"), alt.Tooltip("cost_usd:Q", format="$,.0f")],
        )
        .properties(width=480, height=220)
    )
    mo.vstack([
        _chart,
        mo.md(f"**Total {years.value}-year cost:** ${_total:,.0f} @ $1,000/TB/year."),
    ])
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## 4. MapReduce parallelism (Amdahl's Law)

        A job has a **serial fraction** `s` (coordinator, shuffle, final reduce) and a parallelizable
        rest `1 - s`. Speedup on `P` nodes:

        $$S(P) = \\frac{1}{s + \\frac{1 - s}{P}}$$

        Drag `s` — even 5% serial caps you at 20× no matter how many nodes you add.
        """
    )
    return


@app.cell
def _(mo):
    serial = mo.ui.slider(0.01, 0.5, value=0.1, step=0.01, label="serial fraction s")
    max_nodes = mo.ui.slider(4, 1024, value=256, step=4, label="max nodes P")
    mo.hstack([serial, max_nodes])
    return max_nodes, serial


@app.cell
def _(alt, max_nodes, mo, np, pd, serial):
    _s = serial.value
    _ps = np.unique(np.round(np.logspace(0, np.log10(max_nodes.value), 40)).astype(int))
    _speedup = 1.0 / (_s + (1.0 - _s) / _ps)
    _ceiling = 1.0 / _s

    _df = pd.DataFrame({"nodes": _ps, "speedup": _speedup})
    _line = (
        alt.Chart(_df)
        .mark_line(point=True)
        .encode(
            x=alt.X("nodes:Q", scale=alt.Scale(type="log"), title="nodes P (log)"),
            y=alt.Y("speedup:Q", title=f"speedup (ceiling = {_ceiling:.1f}×)"),
            tooltip=["nodes", alt.Tooltip("speedup:Q", format=".2f")],
        )
        .properties(width=560, height=260)
    )
    _rule = (
        alt.Chart(pd.DataFrame({"y": [_ceiling]}))
        .mark_rule(color="red", strokeDash=[4, 4])
        .encode(y="y:Q")
    )
    mo.vstack([
        _line + _rule,
        mo.md(
            f"**Ceiling:** {_ceiling:.1f}× — you can never go faster than this, no matter how many nodes. "
            "This is why Yahoo ran 42,000 Hadoop servers but still cared deeply about shuffle efficiency."
        ),
    ])
    return


@app.cell
def _(mo):
    mo.md(
        """
        ---

        **Takeaway:** Big Data capability is **federated** — warehouse + Hadoop + streaming + NoSQL +
        cloud all coexist, glued together by SQL/Hive. EA's job is to match each workload to the
        platform where it runs cheapest and fastest, then integrate the results.

        That closes the series: the 5 V's diagnose the workload (NB 01), complexity sets the compute
        cost (NB 02), Banko/Brill and Halevy argue that more data wins (NB 03–04), and Watson names
        the platforms (NB 05).
        """
    )
    return


if __name__ == "__main__":
    app.run()
