---
type: Concept
title: Agent Logic
description: Software primitives -- knowledge graphs, algorithms, program analysis
  libraries -- that operate at the agentic layer within an agent harness to intentionally...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Agent Logic

## Definition
Software primitives -- knowledge graphs, algorithms, program analysis libraries -- that operate at the agentic layer within an agent harness to intentionally steer the LLM in the direction of the enterprise workflow, reducing the context space and driving more performant, cost-effective outcomes.

## Why It Matters
LLMs alone struggle with enterprise workflows that are dynamic, long-running, API-heavy, and policy-constrained. Agent logic acts as a GPS, reducing hallucinations and token consumption while improving accuracy by bounding the LLM to structured, domain-specific reasoning.

## Key Ideas
- Program analysis: pre-indexed representations reduce token usage ~30x for legacy code understanding
- Knowledge graphs: KG-guided local reasoning achieves 4x improvement over ReAct for incident investigation
- Policy-as-code: runtime-enforced governance closes 15-26% accuracy gaps across all model families
- Adaptive planning: algorithmic decomposition boosts compliance automation from single digits to +80%
- DAG-guided reasoning: reduces asset analysis time 97% (15-20 min to 15-30 sec) with 77% lower token usage
- Agent logic reduces the context space the LLM needs to process, focusing it on what matters

## Tradeoffs
- Domain-specific agent logic vs generalist agent capabilities
- Upfront investment in building primitives vs LLM-only rapid prototyping
- Maintaining analysis infrastructure (KGs, program analysis DBs) vs one-off LLM calls

## Related
- [[concepts/Harness-Engineering]]
- [[concepts/Program-Analysis-for-Agents]]
- [[concepts/Knowledge-Graph-for-IT-Ops]]

## Source
[[summaries/NicholasFuller-Agent-Logic-Enterprise-AI]]
