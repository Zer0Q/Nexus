---
type: concept
title: "Durable-Execution"
description: "An execution model where each step is checkpointed, each decision is persisted, and recovery means resuming from the last successful step rather than restarting from scratch."
resource: "https://x.com/djfarrelly/status/2067677007140278630"
timestamp: 2026-06-18
tags:
  - durable-execution
  - agent-infrastructure
  - checkpointing
  - fault-tolerance
---

## Definition

Durable execution is an execution model for agent loops where every step is independently checkpointed. When a process crashes or restarts, recovery means resuming from the last successful step, not re-executing all previous steps.

## Why It Matters

Without durable execution, a process restart causes:
- Re-execution of all previous steps (wasted compute, especially LLM calls)
- Duplicate actions (sent messages, spawned sub-agents)
- Loss of decision state (which LLM calls made which decisions)
- Reset of the compounding loop (every durable skill investment is lost)

## Requirements

- Independent step retry (retry step 3 of 5, not steps 1-2)
- Sub-agent lifecycle management
- Guaranteed event delivery
- Post-hoc observability (step-level traces)
- Hot-deploy without downtime
- Concurrency control

## Related Concepts

- [[Agent-Loop-Architecture]]
- [[Step-Checkpointing]]
- [[Durable-Skills]]
- [[Compounding-Learning-Loops]]
