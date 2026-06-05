# POMDP

## Definition
Partially Observable Markov Decision Process — marco formal que describe cómo un agente interactúa con un mundo: agente → acción → estado → observación → agente.

## Why It Matters
Es la estructura que dio significado técnico al término "world model". Los diferentes tipos de world models (renderers, simulators, planners) son diferentes proyecciones del mismo loop POMDP, cada uno outputteando una pieza diferente.

## Key Ideas
- El agente nunca ve el estado directamente — solo observaciones parciales (fotones en retina, readings de sensor, píxeles)
- State: descripción completa de qué pasa en el mundo (objetos, posiciones, velocidades, propiedades) — completa en principio pero nunca directamente visible
- Observations: vista parcial del estado por parte del agente
- Actions: lo que el agente hace en respuesta
- El loop es la base de reinforcement learning textbooks (Sutton & Barto)
- Kenneth Craik (1943) propuso que las mentes razonan corriendo "small-scale models" de la realidad

## Related
- [[concepts/World-Models]]
- [[concepts/World-Model-Renderer]]
- [[concepts/World-Model-Simulator]]
- [[concepts/World-Model-Planner]]

## Source
[[summaries/DrFeifei-A-Functional-Taxonomy-of-World-Models]]
