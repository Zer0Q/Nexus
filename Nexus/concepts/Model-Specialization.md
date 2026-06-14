# Model Specialization

## Definition
Estrategia de usar diferente modelo de IA para cada tipo de task en vez de sticking a un solo modelo, aprovechando las specialties de cada frontier model.

## Why It Matters
Tres frontier models landing en misma semana cada uno con specialty clara: Kimi K2.6 para multi-agent orchestration, Claude Opus 4.8 para code quality, GPT-5.5 para computer use. Los winners son los que route cada task al right model.

## Key Ideas
- Kimi K2.6: specialty en multi-agent coordination (300 sub-agents), SWE tasks
- Claude Opus 4.8: specialty en production code quality, legal-grade precision, vision
- GPT-5.5: specialty en computer use (78.7% OSWorld), web research (90.1% BrowseComp)
- "Los losers son developers que picked one y stuck to it"
- Cada model tiene diferente cost structure y performance profile
- Routing task al right model = mejor output + menor cost

## Tradeoffs
- Más complexity en routing logic vs un solo model
- Vendor lock-in risk con múltiples providers
- Context switching entre models
- Cost management con múltiples pricing structures

## Related
- [[concepts/Kimi-K26]]
- [[concepts/Parallelization]]
- [[concepts/Coordinator-Pattern]]

## Source
[[summaries/Khairallah-300-AI-Agents-Parallel]]
