---
type: Concept
title: Parallelization Workflow
description: 'Runs multiple LLM calls simultaneously on a task, then aggregates results.
  Two modes: sectioning (independent subtasks) and voting (same task, diverse outputs).'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Parallelization Workflow

## Definition
Runs multiple LLM calls simultaneously on a task, then aggregates results. Two modes: sectioning (independent subtasks) and voting (same task, diverse outputs).

## Why It Matters
Parallel execution reduces latency for complex tasks. Multiple perspectives improve confidence. Separating concerns across LLM calls outperforms single-call handling.

## Key Ideas
- Sectioning: break task into independent subtasks, run in parallel, aggregate
- Voting: run same task with different prompts, require threshold for decision
- Sectioning examples: guardrails + core response, multi-aspect evals
- Voting examples: code vulnerability review, content moderation with thresholds
- LLMs perform better when each consideration gets dedicated attention

## Tradeoffs
- Higher token cost (multiple calls)
- Requires aggregation logic
- Sectioning requires clean task decomposition

## Related
- [[concepts/Agentic-System-Architecture]]
- [[concepts/Routing-Workflow]]

## Source
[[summaries/Anthropic-Building-Effective-AI-Agents]]
