# Federated Knowledge Search

## Definition
Searching across multiple knowledge sources (vault notes + project code) in a single query. The same curated vault can be linked to every project, enabling search from everywhere without duplicating knowledge.

## Why It Matters
Solves the problem of knowledge siloed in your vault being invisible to your coding agents. When you ask your agent to refactor a module, it can now reference your architecture decisions and design trade-offs documented in your vault.

## Key Ideas
- ByteRover source feature links vaults as read-only knowledge sources
- Search results tagged with source prefix ([MyVault]) for provenance
- Curate once, search from every project
- 22+ coding agents supported (Claude Code, Cursor, Windsurf, etc.)
- Zero configuration: no Obsidian running, no plugins, no APIs
- Read-only safety: agents learn from notes but never modify them

## Tradeoffs
- Context-tree is a snapshot -- needs re-curating when notes change
- Search quality depends on curation quality
- May add latency to agent queries if vault is large

## Related
- [[concepts/Markdown-as-Universal-Format]]
- [[concepts/Read-Only-Vault-Safety]]
- [[concepts/Context-Tree-Indexing]]

## Source
[[source-notes/KevinNguyen-ByteRover-Obsidian]]
