# Editorial Drift

## Definition
The gradual degradation of knowledge quality in AI-maintained systems where each synthesis pass introduces small inaccuracies that compound over successive updates.

## Why It Matters
AI summaries inevitably drop nuances, reframe context, or introduce subtle errors. In write-time systems, these errors become permanent artifacts that future queries inherit.

## Key Ideas
- Each AI edit is a lossy compression of the original
- Nuance loss is cumulative across rewrites
- Errors become "facts" when baked into wiki pages
- Hard to detect without comparing against source material
- Mitigated by keeping a [[concepts/Knowledge-Source-of-Truth]] separate from synthesized views

## Tradeoffs
- Preventing drift requires storing raw sources (more storage)
- Periodic re-sync adds operational overhead

## Related
- [[concepts/Error-Compounding]]
- [[concepts/Write-Time-Knowledge-Systems]]
- [[concepts/Knowledge-Source-of-Truth]]

## Source
[[source-notes/NateBJones-Karpathy-Wiki-vs-Open-Brain]]
