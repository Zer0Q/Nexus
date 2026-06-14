# Evidence Validation

## Definition
Proceso de verificar reliability de evidence antes de incluirlo en respuesta final. Parte fundamental del Agentic RAG workflow donde el agent evalúa si la información retrieved es confiable antes de usarla.

## Why It Matters
Sin validation, el agent puede usar información incorrecta o outdated como si fuera fact. La validación es lo que separa un agent que retrieve de uno que investiga.

## Key Ideas
- Evaluar reliability de cada piece de evidence retrieved
- Cross-reference entre múltiples fuentes cuando posible
- Determinar si evidence es suficiente o se necesita más context
- "Is this evidence reliable?" — pregunta clave del agent
- "Do I need more context?" — decide si search again
- Parte del loop: Reason → Search → Evaluate → Search Again
- MCP servers facilitan access a múltiples fuentes para cross-validation

## Tradeoffs
- Validation overhead vs speed de respuesta
- False positives: evidence que parece confiable pero no lo es
- False negatives: rechazar evidence válido por overly strict criteria
- Balance entre thoroughness y utility práctica

## Related
- [[concepts/Agentic-RAG]]
- [[concepts/Multi-Step-Reasoning]]
- [[concepts/Maker-Checker-Split]]

## Source
[[summaries/NainsiDwiv50980-agentic-rag-mcp]]
