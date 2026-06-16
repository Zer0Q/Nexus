# Tree of Thoughts

## Definition
Método de planificación donde el modelo explora múltiples caminos de pensamiento simultáneamente, evalúa cada uno, y elige el mejor. Es una generalización de Chain of Thought que permite branching y pruning.

## Why It Matters
Para problemas donde una sola línea de reasoning no es suficiente, ToT permite explorar opciones y elegir la mejor ruta. Es más preciso que Chain of Thought pero más costoso en tokens y latencia.

## Key Ideas
- Explora múltiples caminos de pensamiento (branching)
- Evalúa cada camino antes de avanzar (pruning)
- Elige el mejor camino para la siguiente iteración
- Más preciso que Chain of Thought para problemas complejos
- Más costoso: más tokens y latencia por explorar múltiples opciones
- Complementa a Chain of Thought (un camino) y Reflexion (aprender de errores)

## Tradeoffs
- Más tokens = más costo y latencia
- Más branching = más precisión pero más riesgo de overthinking
- No siempre mejora resultados — para problemas bien definidos, CoT es suficiente

## Related
- [[concepts/Chain-of-Thought]]
- [[concepts/Reflexion]]
- [[concepts/Agent-Loop]]
- [[concepts/Agent-Guardrails]]

## Source
[[summaries/Alexxubyte-Agent-Anatomy-Loop]]
[[summaries/Santtiagom-What-Is-Agent-Part-3]]
