---
type: Concept
title: Evaluator-Optimizer Workflow
description: Iterative loop where one LLM generates a response and another provides
  evaluation and feedback. Repeats until the output meets quality criteria or a max
  iter...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Evaluator-Optimizer Workflow

## Definition
Iterative loop where one LLM generates a response and another provides evaluation and feedback. Repeats until the output meets quality criteria or a max iteration limit.

## Why It Matters
LLM output quality improves with targeted feedback. When a human can articulate improvements and an LLM can apply them, the evaluator-optimizer pattern automates this refinement loop.

## Key Ideas
- Generator LLM produces initial response
- Evaluator LLM critiques against criteria, provides specific feedback
- Generator incorporates feedback, produces improved version
- Loop continues until quality threshold met or max iterations reached
- Two signs of good fit: (1) human feedback demonstrably improves output, (2) LLM can provide such feedback
- Examples: literary translation, complex search with iterative refinement

## Tradeoffs
- Higher cost and latency (multiple rounds)
- Risk of feedback loops where evaluator and generator reinforce each other's biases
- Requires clear evaluation criteria

## Related
- [[concepts/Agentic-System-Architecture]]
- [[concepts/Prompt-Chaining-Workflow]]

## Source
[[summaries/Anthropic-Building-Effective-AI-Agents]]
