---
type: Concept
title: RRF (Reciprocal Rank Fusion)
description: '- Combines lexical precision (BM25) with semantic recall (dense embeddings)
  - Model-agnostic: works with any ranking-based retriever - Common embedding model...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# RRF (Reciprocal Rank Fusion)

Mathematical formula for unifying results from multiple retrieval engines (e.g., BM25 lexical + dense vector embeddings) by combining their ranked lists:

RRF(d) = sum(1 / (k + rank_i(d)))

Where rank_i(d) is document d's position in retriever i's results, and k is a smoothing constant (typically k=60). Achieves 15-25% improvement in information retrieval rates over single-engine approaches.

- Combines lexical precision (BM25) with semantic recall (dense embeddings)
- Model-agnostic: works with any ranking-based retriever
- Common embedding models used with RRF: Voyage-3, text-embedding-3-large, BGE-M3, Cohere Embed v4

See also: [[concepts/Contextual-Retrieval]], [[concepts/Agentic-GraphRAG]]
