---
type: Concept
title: Attention Mechanism
description: Mecanismo que permite a cada token en una secuencia "mirar" todos los
  demás tokens y decidir dinámicamente qué información es más relevante. Se implementa
  me...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Attention Mechanism

## Definition
Mecanismo que permite a cada token en una secuencia "mirar" todos los demás tokens y decidir dinámicamente qué información es más relevante. Se implementa mediante tres vectores derivados de los input embeddings: Queries (Q), Keys (K), Values (V), calculados como: Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) · V.

## Why It Matters
Es la innovación clave que hace posible los modelos de IA modernos. Sin attention, los modelos no podrían resolver ambigüedad contextual ni capturar conexiones de largo alcance.

## Key Ideas
- No lee de izquierda a derecha: ve la oración completa y conecta puntos dinámicamente
- "Apple" presta alta atención a "bought" y "stock" → concluye compañía
- "apple" presta alta atención a "ate" → concluye fruta
- Step 1: derivar Q, K, V de los input embeddings (suma de token + positional embeddings)
- Step 2: dot product Q×K^T para medir matching entre todos los pares de tokens
- Step 3: escalar por sqrt(d_k) para estabilidad numérica durante training
- Step 4: softmax para obtener pesos de atención (probabilidades que suman 1)
- Step 5: multiplicar pesos × V para obtener context vectors
- Antes de attention: modelos lentos que perdían conexiones de largo alcance
- Explica por qué prompts ambiguos producen outputs inconsistentes

## Related
- [[concepts/Transformer-Architecture]]
- [[concepts/Tokenization]]
- [[concepts/Context-Window]]
- [[concepts/Causal-Self-Attention]]
- [[concepts/Masked-Multi-Head-Attention]]

## Source
[[summaries/Sairahul1-10-AI-Concepts]]
[[summaries/RohitTiwari-A-Visual-Guide-to-LLMs-Part-2]]
