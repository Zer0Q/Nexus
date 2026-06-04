# Multi-Harness Orchestration

## Definition
Pattern where multiple agent harnesses (each with its own model, tools, and context) are coordinated by a master orchestrator to handle complex multi-step tasks.

## Why It Matters
Single agents hit context limits and capability boundaries. Multi-harness orchestration distributes work across specialized agents, each optimized for a specific subtask, then combines results.

## Key Ideas
- Each harness has independent model selection, tool access, and context window
- Orchestrator routes tasks based on capability matching
- Harnesses can run in parallel for independent subtasks
- Results are aggregated by the orchestrator
- Failure in one harness doesn't cascade to others

## Tradeoffs
- Higher token cost (multiple context windows)
- Latency from coordination overhead
- Complex error handling across harness boundaries
- Debugging is harder with distributed state

## Related
- [[concepts/Multi-Agent-Development]]
- [[concepts/Swarm-Orchestration]]
- [[summaries/AddyOsmani-Agent-Harness-Engineering]]

## Source
[[summaries/zachlloydtweets-introducing-multi-harness-orchestration]]
