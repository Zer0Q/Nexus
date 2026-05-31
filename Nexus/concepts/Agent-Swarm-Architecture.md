# Agent Swarm Architecture

## Definition
Massively parallel agent execution where hundreds of agents work concurrently on decomposed subtasks, coordinated by a central orchestrator that handles task distribution and result aggregation.

## Why It Matters
Single agents are sequential bottlenecks. Swarms parallelize work across hundreds of isolated agents, reducing wall-clock time from hours to minutes for large tasks.

## Key Ideas
- Decompose large task into independent subtasks
- Spawn N agents, each handling one subtask
- Each agent runs in isolated context (no shared state)
- Orchestrator collects and aggregates results
- Kimi K26 demonstrates 300-agent swarms

## Tradeoffs
- Task decomposition requires skill
- Not all tasks are parallelizable
- Result aggregation can be complex
- Token cost scales with agent count

## Related
- [[Swarm-Orchestration]]
- [[Single-Threaded-vs-Multi-Agent]]
- [[Multi-Agent-Development]]

## Source
[[rohit4verse-slow-single-threaded-commanding-300-agents-one]]
