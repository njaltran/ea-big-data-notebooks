---
aliases: ["MapReduce", "Mapreduce"]
---

Distributed batch compute pattern. Map out, process, bring together, reduce.

! When you bring together you need to do sum, which is always O(n).

```
[input file]
     │ split
     ▼
┌────┬────┬────┬────┐
│ S1 │ S2 │ S3 │ S4 │
└──┬─┴──┬─┴──┬─┴──┬─┘
   │    │    │    │
   ▼    ▼    ▼    ▼
 map  map  map  map      ◄── parallel, per split
   │    │    │    │
   └────┴─┬──┴────┘
          ▼ shuffle + sort (by key)
   ┌──────┬──────┐
   │  R1  │  R2  │       ◄── reducers per key group
   └──┬───┴──┬───┘
      ▼      ▼
   [output partitions]
```

## Origin
Dean + Ghemawat, Google, 2004. *Simplified Data Processing on Large Clusters*. See [[Hadoop]] for how it spread.

## Programming model
1. **Map** - take input, emit (key, value) pairs.
2. **Shuffle + sort** - framework groups by key.
3. **Reduce** - take (key, list of values), emit (key, aggregated value).

Word count canonical example:
```
map("doc.txt") -> [("the", 1), ("cat", 1), ("the", 1), ...]
shuffle       -> [("the", [1, 1]), ("cat", [1])]
reduce        -> [("the", 2), ("cat", 1)]
```

## Why it worked
- programmer writes only map + reduce
- framework handles: parallelism, fault tolerance, data locality, scheduling, shuffle
- runs on commodity hardware

## Why it died
- batch only, hours per job
- lots of disk I/O between stages
- awkward for iterative algorithms (ML, graph)

## Successors
- **Spark** - same shape, in memory, supports iteration, lazy DAG
- **Flink** - stream native, true low latency
- **Beam** - portable model on top of multiple runners

Related: [[HDFS]], [[Hive]], [[Pig]], [[HBase]].

## Visual - word count flow

```mermaid
flowchart LR
    I["doc.txt<br/>the cat sat<br/>on the mat"] --> S1[split 1]
    I --> S2[split 2]
    S1 -->|map| M1["('the',1)<br/>('cat',1)<br/>('sat',1)"]
    S2 -->|map| M2["('on',1)<br/>('the',1)<br/>('mat',1)"]
    M1 --> SH(("shuffle<br/>by key"))
    M2 --> SH
    SH --> R1["reduce 'the'<br/>= 2"]
    SH --> R2["reduce 'cat'<br/>= 1"]
    SH --> R3["reduce 'mat'<br/>= 1"]
```

## Visual - timing

```mermaid
sequenceDiagram
    participant C as Client
    participant JT as JobTracker
    participant M as Mapper(s)
    participant R as Reducer(s)
    participant H as HDFS
    C->>JT: submit job
    JT->>M: assign split + map fn
    M->>H: read split
    M->>M: emit (k,v)
    M-->>R: shuffle + sort by key
    R->>R: aggregate values per key
    R->>H: write output
    JT-->>C: done
```

## Learn more
- Dean + Ghemawat 2004: [MapReduce paper](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/)
- Visualisation: [MapReduce step-by-step on developer.ibm.com](https://www.ibm.com/topics/mapreduce)
- Successor papers: Zaharia 2012 ([RDDs/Spark](https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/zaharia))

