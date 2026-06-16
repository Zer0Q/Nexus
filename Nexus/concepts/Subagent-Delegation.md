---
type: Concept
title: Subagent Delegation
description: Patrón donde el agente principal delega sub-tareas a agentes con contexto
  y permisos aislados. Cada subagent tiene su propio context window, model, tools
  y p...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Subagent Delegation

## Definition
Patrón donde el agente principal delega sub-tareas a agentes con contexto y permisos aislados. Cada subagent tiene su propio context window, model, tools y permissions. El main agent delega hacia abajo y recibe resultados hacia arriba.

## Why It Matters
Permite mantener el contexto del agente principal limpio mientras se trabaja en paralelo. Sin subagents, el contexto se infla con información de tareas secundarias que no son relevantes para la tarea principal.

## Key Ideas
- Cada subagent tiene su propio context window, model, tools y permissions
- Main agent delega down, recibe results up — simple y limpio
- No infinite recursion: subagents no pueden spawnear subagents
- Hard boundaries por diseño para mantener el contexto principal limpio
- Ideal para tareas que requieren análisis de múltiples fuentes simultáneamente

## Tradeoffs
- Más overhead de setup por cada subagent
- Comunicación entre subagents puede ser lenta
- Más subagents = más tokens consumidos en total

## Related
- [[concepts/Agent-Architecture]]
- 
- [[concepts/Context-Window]]
- [[tools/Claude-Code]]

## Source
[[summaries/LearnWithBrij-Learning-Claude-Code-Part-3]]
[[summaries/Santtiagom-Learning-Claude-Code-Part-1]]
[[summaries/Santtiagom-Learning-Claude-Code-Part-3]]
