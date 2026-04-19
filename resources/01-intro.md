# 01 — Introduction (Enterprise Architectures for Big Data)

**Source:** `1 Intro.pdf` (42 slides, Prof. Dr. Roland M. Mueller)

## Enterprise Architecture (EA)

- **Architecture** = "fundamental organization of a system embodied in its components, their relationships to each other, and to the environment, and the principle guiding its design and evolution" (IEEE 1471-2000).
- *"Structure with a vision."*
- **EA** = architecture at the level of an entire organization. Bridges **business and IT**.
- Avoids **siloed view** — information, product, process, application, technical architectures all connected.

### EA Hierarchy (top → bottom)
1. Mission / Strategy
2. Business Process
3. Data
4. Application
5. Technology

Course focuses on **Data + Application + Technology** layers.

## What is Big Data?

Two definitions:

**1. Technology-based:** more and different data than easily handled by traditional RDBMS / data warehouses.

**2. V's-based:**
- **Volume** — amount (GB → PB → ZB). Sources: transactional, social, sensors/M2M.
- **Velocity** — rate of arrival. Streams: logs, social, RFID, sensors, smart metering. Daily / seasonal / event-triggered peaks.
- **Variety** — types: structured (RDBMS), semi-structured (XML/JSON), unstructured (text, video, audio).
- **Veracity** — trustworthiness.
- **Value** — ability to turn data into value. *Most important V.*

## "Unreasonable Effectiveness of Data"

- Paraphrased from Wigner's "Unreasonable Effectiveness of Mathematics in the Natural Sciences."
- In ML, **more data often matters more than smarter algorithms**.
- Backed by [Banko & Brill (2001)](03-banko-brill-2001.md) and [Halevy/Norvig/Pereira (2009)](04-halevy-unreasonable-effectiveness.md) — both in this resource set.

## Course Scope

### Learning Goals
- Designing data-intensive applications.
- Scalability & efficiency of algorithms and data structures.
- Role of Big Data in EA.
- Use-case development for Big Data projects.
- Big Data tech: **Hadoop, Spark, NoSQL, GPU / Deep Learning, Stream Processing, APIs & Cloud, Blockchain**.
- Software engineering: Linux CLI, Git, programming paradigms, **Docker**, DevOps / CD.
- Ethics of Big Data and AI.

### Tech Environment
Options for running workloads:
1. Local Docker (≥8 GB RAM)
2. Cloud (Google $300 / Azure $100 / AWS $100 / IBM Bluemix / MapR)
3. HWR cluster

### Assessment
- **Big Data Team Project (66%)** — Report 36%, Presentation 30%
- **Oral Exam (24%)**
- **Assignments (10%)**

### Project Rules
- Teams of max 3.
- International + business/IT diversity required.
- Working language: English.
- Must use at least one course technology.
- Data does **not** have to be big.
- All members write code; track responsibilities and time.

## Example Student Projects Mentioned
- BVG geo-data visualization.
- Tech-trend identification via APIs + Stream Processing.
- Stream visualization.
- NLP with Amazon Echo.
- Smart Mirror on Raspberry Pi.
- Image segmentation of welding videos (Deep Learning).
- Image recognition for German glass producer (Deep Learning).
