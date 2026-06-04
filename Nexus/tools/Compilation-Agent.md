# Compilation Agent

## Definition
A specialized AI agent that reads structured data and generates synthesized, human-readable views (wiki pages, summaries, reports) without permanently storing them as source of truth.

## Why It Matters
Enables wiki-like browsing experience while keeping the underlying data structured and reliable. The agent is the bridge between raw data and human-readable knowledge.

## Key Ideas
- Reads from structured source, writes to temporary view layer
- Views are ephemeral -- regenerated on demand or scheduled intervals
- Prevents [[concepts/Error-Compounding]] because source data stays immutable
- Can be scheduled (e.g., nightly wiki refresh) or on-demand
- Different from write-time systems: output is a view, not the source

## Tradeoffs
- Adds latency between data update and view availability
- Requires defining sync intervals and regeneration triggers

## Related
- [[concepts/Graph-Knowledge-Layer]]
- [[concepts/Query-Time-Knowledge-Systems]]
- [[tools/AI-as-Maintainer]]

## Source
[[summaries/NateBJones-Karpathy-Wiki-vs-Open-Brain]]
