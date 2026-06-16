---
type: Concept
title: RAG (Retrieval-Augmented Generation)
description: '- Mejor que fine-tuning para la mayoría de casos: datos cambiantes sin
  reentrenamiento - Citas de fuente disponibles, reduce alucinación dramáticamente
  - Fun...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# RAG (Retrieval-Augmented Generation)

Patrones de arquitectura donde un LLM primero busca en una base de conocimiento antes de responder. Flujo: pregunta → embedding → búsqueda en vector DB → documentos relevantes + pregunta → modelo responde con datos reales.

- Mejor que fine-tuning para la mayoría de casos: datos cambiantes sin reentrenamiento
- Citas de fuente disponibles, reduce alucinación dramáticamente
- Funciona con datos privados que nunca deben estar en entrenamiento

See also: [[concepts/LLM-Hallucination]], [[concepts/Embeddings]], [[concepts/Context-Window]]
