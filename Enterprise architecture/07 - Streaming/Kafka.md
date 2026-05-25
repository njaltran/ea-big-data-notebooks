---
aliases: ["Kafka", "Apache Kafka"]
---

Durable, distributed, partitioned, replayable LOG. The substrate for modern streaming.

```
producer ───► [partition 0: ☐☐☐☐☐☐☐☐☐☐☐...] ──┐
producer ───► [partition 1: ☐☐☐☐☐☐☐...........] ─┼── consumer group A (each partition --> one consumer)
producer ───► [partition 2: ☐☐☐☐☐...............] ─┘
                                                  └── consumer group B (independent offsets)

every box = an event, append only, retained for N days
```

## The Log abstraction
Kreps 2013, *[The Log: What Every Software Engineer Should Know About Real Time Data's Unifying Abstraction](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying)*.

> One append only log is the universal data structure for distributed systems.

Replaces: queues, ETL, change data capture, pub/sub, replication.

## Properties
- **Append only** - new events at the tail
- **Partitioned** - per topic, hashed by key, parallel scale
- **Replicated** - across brokers, leader + followers
- **Persistent** - retain N days or until log size cap
- **Replayable** - reset consumer offset to reprocess

## Why this matters
- new consumer? Read from offset 0, get full history.
- bug in your pipeline? Fix it, reset offset, replay.
- new use case 6 months later? Subscribe, no re-ingestion.

## Use cases
- event sourcing
- microservice communication
- change data capture (Debezium --> Kafka)
- [[Stream Processing]] input
- [[OpenTelemetry]] transport

! Without Kafka (or Kinesis, Pulsar, etc) you can't do [[Kappa Architecture]]. The log IS the architecture.

## Visual - topic + partitions

```mermaid
flowchart LR
    P1[Producer A] --> T
    P2[Producer B] --> T
    subgraph T["Topic: orders"]
        direction TB
        PA["partition 0<br/>[0][1][2][3][4][5]..."]
        PB["partition 1<br/>[0][1][2][3]..."]
        PC["partition 2<br/>[0][1][2][3][4][5][6][7]..."]
    end
    PA --> CA["Consumer A1<br/>offset=4"]
    PB --> CB["Consumer A2<br/>offset=2"]
    PC --> CC["Consumer A3<br/>offset=7"]
    PA --> DA["Consumer B1<br/>offset=1<br/>(independent group)"]
```

## Visual - replay = time travel

```mermaid
sequenceDiagram
    participant L as Log
    participant C as Consumer (today)
    participant C2 as Consumer (new, tomorrow)
    L->>C: events 1..1000 (live)
    Note over C2: bug found, fix logic
    C2->>L: seek(offset=0)
    L-->>C2: replay 1..1000
    C2->>C2: rebuild state from scratch
    L->>C2: continue from 1001
```

## Learn more
- [Apache Kafka](https://kafka.apache.org/) - official
- Kreps 2013: [The Log essay](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying) - the most important read
- [Confluent Developer - Kafka 101](https://developer.confluent.io/learn-kafka/) - free video course, Tim Berglund
- Kreps et al 2011: [Kafka original paper](https://notes.stephenholiday.com/Kafka.pdf)

