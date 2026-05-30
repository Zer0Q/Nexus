# Session Recall

## Definition
Full-text search across every conversation you've ever had with Hermes Agent, powered by SQLite FTS5 indexing with LLM summarization. Ask what you discussed three months ago and it retrieves the answer — no other AI agent offers this.

## Why It Matters
Most AI conversations are ephemeral — close the tab and the context is gone. Session recall turns every interaction into a permanent, searchable record. Business ideas, research findings, technical decisions, and creative explorations are all retrievable on demand.

## Key Ideas
- FTS5 full-text search engine indexes all conversation history
- LLM summarization provides context-aware search results
- Tier 2 of the [[Agent-Multi-Tier-Memory]] system
- Unlimited capacity — every session is logged
- Example: "Remind me of every business idea we discussed last month"
- What links you shared 2 months ago, what you were building 3 months ago

## Tradeoffs
- Search costs tokens per query (LLM summarization)
- Large histories may slow search response time
- Requires active search — not always-in-context like Tier 1 memory

## Related
- [[Agent-Multi-Tier-Memory]] -- Tier 2: session search layer
- [[Session-Recall]] -- the search technology behind it
- [[Compounding-Knowledge-Context]] -- recall enables compounding across sessions

## Source
[[IBuzovskyi-Hermes-Agent-Complete-Guide]]
