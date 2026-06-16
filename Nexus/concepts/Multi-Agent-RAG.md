---
type: Concept
title: Multi-Agent RAG
description: 'Arquitectura de agentic RAG con múltiples agents especializados: un
  master agent coordina retrieval entre agents que se especializan en diferentes fuentes
  (i...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Multi-Agent RAG

## Definition
Arquitectura de agentic RAG con múltiples agents especializados: un master agent coordina retrieval entre agents que se especializan en diferentes fuentes (internal data, personal accounts, web search).

## Why It Matters
Supera la limitación del single-agent RAG donde un solo agente hace reasoning, retrieval y answer generation. La separación permite especialización: un agent para proprietary data, otro para personal accounts, otro para public web info.

## Key Ideas
- Master agent coordina entre specialized retrieval agents
- Cada agent puede tener tools y knowledge sources diferentes
- Permite parallelization de retrieval across sources
- Frameworks como CrewAI y Swarm se enfocan en multi-agent con tool sharing

## Related
- [[concepts/Agentic-RAG]]
- [[concepts/Single-Agent-RAG]]
- [[concepts/Multi-Agent-Development]]
- [[concepts/RAG]]

## Source
[[summaries/Weaviate-What-Is-Agentic-RAG]]
