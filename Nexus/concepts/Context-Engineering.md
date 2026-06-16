# Context Engineering

## Definition
Diseñar intencionalmente el contexto que se pasa al modelo para compensar la naturaleza stateless de los LLMs. Incluye qué información incluir, cómo organizarla, cuándo resumir y cuándo eliminar información.

## Why It Matters
Los LLMs son stateless — no recuerdan nada entre llamadas. Toda la "memoria" se construye artificialmente pasando contexto en cada request. El contexto mal diseñado causa context rot y degrada la capacidad de reasoning del modelo.

## Key Ideas
- Stateless = cada request es independiente, no hay estado interno entre llamadas
- El contexto acumula: mensajes, instrucciones, archivos, resultados de tools
- Context rot = cuando el contexto se llena de ruido y el modelo pierde capacidad de reasoning
- El harness debe gestionar activamente: incluir relevante, resumir antiguo, eliminar irrelevante
- Más contexto no siempre = mejor resultado — la densidad de signal importa más que el volumen

## Tradeoffs
- Más contexto = más tokens = más costo y latencia
- Contexto muy comprimido = pérdida de información importante
- El balance óptimo depende del tipo de tarea

## Related
- [[concepts/Context-Window]]
- [[concepts/Memory-Persistence]]
- 
- 

## Source
[[summaries/Santtiagom-Learning-Claude-Code-Part-1]]
[[summaries/Santtiagom-What-Is-Agent-Part-2]]
