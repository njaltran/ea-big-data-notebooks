---
aliases: ["News Intelligence Platform"]
---

Team project. Global news intelligence platform.

## Pitch
Real time intelligence system that:
- collects news from multiple countries
- classifies (topic, sentiment, framing)
- visualises differences in how countries report the SAME global events

Goal: break away from mindless scrolling. Live dashboard that surfaces narrative divergence.

## Starting countries
- Germany
- USA
- Italy
- Myanmar
- Kazakhstan

! The Myanmar + Kazakhstan picks are the interesting ones. They're the [[Long Tail]] of global news coverage. Capturing them is the differentiation vs an "EU + US" project.

## Ingestion
Two methods:
- **Free APIs** via [dlt](https://dlthub.com)
- **Web scraping + RSS** via BeautifulSoup

## Expected schema (post processing)
```
source
country_target
title
summary
url
published_at
extracted_at
```

## Scale estimate
- 6 week project window
- 126k - 294k records
- 2-5 KB text per record
- ~300 MB - 1.5 GB raw text
- plus embedding vectors

That's [[Volume]] = small. [[Velocity]] = medium (steady ingestion). [[Variety]] = high (every country, every outlet has its own format).

## Course tech used
- [[Stream Processing]] (ingestion) - the required course technology
- [[NoSQL]] or warehouse for storage (DuckDB / S3 likely)
- ML / embeddings for classification
- [[Descriptive Analytics]] dashboard

## Open questions
- topic modelling: BERTopic? LDA?
- embedding model for cross language similarity?
- how to compare narratives quantitatively (sentiment alone is not enough)?
- entity linking across languages?

See [[Talking points may 8]] for the original pitch document.

## Visual - architecture sketch

```mermaid
flowchart TD
    subgraph SRC[Sources]
        A1[NewsAPI]
        A2[GDELT]
        A3[RSS feeds]
        A4[Web scraping]
    end
    SRC --> ING[dlt + BeautifulSoup<br/>ingestion layer]
    ING --> L[(Raw lake<br/>DuckDB / S3)]
    L --> CL[Cleaning + dedup]
    CL --> EMB[Embedding model<br/>multilingual]
    EMB --> VS[(Vector store)]
    CL --> TOP[Topic modeling<br/>BERTopic / LDA]
    VS --> DASH[marimo dashboard]
    TOP --> DASH
```

## Visual - countries + narratives

```mermaid
flowchart LR
    EV[Global event: e.g. climate summit] --> DE[Germany framing]
    EV --> US[USA framing]
    EV --> IT[Italy framing]
    EV --> MM[Myanmar framing]
    EV --> KZ[Kazakhstan framing]
    DE --> COMP[Compare]
    US --> COMP
    IT --> COMP
    MM --> COMP
    KZ --> COMP
    COMP --> DASH[Live divergence dashboard]
```

## Visual - 6-week timeline

```mermaid
gantt
    title News Intelligence Platform - 6 weeks
    dateFormat YYYY-MM-DD
    section Ingest
    NewsAPI + RSS pipelines :a1, 2026-05-25, 7d
    GDELT + scraping        :a2, after a1, 7d
    section Process
    Cleaning + dedup        :b1, after a1, 7d
    Embeddings + topic      :b2, after b1, 10d
    section Serve
    Dashboard prototype     :c1, after b1, 7d
    Polish + writeup        :c2, after c1, 7d
```

## Learn more
- [dlt docs](https://dlthub.com/docs)
- [GDELT Project](https://www.gdeltproject.org/)
- [BERTopic](https://maartengr.github.io/BERTopic/) - the cool topic modelling library
- [marimo](https://marimo.io/) - reactive notebook for the dashboard
- [Sentence Transformers](https://www.sbert.net/) - multilingual embeddings

