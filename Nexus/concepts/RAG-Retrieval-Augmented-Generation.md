# RAG Retrieval-Augmented Generation

## Definition
A technique where an AI model answers questions by first searching a specific document collection for relevant content, then generating its response grounded in that retrieved content rather than relying solely on its training data.

## Why It Matters
RAG turns a general-purpose AI into a domain-specific assistant that answers from your actual notes. Without RAG, the AI guesses from training data; with RAG, it answers from your vault.

## Key Ideas
- Three-step pipeline: (1) embed all documents, (2) find semantically similar documents to the query, (3) pass those documents as context to the model
- Quality depends on embedding accuracy and retrieval relevance
- Can run entirely on-device (Mini-RAG + Smart Connections)
- Solves the hallucination problem by grounding answers in real content
- Works for any document collection: notes, papers, client briefs, codebases

## Tradeoffs
- Retrieval may miss relevant documents if embeddings are poor
- Context window limits how many documents can be passed to the model
- Adds latency compared to direct model queries

## Related
- [[concepts/Embedding-Based-Vault-Search]]
- [[concepts/Context-Aware-AI-Research]]
- [[concepts/On-Device-Knowledge-Base]]

## Source
[[summaries/KanikaBK-Offline-AI-Workflow]]
