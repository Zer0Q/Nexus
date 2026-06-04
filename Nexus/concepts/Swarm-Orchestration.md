# Swarm Orchestration

## Definition
The coordination of 300 concurrent specialized sub-agents across a single task, each handling a domain, coordinated by a meta-agent. The result is parallel execution at a scale that compresses weeks of work into hours. Kimi K2.6 is the only open-source model capable of this.

## Why It Matters
No other open-source model can coordinate 300 concurrent specialized sub-agents. The swarm approach decomposes a large task into parallel workstreams, each handled by a specialist agent, with a meta-agent coordinating dependencies and synthesizing outputs.

## Key Ideas
- Meta-agent decomposes the task into parallel workstreams
- Each workstream has a named specialist agent with exact scope and output format
- Dependency chains define which agents must complete before others can start
- Independent workstreams execute simultaneously
- Meta-agent synthesizes all outputs into a final deliverable once complete
- 300 agents across 4000 steps (Kimi K2.6 ceiling)

## Tradeoffs
- Complex dependency chains can create bottlenecks
- Inter-agent conflicts require meta-agent arbitration
- Token costs scale with the number of agents and steps
- Debugging a swarm failure is harder than debugging a single agent

## Related
- [[tools/Kimi-K26-Model]] -- the model enabling swarm orchestration
- [[concepts/Long-Horizon-Coding]] -- swarms enable long-horizon tasks
- [[concepts/Multi-Agent-Org-Chart]] -- similar concept for agent organization
- [[concepts/Five-Layer-AI-Stack]] -- the coding layer uses swarm orchestration

## Source
[[summaries/Damidefi-Five-Tool-AI-Stack-Full-Build]]
