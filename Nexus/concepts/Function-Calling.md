---
type: Concept
title: Function Calling
description: Capacidad de LLMs para interactuar con servicios externos y APIs especificando
  estructura y definición exacta de funciones, permitiendo al modelo generar lla...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Function Calling

## Definition
Capacidad de LLMs para interactuar con servicios externos y APIs especificando estructura y definición exacta de funciones, permitiendo al modelo generar llamadas a tools predefinidos.

## Why It Matters
Es el mecanismo fundamental para construir agentic systems sin frameworks pesados. OpenAI lo lanzó en junio 2023 para gpt-3.5-turbo y gpt-4; después Cohere, Anthropic, Google y Ollama lo adoptaron para modelos open-source como Llama3.2.

## Key Ideas
- Se define un tools_schema con nombre, descripción y parameters de cada función
- El LLM incluye tool use block en la API response si planea invocar un tool
- Se necesita un loop que route entre LLM y tools
- Ollama introdujo tool support para modelos open-source: Llama3.2, nemotron-mini
- Es la base para implementar agentic RAG sin frameworks — solo LLM API + loop + tools

## Related
- [[concepts/Agentic-RAG]]
- [[concepts/Tool-Use]]
- [[concepts/Agent-Tool-Use]]

## Source
[[summaries/Weaviate-What-Is-Agentic-RAG]]
