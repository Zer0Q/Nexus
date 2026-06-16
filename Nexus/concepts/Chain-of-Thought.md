---
type: Concept
title: Chain of Thought
description: Método de planificación donde el modelo "piensa en voz alta" antes de
  actuar, descomponiendo el problema en pasos secuenciales. El modelo genera reasoning
  in...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Chain of Thought

## Definition
Método de planificación donde el modelo "piensa en voz alta" antes de actuar, descomponiendo el problema en pasos secuenciales. El modelo genera reasoning intermedio que guía la acción final.

## Why It Matters
Para tareas complejas que requieren múltiples pasos, el modelo necesita un camino de reasoning explícito para llegar a la respuesta correcta. Sin CoT, el modelo salta directamente a la respuesta y comete más errores.

## Key Ideas
- El modelo genera reasoning paso a paso antes de la respuesta final
- Descompone problemas complejos en sub-problemas más simples
- El reasoning intermedio sirve como "andamio cognitivo"
- Ampliamente usado en agentes para planning
- Complementa al Tree of Thoughts (múltiples caminos) y Reflexion (aprender de errores)

## Tradeoffs
- Más tokens consumidos (reasoning + respuesta)
- Más latencia (generar reasoning antes de actuar)
- No siempre mejora resultados — para tareas simples puede ser contraproducente

## Related
- [[concepts/Tree-of-Thoughts]]
- [[concepts/Reflexion]]
- [[concepts/Agent-Loop]]
- [[concepts/Agent-Guardrails]]

## Source
[[summaries/Alexxubyte-Agent-Anatomy-Loop]]
[[summaries/Santtiagom-What-Is-Agent-Part-3]]
