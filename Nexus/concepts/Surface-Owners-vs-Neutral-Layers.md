# Surface-Owners vs Neutral Layers

## Definition
A strategic divide in the context layer landscape: surface-owners already own a platform where context is created and add connectors to pull in external data, while neutral layers own no surface and index across everything. The bet differs — surface-owners lead with distribution and native data; neutral layers with breadth and non-competition.

## Surface-Owners
Already own where work happens. They have the data natively and expose it to outside agents via MCP or APIs.

- **Slack** — conversation context
- **Notion** — docs/wiki context
- **Granola** — meeting transcripts
- **Claude / ChatGPT** — assistant interaction context
- **Snowflake / Databricks / Microsoft Fabric** — structured data layer (bucket 3)

Advantage: native data, built-in distribution, work already happens there.
Disadvantage: cannot solve the full bucket alone — the warehouse holds tables, not your Slack or tickets.

## Neutral Layers
Own no surface. They sit on top of multiple sources and build one unified model an agent reads across them. Split further into centralizers (copy data) and federators (query in place).

- **Onyx AI** — open-source, 40+ connectors, hybrid vector + keyword
- **GoSearch** — federated-first, queries data where it lives
- **Glean** — enterprise knowledge graph with entity resolution
- **Hyperspell** — per-user context graph from connected accounts
- **Modern Relay** — context graph in code, runs on your infrastructure
- **Atlan** — metadata layer, models what things mean, not the entities themselves

Advantage: breadth, no competition with existing tools.
Disadvantage: must convince users to connect everything, no native surface to drive adoption.

## Why It Matters
The dichotomy shapes vendor strategy and integration patterns. Surface-owners will always have an advantage in their domain but cannot win outside it. Neutral layers must solve the cold-start problem — getting users to connect enough sources to make the unified layer valuable.

## Key Ideas
- Surface-owners cannot solve the full bucket 3 problem alone
- Neutral layers split into centralizers (Palantir, Stardog) vs federators (Timbr.ai, Denodo)
- MCP is the common protocol surface-owners use to expose context to outside agents

## Related
- [[concepts/Context-Layer-Taxonomy]]
- [[concepts/MCP]]
- [[concepts/Enterprise-Context-Layer]]

## Source
[[summaries/BouBalust-Context-Layer-Landscape]]
