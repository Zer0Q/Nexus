---
type: Concept
title: Mixture of Experts
description: Arquitectura de modelo sparse donde cada token se routea a un subset
  de expertos, activando solo una fracción de los parámetros totales por token.
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Mixture of Experts

## Definition
Arquitectura de modelo sparse donde cada token se routea a un subset de expertos, activando solo una fracción de los parámetros totales por token.

## Why It Matters
Aumenta parameter count sin activar cada parameter para cada token — escala model capacity efficiently. DeepSeek-V3: 671B total parameters con solo 37B activados por token. Mixtral demostró diseño open sparse MoE práctico.

## Key Ideas
- Switch Transformer mostró que sparse expert routing escala capacity efficiently
- Mixtral: diseño open sparse MoE donde cada token routea a subset de expertos
- DeepSeek-V3: 671B total, 37B activated, con MLA + DeepSeekMoE + auxiliary-loss-free load balancing + multi-token prediction
- Llama 4: primer open-weight natively multimodal MoE de Meta
- Qwen3: Qwen3-235B-A22B y Qwen3-30B-A3B (MoE) + 6 dense models
- Kimi K2.6: 1T total parameters, 32B activated, 256K context window, MoonViT vision encoder
- Build a two-expert router es el proyecto introductorio para entender MoE

## Related
- [[concepts/Transformer-Architecture]]
- [[concepts/MoE]]
- [[concepts/KV-Cache]]

## Source
[[summaries/TheAhmadOsman-Step-By-Step-LLM-Engineering-Projects]]
