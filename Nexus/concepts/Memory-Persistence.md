# Memory Persistence

## Definition
Mecanismo de guardar información importante entre sesiones para que el agente no empiece desde cero cada vez. Se implementa mediante archivos como CLAUDE.md (global y por proyecto) o sistemas de memoria persistente del framework.

## Why It Matters
Sin memory, cada sesión requiere re-explicar todo: quién sos, qué estás construyendo, qué decisiones ya tomaste. La memory permite recuperar información de sesiones anteriores y volver a ponerla en contexto cuando hace falta.

## Key Ideas
- CLAUDE.md tiene dos scopes: global (~/.claude/) y por proyecto (.claude/)
- La "memoria" de un agente es artificial: se construye pasando el contexto anterior como parte del prompt
- Long-term memory = vector stores, files, knowledge bases
- Cuando el context window se llena, los agentes resumen turns viejos y avanzan con el resumen
- Cada framework tiene su propio mecanismo: CLAUDE.md (Claude Code), SOUL.md + persistent memory (Hermes)

## Tradeoffs
- Más memory = más contexto pero más tokens consumidos
- Memory mal gestionada puede incluir información irrelevante
- La calidad del resumen determina cuánto se pierde al comprimir

## Related
- [[concepts/Context-Window]]
- 
- 
- [[tools/Claude-Code]]
- [[tools/Hermes-Agent]]

## Source
[[summaries/LearnWithBrij-Learning-Claude-Code-Part-3]]
[[summaries/Santtiagom-Learning-Claude-Code-Part-1]]
[[summaries/Santtiagom-Learning-Hermes-Part-1]]
[[summaries/Santtiagom-What-Is-Agent-Part-1]]
