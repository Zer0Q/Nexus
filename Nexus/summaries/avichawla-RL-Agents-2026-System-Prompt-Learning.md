---
title: How top AI labs are building RL agents in 2026 (using Karpathy's system prompt
  learning idea)
author: '@_avichawla'
published: '2026-04-28'
type: article
resource: https://x.com/_avichawla/status/2049037299334472015
timestamp: '2026-04-28T00:00:00Z'
description: The article traces the evolution of RL for LLMs from RLHF (4-model PPO
  pipeline) through DeepSeek R1's GRPO+RLVR breakthrough to RULER — an LLM-as-judge
  appr...
tags:
- summaries
---


# RL Agents 2026: From RLHF to RULER

## Summary
The article traces the evolution of RL for LLMs from RLHF (4-model PPO pipeline) through DeepSeek R1's GRPO+RLVR breakthrough to RULER — an LLM-as-judge approach that uses relative rankings to score trajectories for non-verifiable tasks. The core insight is that the bottleneck was never the optimizer (GRPO handles that) but the reward signal: RLVR solved it for math/code with binary verifiers, and RULER solves it for agents by having a judge LLM score trajectories relative to each other against the system prompt, which acts as an implicit reward function.

## Core Concepts
- [[concepts/RLVR]] -- Reinforcement Learning with Verifiable Rewards, replaces learned reward models with rule-based verifiers (compilers, checkers) returning binary correct/incorrect signals
- [[concepts/GRPO]] -- Group Relative Policy Optimization, removes the critic model from PPO by generating multiple responses per prompt and normalizing rewards within each group
- [[concepts/RULER]] -- Relative Utility-based LLM Evaluation and Ranking, uses an LLM judge to score trajectories relatively against the system prompt, replacing hand-written reward functions
- [[concepts/System-Prompt-Learning]] -- Karpathy's proposed paradigm where the system prompt carries a richer signal than scalar rewards, and RL training leverages that signal directly
- [[concepts/ART-Framework]] -- OpenPipe's open-source training framework (9k+ stars) implementing GRPO + RULER for agent fine-tuning
- [[concepts/RLHF]] -- Reinforcement Learning from Human Feedback, the original 4-model PPO pipeline (policy + reference + reward model + critic) behind ChatGPT
- [[concepts/RLAIF]] -- Reinforcement Learning from AI Feedback, swaps human labelers for an LLM judge, achieving RLHF-level quality at lower cost
- [[concepts/DPO]] -- Direct Preference Optimization, skips the reward model and optimizes preference pairs directly with classification-style loss

## Key Insights
- PPO required 4 full-size models in memory simultaneously (policy + reference + reward model + critic), meaning ~28B params for a 7B model
- GRPO eliminated the critic model entirely; RLVR eliminated the reward model — collapsing the 4-model PPO to ~2 models (policy + reference)
- DeepSeek R1-Zero went from 15.6% to 77.9% on AIME 2024 using just GRPO + verifiable rewards, with no supervised fine-tuning — the model self-discovered chain-of-thought reasoning
- RULER works because (1) relative scoring is easier than absolute scoring for LLMs, and (2) GRPO normalizes within groups anyway, so relative rankings map directly to what GRPO expects
- RULER example: faithful response scored 0.97, hallucinated 0.45, ignored context 0.05 — nuanced partial credit that would require significant engineering to encode in a rule-based reward function
- RULER deduplicates common prefixes (system prompt + user message) so the judge only sees shared context once, cutting token usage significantly
- Custom rubrics in RULER are natural language, not Python — iterating on criteria is fast without the risk of buggy conditions silently teaching bad behavior
- 4-8 trajectories per group is the recommended range; cheaper models like Qwen3 32B work well as judges

## Open Questions
- How does [[concepts/System-Prompt-Learning]] relate to [[concepts/RULER]] — is RULER an implementation of Karpathy's idea or a different approach to the same problem?
- Can [[concepts/RULER]] be combined with [[concepts/RLVR]] for hybrid tasks where some outputs are verifiable and others require subjective judgment?
- What are the cost implications of using an LLM judge for every training step versus a hand-written reward function at scale?

## Source
- **Raw note:** [[raw-notes/how-top-ai-labs-are-building-rl-agents-in-2026-using-karpathys-s]]
- **Original URL:** https://x.com/_avichawla/status/2049037299334472015
