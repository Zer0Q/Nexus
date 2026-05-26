# Write-Time Knowledge Systems

## Definition
Knowledge systems where AI synthesizes, organizes, and cross-references information at ingestion time, producing pre-compiled artifacts ready for immediate consumption.

## Why It Matters
Eliminates query-time latency -- answers are pre-computed and browsable without additional compute. Ideal for solo researchers building persistent knowledge bases.

## Key Ideas
- AI acts as editor at write time, not query time
- Produces persistent artifacts (wiki pages, notes, markdown files)
- Answers are "baked in" -- no re-derivation needed per query
- Enables human browsing and serendipitous discovery
- Andrej Karpathy's personal wiki is the canonical example

## Tradeoffs
- Risk of [[Editorial-Drift]] and [[Error-Compounding]]
- Hard to update when source information changes
- Doesn't scale well for teams or high-volume structured data

## Related
- [[Query-Time-Knowledge-Systems]]
- [[Structured-Source-Notes]]
- [[AI-as-Maintainer]]

## Source
[[NateBJones-Karpathy-Wiki-vs-Open-Brain]]
