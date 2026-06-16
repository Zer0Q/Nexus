---
type: Concept
title: RULER
description: Relative Utility-based LLM Evaluation and Ranking — uses an LLM judge
  to score trajectories relatively against the agent's system prompt, replacing hand-writ...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# RULER

## Definition
Relative Utility-based LLM Evaluation and Ranking — uses an LLM judge to score trajectories relatively against the agent's system prompt, replacing hand-written reward functions for non-verifiable tasks.

## Why It Matters
Solves the reward signal bottleneck for agent workflows (RAG, customer support, tool use, summarization) where no deterministic verifier exists. The system prompt acts as an implicit reward function, and the judge applies its criteria without Python implementation.

## Key Ideas
- Generates N trajectories per scenario, sends all to a judge LLM with the system prompt
- Judge reads the system prompt to understand what the agent should do, then scores each trajectory 0-1 relative to others
- Two key properties: (1) relative scoring is easier than absolute scoring for LLMs, (2) GRPO normalizes within groups anyway
- Produces nuanced partial credit: faithful response 0.97, hallucinated 0.45, ignored context 0.05
- Implemented in OpenPipe's ART framework (9k+ stars, open-source)
- Custom rubrics are natural language, not Python — fast iteration without buggy conditions

## Tradeoffs
- Requires an LLM judge call per training step — cost-quality tradeoff vs. hand-written reward functions
- Cheaper models (Qwen3 32B) work well as judges; doesn't require the most expensive model
- RULER deduplicates common prefixes (system + user message) to cut token usage
- Caches judge responses to disk for debugging iteration

## Related
- [[concepts/GRPO]]
- [[concepts/RLVR]]
- [[concepts/System-Prompt-Learning]]
- [[concepts/RLAIF]]
- [[concepts/ART-Framework]]

## Source
[[summaries/avichawla-RL-Agents-2026-System-Prompt-Learning]]
