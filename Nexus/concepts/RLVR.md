---
type: Concept
title: RLVR
description: Reinforcement Learning with Verifiable Rewards — replaces learned reward
  models with rule-based verifiers (compilers, checkers, gold answers) that return
  bin...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# RLVR

## Definition
Reinforcement Learning with Verifiable Rewards — replaces learned reward models with rule-based verifiers (compilers, checkers, gold answers) that return binary correct/incorrect signals, eliminating the need for human rankings or explicit reward models.

## Why It Matters
Solved the reward signal bottleneck for verifiable tasks (math, code), enabling DeepSeek R1 to go from 15.6% to 77.9% on AIME 2024 using just GRPO + verifiable rewards with no supervised fine-tuning. The model self-discovered chain-of-thought reasoning purely from binary signals.

## Key Ideas
- Verifier checks output against ground truth: math answers match known solutions, code passes compiler/tests
- Binary rewards (1 for correct, 0 for wrong) — no human rankings or reward models needed
- Works with GRPO: generates multiple responses per prompt, normalizes rewards within each group
- The RL training loop discovers that reasoning improves the reward, so the model learns to reason
- Dominant approach for training reasoning models through 2025

## Tradeoffs
- Only works for tasks with deterministic verifiable outcomes (math, code, logic)
- Does not apply to subjective tasks (RAG answers, support replies, summaries) where no gold label exists
- For non-verifiable tasks, the fallback is hand-written reward functions or LLM-as-judge (RULER)

## Related
- [[concepts/GRPO]]
- [[concepts/RULER]]
- [[concepts/RLHF]]
- [[concepts/Decentralized-Credit-Assignment]]

## Source
[[summaries/avichawla-RL-Agents-2026-System-Prompt-Learning]]
