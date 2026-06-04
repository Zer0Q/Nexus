# ByteRover

## Definition
CLI tool that bridges Obsidian vaults with AI coding agents by treating vault markdown files as native knowledge sources. Indexes vaults as Context Trees and links them as read-only sources to 22+ coding agents.

## Why It Matters
Solves the knowledge gap between personal notes and coding agents. When you ask your agent to refactor a module, it can now reference your architecture decisions and design trade-offs documented in your vault.

## Key Ideas
- Source feature (v3.2.0): link vaults as read-only knowledge sources
- Federated search: vault knowledge + project code in single query
- Curate once, search from every project
- Zero friction: no Obsidian running, no plugins, no REST APIs, no API keys
- Context-tree is a snapshot -- re-curate when notes change significantly
- Install: curl -fsSL https://byterover.dev/install.sh | sh

## Tradeoffs
- Context-tree snapshot needs re-curating after major note changes
- Search quality depends on curation quality
- May add latency to agent queries with large vaults

## Related
- [[concepts/Federated-Knowledge-Search]]
- [[concepts/Markdown-as-Universal-Format]]
- [[concepts/Read-Only-Vault-Safety]]

## Source
[[summaries/KevinNguyen-ByteRover-Obsidian]]
