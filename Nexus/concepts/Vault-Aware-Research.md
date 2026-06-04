# Vault-Aware Research

## Definition
An AI agent that reads your accumulated knowledge vault before answering research questions, synthesizing across your existing notes, thesis documents, signal logs, and source materials rather than relying solely on its training data.

## Why It Matters
A standard AI session is smart but context-blind. It cannot flag contradictions in your notes, surface forgotten connections, or build on your previous thinking. Vault-aware research turns the AI into a partner that knows your domain and your position on it.

## Key Ideas
- Agent reads vault files relevant to the query before generating an answer
- Synthesizes across multiple note types (thesis, signal log, source notes)
- Flags contradictions between current beliefs and saved notes
- Tells you what primary source would resolve uncertainty if the answer is not in your notes
- The SOUL.md instructs the agent to read before answering

## Tradeoffs
- Token cost scales with vault size and query complexity
- Quality depends on how well-structured your notes are
- Agent may over-weight your notes vs. its own knowledge without careful prompting

## Related
- [[concepts/Context-Aware-AI-Research]] -- the broader concept this implements
- [[concepts/SOUL-MD-Configuration]] -- what instructs the agent to read first
- [[concepts/Live-Vault-Memory]] -- the memory model enabling this
- [[concepts/Primary-Source-Over-Secondary]] -- the research philosophy behind it

## Source
[[summaries/DamiDefi-Hermes-Obsidian-Vault-Integration]]
