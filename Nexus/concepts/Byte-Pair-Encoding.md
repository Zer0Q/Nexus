---
type: Concept
title: Byte Pair Encoding
description: Algoritmo de subword tokenization que encuentra los pares más comunes
  de caracteres o subwords y los mergea en subwords más largas hasta alcanzar un vocabula...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Byte Pair Encoding

## Definition
Algoritmo de subword tokenization que encuentra los pares más comunes de caracteres o subwords y los mergea en subwords más largas hasta alcanzar un vocabulario objetivo.

## Why It Matters
Es el algoritmo central de tokenización en la mayoría de LLMs modernos. Maneja palabras raras y desconocidas componiéndolas de subword units familiares — "unbelievable" → "un" + "believe" + "able" — resolviendo el problema de OOV (out-of-vocabulary) words.

## Key Ideas
- Comienza con caracteres individuales
- Encuentra el par más frecuente y lo mergea
- Repite hasta alcanzar el vocabulario target size
- Alternativa: SentencePiece/Unigram hace tokenization trainable directamente desde raw text sin asumir whitespace
- La decisión de tokenización afecta: compresión, multilingual behavior, rare words, code, math, emojis, latency, context usage y model quality

## Related
- [[concepts/Tokenization]]
- [[concepts/Embeddings]]
- [[concepts/LLM-Input-Pipeline]]

## Source
[[summaries/RohitTiwari-A-Visual-Guide-to-LLMs-Part-1]]
