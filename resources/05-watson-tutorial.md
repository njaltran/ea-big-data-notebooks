# 05 — Watson (2014): Big Data Analytics — Concepts, Technologies, and Applications

**Author:** Hugh J. Watson (University of Georgia)
**Publication:** *Communications of the AIS*, Vol. 34, Article 65 (April 2014)
**Source:** `Watson_2014_Tutorial.pdf`

## Framing

Big Data = **fourth generation of decision-support data management**:

1. **1970s** — DSS (application-centric).
2. **1990s** — Enterprise data warehouse (data-centric).
3. **~2000** — Real-time data warehousing.
4. **Today** — Big Data (high volume, velocity, variety).

Storing data creates **no business value** — only analyzing and acting on it does. Some add **Value** as the 4th V.

## Three Types of Analytics

| Type | Question | Analogy | Examples |
|------|----------|---------|----------|
| **Descriptive** | What happened? | Rear-view mirror | Reports, OLAP, dashboards, data viz |
| **Predictive** | What will happen? | Windshield | Regression, ML, neural nets, "golden path" analysis |
| **Prescriptive** | What should we do? | GPS | Optimization, revenue management, math programming |

Most organizations mature descriptive → predictive → prescriptive.

## Illustrative Cases

- **Starbucks** — monitored blogs/Twitter/forums during new coffee launch; found the product was seen as *too expensive* within hours, dropped the price, negative sentiment disappeared by end of day.
- **Chevron** — each Gulf-of-Mexico miss costs ~$100M. Analyzing **50 TB of seismic data** improved odds from 1-in-5 to ~1-in-3.
- **U.S. Xpress** — trucks stream **900+ sensor fields**; saved millions in fuel by distinguishing avoidable idle time from traffic idle.
- **Target** — pregnancy prediction model (25 variables: unscented lotions, supplements, scent-free soap, cotton balls, hand sanitizer, washcloths). Public-relations backlash → Target now mixes pregnancy coupons with unrelated offers.

## Seven Requirements for Success

1. **Clear business need** — business-driven, not tech-driven. Start narrow, not "build it and they will come."
2. **Strong committed sponsorship** — often CIO early, shifts to CMO/CFO/CEO as it matures.
3. **Alignment between business and analytics strategy** — ideally inseparable (Amazon, Overstock, "We're a BI company" — Patrick Byrne).
4. **Fact-based decision-making culture** — "At Harrah's, three things get you fired: stealing, sexual harassment, and not making decisions based on the facts."
5. **Strong data infrastructure** — enables days-long application dev.
6. **Right analytical tools** (see below).
7. **Skilled people** — business users → analysts (BI + business) → **data scientists**. Demand: McKinsey forecast 140K–190K deep-analytics shortage + 1.5M managers in US alone.

## Platforms and Technologies

### Storage / Compute

- **Scale-out MPP architecture** — hundreds/thousands of commodity servers, shared-memory caches, data partitioned + parallel processing. Foundation of Big Data platforms.
- **In-memory** — RAM-based, 10× to 1,000× faster than disk (e.g. SAP HANA on the platform; QlikView on desktop).
- **Solid-state disks** — reduce I/O bottleneck.
- **Columnar databases** — rows ↔ columns flip; faster for analytical queries (few columns across many rows), better compression. Pioneered by Sybase IQ (mid-90s); used by Vertica, ParAccel, Teradata.
- **In-database analytics** — move analytics to the data (SAS partnered with Oracle/Teradata). Eliminates data movement, enables full-warehouse modeling.

### Architectures

- **Data warehouses** — "squeaky clean" integrated structured data. Workhorse for descriptive analytics. Vendors: IBM, Oracle, SAP, Microsoft, Teradata.
- **Data mart appliances** — integrated hw+sw+storage "box" (Netezza coined "appliance"; now IBM PureData). Used standalone, as offload, or as sandboxes.
- **Analytical sandboxes** — real (separate appliance) or virtual (warehouse partition) for modelers.
- **Streaming / CEP** — Tibco StreamBase, BusinessEvents. Ingest real-time data, correlate with historical, apply rules, trigger actions. Use cases: auto stock trading, credit-card fraud, supply chain, equipment monitoring. **Streaming = single source; CEP = multiple sources.**

### Cloud

- **SaaS** — vendor provides hardware + app (Cognos, Business Objects, MicroStrategy, SAS cloud).
- **PaaS** — vendor provides platform, you build the app (Oracle Cloud, Azure, Google App Engine).
- **IaaS** — raw compute + storage (Amazon EC2, Rackspace, Google Compute Engine).
- **Amazon RedShift** (2013) — data warehouse in the cloud, $1,000/TB/year.
- **Zynga** — launches games on Amazon EC2 for unknown demand, moves to in-house Z Cloud once demand stabilizes. Mix flipped from 80/20 EC2 to 20/80 Z Cloud.

### NoSQL

- Non-relational, stores any structure (XML, text, audio, video, image) via key-value pairs.
- Examples: Apache Cassandra, MongoDB, Apache Couchbase.
- Distributed scale-out, commodity hardware, open-source. Weaker security and maturity than RDBMS.

### Hadoop / MapReduce

- Origin: Doug Cutting + Mike Cafarella working on **Nutch**; Google published GFS (2003) and MapReduce (2004) papers; Cutting joined Yahoo!, created **Hadoop** (named after his son's stuffed elephant).
- Yahoo ran 42,000 servers on Hadoop.
- **HDFS** — distributed file system; no data model, stores any file.
- **MapReduce** — splits data, map programs (Java / Python / C / R / Perl) process splits in parallel, shuffle/sort, reduce aggregates.
- Runs **batch only** — limits real-time applicability.
- Fault tolerant: data replicated on 3 servers, failed nodes auto-replaced. Weakness: **NameNode** single point of failure.
- Ecosystem: **Pig** (high-level MR), **HBase** (distributed columnar store), **Hive** (SQL-like HiveQL), **Mahout** (ML library).
- Distros: **Cloudera, Hortonworks, MapR** wrap Apache parts with integration + support.
- Three use patterns:
  1. Online archive (cheap, expandable).
  2. Source system feeding a data warehouse.
  3. Analytics engine itself.

### Which Platform?

No formula. Consider: **volume, velocity, variety, applications, users, batch vs. real-time, cost**. Integrated use across multiple platforms is common.

## Integrated Analytics Architecture (Eckerson)

- **Top-down BI** — casual users, reports/dashboards/viz over structured warehouse data.
- **Bottom-up BI** — power users (analysts, data scientists) against Hadoop, streaming/CEP, free-standing sandboxes, external data.
- Warehouse + Hadoop **co-exist** — neither replaces the other.
- **SQL / SQL-like (Hive)** is the integration glue across platforms.

## People Continuum

| Role | Consumer or Producer | Skill emphasis |
|------|---------------------|----------------|
| Business user | Consumer | Domain knowledge, use tools |
| BI analyst | Producer (IT-side) | Enterprise data + tools |
| Business analyst | Producer (business-side) | Business-unit domain |
| **Data scientist** | Producer | RDBMS + Hadoop + code (Java/Python/R) + SQL/Hive + stats/regression/SNA + communication. "Sexiest job of the 21st century" (Davenport & Patil 2012). Often PhDs. |

## Privacy

Three kinds of invasion (Clemons et al. 2014):
1. **Uninvited intrusion** — spam, pop-ups (most salient, least harmful).
2. **Fraud / identity theft** — most serious.
3. **Personal profiling for commercial advantage** — data blending by Google, Facebook, Yahoo! Public awareness is low; concern rises sharply with understanding.

Few regulations govern Internet firms. Author argues for "consistent, reasonable, transparent, easy to understand" privacy laws.

## Key Takeaway for EA

Big Data capability is **federated by nature** — warehouse, Hadoop, appliances, sandboxes, streaming/CEP, cloud services, NoSQL all coexist. Architecture job is to integrate them (data governance, BI/analytics centers of excellence, SQL/Hive as lingua franca) while matching workloads to the platforms where they run cheapest and fastest.
