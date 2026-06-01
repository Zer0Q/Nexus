# Agent Pipeline Pattern

## Definition
Sequential agent workflow where each agent produces a structured output that becomes the next agent's input, connected by handoff files in a shared pipeline directory.

## Why It Matters
Parallel agents lose context; single agents hit token limits. Pipelines chain specialized agents with clear handoff points, enabling complex multi-stage workflows like plan → code → test → review.

## Key Ideas
- Each agent reads a handoff file, does its work, writes the next handoff file
- Pipeline directory (.pipeline/) stores intermediate artifacts
- Spec → Plan → Code → Test → Review stages
- Different models per stage (Opus for planning/review, Sonnet for coding/testing)
- Orchestrator triggers the chain with one command

## Tradeoffs
- Sequential execution is slower than parallel
- Handoff file format must be strictly maintained
- Failure at any stage breaks the chain

## Related
- [[concepts/Multi-Agent-Development]]
- [[concepts/Multi-Harness-Orchestration]]
- [[concepts/Swarm-Orchestration]]

## Source
[[source-notes/zodchiii-build-agent-team-ships-feature-while-sleep]]
