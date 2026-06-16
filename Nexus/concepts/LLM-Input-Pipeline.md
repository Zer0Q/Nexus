---
type: Concept
title: LLM Input Pipeline
description: 'Primera fase de la arquitectura LLM que transforma texto humano en vectores
  numéricos: tokenization → token IDs → token embeddings → positional embeddings →
  ...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# LLM Input Pipeline

## Definition
Primera fase de la arquitectura LLM que transforma texto humano en vectores numéricos: tokenization → token IDs → token embeddings → positional embeddings → final input vectors.

## Why It Matters
Es el puente entre lenguaje humano y formato numérico que el modelo puede procesar. Cada decisión en el input pipeline (tokenization method, embedding size, positional encoding) afecta downstream: context length, multilingual behavior, latency y model quality.

## Key Ideas
- Step 1: Tokenization — dividir texto en tokens (word-based, subword BPE, character-based)
- Step 2: Token IDs — cada token mapeado a ID numérico único
- Step 3: Token Embeddings — IDs convertidos a vectores con significado semántico
- Step 4: Positional Embeddings — añadir información de posición
- Step 5: Sum — embeddings + positional = final input vector con significado + ubicación
- Tokens especiales (|im_start|, |im_sep|, |im_end|) marcan boundaries de mensajes
- Los LLMs predicen un token a la vez iterativamente — cada token predicho se appendea al input previo

## Related
- [[concepts/Tokenization]]
- [[concepts/Embeddings]]
- [[concepts/Positional-Embeddings]]
- [[concepts/Transformer-Architecture]]

## Source
[[summaries/RohitTiwari-A-Visual-Guide-to-LLMs-Part-1]]
