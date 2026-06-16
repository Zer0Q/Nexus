# Context Rot

## Definition
Degración de la capacidad de reasoning del modelo cuando el contexto se llena de información irrelevante o redundante. El "ruido" en el contexto compite con la información relevante por la atención del modelo.

## Why It Matters
El context window tiene un límite físico. Cuando se llena de ruido, el modelo pierde capacidad de enfocarse en lo importante. Es uno de los problemas más críticos en agentes de larga duración.

## Key Ideas
- El contexto acumula mensajes, archivos, resultados de tools — no toda es relevante
- La atención del modelo se distribuye entre todo el contexto, no solo lo relevante
- Más contexto no siempre = mejor resultado — la densidad de signal importa más
- El harness debe gestionar activamente: incluir relevante, resumir antiguo, eliminar irrelevante
- La compresión de contexto es una habilidad clave para agentes de producción

## Tradeoffs
- Comprimir demasiado = perder información importante
- Mantener demasiado = degradar el reasoning
- El balance óptimo depende del tipo de tarea y la longitud del contexto

## Related
- [[concepts/Context-Engineering]]
- [[concepts/Context-Window]]
- [[concepts/Memory-Persistence]]
- [[concepts/Agent-Harness]]

## Source
[[summaries/Santtiagom-What-Is-Agent-Part-2]]
[[summaries/Memory-Persistence]]
[[summaries/Context-Engineering]]
