---
type: Concept
title: Agent Teams
description: Patrón de ejecución paralela y coordinación entre múltiples agentes.
  Cada agente en el equipo tiene su propio contexto, herramientas y permisos. Los
  agentes ...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Agent Teams

## Definition
Patrón de ejecución paralela y coordinación entre múltiples agentes. Cada agente en el equipo tiene su propio contexto, herramientas y permisos. Los agentes pueden pasar mensajes entre sí y coordinar tareas complejas.

## Why It Matters
Permite resolver problemas que exceden la capacidad de un solo agente. Los agentes especializados pueden trabajar en paralelo y combinar resultados.

## Key Ideas
- Ejecución paralela de múltiples agentes
- Message passing entre agentes para coordinación
- Shared permissions para trabajar con los mismos recursos
- Cada agente tiene contexto y herramientas aisladas
- Complementa al patrón de subagentes (delegación jerárquica)

## Tradeoffs
- Más overhead de comunicación entre agentes
- Coordinación compleja puede introducir bugs
- Más tokens consumidos en total

## Related
- [[concepts/Subagent-Delegation]]
- [[concepts/Agent-Architecture]]
- [[tools/Claude-Code]]

## Source
[[summaries/Santtiagom-Learning-Claude-Code-Part-2]]
[[summaries/Subagent-Delegation]]
