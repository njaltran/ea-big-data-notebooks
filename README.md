# Enterprise Architectures for Big Data

Course repo for *Enterprise Architectures for Big Data* (Prof. Dr. Roland M. Mueller, HWR Berlin). Two tracks live here:

1. **Team project** (`project/`): News Intelligence Platform. Real-time intelligence system that collects multilingual news from five countries (Germany, USA, Italy, Myanmar, Kazakhstan), classifies topic and sentiment, and visualises how each country frames the same global events. See [`project/README.md`](project/README.md).
2. **Personal course study** (`notebooks/`, `resources/`, `Enterprise architecture/`): five reactive marimo notebooks, structured paper takeaways, and an Obsidian vault that maps the course into a single navigable wiki.

## Repository layout

```
.
├── project/                  # team project (News Intelligence Platform)
├── notebooks/                # 5 reactive marimo notebooks (PEP 723)
├── resources/                # structured paper takeaways (markdown)
├── Enterprise architecture/  # Obsidian vault, course concepts as a wiki
├── exercises/                # course exercises
├── README.md
└── LICENSE                   # MIT
```

## The intellectual thread

Three course papers (Banko and Brill 2001, Halevy/Norvig/Pereira 2009, Watson 2014) converge on a single claim:

> **More data beats smarter algorithms, up to a point.**

That claim motivates the entire Big Data stack (Hadoop, Spark, NoSQL, streaming, cloud). The notebooks make you *feel* the claim by reproducing the papers' key figures interactively. The team project bites the same argument from the Long Tail end: cross-country coverage of Myanmar and Kazakhstan, where the data is rare and the framing differs the most.

## Notebooks (personal study)

Each notebook is a [PEP 723](https://peps.python.org/pep-0723/) script with inline dependencies. No `pip install`, no virtualenv setup.

| # | Notebook | What you do | Paired reading |
|---|----------|-------------|----------------|
| 01 | [`01_enterprise_architecture.py`](notebooks/01_enterprise_architecture.py) | Feel the 5 Vs of Big Data, match workloads to the stack | [`01-intro.md`](resources/01-intro.md) |
| 02 | [`02_complexity.py`](notebooks/02_complexity.py) | See O(n) vs O(n²) vs O(2ⁿ) diverge, find crossover points | [`02-time-space-complexity.md`](resources/02-time-space-complexity.md) |
| 03 | [`03_learning_curves.py`](notebooks/03_learning_curves.py) | Reproduce Banko and Brill's log-linear learning curves | [`03-banko-brill-2001.md`](resources/03-banko-brill-2001.md) |
| 04 | [`04_unreasonable_effectiveness.py`](notebooks/04_unreasonable_effectiveness.py) | Climb the corpus scale ladder (1M to 1T words), watch the long tail fill in | [`04-halevy-unreasonable-effectiveness.md`](resources/04-halevy-unreasonable-effectiveness.md) |
| 05 | [`05_big_data_analytics.py`](notebooks/05_big_data_analytics.py) | Pick the right platform per V/V/V profile, price it, simulate Amdahl's Law | [`05-watson-tutorial.md`](resources/05-watson-tutorial.md) |

**Prerequisite:** [`uv`](https://docs.astral.sh/uv/) (fast Python package manager).

```bash
brew install uv
# or: curl -LsSf https://astral.sh/uv/install.sh | sh
```

Open a notebook in edit mode (reactive, full interactivity):

```bash
uv run marimo edit notebooks/01_enterprise_architecture.py
```

Run as a read-only app (good for sharing):

```bash
uv run marimo run notebooks/02_complexity.py
```

### Notebook design choices

- **Self-contained.** Data is synthetic. Magnitudes mirror the papers but nothing is fetched or bundled. Runs offline on a fresh machine.
- **Reactive, not linear.** Marimo's dataflow means every slider change propagates automatically. No "Run all cells" dance.
- **1:1 pairing.** Each notebook sits next to exactly one `resources/NN-*.md` takeaway. Read the takeaway, then go play with the notebook.
- **No heavy dependencies.** `marimo`, `altair`, `pandas`, `numpy`. That's it.

## Resources and vault

- `resources/` holds longer-prose paper takeaways. Read these before the oral exam, or as reference while working a notebook. See [`resources/README.md`](resources/README.md) for the index.
- `Enterprise architecture/` is an Obsidian vault with wiki-style concept notes and `[[wikilinks]]`. Start at `EA Wiki.md` for the map of content. Primary source of truth for course concepts.

## Team project

The News Intelligence Platform lives entirely under `project/`. It has its own README, `.dlt/` workspace, venv, and `CLAUDE.md` (gitignored). Pipeline commands run from inside `project/`, not the repo root. See [`project/README.md`](project/README.md).

## Course assessment

Report 36%, Presentation 30%, Oral Exam 24%, Assignments 10%. The team project drives the report and presentation.

## License

[MIT](LICENSE). Course slides and lecture PDFs (under `course_material/` and the root) are not redistributed via this repo (they are gitignored).
