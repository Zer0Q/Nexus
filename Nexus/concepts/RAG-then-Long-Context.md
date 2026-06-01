# RAG-then-Long-Context

## Definition
Two-stage retrieval pipeline: first phase uses traditional RAG to filter the 50-200 most relevant documents from millions of records; second phase loads this refined set directly into an extended context window (100K+ tokens) for exhaustive step-by-step reasoning.

## Why It Matters
Combines the cost-efficiency of selective retrieval with the deep reasoning capabilities of long-context models. Instead of sending a few fragments to the LLM, it sends dozens of complete documents, enabling cross-document synthesis and complex analytical reasoning at minimal compute cost.

## Key Ideas
- **Phase 1 -- RAG filtering:** Fast, cheap retrieval narrows millions of documents to 50-200 relevant ones
- **Phase 2 -- Long-context reasoning:** Full documents loaded into 100K+ token window for comprehensive analysis
- **Cost advantage** -- Far cheaper than sending entire corpus; far more context than traditional RAG's 3-5 chunks
- **Traceability** -- Answers include logical justification grounded in the full documents, not isolated fragments

## Tradeoffs
- Requires models with large context windows (100K+ tokens)
- Phase 2 latency scales with document count
- Diminishing returns if Phase 1 retrieval quality is poor (garbage in, garbage out)

## Related
- [[concepts/Agentic-GraphRAG]]
- [[concepts/Contextual-Retrieval]]
- [[concepts/Context-Graph-RAG]]
- [[glossary/RAG]]

## Source
[[source-notes/DeepResearch-Semantic-Models-and-Agentic-Architectures]]
