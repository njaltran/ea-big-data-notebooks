---
aliases: ["In-memory", "In memory"]
---

Keep working set in RAM instead of disk.

! 10x to 1,000x faster than disk depending on workload.

## Why
- disk seeks = 5-10ms. RAM access = 100ns. ~10⁵ difference.
- analytical queries touch many rows, few columns - RAM keeps the column hot.
- transactional workloads also benefit if dataset fits.

## Examples
- **SAP HANA** - in memory + [[Columnar Database]] platform.
- **QlikView** - in memory BI on the desktop. Smaller scale but same principle.
- **Redis, Memcached** - cache layer for OLTP.
- **Spark** - keeps RDDs in memory across stages (vs MapReduce that hits disk between).

## Cost catch
RAM is 100x more expensive per GB than disk. So:
- only the hot working set lives in RAM
- cold data stays on disk / object store
- compression matters (columnar wins again)

! [[Columnar Database]] + [[In-memory]] is the modern OLAP stack. See [[MPP]] for how it scales sideways.

## Visual - the speed ladder

```mermaid
flowchart TB
    L1["L1 cache<br/>~1 ns"]:::fast
    L2["L2 cache<br/>~3 ns"]:::fast
    L3["L3 cache<br/>~12 ns"]:::fast
    RAM["RAM<br/>~100 ns"]:::med
    SSD["SSD<br/>~100 us<br/>= 100,000 ns"]:::slow
    HDD["HDD<br/>~10 ms<br/>= 10,000,000 ns"]:::vslow
    L1 --> L2 --> L3 --> RAM --> SSD --> HDD
    classDef fast fill:#84e184
    classDef med fill:#f4d35e
    classDef slow fill:#f4a261
    classDef vslow fill:#e57373
```
Each step down = 10x to 100x slower.

```mermaid
xychart-beta
    title "Throughput rough comparison"
    x-axis "tier" ["L1", "L2", "RAM", "SSD", "HDD"]
    y-axis "relative speed" 0 --> 100
    bar [100, 30, 10, 0.1, 0.001]
```

## Learn more
- [Latency Numbers Every Programmer Should Know](https://gist.github.com/jboner/2841832)
- [SAP HANA overview](https://www.sap.com/products/technology-platform/hana.html)
- [Apache Spark - RDDs in memory](https://spark.apache.org/docs/latest/rdd-programming-guide.html)

