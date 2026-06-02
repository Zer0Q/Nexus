# AgentQL

## Definition
A semantic query language built specifically for AI agents to interact with web pages. Instead of brittle CSS selectors that break on every redesign, you describe what you want semantically and the query finds it regardless of underlying markup changes.

## Why It Matters
CSS selectors are fragile -- a site redesign breaks every scraper that depends on them. AgentQL uses semantic descriptions that survive structural changes, making web scraping more resilient and maintainable.

## Key Ideas
- Query language for AI agents, not developers
- Semantic descriptions instead of CSS selectors
- Survives site redesigns -- query adapts to markup changes
- Built for production agent workflows
- Alternative to XPath, CSS selectors, and DOM traversal

## Tradeoffs
- Semantic resolution accuracy -- may not always find the right element
- Performance overhead vs direct selector matching
- Learning curve for writing effective semantic queries

## Related
- [[tools/Browser-Use]]
- [[tools/Stagehand]]
- [[concepts/Tool-Selection-Hierarchy]]

## Source
[[source-notes/DamiDefi-20-GitHub-Scraping-Repos]]
