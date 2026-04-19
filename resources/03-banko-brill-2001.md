# 03 — Banko & Brill (2001): Scaling to Very Very Large Corpora for Natural Language Disambiguation

**Authors:** Michele Banko, Eric Brill (Microsoft Research)
**Source:** `Banko and Brill - 2001 - Scaling to very very large corpora for natural lan.pdf`

## Central Claim

**For NLP disambiguation, orders of magnitude more training data beats algorithmic sophistication.** None of the learners tested asymptote in accuracy even at 1 billion words.

## Setup

- **Task:** Confusion-set disambiguation — pick the right word from a commonly confused set. Examples: `{principle, principal}`, `{then, than}`, `{to, two, too}`, `{weather, whether}`.
- **Why this task:** labeled training data is **essentially free** — correct answer is visible in any well-edited text.
- **Corpus:** 1 billion words (3 orders of magnitude larger than prior work), sampled probabilistically from news, scientific abstracts, government transcripts, literature, etc.
- **Test set:** 1 million words of Wall Street Journal (disjoint from training).
- **Learners tested:** Winnow, Perceptron, Naïve Bayes, memory-based.

## Key Findings

### 1. Learning Curves (Figure 1)
- Accuracy vs. training size is **log-linear** even out to 10⁹ words.
- All four learners keep improving — no asymptote observed.
- **Implication:** reconsider the trade-off between investing in better algorithms vs. investing in more data.

### 2. Representation Cost (Figure 2)
- Learned representation size grows **log-linearly** with training data.
- Gains from billion-word data may require compression for space-constrained applications.

### 3. Voting (§4)
- Voting helps on **small** training corpora (reduces bias of corpus + learner).
- Beyond ~1M words, voting offers little gain.
- On the **largest** training sets, voting actually **hurts** accuracy.
- **Complementarity** between classifiers decreases as training size grows:

  | Training size | Complementarity(L1, L2) |
  |---------------|-------------------------|
  | 10⁶           | 0.2612 |
  | 10⁷           | 0.2410 |
  | 10⁸           | 0.1759 |
  | 10⁹           | 0.1612 |

### 4. When Labels Cost Money — Active Learning (§5.1)
- Use **bagging** (10 Naïve Bayes classifiers on bootstrapped samples) to score instance uncertainty via vote entropy.
- Select **M/2 most uncertain + M/2 random** for human annotation (picking only most-uncertain biases sample toward hard instances).
- Result: sample selection **beats sequential sampling**. Larger unlabeled pools → better accuracy for fixed annotation budget.

### 5. Weakly / Unsupervised Learning (§5.2)
- Auto-label instances where all bagged classifiers agree (highest confidence).
- Gain accuracy up to a point, **then accuracy declines** as automatically-labeled data accumulates (sample bias compounds).
- Table showing committee agreement → accuracy:

  | # Classifiers Agreeing | Accuracy |
  |------------------------|----------|
  | 10 | 0.8734 |
  | 9  | 0.6892 |
  | 8  | 0.6286 |
  | 7  | 0.6027 |
  | 6  | 0.5497 |
  | 5  | 0.5000 |

## Takeaways for the Course

1. **Data scale is an architectural decision** — if labels are free, scale the corpus; don't over-invest in algorithmic elegance.
2. **Ensemble / voting tricks have diminishing returns** with scale.
3. **Active + unsupervised learning** can partially close the cost gap when labels are expensive — but unsupervised learning plateaus and then degrades.
4. Authors' proposal: the community should spend more effort on **growing annotated collections** rather than comparing algorithms on tiny corpora.
