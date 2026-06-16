---
type: Concept
title: Multi-Query Attention
description: Variante de multi-head attention donde los query heads comparten keys
  y values, reduciendo memory bandwidth durante inference.
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Multi-Query Attention

## Definition
Variante de multi-head attention donde los query heads comparten keys y values, reduciendo memory bandwidth durante inference.

## Why It Matters
Standard multi-head attention da a cada query head sus propias key y value heads — duplica memory usage. MQA comparte KV heads across query heads, reduciendo significativamente el footprint de KV cache.

## Key Ideas
- Comparte keys y values across query heads
- Reduce memory bandwidth durante autoregressive inference
- Mistral 7B popularizó combinación práctica de sliding-window attention + GQA en modelo open
- Tradeoff: menos KV heads puede preservar menos calidad vs eficiencia

## Related
- [[concepts/Grouped-Query-Attention]]
- [[concepts/KV-Cache]]
- [[concepts/Transformer-Architecture]]

## Source
[[summaries/TheAhmadOsman-Step-By-Step-LLM-Engineering-Projects]]
