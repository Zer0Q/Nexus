---
type: Concept
title: Durable Agent Execution
description: Agent execution model that preserves progress across transient failures,
  restarts, and long-running workflows. Enables agents to survive API rate limits,
  net...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Durable Agent Execution

## Definition
Agent execution model that preserves progress across transient failures, restarts, and long-running workflows. Enables agents to survive API rate limits, network errors, and application crashes without losing state.

## Why It Matters
Production agents run multi-step workflows that can take minutes or hours. Without durability, a single failure loses all progress. Durable execution treats agent state as persistent, not ephemeral.

## Key Ideas
- Agent state serialized between steps (tool calls, LLM responses, intermediate results)
- Checkpointing: save state after each step, resume from last checkpoint on failure
- Human-in-the-loop: agent pauses, human acts, agent resumes with full context
- Long-running workflows: async tasks, scheduled retries, timeout handling
- Production-grade reliability: idempotent operations, retry with backoff

## Tradeoffs
- Storage overhead for checkpoints
- Complexity in state management and versioning
- Not needed for simple single-turn agents

## Related
- [[tools/PydanticAI]]
- [[concepts/Agent-Graph-Support]]

## Source
[[summaries/Pydantic-Team-Pydantic-AI-Overview]]
