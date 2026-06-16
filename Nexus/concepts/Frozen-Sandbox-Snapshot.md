---
type: Concept
title: Frozen Sandbox Snapshot
description: Imagen inmutable del entorno de un agent (packages, files, versions)
  que se congela cuando el usuario está satisfecho y se mantiene congelada hasta que
  el us...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Frozen Sandbox Snapshot

## Definition
Imagen inmutable del entorno de un agent (packages, files, versions) que se congela cuando el usuario está satisfecho y se mantiene congelada hasta que el usuario edita el entorno nuevamente. Garantiza que Monday's run behaves like Friday's — reproducibilidad determinista en infraestructura cloud.

## Why It Matters
En desktop, un pip install de hace 6 meses resuelve a versiones diferentes hoy. Un snapshot cloud resuelve a los mismos bytes para siempre. La reproducibilidad es algo que la plataforma debe garantizar al usuario, y un snapshot congelado es la forma más barata de entregarla.

## Key Ideas
- **Freeze on satisfaction:** snapshot cuando el usuario está happy con su entorno, no en cada run
- **Deterministic boots:** cada run boots del mismo image — mismos packages, mismos files, mismas versiones
- **Ownership boundary:** el snapshot pertenece al usuario (cambia cuando el usuario elige), no a la plataforma (que deploya muchas veces al día)
- **Coupling problem:** si el snapshot también contiene código de plataforma, cada deployment fuerza una elección: runner stale o destruir el entorno congelado del usuario

## Tradeoffs
- Snapshots grandes aumentan boot time y storage cost
- Freezing el entorno puede retrasar security patches de packages del usuario
- Re-snapshot después de hot-swaps para bake-in cambios sin perder state del usuario

## Related
- [[concepts/Cloud-Agent-Infrastructure]]
- [[concepts/Runner-Hot-Swap]]

## Source
[[summaries/IntuitiveML-Building-Cloud-Agent-Infrastructure]]
