# Agent Guardrails

## Definition
Conjunto de mecanismos de seguridad que controlan la autonomía del agente para prevenir daño al sistema, datos o usuarios. Incluye sandboxing, validación de output, límites de tokens, límites de scope y human-in-the-loop.

## Why It Matters
Más autonomía = más necesidad de guardrails. Sin guardrails, un agente autónomo puede tomar decisiones costosas o destructivas. El balance entre autonomía y seguridad es el desafío central del diseño de agentes.

## Key Ideas
- Sandboxing: aislar la ejecución del agente para prevenir daño al sistema
- Output validation: verificar que la salida cumple reglas antes de aplicarla
- Token limits: prevenir loops infinitos y controlar costos
- Scope limits: definir claramente qué el agente puede y no puede hacer
- Human-in-the-loop: intervención humana para decisiones críticas
- No son estrictamente "anatomía" del agente pero son cruciales para producción

## Tradeoffs
- Más guardrails = menos autonomía pero más seguridad
- Guardrails mal configurados pueden bloquear flujos legítimos
- El balance óptimo depende del contexto de uso

## Related
- [[concepts/Hook-Mechanism]]
- [[concepts/Agent-Architecture]]
- 
- [[concepts/Evidence-Validation]]

## Source
[[summaries/Alexxubyte-Agent-Anatomy-Loop]]
[[summaries/Santtiagom-What-Is-Agent-Part-5]]
