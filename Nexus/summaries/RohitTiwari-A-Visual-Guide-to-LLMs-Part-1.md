---
title: A Visual Guide to LLMs (Part 1)
author: '@_rohit_tiwari_'
published: '2026-01-20'
type: article
resource: https://x.com/_rohit_tiwari_/status/2013580072788336643
timestamp: '2026-01-20T00:00:00Z'
description: 'Guía visual del input pipeline de LLMs: cómo el texto se convierte en
  vectores numéricos que el modelo puede procesar. Cubre tokenización (word-based,
  subwor...'
tags:
- summaries
---


# A Visual Guide to LLMs (Part 1)

## Summary
Guía visual del input pipeline de LLMs: cómo el texto se convierte en vectores numéricos que el modelo puede procesar. Cubre tokenización (word-based, subword BPE, character-based), token embeddings (vectores con similitud semántica) y positional embeddings (información de orden). Ejemplo paso a paso con "Every moment is a beginning" mostrando la transformación desde texto hasta vectores finales con significado + posición codificados.

## Core Concepts
- [[concepts/Tokenization]] -- proceso de dividir texto en unidades más pequeñas (tokens) que son los building blocks del LLM
- [[concepts/Byte-Pair-Encoding]] -- algoritmo de subword tokenization que mergea pares de caracteres/subwords más comunes hasta alcanzar un vocabulario objetivo
- [[concepts/Embeddings]] -- representaciones numéricas (vectores) de tokens que capturan significado y relaciones semánticas
- [[concepts/Positional-Embeddings]] -- vectores añadidos a token embeddings para codificar la posición absoluta o relativa de cada token en la secuencia
- [[concepts/Semantic-Similarity]] -- tokens con significado similar tienen vectores de embedding cercanos (king ≈ queen)
- [[concepts/LLM-Input-Pipeline]] -- primera fase de la arquitectura LLM: tokenización → embeddings → positional embeddings → vectores de input finales

## Key Insights
- Los LLMs predicen un token a la vez de forma iterativa — cada token predicho se appendea al input previo como contexto para la siguiente predicción
- La tokenización subword resuelve el problema de palabras desconocidas: "unbelievable" → "un" + "believe" + "able"
- En GPT-3, el embedding size es de 12,288 dimensiones — cada token responde implícitamente a cientos de "preguntas" sobre sus características
- Las relaciones aritméticas en embeddings: king - man + woman ≈ queen, demostrando que capturan estructura semántica
- Los positional embeddings son necesarios porque "The dog jumps on the cat" y "The cat jumps on the dog" tienen los mismos tokens pero significados opuestos
- Los token embeddings son idénticos para "the" al inicio y al medio de una frase — los positional embeddings los diferencian
- Los tokens especiales (|im_start|, |im_sep|, |im_end|) ayudan al modelo a identificar dónde empiezan las mensajes, dónde se separan partes y dónde terminan
- El ejemplo numérico muestra vectores de 3 dimensiones para claridad pedagógica — en modelos reales son miles de dimensiones

## Open Questions
- ¿Cómo afectan las diferentes estrategias de positional embeddings (sinusoidal vs RoPE vs ALiBi) a la capacidad de extrapolación de longitud?
- ¿Qué tradeoffs hay entre vocabularios grandes (menos tokens, más memoria) vs pequeños (más tokens, menos memoria) en la práctica?

## Source
- **Raw note:** [[raw-notes/a-visual-guide-to-llms-part-1]]
- **Original URL:** https://x.com/_rohit_tiwari_/status/2013580072788336643
