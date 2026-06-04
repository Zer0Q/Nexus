# Smart Connections Plugin

## Definition
An Obsidian plugin that creates local embeddings of every note in your vault and provides a chat interface for asking questions across your entire knowledge base, powered by a local or cloud LLM.

## Why It Matters
Smart Connections turns Obsidian from a note-taking app into a conversational knowledge base. You can ask "What did I learn about X last month?" and get answers grounded in your actual notes.

## Key Ideas
- Creates embeddings of every note automatically
- Semantic search finds relevant notes even without keyword matches
- Connects to local LLM via `http://localhost:1234/v1` (or cloud API)
- Answers are grounded in your vault content, not general training data
- Core component of [[concepts/RAG-Retrieval-Augmented-Generation]] in Obsidian

## Configuration
- API provider: Local
- API base URL: `http://localhost:1234/v1`
- Model: name of active LM Studio model

## Related
- [[concepts/Embedding-Based-Vault-Search]]
- [[concepts/RAG-Retrieval-Augmented-Generation]]
- [[tools/LM-Studio]]

## Source
[[summaries/KanikaBK-Offline-AI-Workflow]]
