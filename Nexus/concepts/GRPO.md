# GRPO

## Definition
Group Relative Policy Optimization — generates multiple responses per prompt (typically 4-16) and normalizes rewards within each group, eliminating the need for a separate critic model in the PPO training pipeline.

## Why It Matters
Collapsed the 4-model PPO setup (policy + reference + critic + reward model) to ~2 models. Combined with RLVR, it enabled DeepSeek R1's breakthrough results with minimal infrastructure.

## Key Ideas
- Generates N responses per prompt, scores each, then computes mean/std within the group for normalization
- Training signal comes from relative ordering — which trajectories were above/below average
- Removed the critic model entirely (no longer need a separate model to predict expected reward per prompt)
- General-purpose optimizer: doesn't care whether reward comes from math verifier, code compiler, human, or Python script
- 4-8 trajectories per group is the recommended range for RULER integration

## Tradeoffs
- Needs exactly one scalar reward per response — the bottleneck is the scoring function, not the optimizer
- Fewer than 4 trajectories gives too little to compare; more than 8 can confuse the judge and increase cost
- Reward normalization within groups means absolute score calibration doesn't matter

## Related
- [[concepts/RLVR]]
- [[concepts/RULER]]
- [[concepts/RLHF]]
- [[concepts/DPO]]

## Source
[[summaries/avichawla-RL-Agents-2026-System-Prompt-Learning]]
