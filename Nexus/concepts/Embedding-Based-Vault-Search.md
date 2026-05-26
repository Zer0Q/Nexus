# Embedding-Based Vault Search

## Definition
Converting every note in a knowledge base into a numerical vector representation (embedding) that captures its semantic meaning, then using vector similarity to find relevant notes when answering questions -- rather than keyword matching.

## Why It Matters
Keyword search fails when the vocabulary differs between query and content. Embedding search finds notes about "neural network optimisation" when you search for "how to make AI training faster" -- even though no words match.

## Key Ideas
- Embeddings are mathematical representations of meaning, not text
- Similarity is measured by vector distance (cosine similarity)
- Works across languages and synonyms automatically
- Computed once per note, then reused for all queries
- Foundation of [[RAG-Retrieval-Augmented-Generation]] systems

## Tradeoffs
- Embedding quality varies by model choice
- Very large vaults (5000+ notes) may slow down search
- Static embeddings do not update when notes change unless re-embedded

## Related
- [[RAG-Retrieval-Augmented-Generation]]
- [[Smart-Connections-Plugin]]
- [[On-Device-Knowledge-Base]]

## Source
[[KanikaBK-Offline-AI-Workflow]]
