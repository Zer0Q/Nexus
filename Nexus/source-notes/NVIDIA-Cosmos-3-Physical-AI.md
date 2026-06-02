---
title: "Develop Physical AI Reasoning, World, and Action Models with NVIDIA Cosmos 3"
source: "https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/"
author: "Asawaree Bhide"
published: "2026-06-01"
type: article
---

# NVIDIA Cosmos 3 Physical AI

## Summary
NVIDIA Cosmos 3 unifies physical reasoning, world generation, and action generation in a single Mixture-of-Transformers model with two towers (reasoner + generator). Open-sourced with checkpoints, training scripts, deployment tools, and six synthetic datasets for robotics, driving, and warehouse domains.

## Core Concepts
- [[concepts/Physical-AI]] -- AI systems that understand and act in the real physical world
- [[concepts/World-Models]] -- generative models that predict future states given actions and observations
- [[concepts/Mixture-of-Transformers]] -- architecture combining multiple transformer specializations in one model
- concepts/Two-Tower-Architecture -- reasoner tower (VLM) feeds generator tower (diffusion) for guided generation
- [[tools/NVIDIA-Cosmos]] -- frontier foundation model for physical AI with reasoning and generation
- [[concepts/Synthetic-Data-Generation]] -- generating training data via simulation for physical AI domains
- [[concepts/Action-Conditioned-World-Model]] -- world model conditioned on action sequences for robot policy learning
- [[glossary/NVFP4]] -- 4-bit floating point quantization for 2x inference speedup

## Key Insights
- Single model replaces orchestration between multiple specialized models
- Cosmos 3 Nano (16B) targets workstation GPUs; Super (64B) targets datacenter GPUs
- HUE benchmark shifts evaluation from subjective grading to atomic binary fact verification
- Action post-training enables forward/inverse dynamics and policy generation

## Open Questions
- How does MoT scaling compare to MoE for physical reasoning workloads?
- Can the reasoner tower be fine-tuned independently for domain-specific reasoning?
