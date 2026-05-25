---
aliases: ["CDN", "Content Delivery Network", "Edge Cache"]
---

A network of servers spread around the world that cache your static files near your users. Cuts latency, cuts origin load.

```
              CDN edges (close to users)
   ┌─────┐                 ┌────┐ Frankfurt
   │ User│ ──► get img ──► │CDN │ ──► (HIT) returns image, ~10ms
   │  A  │                 └────┘
   └─────┘                    │ (MISS first time)
                              ▼
                         ┌────────┐
                         │ Origin │ in Virginia, ~120ms RTT
                         │ server │
                         └────────┘
   ┌─────┐                 ┌────┐ Singapore
   │ User│ ──► get img ──► │CDN │ ──► (HIT) returns image, ~5ms
   │  B  │                 └────┘
   └─────┘
```

## Why
- **lower latency**: edge is geographically near the user (see [[Latency Numbers]]: CA -> NL = 150 ms).
- **lower origin load**: edge absorbs reads, origin handles writes + cache fills.
- **higher availability**: origin can be down while edges serve cached copies.
- **cheaper bandwidth**: CDNs negotiate peering deals you can't.

## What gets cached
- "static assets": images, videos, CSS, JS, static HTML.
- modern CDNs also cache dynamic responses with smart rules (key by cookie, query, geo).
- not for: user-specific dashboards, anything personalised by default.

## Providers
- Cloudflare
- Akamai (the OG, 1998)
- Amazon CloudFront
- Google Cloud CDN
- Fastly
- BunnyCDN

## Cache miss flow
```mermaid
sequenceDiagram
    participant U as User A
    participant E as CDN Edge (Frankfurt)
    participant O as Origin Server
    U->>E: GET image.jpg
    E->>E: cache lookup
    Note over E: MISS
    E->>O: GET image.jpg
    O-->>E: image.jpg + Cache-Control: max-age=86400
    E->>E: store in edge cache
    E-->>U: image.jpg (slow first time, ~150ms)
    Note over U,O: ── 5 minutes later ──
    U->>E: GET image.jpg
    E-->>U: image.jpg (HIT, ~10ms)
```

## Cache controls (origin tells the CDN)
- `Cache-Control: public, max-age=86400` -> cache 1 day everywhere
- `Cache-Control: private` -> don't cache at shared CDN, only browser
- `Cache-Control: no-store` -> never cache
- `ETag: "abc123"` -> versioned response, browser revalidates

## Cache busting
- when the asset changes, change the URL.
- common trick: `style.abc123.css` where the hash = file content.
- new content = new URL = no stale cache.

## Visual

```mermaid
flowchart TB
    subgraph users["Users worldwide"]
        UA[User A - Berlin]
        UB[User B - Singapore]
        UC[User C - SF]
    end
    subgraph edges["CDN edge locations"]
        EF[Edge Frankfurt]
        ES[Edge Singapore]
        EW[Edge San Jose]
    end
    O[(Origin Server<br/>Virginia)]
    UA --> EF
    UB --> ES
    UC --> EW
    EF -.MISS only.-> O
    ES -.MISS only.-> O
    EW -.MISS only.-> O
```

Related: [[Cache]], [[HTTP]], [[Load Balancer]], [[Latency Numbers]], [[DNS and URL]].

## Learn more
- [How CDNs work (Cloudflare)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)
- [Akamai history](https://en.wikipedia.org/wiki/Akamai_Technologies)
- [HTTP caching (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
