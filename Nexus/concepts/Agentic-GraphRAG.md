---
type: Concept
title: Agentic GraphRAG
description: RAG architecture where the knowledge graph serves as the agent's working
  memory, with dynamic switching between dense vector search (direct semantic similari...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Agentic GraphRAG

## Definition
RAG architecture where the knowledge graph serves as the agent's working memory, with dynamic switching between dense vector search (direct semantic similarity) and multi-hop graph traversal (complex relational reasoning) based on query complexity.

## Why It Matters
Traditional RAG retrieves isolated chunks; GraphRAG adds relational context. Agentic GraphRAG goes further by making the graph the agent's operational memory -- the agent reads from it, writes to it, and traverses it autonomously during task execution, enabling multi-step reasoning over interconnected facts.

## Key Ideas
- **Adaptive query routing** -- Simple factual queries use Naive/Advanced RAG (100ms-2s); complex analytical queries route to GraphRAG (1s-5s) or Agentic RAG (2s-10s+)
- **Graph as working memory** -- Agent maintains state, tracks entity relationships, and performs multi-hop reasoning directly on graph structures
- **Hybrid recall-precision flow:** Vector recall (speed) → topological validation on graph (accuracy) → ontological filtering (compliance) → deterministic execution
- **LazyGraphRAG variant** -- Builds graph index lazily, only for subgraphs relevant to the current query, reducing upfront indexing costs
- **Context-Graph RAG extension** -- Injects governance metadata (data lineage, quality indicators, content ownership, access policies) directly onto graph nodes, reducing logical hallucinations by 40%

## Tradeoffs
- Higher token costs ($0.02-$0.15/query for GraphRAG indexing phase)
- Latency tradeoff: 1-10s+ vs 100ms for Naive RAG
- Graph maintenance overhead as corpus grows

## Related
- [[concepts/Contextual-Retrieval]]
- [[concepts/Context-Graph-RAG]]
- [[concepts/RAG-then-Long-Context]]
- [[concepts/RAG]]
- [[concepts/Three-Layer-Semantic-Infrastructure]]

## Source
[[summaries/DeepResearch-Semantic-Models-and-Agentic-Architectures]]
