# Agent Memory Ontology

## Definition
Structured memory system using predefined schemas (ontologies) to extract, store, and retrieve agent knowledge — ensuring consistency across sessions and enabling multi-hop reasoning.

## Why It Matters
Flat text retrieval breaks on complex queries. Ontology-based memory structures knowledge into typed entities and relationships, enabling precise retrieval and reasoning chains.

## Key Ideas
- Define schema upfront (Pydantic models)
- Extract entities and relationships from conversations
- Store in structured format (SQLite, JSON)
- Retrieve by querying the ontology, not flat text
- Enables multi-hop: "What did I learn about X that relates to Y?"

## Tradeoffs
- Schema design requires domain knowledge
- Extraction step adds latency
- Schema changes require data migration

## Related
- [[Structured-Agent-Memory]]
- [[Agent-Multi-Tier-Memory]]
- [[Graph-Based-Knowledge-Discovery]]

## Source
[[akshaypachaar-pydantic-fixed-agent-memory]]
