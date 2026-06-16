---
title: "Post by @santtiagom_ on X"
source: "https://x.com/santtiagom_/status/2066599044788553084"
author: "@santtiagom_"
published: "2026-06-13"
type: article
---

# Agent Planning Methods: CoT, ToT, Reflexion

## Summary
@santtiagom_ explica los métodos de planificación que usan los agentes para resolver problemas complejos: Chain of Thought (pensar paso a paso), Tree of Thoughts (explorar opciones) y Reflexion (aprender de errores). Cada método tiene diferentes tradeoffs entre precisión y eficiencia.

## Core Concepts
- [[concepts/Chain-of-Thought]] -- Método de planificación donde el modelo piensa paso a paso antes de actuar, descomponiendo el problema
- [[concepts/Tree-of-Thoughts]] -- Método que explora múltiples caminos de pensamiento y elige el mejor
- [[concepts/Reflexion]] -- Patrón donde el agente aprende de errores pasados y retry con mejora iterativa
- [[concepts/Agent-Loop]] -- Bucle ejecutar → observar → validar → corregir → repetir
- [[concepts/Agent-Guardrails]] -- Límites que controlan la autonomía del agente para evitar errores costosos

## Key Insights
- Chain of Thought: el modelo "piensa en voz alta" antes de actuar, descomponiendo el problema en pasos
- Tree of Thoughts: explora múltiples opciones simultáneamente y elige el mejor camino
- Reflexion: el agente mira sus errores pasados, aprende de ellos y retry con un enfoque diferente
- Tradeoff: ToT es más preciso pero más lento (explora más opciones); Reflexion es más eficiente a largo plazo
- Los métodos de planificación son parte del "Brain" del agente — la capa de reasoning

## Open Questions
- ¿Cuándo conviene usar ToT vs Chain of Thought?
- ¿Reflexion requiere memoria explícita o puede funcionar con el contexto actual?
- ¿Hay benchmarks que comparen estos métodos en tareas reales?

## Source
- **Raw note:** [[raw-notes/santtiagom-what-is-an-agent-part-3]]
- **Original URL:** https://x.com/santtiagom_/status/2066599044788553084
