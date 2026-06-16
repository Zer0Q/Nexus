---
type: Concept
title: Grouped Query Attention
description: Middle ground entre multi-head attention y multi-query attention — mantiene
  varios KV heads en lugar de uno, preservando más calidad mientras mejora eficienc...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Grouped Query Attention

## Definition
Middle ground entre multi-head attention y multi-query attention — mantiene varios KV heads en lugar de uno, preservando más calidad mientras mejora eficiencia de inference.

## Why It Matters
Por 2026, KV-cache reduction es un major architecture design axis. GQA preserva más calidad que MQA (que usa solo un KV head) mientras sigue reduciendo memory bandwidth significativamente.

## Key Ideas
- Mantener several KV heads en lugar de uno (MQA) o uno por query head (MHA)
- Mistral 7B popularizó sliding-window attention + GQA en open model
- DeepSeek-V2 introdujo Multi-head Latent Attention (MLA), low-rank KV compression — evolución de GQA
- Part of KV-cache reduction axis junto con MLA

## Related
- [[concepts/Multi-Query-Attention]]
- [[concepts/KV-Cache]]
- [[concepts/Transformer-Architecture]]

## Source
[[summaries/TheAhmadOsman-Step-By-Step-LLM-Engineering-Projects]]
