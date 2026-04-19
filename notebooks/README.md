# Marimo notebooks — learn the resources interactively

Reactive marimo notebooks paired 1:1 with the takeaway files in [`../resources/`](../resources/). Each notebook is **self-contained** (synthetic data, no network) and **interactive** — move sliders, watch charts update.

## Run

Each file is a [PEP 723](https://peps.python.org/pep-0723/) script — dependencies are declared inline. With `uv` installed:

```bash
uv run marimo edit notebooks/01_enterprise_architecture.py
```

Or to open all at once on different ports:

```bash
for f in notebooks/0*.py; do uv run marimo edit "$f" & done
```

Run as a read-only app (no editing):

```bash
uv run marimo run notebooks/02_complexity.py
```

## Notebooks

| # | Notebook | Learning goal | Paired resource |
|---|----------|---------------|-----------------|
| 01 | [`01_enterprise_architecture.py`](01_enterprise_architecture.py) | Feel the 5 V's of Big Data; match workloads to the course technology stack | [`01-intro.md`](../resources/01-intro.md) |
| 02 | [`02_complexity.py`](02_complexity.py) | See how O(n), O(n²), O(2ⁿ) diverge; find algorithm crossover points | [`02-time-space-complexity.md`](../resources/02-time-space-complexity.md) |
| 03 | [`03_learning_curves.py`](03_learning_curves.py) | Reproduce Banko & Brill's log-linear curves; watch committee voting break down at scale | [`03-banko-brill-2001.md`](../resources/03-banko-brill-2001.md) |
| 04 | [`04_unreasonable_effectiveness.py`](04_unreasonable_effectiveness.py) | Corpus scale ladder (1M → 1T words); see how the long tail fills in | [`04-halevy-unreasonable-effectiveness.md`](../resources/04-halevy-unreasonable-effectiveness.md) |
| 05 | [`05_big_data_analytics.py`](05_big_data_analytics.py) | Pick the right platform for volume/velocity/variety; price it; simulate MapReduce parallelism | [`05-watson-tutorial.md`](../resources/05-watson-tutorial.md) |

## Notes

- Data is synthetic — magnitudes mirror the papers but nothing is fetched or bundled.
- If `uv` is missing: `brew install uv` (macOS) or see <https://docs.astral.sh/uv/>.
