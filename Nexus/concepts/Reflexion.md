---
type: Concept
title: Reflexion
description: Patrón de planificación donde el agente aprende de errores pasados y
  retry con un enfoque mejorado. El agente mira sus propios errores, extrae lessons,
  y aju...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Reflexion

## Definition
Patrón de planificación donde el agente aprende de errores pasados y retry con un enfoque mejorado. El agente mira sus propios errores, extrae lessons, y ajusta su estrategia para la siguiente iteración del loop.

## Why It Matters
Permite que el agente mejore su propio performance con el tiempo, sin intervención humana. Es más eficiente que Tree of Thoughts para tareas donde los errores siguen patrones predecibles.

## Key Ideas
- El agente analiza sus propios errores como signal de training
- Aprende de cada fallo y ajusta la estrategia
- Retry con enfoque mejorado basado en el error anterior
- Más eficiente que explorar múltiples opciones (ToT) cuando los errores son patrones conocidos
- Complementa a Chain of Thought (planificación proactiva) y Tree of Thoughts (exploración)

## Tradeoffs
- Requiere que los errores sean diagnosticables y corregibles
- Puede entrar en loops si el agente no aprende correctamente
- Más efectivo en tareas con feedback claro que en tareas creativas

## Related
- [[concepts/Chain-of-Thought]]
- [[concepts/Tree-of-Thoughts]]
- [[concepts/Agent-Loop]]
- [[concepts/Agent-Guardrails]]

## Source
[[summaries/Alexxubyte-Agent-Anatomy-Loop]]
[[summaries/Santtiagom-What-Is-Agent-Part-3]]
