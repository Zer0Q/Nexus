# Error Compounding

## Definition
A failure mode in AI-maintained knowledge systems where an initial error in one note propagates through cross-references, causing cascading inaccuracies across the knowledge base.

## Why It Matters
In write-time wiki systems, a single incorrect synthesis can infect dozens of related pages through automated cross-linking, making the entire knowledge base unreliable.

## Key Ideas
- One bad edit becomes many bad edits via cross-references
- Errors compound exponentially in highly interconnected wikis
- Detection requires comparing against raw source data
- Structured data layers prevent propagation by keeping source separate from view

## Tradeoffs
- Isolation prevents compounding but reduces automation
- Manual review catches errors but doesn't scale

## Related
- [[concepts/Editorial-Drift]]
- [[concepts/Knowledge-Source-of-Truth]]
- [[architectures/Graph-Knowledge-Layer]]

## Source
[[source-notes/NateBJones-Karpathy-Wiki-vs-Open-Brain]]
