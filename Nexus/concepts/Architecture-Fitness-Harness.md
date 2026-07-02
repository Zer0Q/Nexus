# Architecture Fitness Harness

## Definition
An Architecture Fitness Harness is a set of guides and sensors that encode architecture characteristics and test whether agent-generated changes preserve them.

## Why It Matters
Coding agents can satisfy local tasks while eroding module boundaries, performance constraints, observability standards, or API design. Architecture fitness harnesses make those cross-cutting constraints visible to both the agent and the reviewer.

## Key Ideas
- Feedforward guides describe architecture decisions, boundaries, and required qualities.
- Feedback sensors include fitness functions, structural tests, dependency rules, performance checks, and architecture review agents.
- The harness should run early enough that architecture drift is caught before merge.
- Architecture fitness is easier when the codebase has clear modules and strong tooling.

## Related
- [[concepts/Harness-Engineering]]
- [[concepts/Fitness-Function-Driven-Development]]
- [[concepts/Harnessability]]
- [[concepts/Agent-Guardrails]]

## Source
[[summaries/BirgittaBockeler-Harness-Engineering-Coding-Agents]]
