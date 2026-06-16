---
type: Concept
title: ReAct Framework
description: 'Framework agentic que combina Reason + Act: el agent razona sobre la
  siguiente acción (Thought), la ejecuta (Action), observa el feedback (Observation)
  e ite...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# ReAct Framework

## Definition
Framework agentic que combina Reason + Act: el agent razona sobre la siguiente acción (Thought), la ejecuta (Action), observa el feedback (Observation) e itera hasta completar la tarea.

## Why It Matters
Es el framework más popular para agents que manejan sequential multi-part queries manteniendo state en memory. Combina routing, query planning y tool use en una sola entidad.

## Key Ideas
- Thought: agent razona sobre qué hacer a continuación
- Action: agent decide y ejecuta (tool use, search, API call)
- Observation: agent observa feedback de la acción
- Loop itera hasta completar tarea y responder al usuario
- Usado en agentic RAG para retrieval iterativo: recuperar → evaluar → re-recuperar → validar
- DSPy soporta ReAct agents y Avatar optimization (prompt engineering automático para tool descriptions)

## Related
- [[concepts/Agentic-RAG]]
- [[concepts/Agent-Logic]]
- [[concepts/Tool-Use]]

## Source
[[summaries/Weaviate-What-Is-Agentic-RAG]]
