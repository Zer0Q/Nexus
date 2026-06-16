# Agent Definition

## Definition
Sistema que combina modelo, contexto, memory, tools, harness y loop para perseguir objetivos de forma autónoma. Un agente no es solo un modelo con tools — es la coordinación de todos estos componentes en un loop de ejecución.

## Why It Matters
La definición correcta de agente es fundamental para diseñar sistemas efectivos. Confundir un modelo con un agente lleva a arquitecturas deficientes que no escalan.

## Key Ideas
- Modelo + Tools + Context + Memory + Harness + Loop = Agente completo
- Cada componente resuelve un problema específico que el modelo por sí solo no puede resolver
- El loop es lo que permite perseguir objetivos, no solo responder preguntas
- La autonomía viene del loop, no del modelo
- Los agentes más efectivos coordinan mejor sus componentes, no tienen el mejor modelo

## Tradeoffs
- Más componentes = más capacidad pero más complejidad
- Un componente débil limita todo el sistema
- El balance óptimo depende del caso de uso

## Related
- [[concepts/Agent-Architecture]]
- [[concepts/Agent-Loop]]
- [[concepts/Agent-Harness]]
- [[concepts/Memory-Persistence]]

## Source
[[summaries/Santtiagom-What-Is-Agent-Part-1]]
[[summaries/Santtiagom-What-Is-Agent-Part-7]]
