# Knowledge Source of Truth

## Definition
A single, reliable data layer that stores raw information independently of any AI-generated synthesis. All derived views, summaries, and wiki pages reference back to this source.

## Why It Matters
Prevents [[Editorial-Drift]] and [[Error-Compounding]] by ensuring synthesized knowledge can always be verified against original data. The foundation of hybrid knowledge architectures.

## Key Ideas
- Raw data stored separately from AI-generated views
- Structured format (SQL, graph DB, tagged files)
- Enables verification: any synthesized claim can be traced to source
- Multiple agents can safely read from the same source
- Immutable or append-only to prevent silent corruption

## Tradeoffs
- Requires more storage than write-only systems
- Adds a verification step to the workflow

## Related
- [[Graph-Knowledge-Layer]]
- [[Structured-Source-Notes]]
- [[Compilation-Agent]]

## Source
[[NateBJones-Karpathy-Wiki-vs-Open-Brain]]
