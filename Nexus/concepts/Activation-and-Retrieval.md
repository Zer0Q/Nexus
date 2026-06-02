# Activation and Retrieval

## Definition
The translation layer that delivers canonical context to the right human or agent, in the right interface, at the right moment. Because different systems consume context through different mechanisms (MCP, APIs, SQL, vector retrieval, graph traversal), the layer translates one canonical context into many local dialects.

## Why It Matters
Context is only valuable if it reaches its consumer. Tying the context layer to one interface or standard assumes a single winner, which is unlikely. The winning architecture translates rather than forces convergence.

## Key Ideas
- Consumers: copilots, search, analytics, workflows, code editors, agent frameworks
- No single winner -- MCP, APIs, SQL, vectors, graphs will coexist
- Translation: even within Google ecosystem, Looker wants LookML while Gemini wants skill files
- Short-term reality: translation between canonical context and local dialects
- The layer cannot assume any single standard is always the answer

## Tradeoffs
- Canonical representation vs local optimization
- Translation overhead vs interface diversity
- Real-time retrieval vs cached/preprocessed context

## Related
- [[concepts/Enterprise-Context-Layer]]
- [[concepts/Context-Substrate]]
- [[concepts/Context-Efficiency-Frontier]]

## Source
[[source-notes/Prukalpa-Enterprise-Context-Layer]]
