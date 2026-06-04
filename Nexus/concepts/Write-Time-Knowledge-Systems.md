# Write-Time Knowledge Systems

## Definition
Knowledge systems where information is processed, structured, and indexed at the time of ingestion (write time), rather than at the time of querying. The LLM compiles knowledge once into a persistent artifact that is then kept current.

## Why It Matters
Contrasts with query-time systems (RAG) where the LLM rediscovers knowledge from scratch on every question. Write-time systems accumulate: cross-references are already there, contradictions already flagged, synthesis already done.

## Key Ideas
- RAG: upload files, retrieve chunks at query time, generate answer -- no accumulation
- Write-time: ingest source, extract knowledge, integrate into existing wiki -- compounds
- The LLM does the grunt work: summarizing, cross-referencing, filing, bookkeeping
- Each new source touches 10-15 wiki pages, updating entity pages, revising summaries
- Query becomes reading pre-synthesized pages, not piecing together fragments

## Tradeoffs
- Requires trust in LLM synthesis accuracy
- Initial compilation cost vs. per-query cost
- Stale claims need periodic linting to catch

## Related
- [[concepts/Query-Time-Knowledge-Systems]]
- [[concepts/LLM-Wiki-Pattern]]
- [[tools/Compilation-Agent]]

## Source
[[summaries/Karpathy-LLM-Wiki-Pattern]]
