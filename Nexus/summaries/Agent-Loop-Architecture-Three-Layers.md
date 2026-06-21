---
type: article
title: "The Agent Loop Architecture"
description: "The three-layer architecture for durable agent loops: loop, skill, and orchestrator. Why durability is foundational, not optional."
resource: "https://x.com/djfarrelly/status/2067677007140278630"
timestamp: 2026-06-18
tags:
  - agent-loop
  - durable-execution
  - orchestration
  - architecture
  - agent-harness
---

## Synthesis

The article argues that the AI discourse has converged on loops as a core primitive, but nobody is asking the right question: "what runs the loop?" The answer is a three-layer architecture:

**Layer 1: The Loop.** A loop is cron plus a decision-maker. It runs on a schedule, evaluates state, and decides what to do next. The LLM is the decision-maker inside the loop, not the loop itself. Each step is checkpointed so recovery means resuming from the last successful step, not restarting.

**Layer 2: The Skill.** A skill is not a prompt. It's a durable workflow — multi-step, retryable, composable, independently deployable. Each new skill the system learns makes every loop more capable. Skills compound.

**Layer 3: The Orchestrator.** The engine that runs everything: schedules crons, executes steps, manages retries, enforces concurrency limits, stores run history, and hot-deploys new functions without disrupting running ones. This layer is supposed to be invisible but is foundational.

The key insight: agents should be reframed as "loops + skills + orchestration," not "LLM + tools." The LMM + tools are inside the loops. The orchestration enables the architecture.

Durability requirements include: independent step retry, sub-agent lifecycle management, guaranteed event delivery, post-hoc observability, hot-deploy without downtime, and concurrency control. "Just run it in a container" gets uptime but not correctness — a container that restarts after a crash brings the process back but every in-flight loop starts over.

The article also describes an agent that builds its own skills: the agent writes functions, registers them with the orchestration engine, and they start running immediately. A review loop evaluates skill performance and iterates. The agent is ephemeral; its output is durable.

Satya Nadella's thesis: the moat isn't the model — it's the loop. Human capital and token capital compound together. If skills die on process restart, the compounding resets to zero.

## Key Insights

- Step-level checkpointing is not just a correctness feature; it's a money saver. If a skill retries from the beginning, you burn tokens unnecessarily
- The agent that builds its own skills is not magic — it's a sidecar pattern where the agent has access to the orchestration SDK as a tool
- Observability isn't a nice-to-have when the thing that wrote the code isn't a human; it's the trust layer
- The compounding loop requires durability: every durable skill the agent deploys is institutional knowledge encoded as executable infrastructure

## Questions

- How does this three-layer architecture map to existing frameworks like [[Agent-Loop]] and [[Hermes-Agent]]?
- What are the trade-offs between Inngest's durable execution and other orchestration approaches?
- Can the "agent writes its own skills" pattern be safely generalized, or does it need strict guardrails?
