---
title: What Is Agentic RAG? From LLM RAG to AI Agents
author: Erika Shorten & Leonie Monigatti (Weaviate)
published: '2024-11-05'
type: article
resource: https://weaviate.io/blog/what-is-agentic-rag
timestamp: '2024-11-05T00:00:00Z'
description: Agentic RAG incorpora AI agents en el pipeline de RAG para superar las
  limitaciones del vanilla RAG (single knowledge source, one-shot retrieval). El agente
  ...
tags:
- summaries
---


# What Is Agentic RAG

## Summary
Agentic RAG incorpora AI agents en el pipeline de RAG para superar las limitaciones del vanilla RAG (single knowledge source, one-shot retrieval). El agente puede recuperar, evaluar, re-recuperar y validar contexto antes de generar la respuesta final, usando tools (vector search, web search, calculadora, APIs). Dos arquitecturas: single-agent (router) y multi-agent (master + specialized retrievers). Implementable vía function calling directo o frameworks (DSPy, LangChain, CrewAI, LlamaIndex, Swarm, Letta).

## Core Concepts
- [[concepts/RAG]] -- Retrieval-Augmented Generation, técnica que usa knowledge source externo para proveer contexto al LLM y reducir hallucinations
- [[concepts/Agentic-RAG]] -- implementación de RAG basada en AI agents con planning, tool use y validation loops
- [[concepts/ReAct-Framework]] -- patrón Reason + Act: Thought → Action → Observation loop iterativo hasta completar la tarea
- [[concepts/Single-Agent-RAG]] -- arquitectura simple donde un agente/router decide qué knowledge source consultar
- [[concepts/Multi-Agent-RAG]] -- master agent coordina retrieval entre múltiples agents especializados (internal data, personal accounts, web search)
- [[concepts/Function-Calling]] -- capacidad de LLMs para interactuar con tools predefinidos vía schema de funciones (OpenAI, Cohere, Anthropic, Google, Ollama)

## Key Insights
- Vanilla RAG tiene dos limitaciones clave: solo considera un external knowledge source y es one-shot (context retrieved una vez, sin reasoning sobre calidad)
- Los core components de un AI agent: LLM (con role y task), Memory (short-term y long-term), Planning (reflection, self-critics, query routing), Tools (calculator, web search, etc.)
- En agentic RAG, retrieved results actúan como forma de long-term memory, permitiendo a agents recordar info relevante across steps
- El agente puede: decidir si recuperar o no, elegir qué tool usar, formular la query, evaluar el contexto retrieved y decidir si re-recuperar
- OpenAI lanzó function calling en junio 2023 para gpt-3.5-turbo y gpt-4; Ollama introdujo tool support para modelos open-source como Llama3.2
- Los frameworks agenticos tienen enfoques distintos: DSPy soporta ReAct y Avatar optimization (prompt engineering automático para tool descriptions), LangGraph ofrece built-in tools, CrewAI se enfoca en multi-agent con tool sharing, Letta refleja y refina internal world model como functions
- Replit lanzó un agent para developers; Microsoft anunció copilots autónomos — ejemplos de agents en producción
- Limitaciones de agentic RAG: added latency, unreliability del LLM, posible failure en completar tareas — necesita proper failure modes para unstick agents

## Open Questions
- ¿Cómo cuantificar el tradeoff entre la mejora en calidad de respuesta vs el aumento de latencia en agentic RAG vs vanilla RAG?
- ¿Qué patrones de failure son más comunes cuando agents fallan en completar retrieval tasks y cómo diseñar fallbacks efectivos?

## Source
- **Raw note:** [[raw-notes/what-is-agentic-rag-from-llm-rag-to-ai-agents]]
- **Original URL:** https://weaviate.io/blog/what-is-agentic-rag
