# Knowledge Interoperability

## Definition
Capacidad de knowledge bases escritas por diferentes producers (teams, vendors, frameworks) de ser consumidas por diferentes consumers (agents, tools, humans) sin necesidad de translation o custom integration.

## Why It Matters
La fragmentación de knowledge en organizaciones impide que agents respondan preguntas que requieren contexto multi-sistema. Interoperabilidad permite que agents naveguen entre docs, Slack, CRM, SQL, analytics sin custom connectors para cada fuente.

## Key Ideas
- OKF busca resolver esto con schema acordado para metadata
- Cada vendor tiene su propio catálogo, SDK y schema — ninguno portable
- "Every agent builder is solving same context-assembly problem from scratch"
- "Every catalog vendor reinventing same data models"
- Knowledge locked behind surface que lo creó
- Estándares como OKF permiten cross-platform consumption
- Similar a cómo YAML frontmatter unifica metadata entre Hugo, Obsidian, Notion

## Tradeoffs
- Standardización vs flexibility para casos específicos
- Adoption threshold: necesita múltiples producers para ser útil
- Schema evolution: cómo mantener compatibilidad con versiones nuevas
- Tension entre simplicity (OKF) y comprehensiveness (vendor schemas)

## Related
- [[concepts/Open-Knowledge-Format]]
- [[concepts/Knowledge-Fragmentation]]
- [[concepts/Context-Assembly]]
- [[concepts/Metadata-as-Code]]

## Source
[[summaries/google-open-knowledge-format-okf]]
