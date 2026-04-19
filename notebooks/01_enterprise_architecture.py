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
    import pandas as pd
    import altair as alt
    import numpy as np

    return alt, mo, pd


@app.cell
def _(mo):
    mo.md("""
    # 01 — Enterprise Architecture & the 5 V's of Big Data

    Paired with [`resources/01-intro.md`](../resources/01-intro.md).

    Three interactive ideas:

    1. **EA hierarchy** — where Big Data sits in an enterprise
    2. **The 5 V's** — Volume, Velocity, Variety, Veracity, Value
    3. **Stack picker** — match a workload profile to course technologies
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 1. EA Hierarchy

    An Enterprise Architecture is a layered view of an organization. The course focuses on the
    bottom three: **Data, Application, Technology**. Click to expand the layers.
    """)
    return


@app.cell
def _(mo):
    hierarchy = mo.accordion(
        {
            "🎯 Mission / Strategy": "Why the organization exists. Sets the frame for every lower layer.",
            "🔄 Business Process": "The workflows that realize the strategy. Where data is produced and consumed.",
            "📊 Data": "Entities, flows, warehouses, lakes, streams. **Course layer #1.**",
            "🧩 Application": "Services, APIs, analytics apps — what reads/writes the data. **Course layer #2.**",
            "⚙️ Technology": "Servers, clusters, storage, network. Hadoop, Spark, Kafka, cloud. **Course layer #3.**",
        }
    )
    hierarchy
    return


@app.cell
def _(mo):
    mo.md("""
    ## 2. The 5 V's

    Pick a V — see example magnitudes from real systems, and which course technologies address it.
    """)
    return


@app.cell
def _(mo):
    v_choice = mo.ui.dropdown(
        options=["Volume", "Velocity", "Variety", "Veracity", "Value"],
        value="Volume",
        label="Pick a V",
    )
    v_choice
    return (v_choice,)


@app.cell
def _(alt, pd, v_choice):
    v_data = {
        "Volume": {
            "explainer": "Amount of data. Ranges from GB → PB → ZB. Transactions, social feeds, sensors.",
            "examples": [
                ("Personal laptop SSD", 5e11),          # 500 GB
                ("Enterprise warehouse", 1e14),         # 100 TB
                ("Facebook daily upload (2014)", 6e14), # 600 TB
                ("Google index (est.)", 1e17),          # 100 PB
                ("Global datasphere 2025", 1.75e23),    # 175 ZB
            ],
            "units": "bytes",
            "tech": "Hadoop/HDFS, object storage (S3), columnar warehouses",
        },
        "Velocity": {
            "explainer": "Rate of arrival. Streams, logs, RFID, sensors, metering. Peaks daily or per-event.",
            "examples": [
                ("Heart-rate monitor", 1),               # 1 evt/s
                ("Stock exchange ticks", 1e5),           # 100K evt/s
                ("IoT fleet telemetry", 1e6),            # 1M evt/s
                ("LinkedIn Kafka (2019)", 7e6),          # 7M evt/s
                ("LHC detectors raw", 4e13 / (3600*24)), # ~500M evt/s of raw hits
            ],
            "units": "events / second",
            "tech": "Kafka, Flink, stream processing / CEP",
        },
        "Variety": {
            "explainer": "Types of data: structured, semi-structured, unstructured.",
            "examples": [
                ("RDBMS row", 1),
                ("JSON doc", 2),
                ("Log line", 3),
                ("Image frame", 4),
                ("Video / audio", 5),
            ],
            "units": "structural tier",
            "tech": "NoSQL (Mongo, Cassandra), object store, embeddings",
        },
        "Veracity": {
            "explainer": "Trustworthiness. Noise, missing fields, sensor drift, adversarial input.",
            "examples": [
                ("Clean warehouse fact table", 0.01),
                ("Curated CRM", 0.05),
                ("Web-scraped product pages", 0.20),
                ("Social-media text", 0.40),
                ("Raw sensor stream (pre-calibration)", 0.60),
            ],
            "units": "estimated error rate",
            "tech": "dbt tests, Great Expectations, schema-on-read",
        },
        "Value": {
            "explainer": "Ability to turn data into a decision or product. Watson (2014): 'most important V.'",
            "examples": [
                ("Raw stored-but-unused logs", 0.0),
                ("Dashboard someone actually reads", 0.3),
                ("Anomaly alert routed to on-call", 0.6),
                ("Pricing/routing optimization in prod", 0.9),
                ("Core product feature (recs, search)", 1.0),
            ],
            "units": "business leverage (0–1)",
            "tech": "BI, ML pipelines, decision systems",
        },
    }

    cfg = v_data[v_choice.value]
    df = pd.DataFrame(cfg["examples"], columns=["example", "magnitude"])
    is_log = cfg["units"] in ("bytes", "events / second")
    scale = alt.Scale(type="log") if is_log else alt.Scale(type="linear")
    # Log-scale bars render invisibly (baseline at 0 = -∞); use circles instead.
    base = alt.Chart(df).encode(
        x=alt.X("magnitude:Q", scale=scale, title=cfg["units"]),
        y=alt.Y("example:N", sort="-x", title=None),
        tooltip=["example", "magnitude"],
    )
    mark = base.mark_circle(size=220, opacity=0.85) if is_log else base.mark_bar()
    chart = mark.properties(
        height=220, width=560, title=f"{v_choice.value} — {cfg['explainer']}"
    )
    chart
    return (cfg,)


@app.cell
def _(cfg, mo):
    mo.md(f"""
    **Typical tech:** {cfg['tech']}
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 3. Stack picker

    Rate your workload along Volume / Velocity / Variety (low, medium, high). The table below filters
    to course technologies whose sweet spot matches.
    """)
    return


@app.cell
def _(mo):
    vol = mo.ui.slider(1, 3, value=2, label="Volume (1=low, 3=high)")
    vel = mo.ui.slider(1, 3, value=2, label="Velocity")
    var = mo.ui.slider(1, 3, value=2, label="Variety")
    mo.vstack([vol, vel, var])
    return var, vel, vol


@app.cell
def _(mo, pd, var, vel, vol):
    # (min_v, min_vel, min_var) profile each tech needs; we surface techs where the user's sliders meet the floor.
    stack = pd.DataFrame(
        [
            ("RDBMS warehouse",      1, 1, 1, "Structured historical analytics, descriptive BI"),
            ("Columnar MPP (Redshift, BigQuery)", 2, 1, 1, "OLAP at TB–PB, ad-hoc SQL"),
            ("Hadoop / HDFS + Spark", 3, 1, 2, "Batch over PB, multi-format files"),
            ("NoSQL (Mongo, Cassandra)", 2, 2, 3, "Semi-structured, high write throughput"),
            ("Kafka + stream processor", 1, 3, 2, "Low-latency event pipelines"),
            ("CEP engine", 1, 3, 3, "Multi-source correlation, rules → actions"),
            ("Cloud object store + lake", 3, 2, 3, "Cheap archive + flexible compute layered on top"),
            ("GPU / deep-learning cluster", 2, 2, 3, "Vision, NLP, embeddings at scale"),
        ],
        columns=["Technology", "Vol", "Vel", "Var", "Sweet spot"],
    )
    match = stack[
        (stack["Vol"] <= vol.value)
        & (stack["Vel"] <= vel.value)
        & (stack["Var"] <= var.value)
    ].drop(columns=["Vol", "Vel", "Var"])

    _out = (
        mo.md("_No match — drag the sliders up._")
        if match.empty
        else mo.ui.table(match, selection=None, pagination=False)
    )
    _out
    return


@app.cell
def _(mo):
    mo.md("""
    ---

    **Recap** — EA gives the layered lens; the 5 V's diagnose the workload; the tech stack follows.
    Banko/Brill and Halevy (next notebooks) show *why* Volume alone is often the biggest win.
    """)
    return


if __name__ == "__main__":
    app.run()
