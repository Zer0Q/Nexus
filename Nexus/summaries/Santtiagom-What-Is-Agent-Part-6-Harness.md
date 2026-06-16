---
title: Post by @santtiagom_ on X
author: '@santtiagom_'
published: '2026-06-15'
type: article
resource: https://x.com/santtiagom_/status/2068139076377595384
timestamp: '2026-06-15T00:00:00Z'
description: '@santtiagom_ explica el patrón del harness: la capa que coordina todo
  en un sistema de agente — qué memory cargar, cuándo usar tools, cómo verificar resultad...'
tags:
- summaries
---


# Agent Harness Patterns

## Summary
@santtiagom_ explica el patrón del harness: la capa que coordina todo en un sistema de agente — qué memory cargar, cuándo usar tools, cómo verificar resultados. El harness es lo que diferencia un sistema de agente de un modelo de lenguaje aislado.

## Core Concepts
- [[concepts/Agent-Harness]] -- Capa de coordinación que gestiona memory, tools y verificación de resultados
- [[concepts/Agent-Loop]] -- Bucle ejecutar → observar → validar → corregir → repetir
- [[concepts/Memory-Persistence]] -- Gestión de qué información de memory cargar en cada paso del loop
- [[concepts/Tool-Use]] -- Coordinación de cuándo y qué tools usar
- [[concepts/Evidence-Validation]] -- Verificación de que los resultados del agente son correctos

## Key Insights
- El harness coordina: qué memory cargar, cuándo usar tools, cómo verificar resultados
- Sin harness, un modelo con tools y memory es solo un conjunto de piezas sin coordinar
- El harness es la capa de "inteligencia de coordinación" — no reasoning, sino gestión
- La coordinación del contexto es el problema más difícil del harness
- El loop (ejecutar → observar → validar → corregir → repetir) es gestionado por el harness

## Open Questions
- ¿Qué patrones de harness existen más allá de Claude Code y Hermes?
- ¿El harness puede ser a su vez un agente (meta-harness)?
- ¿Cómo se mide la efectividad de un harness?

## Source
- **Raw note:** [[raw-notes/santtiagom-what-is-an-agent-part-6-harness]]
- **Original URL:** https://x.com/santtiagom_/status/2068139076377595384
