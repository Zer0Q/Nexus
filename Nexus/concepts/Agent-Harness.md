---
type: Concept
title: Agent Harness
description: 'Capa de coordinación que gestiona los componentes de un sistema de agente:
  decide qué memory cargar, cuándo usar tools, cómo verificar resultados y cuándo
  it...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Agent Harness

## Definition
Capa de coordinación que gestiona los componentes de un sistema de agente: decide qué memory cargar, cuándo usar tools, cómo verificar resultados y cuándo iterar. Es la "inteligencia de coordinación" — no reasoning, sino gestión de los componentes del agente.

## Why It Matters
Sin harness, un modelo con tools y memory es solo un conjunto de piezas sin coordinar. El harness es lo que convierte un modelo en un sistema operativo de agente capaz de perseguir objetivos complejos.

## Key Ideas
- Coordina: qué memory cargar, cuándo usar tools, cómo verificar resultados
- El loop (ejecutar → observar → validar → corregir → repetir) es gestionado por el harness
- La coordinación del contexto es el problema más difícil del harness
- Diferencia entre un modelo y un sistema de agente
- Cada framework tiene su propio patrón de harness: Claude Code, Hermes Agent, etc.

## Tradeoffs
- Más coordinación = más overhead de tokens
- Un harness demasiado rígido limita la flexibilidad del agente
- El balance óptimo depende del tipo de tareas

## Related
- [[concepts/Agent-Architecture]]
- [[concepts/Agent-Loop]]
- [[concepts/Context-Engineering]]
- [[concepts/Agent-Guardrails]]

## Source
[[summaries/Santtiagom-What-Is-Agent-Part-1]]
[[summaries/Santtiagom-What-Is-Agent-Part-2]]
[[summaries/Santtiagom-What-Is-Agent-Part-6-Harness]]
[[summaries/Context-Engineering]]
