# Runner Hot-Swap

## Definition
Mecanismo para actualizar el código de plataforma (runner) dentro de un sandbox sin destruir el snapshot congelado del usuario. Inspirado en cómo los OS actualizan el kernel sin borrar /home — separa lo que cambia rápido (runner) de lo que cambia lento (entorno del usuario).

## Why It Matters
El usuario quiere su entorno estable. La plataforma necesita deployar muchas veces al día. Unirlos en un solo artefacto fuerza una elección tóxica en cada deployment. El hot-swap permite que cada lado evolucione en su propio reloj.

## Key Ideas
- **5-step atomic swap:** (1) stage new runner en temp dir, (2) validate con node --check, (3) atomic swap con chattr +i, (4) purge V8 compile cache, (5) kill sandbox on failure
- **~300ms swap time:** suficiente para ser imperceptible, lo suficientemente lento para que el bake-in post-run sea la ruta normal
- **Diagnostic question:** "¿Quién controla la cadencia de cambio en este artefacto?" Si usuario y plataforma lo comparten, divide el artefacto por ownership boundary
- **Bake-in:** después de un run exitoso con runner swapped, re-snapshot para que el próximo run skip el swap

## Tradeoffs
- Complejidad operativa: 5 pasos con rollback en cada uno
- V8 cache purge necesario — sin esto, el runner stale se ejecuta desde bytecode cached
- chattr +i para inmutabilidad, pero requiere esconder el binary de chattr para que el sandbox no lo revierta

## Related
- [[concepts/Frozen-Sandbox-Snapshot]]
- [[concepts/Cloud-Agent-Infrastructure]]

## Source
[[summaries/IntuitiveML-Building-Cloud-Agent-Infrastructure]]
