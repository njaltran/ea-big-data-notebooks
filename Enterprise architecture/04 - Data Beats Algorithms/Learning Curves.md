---
aliases: ["Learning Curves"]
---

Accuracy as a function of training set size. The killer chart of [[Banko and Brill]].

## The shape
On log scale: STRAIGHT LINE. No knee, no asymptote. All four learners keep improving from 10⁶ to 10⁹ words.

```
accuracy ▲
         │              ╭──── still climbing
         │           ╭──╯
         │        ╭──╯     ╲
         │     ╭──╯         ╲ all 4 learners,
         │  ╭──╯              same slope-ish
         │──╯
         └─────────────────────►  log(n)
```

## Implications
1. **The ceiling is unknown.** Maybe 10¹⁰ asymptotes. Maybe 10¹². Nobody has the corpus.
2. **Algorithm choice matters less than data size.** Different learners converge to the same line.
3. **Investment shifts.** Spend on data acquisition + pipelines, not on a slightly cleverer model.

! This is the most architecturally consequential chart in the course. It justifies every Big Data tech below.

## Counterpoint
Modern deep learning + scaling laws (Kaplan, Hoffmann/Chinchilla) refined this: there ARE asymptotes when compute and data are balanced wrong. But the directional claim survives: more data ↑, accuracy ↑, mostly.

See [[Memorization vs Generalization]] for why this happens. See [[Long Tail]] for what fills in as n grows.

## Visual

```mermaid
xychart-beta
    title "Accuracy vs log(training size) - all learners still climbing"
    x-axis "log10(words)" [6, 7, 8, 9]
    y-axis "accuracy" 0.75 --> 1.0
    line "Memory-based" [0.82, 0.88, 0.93, 0.97]
    line "Naive Bayes" [0.79, 0.86, 0.91, 0.95]
    line "Perceptron" [0.81, 0.87, 0.92, 0.96]
    line "Winnow" [0.80, 0.86, 0.91, 0.95]
```

```mermaid
flowchart LR
    A[more data] --> B[accuracy climbs]
    B --> C{asymptote?}
    C -->|"Banko + Brill: not at 1B"| D[buy more data]
    C -->|"Kaplan/Chinchilla: only when undertrained"| E[balance data + compute]
    D --> F[stack design]
    E --> F
```

## Learn more
- [Banko + Brill 2001 PDF](https://aclanthology.org/P01-1005.pdf)
- Kaplan 2020: [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)
- Chinchilla 2022: [Training Compute-Optimal LLMs](https://arxiv.org/abs/2203.15556)
- Sutton: [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)

