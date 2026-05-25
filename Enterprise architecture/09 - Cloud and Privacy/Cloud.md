---
aliases: ["Cloud"]
---

Rent compute + storage from someone else's data centre.

## Three flavours

| | What | Examples |
|---|------|----------|
| **SaaS** | full app, vendor hosts everything | Cognos cloud, Business Objects, Salesforce, Tableau Online |
| **PaaS** | platform, you build the app | Heroku, App Engine, Azure App Service |
| **IaaS** | raw VMs + storage | EC2, GCE, DigitalOcean |

```
       you manage:
       
SaaS:      ░░░░░░░░░░  nothing (just data)
PaaS:      ████░░░░░░  your code
IaaS:      ███████░░░  OS + above
On-prem:   ██████████  everything
```

## Big Data cloud notables
- **Amazon Redshift** (2013) - warehouse in the cloud, $1k/TB/year (then)
- **BigQuery** - serverless warehouse on Google
- **Snowflake** - cross cloud warehouse SaaS
- **Databricks** - Spark + lakehouse SaaS

## Zynga case ([[Watson 2014]])
Launches games on EC2 for unknown demand. Once demand stabilises, moves to in-house "Z Cloud." Started 80/20 EC2 vs Z Cloud, flipped to 20/80.

! Cloud is the ELASTIC layer. On prem is the COMMITTED layer. Hybrid is the norm.

## Cost gotcha
Cloud beats on prem until your usage is large + stable. Then on prem beats cloud. Watch your monthly bill, not just the hourly rate.

## Visual - the responsibility stack

```mermaid
flowchart TB
    subgraph SAAS["SaaS"]
        S1[App]:::vendor
        S2[Runtime]:::vendor
        S3[OS]:::vendor
        S4[Hardware]:::vendor
        S5[Data]:::you
    end
    subgraph PAAS["PaaS"]
        P1[App]:::you
        P2[Runtime]:::vendor
        P3[OS]:::vendor
        P4[Hardware]:::vendor
        P5[Data]:::you
    end
    subgraph IAAS["IaaS"]
        I1[App]:::you
        I2[Runtime]:::you
        I3[OS]:::you
        I4[Hardware]:::vendor
        I5[Data]:::you
    end
    subgraph OP["On-prem"]
        O1[App]:::you
        O2[Runtime]:::you
        O3[OS]:::you
        O4[Hardware]:::you
        O5[Data]:::you
    end
    classDef vendor fill:#84c7d0
    classDef you fill:#f4d35e
```
Blue = vendor manages. Yellow = you manage.

## Visual - cost vs scale

```mermaid
xychart-beta
    title "When cloud stops being cheaper"
    x-axis "scale + stability" [1, 2, 3, 4, 5, 6, 7, 8]
    y-axis "$ per unit" 0 --> 100
    line "Cloud" [80, 65, 50, 40, 35, 35, 38, 42]
    line "On-prem" [200, 100, 60, 40, 30, 22, 18, 15]
```
Lines cross. After crossover, on-prem is cheaper.

## Learn more
- [Cloud vs on-prem TCO comparison (a16z)](https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/)
- [AWS / GCP / Azure free tiers](https://aws.amazon.com/free/)
- [The serverless tradeoffs (Hellerstein 2019)](https://arxiv.org/abs/1812.03651)

