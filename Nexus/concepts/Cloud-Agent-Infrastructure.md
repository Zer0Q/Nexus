# Cloud Agent Infrastructure

## Definition
Plataforma que ejecuta AI agents en sandboxes efímeros en hardware compartido, triggerizados por schedules, HTTP requests u otros agents — sin las garantías de desktop como persistencia, identidad o confianza de red. Cada run boots fresh, el código puede ser adversarial, y el usuario suele estar ausente.

## Why It Matters
Los frameworks de agents desktop asumen un solo usuario, una máquina, un proceso. En la nube, los agents son funciones que el resto del stack puede llamar — persistentes, remotas, y accesibles por callers que el usuario nunca anticipó. Requiere reconstruir como sistemas explícitos todo lo que el desktop da gratis.

## Key Ideas
- **Sandbox efímero:** cada run boots desde un snapshot congelado, no desde el filesystem del usuario
- **Hardware compartido:** el código dentro del sandbox se trata como potencialmente adversarial
- **Triggers múltiples:** UI clicks, cron jobs, API calls — un executeAgent maneja todos sin distinguir
- **Four properties:** state frozen until user changes, code hot-swappable, credentials host-side, single execution pipeline for all callers
- **Agent as function:** implementación del usuario, pero trigger surface, runtime y security boundary pertenecen a la plataforma

## Related
- [[concepts/Frozen-Sandbox-Snapshot]]
- [[concepts/Runner-Hot-Swap]]
- [[concepts/API-Bridge-Pattern]]
- [[concepts/Execution-Boundary]]
- [[concepts/Agent-Architecture-over-Intelligence]]

## Source
[[summaries/IntuitiveML-Building-Cloud-Agent-Infrastructure]]
