---
type: concept
title: "POPE-RL"
description: "Privileged On-Policy Exploration: a reinforcement learning method for LLMs that uses solution prefixes as hints during training, enabling the model to learn both solving and finding good starting states."
resource: "https://www.deeplearning.ai/the-batch/issue-358"
timestamp: 2026-06-19
tags:
  - reinforcement-learning
  - grpo
  - exploration
  - privileged-information
---

## Definition

POPE (Privileged On-Policy Exploration) is a training method for LLMs that pairs GRPO with custom datasets containing solution prefixes. During training, the model receives both hinted and unhinted versions of problems, learning to both solve from a good starting state and find that starting state without hints.

## How It Works

1. Select problems the pretrained model fails to solve
2. Extract the beginning of the solution (prefix) for each
3. Feed the model progressively longer prefixes until it completes correctly
4. Append prefix to problem with instruction to continue solving
5. During GRPO, show each problem with and without prefix in equal ratio

## Results

On AIME 2025 (competition math):
- POPE: 53.1% pass@1, 82.6% pass@16
- GRPO: 49.6% pass@1, 81.4% pass@16

On HMMT 2025:
- POPE: 37.8% pass@1, 67.5% pass@16
- GRPO: 31.0% pass@1, 63.8% pass@16

## Key Insight

POPE breaks learning hard problems into two steps: (1) finding a good state from which to solve, and (2) solving from that state. Instead of trying to do both at once, the model first learns (2), then learns (1).

## Related Concepts

- [[GRPO]]
- [[Reinforcement-Learning]]
- [[Exploration-Bottleneck]]
- [[Supervised-Fine-Tuning]]
