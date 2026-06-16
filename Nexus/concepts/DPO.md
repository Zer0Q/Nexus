---
type: Concept
title: DPO
description: Direct Preference Optimization — skips the reward model entirely and
  optimizes preference pairs directly with a classification-style loss, simplifying
  the RL...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# DPO

## Definition
Direct Preference Optimization — skips the reward model entirely and optimizes preference pairs directly with a classification-style loss, simplifying the RLHF pipeline.

## Why It Matters
Eliminates the reward model training step from the alignment pipeline, reducing complexity from a multi-stage process (human rankings -> reward model -> PPO) to a single optimization step.

## Key Ideas
- Takes (prompt, chosen, rejected) triplets and optimizes directly via classification loss
- No separate reward model needed; the policy model itself learns preferences
- Simpler than PPO: no critic model, no reward model, no KL divergence penalty from reference
- Mathematically equivalent to RLHF under certain assumptions but much more stable in practice

## Tradeoffs
- Requires preference data (chosen/rejected pairs) which still needs human or AI labeling
- Less flexible than RLHF for incorporating complex reward signals
- May not match PPO performance on tasks requiring nuanced reward shaping

## Related
- [[concepts/RLHF]]
- [[concepts/RLAIF]]
- [[concepts/GRPO]]

## Source
[[summaries/avichawla-Top-15-Fine-Tuning-Techniques]]
