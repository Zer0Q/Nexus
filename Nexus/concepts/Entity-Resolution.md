---
type: Concept
title: Entity Resolution
description: The process of identifying, deduplicating, and merging equivalent entities
  extracted from unstructured text into canonical representations within a knowledge...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Entity Resolution

## Definition
The process of identifying, deduplicating, and merging equivalent entities extracted from unstructured text into canonical representations within a knowledge graph, using semantic similarity, hybrid search, and LLM-based disambiguation.

## Why It Matters
Raw LLM extraction produces fragmented graphs: "Wind Turbine A-1" and "Wind Generator A1" appear as separate nodes. Without entity resolution, graphs become unusable for production retrieval -- high topological dispersion, redundant isolated nodes, and broken relationship chains.

## Key Ideas
- **Vector embeddings** -- All unique nodes embedded (e.g., S-BERT) for semantic similarity computation
- **k-means clustering** -- Entities partitioned into homogeneous clusters (max 128 per partition)
- **Hybrid candidate search** -- For each entity, retrieve k most similar candidates combining BM25 lexical match + cosine similarity of embeddings (default k=16)
- **LLM disambiguation** -- Structured prompt asks high-capability model to identify true duplicates, evaluating complex morphological variations (verb tenses, plurals, abbreviations, acronyms)
- **Canonical representative selection** -- LLM picks one entity per confirmed duplicate group that best captures shared meaning; all aliases redirect to this unified node
- **Recursive until clean** -- Process repeats until no inconsistencies remain in the partition

## Tradeoffs
- LLM disambiguation adds cost per cluster
- k-means may split semantically related entities across clusters
- Canonical selection is subjective; different LLMs may choose different representatives

## Related
- [[concepts/Ontology-Enforcement]]
- [[concepts/Agentic-GraphRAG]]
- [[tools/KGGen]]
- [[concepts/Three-Layer-Semantic-Infrastructure]]

## Source
[[summaries/DeepResearch-Semantic-Models-and-Agentic-Architectures]]
