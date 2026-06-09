# Agent Loop

## Definition
A recurring, self-verifying agent process. Something kicks it off, the agent does work, checks its own work against a signal, then either runs again or stops and calls a human. You write the structure once, and from then on the machine is the thing prompting the model.

## Why It Matters
Manual prompting is a linear bottleneck — one human, one turn at a time. Loops automate the feedback cycle: trigger, act, verify, repeat. They only pay off when the work has two properties: it repeats, and the agent can check whether it got the answer right.

## Anatomy
- **Trigger** — schedule, event, or condition that starts the loop
- **Context** — what the agent needs to know (skills, project knowledge, prior state)
- **Tools** — what the agent can do (filesystem, git, APIs, MCP connectors)
- **Verification** — how the agent checks its own work (tests, benchmarks, proof gates)
- **Repeat condition** — when to continue iterating
- **Stop rule** — when to halt and call a human

## Key Ideas
- Skip verification and you don't have a loop — you have a token bonfire with a calendar invite
- A mature loop turns repeated steps into scripts rather than calling the model for the same operation repeatedly
- Loops compound through memory: every failure becomes future context (CLAUDE.md, AGENTS.md)
- The annoyance signal: when you're annoyed doing repetitive observation for an agent, it's ready to be looped

## Tradeoffs
- Only effective for repetitive, verifiable work (PR maintenance, flaky tests, profiling)
- One-off, exploratory, or hard-to-verify work is the wrong fit
- Requires real guardrails before running unattended: auto-verification and sane stop conditions

## Related
- [[concepts/Loop-Engineering]]
- [[concepts/Evaluator-Optimizer-Workflow]]
- [[concepts/Agent-Reflection-Self-Correction]]
- [[concepts/Durable-Agent-Execution]]
- [[concepts/Goal-Driven-Agents]]

## Source
[[summaries/AddyOsmani-Loop-Engineering]], [[summaries/Tonbis-What-Actually-Are-Loops]]
