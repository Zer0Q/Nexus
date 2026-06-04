# LLM Wiki Pattern

## Definition
A pattern where an LLM incrementally builds and maintains a persistent wiki of interlinked markdown files from raw source documents, rather than retrieving from raw documents at query time (RAG). Knowledge is compiled once and kept current.

## Why It Matters
Eliminates the bookkeeping bottleneck that causes humans to abandon wikis. The LLM handles cross-referencing, updating summaries, flagging contradictions, and maintaining consistency across dozens of pages with near-zero marginal cost.

## Key Ideas
- Three layers: raw sources (immutable), wiki (LLM-maintained), schema (instructions)
- Three operations: ingest (compile new sources), query (ask + file answers back), lint (health checks)
- Index file catalogs all pages; log file tracks chronological changes
- At moderate scale (~100 sources, hundreds of pages), index files outperform RAG infrastructure
- Related to Vannevar Bush's Memex (1945): private, curated, associative links
- The wiki is a compounding artifact -- cross-refs, contradictions, synthesis accumulate

## Tradeoffs
- LLM synthesis errors can compound if filed back without review
- Schema quality determines wiki quality -- vague schema produces vague output
- At very large scale (1000+ pages), index files may need vector search augmentation

## Related
- [[concepts/Write-Time-Knowledge-Systems]]
- [[tools/Compilation-Agent]]
- [[concepts/Knowledge-Source-of-Truth]]
- [[concepts/Anti-Graveyard-Capture]]

## Source
[[summaries/Karpathy-LLM-Wiki-Pattern]]
