# Multi-Agent Org Chart

## Definition
Profile-based multi-agent setup where each Hermes agent instance has a distinct role (Chief of Staff, Head of Research, Head of Content, DevOps Engineer). Each profile runs simultaneously with its own memories, skills, model, and personality, coordinated through a shared messaging channel.

## Why It Matters
Simulates an organizational structure with specialized roles. Instead of one generalist agent doing everything poorly, specialized agents each excel at their domain while a coordinator agent merges outputs into a unified deliverable.

## Key Ideas
- One profile = one agent with isolated memories, skills, and model
- **Chief of Staff profile**: Coordinates all other agents, morning brief at 7am, delegates tasks, reports merged summary
- **Head of Research profile**: Monitors X for niche posts, tracks competitors, sends weekly intelligence brief
- **Head of Content profile**: Drafts posts from research briefs, repurposes articles, maintains content calendar
- Each profile has its own soul.md defining personality and scope
- Run simultaneously, each improving independently
- One morning brief in Telegram, multiple agents working in parallel

## Tradeoffs
- More profiles = more API keys, more bots, more maintenance overhead
- Skills don't transfer between profiles by default
- Memory isolation means agents can't share learned facts
- Coordination complexity grows with agent count

## Related
- [[concepts/Agent-Profiles]] -- the mechanism enabling separate agent instances
- [[concepts/Kanban-Board-Workflow]] -- agents claim tasks from the shared board
- [[concepts/Multi-Agent-Development]] -- broader concept of coordinating multiple agents
- [[concepts/Hermes-Dashboard]] -- Profiles tab for managing the org chart

## Source
[[summaries/IBuzovskyi-Hermes-Agent-Complete-Guide]]
