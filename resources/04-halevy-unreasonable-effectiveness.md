# 04 — Halevy, Norvig & Pereira (2009): The Unreasonable Effectiveness of Data

**Authors:** Alon Halevy, Peter Norvig, Fernando Pereira (Google)
**Publication:** *IEEE Intelligent Systems*, March/April 2009
**Source:** `Halevy et al_2009_The unreasonable effectiveness of data.pdf`

## Thesis

Borrowing from Wigner's "Unreasonable Effectiveness of Mathematics in the Natural Sciences": for problems involving **human behavior** (language, image understanding), elegant mathematical theories fail. The antidote is not better theory — it's **web-scale data**.

> "Embrace complexity and make use of the best ally we have: the unreasonable effectiveness of data."

## Key Arguments

### 1. Scale Changes the Game
- Brown Corpus (1967): 1M English words.
- Google 2006: **1-trillion-word** corpus with n-gram frequencies up to length 5.
- Noisy (spelling errors, fragments, no annotations) **but a million times bigger**.
- Size outweighs the noise for many tasks.

### 2. Use Data That Exists in the Wild
- **Speech recognition** and **statistical machine translation** succeed because input-output pairs occur naturally (closed-captioning, EU translations).
- Tasks needing skilled human annotation (POS tagging, NER, parsing) don't have this — expensive, slow, experts disagree.
- **Lesson:** use large available data rather than hoping for annotations.

### 3. Memorization Beats Generalization at Scale
- Statistical language models = **huge databases of n-gram counts**.
- "Simple models and a lot of data trump more elaborate models based on less data."
- Modern statistical MT = large memorized phrase tables; general rules only added when they beat memorization (e.g. dates, numbers).
- James Hays & Alexei Efros's photo scene completion: poor with thousands of photos, **excellent with millions** — same algorithm.

### 4. Finite Distinctions in Practice
- English grammatical sentences are infinite in theory, 2 MB photos number 256^2,000,000.
- In practice humans make only a finite number of distinctions.
- **~1 billion examples ≈ closed set** for many tasks.

### 5. Don't Throw Away Rare Events
- "All experimental evidence from the last decade suggests that throwing away rare events is almost always a bad idea."
- Web data = **individually rare but collectively frequent** events.
- Words and word co-occurrences provide the representational machinery — human language already evolved words for the important concepts.

### 6. False Dichotomy
People believe there are only two approaches to NLP:
- **Deep**: hand-coded grammars and ontologies.
- **Statistical**: n-gram counts from corpora.

Reality: three orthogonal problems — **representation choice**, **encoding the model**, **inference**. Many combinations possible (statistical relational learning, max-margin parsing, relational logic over web-scale corpora).

### 7. Semantic Web ≠ Semantic Interpretation
- **Semantic Web** = conventions for software services to interoperate.
- **Semantic interpretation** = making sense of ambiguous natural language.
- Huge shared cognitive/cultural context lets humans disambiguate; software doesn't have that.
- Hurdles for Semantic Web: ontology-writing cost (Project Halo: **$10,000/page** for a chemistry textbook — infeasible for trillions of pages), implementation difficulty, competing factions, inaccuracy/deception.

### 8. Use Web Tables for Semantic Work
- 150M web tables → 2.5M distinct schemata extracted.
- Enables: synonym discovery (`Company` ↔ `Company Name`), disambiguation (`HP` = Helmerich & Payne or Hewlett-Packard depending on column), schema autocomplete (`Make + Model` → suggest `Year`, `Color`, `Mileage`).
- Paşca: 90% precision on top-10 class attributes (Company → `CEO`, `headquarters`, `stock price`).

## Closing Advice

> "**Choose a representation that can use unsupervised learning on unlabeled data**, which is so much more plentiful than labeled data. Represent all the data with a nonparametric model rather than trying to summarize it with a parametric model... See how far you can go by tying together the words that are already there, rather than by inventing new concepts with clusters of words. Now go out and gather some data, and see what it can do."

## Relevance to the Course

- Justifies the **data-first mindset** behind Big Data architectures.
- Motivates **non-parametric / memorization-heavy** stacks (retrieval-augmented, n-gram, embedding lookup) over highly-parametric symbolic pipelines.
- Aligns with [Banko & Brill (2001)](03-banko-brill-2001.md) — the empirical backbone of the claim.
