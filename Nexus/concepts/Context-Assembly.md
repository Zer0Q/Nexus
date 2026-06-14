# Context Assembly

## Definition
Problema de ensamblar contexto desde superficies de conocimiento mutuamente incompatibles para que un agent pueda responder preguntas que requieren información multi-sistema.

## Why It Matters
Cada agent builder resuelve el mismo context-assembly problem desde scratch. Sin estandarización (como OKF), cada integración requiere custom code, cada data source necesita custom connector, cada workflow se convierte en maintenance nightmare.

## Key Ideas
- Ejemplo: "Why did revenue drop in Q2?" requiere context de docs, Slack, CRM, analytics, SQL, meeting notes
- Vector search alone can't navigate estas fuentes heterogéneas
- Cada vendor tiene su propio SDK y schema — ninguno compatible
- OKF reduce necesidad de custom integration
- Agentic RAG trata retrieval como capability callable en vez de infrastructure
- MCP servers estandarizan access a external tools

## Tradeoffs
- Custom integration = más control pero más mantenimiento
- Standardization = menos per-control pero más reuse
- Costo de build vs cost de maintain cada integración
- Tension entre flexibility y interoperabilidad

## Related
- [[concepts/Open-Knowledge-Format]]
- [[concepts/Knowledge-Interoperability]]
- [[concepts/Knowledge-Fragmentation]]
- [[concepts/Metadata-as-Code]]

## Source
[[summaries/google-open-knowledge-format-okf]]
