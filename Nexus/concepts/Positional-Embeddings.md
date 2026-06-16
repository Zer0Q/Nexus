---
type: Concept
title: Positional Embeddings
description: Vectores añadidos a token embeddings para codificar la posición absoluta
  o relativa de cada token en la secuencia de input.
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Positional Embeddings

## Definition
Vectores añadidos a token embeddings para codificar la posición absoluta o relativa de cada token en la secuencia de input.

## Why It Matters
Sin positional embeddings, "The dog jumps on the cat" y "The cat jumps on the dog" tendrían los mismos tokens y el modelo no distinguiría el orden. Son esenciales para que el LLM entienda que el orden importa.

## Key Ideas
- Token embeddings son idénticos para "the" al inicio y al medio — positional embeddings los diferencian
- Piensa como añadir un "seat number" único a cada token
- Métodos: sinusoidal (original Transformer), learned positions, RoPE (rotary — codifica posición relativa through rotations), ALiBi (biases attention scores basado en distancia)
- RoPE-scaling variants y YaRN permiten context extension más data/compute-efficient
- Attention sin position es permutation-invariant — "dog bites man" y "man bites dog" se ven demasiado similares

## Related
- [[concepts/Tokenization]]
- [[concepts/Embeddings]]
- [[concepts/Transformer-Architecture]]
- [[concepts/LLM-Input-Pipeline]]

## Source
[[summaries/RohitTiwari-A-Visual-Guide-to-LLMs-Part-1]]
