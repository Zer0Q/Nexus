---
type: Concept
title: Coordinator Pattern
description: Patrón de arquitectura donde un agent central orchestrates workers paralelos,
  asigna tasks, monitorea progress y mergea outputs en un deliverable unificado.
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Coordinator Pattern

## Definition
Patrón de arquitectura donde un agent central orchestrates workers paralelos, asigna tasks, monitorea progress y mergea outputs en un deliverable unificado.

## Why It Matters
Sin coordinator, workers paralelos producen outputs desconectados. El coordinator es el que hace el fan-out pattern útil: toma inputs, distribuye trabajo, y produce un deliverable coherente.

## Key Ideas
- Single prompt → coordinator → N workers → merge → deliverable
- Coordinator mantiene contexto global mientras workers procesan localmente
- Merge puede ser simple (concat) o complejo (synthesis con citations)
- Kimi K2.6: orchestration baked into model layer, no bolted onto chat interface
- Coordinator puede ser otro agent o parte del mismo agent

## Tradeoffs
- Coordinator puede ser bottleneck de performance
- Merge complexity depende de naturaleza de outputs
- Error handling: qué pasa cuando workers fallan
- Context window limits para coordinator con many workers

## Related
- [[concepts/Fan-Out-Pattern]]
- [[concepts/Parallelization]]
- [[concepts/Orchestrator-Workers]]

## Source
[[summaries/Khairallah-300-AI-Agents-Parallel]]
