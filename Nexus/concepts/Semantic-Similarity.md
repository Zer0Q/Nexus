---
type: Concept
title: Semantic Similarity
description: Propiedad de embeddings donde tokens con significado similar tienen vectores
  numéricamente cercanos en el espacio vectorial.
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Semantic Similarity

## Definition
Propiedad de embeddings donde tokens con significado similar tienen vectores numéricamente cercanos en el espacio vectorial.

## Why It Matters
Es la base de la capacidad de los LLMs para entender relaciones semánticas. "King" y "Queen" son numéricamente cercanos; king - man + woman ≈ queen. Permite al modelo generalizar más allá de co-occurrence exacta.

## Key Ideas
- En GPT-3, cada embedding tiene 12,288 dimensiones — cada dimensión captura una característica implícita
- Los embeddings responden implícitamente a cientos de "preguntas": ¿eres un noun? ¿asociado a emociones positivas/negativas? ¿formal/informal?
- Las relaciones aritméticas en embedding space capturan estructura semántica: king - man + woman ≈ queen
- Base para retrieval en RAG: buscar documentos semanticamente similares a la query

## Related
- [[concepts/Embeddings]]
- [[concepts/Tokenization]]
- [[concepts/RAG]]

## Source
[[summaries/RohitTiwari-A-Visual-Guide-to-LLMs-Part-1]]
