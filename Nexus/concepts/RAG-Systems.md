---
type: Concept
title: RAG Systems
description: 'Sistema que complementa el conocimiento del modelo con datos externos:
  embedding de documentos en un vector index, retrieval de chunks relevantes en query
  ti...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# RAG Systems

## Definition
Sistema que complementa el conocimiento del modelo con datos externos: embedding de documentos en un vector index, retrieval de chunks relevantes en query time, y concatenación al prompt. El pipeline típico: chunk size + overlap → query rewriting → vector retrieval → reranking con cross-encoder.

## Why It Matters
El prompting tiene un límite cuando la respuesta requiere datos que el modelo nunca vio. RAG rompe esa barrera permitiendo acceso a documentos dinámicos, historial de clientes, o cualquier dato pasado el cutoff de training.

## Key Ideas
- Pipeline: embedding → retrieval → reranking
- 8 arquitecturas de RAG: Naive, ReRanking, Multi-Document QA, Agentic RAG, etc.
- Chunk size y overlap son hiperparámetros críticos
- Query rewriting antes del retrieval mejora la precisión
- Reranking con cross-encoder después del retrieval mejora la calidad
- Fine-tuning para patrones de output; RAG para datos dinámicos

## Tradeoffs
- RAG añade latencia al pipeline (embedding + retrieval)
- La calidad del retrieval depende de la calidad del embedding
- No es un reemplazo del fine-tuning — son complementarios

## Related
- 
- [[concepts/Prompt-Engineering]]
- 
- 

## Source
[[summaries/Avichawla-LLM-Engineering-Roadmap]]
