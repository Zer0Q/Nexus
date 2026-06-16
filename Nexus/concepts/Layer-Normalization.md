---
type: Concept
title: Layer Normalization
description: Técnica que normaliza las features de cada token independientemente,
  estabilizando los valores de activación durante training. Calcula la media (μ) y
  varianz...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Layer Normalization

## Definition
Técnica que normaliza las features de cada token independientemente, estabilizando los valores de activación durante training. Calcula la media (μ) y varianza (σ²) de las features, luego estandariza: x^_i = (x_i - μ) / sqrt(σ² + ε).

## Why It Matters
Sin normalización, las activaciones crecen demasiado grandes o se hacen demasiado pequeñas al pasar por múltiples capas, ralentizando el aprendizaje. LayerNorm mantiene las activaciones en un rango estable, haciendo el training significativamente más rápido y confiable.

## Key Ideas
- Normaliza por token (no por batch como BatchNorm)
- Calcula media: μ = (1/n) Σ x_i
- Calcula varianza: σ² = (1/n) Σ (x_i - μ)²
- Output normalizado: x^_i = (x_i - μ) / sqrt(σ² + ε) donde ε evita división por cero
- Se aplica múltiples veces dentro de cada transformer block
- GPT usa pre-norm: LayerNorm ANTES de attention y FFN

## Related
- [[concepts/Transformer-Architecture]]
- [[concepts/Residual-Connections]]

## Source
[[summaries/RohitTiwari-A-Visual-Guide-to-LLMs-Part-2]]
