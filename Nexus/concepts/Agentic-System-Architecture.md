---
type: Concept
title: Agentic System Architecture
description: Architectural distinction between workflows (predefined code paths orchestrating
  LLMs and tools) and agents (LLMs dynamically directing their own processes a...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Agentic System Architecture

## Definition
Architectural distinction between workflows (predefined code paths orchestrating LLMs and tools) and agents (LLMs dynamically directing their own processes and tool usage). Both fall under "agentic systems."

## Why It Matters
The workflow vs agent distinction determines predictability, flexibility, and cost. Workflows offer consistency for well-defined tasks; agents offer adaptability for open-ended problems. Choosing the right pattern prevents over-engineering.

## Key Ideas
- Workflows: LLMs + tools orchestrated through predefined code paths
- Agents: LLMs dynamically direct their own process and tool usage
- Start simple: optimize single LLM calls before adding multi-step systems
- Agentic systems trade latency and cost for better task performance
- Frameworks abstract away useful debugging visibility
- Three core principles: simplicity, transparency, careful ACI design

## Tradeoffs
- Agents are more flexible but less predictable and more expensive
- Workflows are predictable but can't handle unexpected inputs
- Adding complexity should be justified by measurable improvement

## Related
- [[concepts/Prompt-Chaining-Workflow]]
- [[concepts/Orchestrator-Workers-Workflow]]
- [[concepts/Augmented-LLM]]

## Source
[[summaries/Anthropic-Building-Effective-AI-Agents]]
