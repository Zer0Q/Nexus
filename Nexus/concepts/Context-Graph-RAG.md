---
type: Concept
title: Context-Graph RAG
description: 'GraphRAG extended with operational governance metadata directly on graph
  nodes: data lineage, source quality indicators, content ownership, and corporate
  acc...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Context-Graph RAG

## Definition
GraphRAG extended with operational governance metadata directly on graph nodes: data lineage, source quality indicators, content ownership, and corporate access/security policies.

## Why It Matters
Standard GraphRAG retrieves relational context but lacks auditability. Context-Graph RAG adds the governance layer required for production enterprise systems -- every retrieved fact carries its provenance, quality score, and access permissions. Reduces logical hallucinations by 40% and achieves 81%+ precision on complex audit tasks.

## Key Ideas
- **Metadata on nodes** -- Each graph node carries: lineage (origin), quality score, owner, access policy
- **Governance-aware retrieval** -- Query results are filtered by user permissions and quality thresholds before reaching the LLM
- **Audit trail** -- Every answer can trace back through the graph to original sources with quality metrics
- **Complements Three-Layer Infrastructure** -- Governance metadata lives at Layer 3 (Knowledge Graph) while access rules live at Layer 2 (Ontologies)

## Tradeoffs
- Metadata maintenance overhead (who updates quality scores, ownership changes?)
- Larger node payloads increase graph storage and query latency
- Requires organizational processes to populate governance fields

## Related
- [[concepts/Agentic-GraphRAG]]
- [[concepts/Three-Layer-Semantic-Infrastructure]]
- [[concepts/Contextual-Retrieval]]
- [[concepts/RAG]]

## Source
[[summaries/DeepResearch-Semantic-Models-and-Agentic-Architectures]]
