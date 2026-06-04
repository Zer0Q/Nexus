# Contextual Retrieval

## Definition
Anthropic's technique for preventing semantic isolation of document chunks: before vectorizing individual segments, a fast LLM generates a one-sentence contextual summary of the parent document, which is prepended to each chunk before embedding.

## Why It Matters
Standard chunk-and-embed approaches lose document-level context. A chunk about "Q3 revenue declined 15%" means nothing without knowing which company, fiscal year, and business segment it refers to. Contextual Retrieval injects this global context directly into each chunk's embedding, reducing retrieval failures by 35-49%.

## Key Ideas
- **Formula:** Vectorized Text = Contextual Summary Prefix + Raw Segmented Chunk
- **Two-pass process:** First pass generates document-level summary; second pass prepends it to every chunk before embedding
- **Cost-effective** -- Uses a fast LLM for summary generation, not the primary reasoning model
- **Solves orphaned chunks** -- Chunks that would retrieve incorrectly in isolation now carry enough context for accurate similarity matching

## Tradeoffs
- Adds one LLM call per document during ingestion
- Summary quality affects all chunk embeddings for that document
- Less effective for documents where context is already explicit in each chunk

## Related
- [[concepts/Agentic-GraphRAG]]
- [[concepts/RAG-then-Long-Context]]
- [[concepts/Context-Graph-RAG]]
- [[concepts/RAG]]

## Source
[[summaries/DeepResearch-Semantic-Models-and-Agentic-Architectures]]
