# Learning Loop

## Definition
Mecanismo por el cual un agente guarda aprendizajes de la experiencia y los convierte en capacidades reutilizables. Puede crear nuevas skills o mejorar las existentes basándose en lo aprendido.

## Why It Matters
Es lo que diferencia a un agente de una herramienta estática. Un agente con learning loop se vuelve más efectivo con el tiempo, acumulando conocimiento y mejorando sus capacidades.

## Key Ideas
- El agente guarda experiencias como nuevas skills o mejoras a existentes
- Si al revisar PRs aparecen seguido problemas de permisos, ese aprendizaje mejora la skill
- El aprendizaje puede derivar en skills más específicas (ej: "review de endpoints públicos")
- No es un prompt suelto — es conocimiento formalizado que persiste entre sesiones
- Es el núcleo del valor a largo plazo de un sistema de agente

## Tradeoffs
- Aprendizajes incorrectos pueden degradar la efectividad del agente
- Demasiadas skills pueden inflar el contexto
- El aprendizaje automático sin supervisión puede derivar en comportamientos no deseados

## Related
- [[concepts/Skill-Files]]
- [[concepts/Memory-Persistence]]
- 
- [[tools/Hermes-Agent]]

## Source
[[summaries/Santtiagom-Learning-Hermes-Part-1]]
[[summaries/Santtiagom-Learning-Hermes-Part-2]]
