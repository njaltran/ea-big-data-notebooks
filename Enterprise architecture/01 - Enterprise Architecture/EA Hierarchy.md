---
aliases: ["EA Hierarchy"]
---

Five layers, top down.

```
1. Mission / Strategy       ◄── why does the org exist
2. Business Process         ◄── how does it run
3. Data                     ◄── what does it know     ┐
4. Application              ◄── what tools touch it    │ course focus
5. Technology               ◄── what runs underneath  ┘
```

Each layer constrains the one below. Strategy says "go global" --> processes need follow-the-sun --> data must be replicated globally --> apps must be region aware --> tech needs multi region cloud.

! Higher layers change less often. Tech swaps every few years. Mission lasts decades.

## Course focus
Bottom three: **Data + Application + Technology**. That's where [[Big Data]] forces redesign.

Top two (strategy, business process) come from MBA territory. Touched in `Watson_2014` via the "[[Predictive Analytics|business need]]" requirement.

See [[Enterprise Architecture]] for the framing, [[Big Data]] for the disruption.

## Visual

```mermaid
flowchart TD
    M["1. Mission / Strategy<br/>why exist"]:::top
    P["2. Business Process<br/>how run"]:::top
    D["3. Data<br/>what we know"]:::course
    A["4. Application<br/>tools that touch it"]:::course
    T["5. Technology<br/>what runs underneath"]:::course
    M --> P --> D --> A --> T
    classDef top fill:#f4d35e,stroke:#333
    classDef course fill:#84c7d0,stroke:#333
```
Blue = course focus.

```mermaid
timeline
    title When each layer changes
    Decades : Mission / Strategy
    5-10 years : Business Process
    2-5 years : Data model
    1-3 years : Application
    Months : Technology
```

## Learn more
- Wikipedia: [Enterprise architecture framework](https://en.wikipedia.org/wiki/Enterprise_architecture_framework)
- [TOGAF](https://www.opengroup.org/togaf) - the most-cited EA framework
- [Zachman Framework](https://en.wikipedia.org/wiki/Zachman_Framework)

