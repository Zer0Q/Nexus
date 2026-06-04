# Specialized Agent Crews

## Definition
A multi-agent architecture where each agent has a specific, well-defined role and clear ownership, rather than one bloated agent trying to do everything. Singular agents with specific tasks are more scalable, easier to debug, route, and trust.

## Why It Matters
One giant agent becomes harder to debug, route, and trust as complexity grows. Specialized crews enable parallel execution, clearer failure modes, and independent scaling of different capabilities.

## Key Ideas
- Clear ownership: each agent owns a specific domain or function
- Research agent as input intelligence layer feeding all other agents
- Supervisor/monitor agent watches intended flow vs actual flow
- Easier to debug: failures are isolated to specific agents
- Easier to scale: add specialized agents without bloating existing ones
- Route decisions are simpler: task -> agent mapping is explicit

## Tradeoffs
- Orchestration overhead -- coordinating multiple agents adds complexity
- Context handoff -- information loss between agent boundaries
- Diminishing returns -- too many specialized agents creates management overhead

## Related
- [[concepts/Agent-Swarm-Architecture]]
- [[concepts/Multi-Agent-Development]]
- [[concepts/Research-First-Architecture]]

## Source
[[summaries/gkisokay-21-Mistakes-Building-AI-Agents]]
