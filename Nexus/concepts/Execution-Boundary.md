---
type: Concept
title: Execution Boundary
description: Modelo de seguridad para agents en la nube que trata todo dentro del
  sandbox como comprometido por defecto. No confía en el código del agent, asume que
  puede...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Execution Boundary

## Definition
Modelo de seguridad para agents en la nube que trata todo dentro del sandbox como comprometido por defecto. No confía en el código del agent, asume que puede ser adversarial, y contiene el daño mediante JWT short-lived, IP allowlists y la regla de que las credenciales de largo plazo nunca viven dentro del sandbox.

## Why It Matters
Un agent desktop corre como el usuario en su máquina. Un agent cloud corre como nobody en hardware compartido, ejecutando código que un LLM escribió desde un prompt que puede haber sido adversarial. El modelo de seguridad debe asumir compromiso, no esperar lo contrario.

## Key Ideas
- **Default-compromised model:** todo dentro del sandbox se trata como no-confiable por diseño
- **JWT per run:** token firmado al boot, scoped a user/app/session, con expiry que cubre solo la ventana del run
- **IP allowlist:** el bridge solo acepta conexiones del rango de red interna de sandboxes
- **No master credential:** si un sandbox es hijacked, el atacante hereda un token que muere con el run y solo autoriza calls scoped a esa sesión
- **Everything else is compromised:** billing, logs, metrics salen por el bridge; todo lo demás dentro del sandbox es no-confiable

## Tradeoffs
- Overhead de verificación en cada llamada al bridge
- Complejidad de运营管理: firmar, verificar y rotar JWTs por run
- Debugging más difícil: no puedes simplemente entrar al sandbox y ver los tokens

## Related
- [[concepts/API-Bridge-Pattern]]
- [[concepts/Cloud-Agent-Infrastructure]]
- [[concepts/Cloud-Security]]

## Source
[[summaries/IntuitiveML-Building-Cloud-Agent-Infrastructure]]
