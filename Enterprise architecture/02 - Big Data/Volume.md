---
aliases: ["Volume"]
---

How much data. Bytes ladder:

```
KB → MB → GB → TB → PB → EB → ZB → YB
                ▲        ▲
              big      huge
        (warehouse)  (web scale)
```

## Sources
- transactional databases (orders, clicks, payments)
- social media streams
- M2M / sensor / IoT (often the biggest by raw byte count)

## Architectural response
- partition + parallelise --> [[MPP]]
- store cheap, compute later --> [[HDFS]], object storage
- columnar compression --> [[Columnar Database]]

! Volume alone is the easiest V. Throw money at storage. [[Velocity]] + [[Variety]] are harder.

## Visual

```mermaid
flowchart LR
    KB[KB] --> MB[MB] --> GB[GB] --> TB[TB] --> PB[PB] --> EB[EB] --> ZB[ZB]
    GB -.warehouse era.-> GB
    PB -.big data era.-> PB
    ZB -.web scale.-> ZB
```

```mermaid
pie title where bytes come from
    "M2M / IoT sensors" : 45
    "Social media" : 25
    "Transactional" : 20
    "Scientific" : 10
```

## Learn more
- IDC Data Age 2025 report - global datasphere projections
- [Latency Numbers Every Programmer Should Know](https://gist.github.com/jboner/2841832)

