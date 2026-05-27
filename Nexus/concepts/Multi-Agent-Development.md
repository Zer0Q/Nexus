# Multi-Agent Development

## Definition
Development approach using specialized AI agents, each with a defined role (Analyst, PM, Architect, Developer, QA), working together through structured handoffs. Each agent operates in a separate context with its own expertise and output artifacts.

## Why It Matters
Simulates the role separation of human Agile teams, reducing the cognitive load on any single agent and improving output quality through specialized focus and structured handoffs.

## Key Ideas
- Role separation: each agent specializes in one phase or concern
- Handoffs: artifacts pass between agents with clear interfaces
- Fresh context per agent prevents cross-contamination
- Reduces LLM drift by constraining each agent's scope

## Tradeoffs
- Coordination overhead between agents
- Context explosion when specs grow large
- Handoff quality determines overall system quality

## Related
- [[BMAD-Method]], [[Agentic-SDLC]], [[Skill-Based-AI-Agents]]

## Source
[[BMAD-Method-Getting-Started]], [[SDD-vs-BMAD-Frameworks-Comparison]]
