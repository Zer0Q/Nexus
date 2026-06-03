# LLM Hallucination

## Definition
Generación de respuestas falsas, inventadas o incorrectas con alta confianza por parte de un LLM. Ocurre porque el modelo predice el token más probable basado en patrones de entrenamiento, no verifica hechos.

## Why It Matters
Es el modo de fallo core de los LLMs. Sin mitigación, los productos de IA en producción generan información errónea que daña credibilidad y puede causar daños.

## Key Ideas
- El modelo no intenta decir la verdad: completa patrones
- Cita papers inexistentes, describe funciones de API no creadas, inventa estadísticas
- Nunca suena incierto: la confianza es independiente de la veracidad
- Mitigaciones: RAG (datos reales, no memoria), capas de verificación, tool calls (que el modelo verifique, no adivine)
- Nunca usar output crudo de LLM para hechos en producción sin verificación

## Related
- [[RAG]]
- [[Context-Window]]
- [[Temperature-Parameter]]

## Source
[[Sairahul1-10-AI-Concepts]]
