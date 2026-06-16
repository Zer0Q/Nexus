---
type: Concept
title: Query-Time Knowledge Systems
description: Knowledge systems that store raw information and defer AI synthesis until
  a specific query is made. The "thinking" happens on demand, not at ingestion.
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

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
- [[concepts/Write-Time-Knowledge-Systems]]
- [[concepts/Knowledge-Source-of-Truth]]
- [[tools/Compilation-Agent]]

## Source
[[summaries/NateBJones-Karpathy-Wiki-vs-Open-Brain]]
