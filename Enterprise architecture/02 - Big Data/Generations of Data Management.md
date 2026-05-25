---
aliases: ["Generations of Data Management"]
---

Watson 2014's framing. Four generations of decision support data infrastructure.

| Gen | Era | Approach | Centred on |
|-----|-----|----------|------------|
| 1 | 1970s | DSS | the application |
| 2 | 1990s | Enterprise [[Data Warehouse]] | the data |
| 3 | ~2000 | Real time warehousing | the latency |
| 4 | Today | [[Big Data]] | the [[5 Vs]] |

! Each gen does not replace the prior. They coexist. Most orgs run all four at once.

## What changed each gen
- **Gen 1** - one app, one DB, custom reports. No integration.
- **Gen 2** - star schemas, ETL, [[Descriptive Analytics]]. "Single source of truth."
- **Gen 3** - trickle ETL, micro batches. Dashboards stop being a day behind.
- **Gen 4** - [[NoSQL]], [[Hadoop]], [[Stream Processing]], cloud. Schema on read. Petabytes.

The course argument: gen 4 is where the team project lives. Pick the stack that matches your dominant Vs (see [[Big Data]]).

## Visual

```mermaid
timeline
    title Four generations of decision support data
    1970s : DSS (application-centric)
    1990s : Enterprise Data Warehouse (data-centric)
    2000s : Real-time data warehousing
    2010s+ : Big Data (5 Vs)
```

```mermaid
flowchart LR
    G1[Gen 1: DSS<br/>per-app DB] --> G2[Gen 2: EDW<br/>star schemas]
    G2 --> G3[Gen 3: Real-time DWH<br/>trickle ETL]
    G3 --> G4[Gen 4: Big Data<br/>NoSQL + Hadoop + Stream]
    G1 -.coexist.-> G4
    G2 -.coexist.-> G4
    G3 -.coexist.-> G4
```
Each gen layered on top, none retired.

## Learn more
- Kimball + Ross, *The Data Warehouse Toolkit*
- Inmon, *Building the Data Warehouse*
- [[Watson 2014]] - the original framing

