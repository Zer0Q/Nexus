# Graph Knowledge Layer

## Definition
A hybrid architecture that stores knowledge as structured data (SQL/graph database) while generating wiki-like synthesized views on demand through a [[Compilation-Agent]].

## Why It Matters
Combines the reliability of structured data with the human-friendly browsability of wikis, without the [[Editorial-Drift]] risk of permanent synthesized artifacts.

## Key Ideas
- Source of truth is raw structured data, not AI-generated pages
- Wiki views are regenerated on demand, not stored permanently
- Graph relationships enable precise queries AND narrative synthesis
- Solves the write-time vs query-time tradeoff
- Open Brain's Graph Plugin is the reference implementation

## Tradeoffs
- More complex architecture to maintain
- Requires both database infrastructure and compilation agents

## Related
- [[Knowledge-Source-of-Truth]]
- [[Compilation-Agent]]
- [[Hybrid-AI-Workflow]]

## Source
[[NateBJones-Karpathy-Wiki-vs-Open-Brain]]
