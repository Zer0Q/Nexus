---
type: Concept
title: Agentic RAG
description: Implementación de RAG basada en AI agents que incorpora planning, tool
  use y validation loops en el pipeline de retrieval, superando las limitaciones del
  van...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Agentic RAG

## Definition
Implementación de RAG basada en AI agents que incorpora planning, tool use y validation loops en el pipeline de retrieval, superando las limitaciones del vanilla RAG (single source, one-shot retrieval).

## Why It Matters
El agente puede recuperar, evaluar, re-recuperar y validar contexto antes de generar la respuesta final — making RAG más robusto en producción. Vanilla RAG es como estar en una biblioteca antes de smartphones; agentic RAG es como tener smartphone con browser, calculator, emails.

## Key Ideas
- Vanilla RAG limitations: solo un external knowledge source, one-shot retrieval sin reasoning sobre calidad
- Agentic RAG adds: multi-step retrieval, tool use (vector search, web search, calculator, APIs), validation loops
- Retrieved results actúan como long-term memory, permitiendo a agents recordar info across steps
- El agent puede: decidir si recuperar, elegir tool, formular query, evaluar contexto, re-recuperar
- Dos implementaciones: function calling directo (OpenAI, Anthropic, Google, Ollama) o agent frameworks (DSPy, LangChain, CrewAI, LlamaIndex, Swarm, Letta)
- Beneficios: respuestas más accurate, tareas autónomas, mejor colaboración humano-AI
- Limitaciones: added latency, unreliability del LLM, necesita proper failure modes para unstick agents

## Related
- [[concepts/RAG]]
- [[concepts/Single-Agent-RAG]]
- [[concepts/Multi-Agent-RAG]]
- [[concepts/ReAct-Framework]]
- [[concepts/Function-Calling]]

## Source
[[summaries/Weaviate-What-Is-Agentic-RAG]]
