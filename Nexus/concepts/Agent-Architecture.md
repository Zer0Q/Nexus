# Agent Architecture

## Definition
Estructura de capas que envuelve a un LLM para hacerlo operativo como sistema autónomo. El principio "thin harness, fat skills" establece que el harness debe ser mínimo (loop, archivos, contexto, seguridad) y el conocimiento debe vivir en skills.

## Why It Matters
La diferencia entre usuarios 10x y 100x de agentes no es el modelo, sino la arquitectura. Un buen harness da al modelo el contexto correcto en el momento correcto sin drowning en ruido.

## Key Ideas
- Las capas típicas: memoria, conocimiento, guardrails, delegación, distribución
- El bottleneck nunca es la inteligencia del modelo — los modelos ya saben razonar
- Los modelos fallan porque no entienden TU data: schema, convenciones, forma particular del problema
- Anti-pattern: fat harness con 40+ tool definitions comiendo el context window
- Markdown como lenguaje de programación: skills describen proceso, judgment y contexto

## Tradeoffs
- Más capas = más capacidad pero más complejidad
- Thin harness reduce tokens y latencia pero requiere skills bien diseñadas
- Fat skills requieren más mantenimiento pero escalan mejor

## Related
- [[concepts/Agent-Loop]]
- [[concepts/Skill-Files]]
- [[concepts/Context-Window]]
- [[tools/Claude-Code]]
- [[tools/Hermes-Agent]]

## Source
[[summaries/LearnWithBrij-Learning-Claude-Code-Part-3]]
[[summaries/GarryTan-Thin-Harness-Fat-Skills]]
[[summaries/Santtiagom-What-Is-Agent-Part-1]]
