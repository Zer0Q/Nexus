---
type: Concept
title: RLHF
description: Reinforcement Learning from Human Feedback — proceso de post-training
  que convierte un base model (que predice texto) en un assistant que sigue instrucciones...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# RLHF

## Definition
Reinforcement Learning from Human Feedback — proceso de post-training que convierte un base model (que predice texto) en un assistant que sigue instrucciones, usando feedback humano para alinear el modelo con user intent.

## Why It Matters
Reinforcement learning se volvió especialmente importante para reasoning models. OpenAI o1强调了 performance improves con más RL y más inference-time thinking. DeepSeek-R1 popularizó pure-RL R1-Zero stage + multi-stage pipeline.

## Key Ideas
- InstructGPT mostró que human-feedback fine-tuning alinea models mejor que simplemente scaling pretrained models
- DPO (Direct Preference Optimization) simplificó preference training evitando explicit reward model y RL loop
- PPO: Proximal Policy Optimization, standard RL algorithm
- GRPO (Group Relative Policy Optimization): alternativa PPO-style que reduce memory overhead evitando separate critic model
- RLVR: Reinforcement Learning with Verifiable Rewards
- Build toy RLHF, PPO, GRPO y RLVR lab es el proyecto para entenderlo

## Related
- [[Fine-tuning-with-TRL]] -- needs research: framework de fine-tuning de HuggingFace
- [[Simpo-Training]] -- needs research: Simple Preference Optimization para alignment
- [[Grpo-RL-Training]] -- needs research: Group Relative Policy Optimization para RL

## Source
[[summaries/TheAhmadOsman-Step-By-Step-LLM-Engineering-Projects]]
