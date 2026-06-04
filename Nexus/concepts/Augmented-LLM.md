# Augmented LLM

## Definition
Foundational building block of agentic systems: an LLM enhanced with retrieval, tools, and memory. The LLM actively uses these capabilities -- generating search queries, selecting tools, and deciding what to retain.

## Why It Matters
Every agentic system, from simple workflows to autonomous agents, starts with an augmented LLM. The quality of augmentations determines the ceiling of agent performance.

## Key Ideas
- Retrieval: access to external knowledge (RAG, vector search, document stores)
- Tools: functions for external actions (APIs, databases, code execution)
- Memory: persistent state across interactions (conversation history, learned preferences)
- LLM actively generates queries, selects tools, manages memory
- MCP (Model Context Protocol) standardizes tool integration
- Success depends on: (1) tailoring augmentations to use case, (2) well-documented tool interfaces

## Tradeoffs
- Each augmentation adds latency and cost
- Poor tool documentation leads to incorrect tool usage
- Too many tools overwhelms the LLM's selection capability

## Related
- [[concepts/Agentic-System-Architecture]]
- [[concepts/Agent-Tool-Use]]

## Source
[[summaries/Anthropic-Building-Effective-AI-Agents]]
