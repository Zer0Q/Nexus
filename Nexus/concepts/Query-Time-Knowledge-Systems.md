# Query-Time Knowledge Systems

## Definition
Knowledge systems that store raw information and defer AI synthesis until a specific query is made. The "thinking" happens on demand, not at ingestion.

## Why It Matters
Always produces fresh synthesis without stale cached knowledge. Scalable for teams and structured data where write-time compilation would be too expensive.

## Key Ideas
- Raw data stored with tags/metadata, no pre-synthesis
- AI performs synthesis only when queried
- Each query re-derives answers from source truth
- No permanent editorial decisions baked in
- Open Brain architecture is the canonical example

## Tradeoffs
- Higher per-query token cost and latency
- Lacks immediate browsability of a wiki
- Repeated synthesis of same concepts wastes compute

## Related
- [[Write-Time-Knowledge-Systems]]
- [[Knowledge-Source-of-Truth]]
- [[Compilation-Agent]]

## Source
[[NateBJones-Karpathy-Wiki-vs-Open-Brain]]
