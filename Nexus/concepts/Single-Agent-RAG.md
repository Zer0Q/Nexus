---
type: Concept
title: Single-Agent RAG
description: Arquitectura simple de agentic RAG donde un agente/router decide qué
  knowledge source consultar entre múltiples fuentes (vector DB, web search, APIs,
  Slack, ...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Single-Agent RAG

## Definition
Arquitectura simple de agentic RAG donde un agente/router decide qué knowledge source consultar entre múltiples fuentes (vector DB, web search, APIs, Slack, email).

## Why It Matters
Es la forma más básica de agentic RAG — un router que generaliza retrieval más allá de un solo vector database. Permite access a external tools, query pre-processing, multi-step retrieval y validation de retrieved information.

## Key Ideas
- Al menos dos external knowledge sources
- El agent decide cuál consultar basado en la query
- Sources no limitados a databases — puede ser web search, API, Slack, email
- Limitación: un solo agent con reasoning, retrieval y answer generation en uno

## Related
- [[concepts/Agentic-RAG]]
- [[concepts/Multi-Agent-RAG]]
- [[concepts/RAG]]

## Source
[[summaries/Weaviate-What-Is-Agentic-RAG]]
