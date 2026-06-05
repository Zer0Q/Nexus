# API Bridge Pattern

## Definition
Proxy que vive fuera del sandbox y actúa como el único punto de cruce autenticado entre el agent y servicios externos. El sandbox envía HTTP requests al bridge, que adjunta credenciales OAuth del lado del host y reenvía la llamada — el token nunca entra en la memoria del sandbox.

## Why It Matters
En desktop, el agent corre como el usuario con sus keys. En cloud, el sandbox corre como nobody en hardware compartido ejecutando código potencialmente adversarial. El bridge mantiene las credenciales fuera del boundary de ejecución, haciendo que un sandbox comprometido no exponga tokens de largo plazo.

## Key Ideas
- **Two-layer verification:** IP allowlist (solo red interna de sandboxes) + JWT short-lived por run (scoped a user/app/session con expiry)
- **No long-lived credentials in sandbox:** regla absoluta, no aspiracional
- **Single interface:** el bridge también lleva billing, logs y metrics — es el único punto que cruza el sandbox boundary
- **Damage containment:** si un prompt injection logra que un agent exfilere process.env, el atacante obtiene un JWT que solo funciona desde la red interna y expira con el run

## Tradeoffs
- Latencia adicional por cada llamada auth (round-trip al bridge)
- El bridge se convierte en single point of failure — debe ser altamente disponible
- Escalabilidad: cada usuario tiene credenciales diferentes para decenas de servicios

## Related
- [[concepts/Execution-Boundary]]
- [[concepts/Cloud-Agent-Infrastructure]]
- [[concepts/Cloud-Security]]

## Source
[[summaries/IntuitiveML-Building-Cloud-Agent-Infrastructure]]
