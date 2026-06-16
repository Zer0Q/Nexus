---
type: Concept
title: Prompt Chaining Workflow
description: Decomposes a task into sequential LLM calls, where each call processes
  the output of the previous one. Programmatic gates between steps ensure the process
  st...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Prompt Chaining Workflow

## Definition
Decomposes a task into sequential LLM calls, where each call processes the output of the previous one. Programmatic gates between steps ensure the process stays on track.

## Why It Matters
Breaking complex tasks into smaller, focused LLM calls improves accuracy. Each step solves an easier problem, and gates catch errors before they cascade.

## Key Ideas
- Sequential LLM calls: step 1 output -> step 2 input -> step 3 input
- Programmatic gates between steps validate intermediate results
- Trade latency for accuracy by making each LLM call an easier task
- Best for tasks that decompose cleanly into fixed subtasks
- Examples: generate copy -> translate, write outline -> check criteria -> write document

## Tradeoffs
- Higher latency (sequential calls)
- Requires clean task decomposition
- Gates add implementation complexity

## Related
- [[concepts/Agentic-System-Architecture]]
- [[concepts/Evaluator-Optimizer-Workflow]]

## Source
[[summaries/Anthropic-Building-Effective-AI-Agents]]
