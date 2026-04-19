# Enterprise Architectures for Big Data — Interactive Notebooks

Reactive [marimo](https://marimo.io/) notebooks that turn five foundational Big Data readings into hands-on, slider-driven explorations. Drag a slider — watch the chart update, the crossover shift, the long tail fill in.

Companion to the course *Enterprise Architectures for Big Data* (Prof. Dr. Roland M. Mueller, HWR Berlin).

---

## The thread

Three of the papers below — **Banko & Brill (2001)**, **Halevy/Norvig/Pereira (2009)**, **Watson (2014)** — converge on a single claim:

> **More data beats smarter algorithms — up to a point.**

That claim motivates the entire Big Data stack (Hadoop, Spark, NoSQL, streaming, cloud). The notebooks make you *feel* the claim by reproducing the papers' key figures interactively.

---

## Contents

```
.
├── notebooks/     # 5 reactive marimo notebooks (PEP 723, self-contained)
├── resources/     # 5 structured takeaway notes (markdown)
└── README.md
```

| # | Notebook | What you'll do | Paired reading |
|---|----------|----------------|----------------|
| 01 | [`01_enterprise_architecture.py`](notebooks/01_enterprise_architecture.py) | Feel the **5 V's** of Big Data; match workloads to the stack | [`01-intro.md`](resources/01-intro.md) |
| 02 | [`02_complexity.py`](notebooks/02_complexity.py) | See **O(n) vs O(n²) vs O(2ⁿ)** diverge; find crossover points | [`02-time-space-complexity.md`](resources/02-time-space-complexity.md) |
| 03 | [`03_learning_curves.py`](notebooks/03_learning_curves.py) | Reproduce **Banko & Brill's** log-linear learning curves | [`03-banko-brill-2001.md`](resources/03-banko-brill-2001.md) |
| 04 | [`04_unreasonable_effectiveness.py`](notebooks/04_unreasonable_effectiveness.py) | Climb the **corpus scale ladder** (1M → 1T words); watch the long tail fill in | [`04-halevy-unreasonable-effectiveness.md`](resources/04-halevy-unreasonable-effectiveness.md) |
| 05 | [`05_big_data_analytics.py`](notebooks/05_big_data_analytics.py) | Pick the right platform per V/V/V profile; price it; simulate **Amdahl's Law** | [`05-watson-tutorial.md`](resources/05-watson-tutorial.md) |

---

## Run locally

Each notebook is a [PEP 723](https://peps.python.org/pep-0723/) script — dependencies are declared inline. No `pip install`, no virtualenv setup.

**Prerequisite:** [`uv`](https://docs.astral.sh/uv/) (fast Python package manager).

```bash
# macOS
brew install uv

# or (any platform)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Open a notebook in edit mode** (reactive, full interactivity):

```bash
uv run marimo edit notebooks/01_enterprise_architecture.py
```

**Run as a read-only app** (good for sharing):

```bash
uv run marimo run notebooks/02_complexity.py
```

**Open them all at once** on different ports:

```bash
for f in notebooks/0*.py; do uv run marimo edit "$f" & done
```

---

## Design choices

- **Self-contained.** Data is synthetic — magnitudes mirror the papers but nothing is fetched or bundled. You can run the notebooks offline on a fresh machine.
- **Reactive, not linear.** Marimo's dataflow means every slider change propagates automatically; no "Run all cells" dance.
- **1:1 pairing.** Each notebook sits next to exactly one `resources/NN-*.md` takeaway — read the takeaway, then go play with the notebook.
- **No heavy dependencies.** `marimo`, `altair`, `pandas`, `numpy`. That's it.

---

## What's in `resources/`

Distilled takeaways from each source — the "why does this matter" in 1–2 pages. Written for quick review before an oral exam or as a reference while working through the notebook. See [`resources/README.md`](resources/README.md) for the index.

---

## License

[MIT](LICENSE) — use freely, credit appreciated.
