---
title: 'Building cloud agent infrastructure: what''s different, and what we learned'
author: '@intuitiveml'
published: '2026-06-05'
type: article
resource: https://x.com/intuitiveml/status/2062699747224568212
timestamp: '2026-06-05T00:00:00Z'
description: 'El equipo de CREAO comparte dos lecciones clave al mover agents del
  desktop a la nube: separar lo que cambia lento del que cambia rápido, y mantener
  los secr...'
tags:
- summaries
---


# Building Cloud Agent Infrastructure

## Summary
El equipo de CREAO comparte dos lecciones clave al mover agents del desktop a la nube: separar lo que cambia lento del que cambia rápido, y mantener los secretos fuera del boundary de ejecución. Los frameworks de agents desktop asumen persistencia, identidad y confianza de red gratis — en la nube, cada garantía se reconstruye como sistema explícito. El modelo de seguridad asume que el código dentro del sandbox ya está comprometido.

## Core Concepts
- [[concepts/Cloud-Agent-Infrastructure]] -- plataforma para agents en la nube: sandboxes efímeros, hardware compartido, triggers automáticos, sin garantías de desktop
- [[concepts/Frozen-Sandbox-Snapshot]] -- snapshot inmutable del entorno del usuario (packages, files, versions) que garantiza reproducibilidad entre runs; el equivalente cloud de "pip install que resuelve a los mismos bytes para siempre"
- [[concepts/Runner-Hot-Swap]] -- desacoplar código de plataforma (runner) del entorno del usuario mediante hot-swap atómico de 300ms, inspirado en cómo los OS actualizan el kernel sin borrar /home
- [[concepts/API-Bridge-Pattern]] -- proxy que vive fuera del sandbox y adjunta credenciales OAuth del lado del host; el sandbox nunca ve tokens, solo envía HTTP requests al bridge
- [[concepts/Execution-Boundary]] -- modelo de seguridad que trata todo dentro del sandbox como comprometido por defecto; un JWT short-lived por run limita el daño si un sandbox es hijacked

## Key Insights
- Los agents cloud corren en sandboxes que boot fresh, en hardware compartido, triggerizados por schedules, HTTP requests u otros agents — el usuario suele estar dormido
- Problema de acoplamiento: el snapshot congela el entorno del usuario pero también contiene el runner de la plataforma — el usuario quiere estabilidad, la plataforma necesita deployar muchas veces al día
- Primer fix (brutal): si el runner del snapshot no matchea, tirar el snapshot y boot desde template limpio — funcionaba hasta que un cron job a las 9am perdió su entorno porque se deployó a las 8:55
- Fix final: hot-swap atómico del runner en 5 pasos (stage, validate, swap con chattr +i, purge V8 cache, kill on failure) en ~300ms
- Diagnostic question: para cualquier artefacto persistente, pregunta "¿quién controla la cadencia de cambio?" Si usuario y plataforma lo comparten, paga el acoplamiento — divide el artefacto por ownership boundary
- El bridge usa dos capas de verificación: IP allowlist (solo red interna de sandboxes) + JWT short-lived por run (scoped a user/app/session con expiry)
- Si un prompt injection logra que un agent dump process.env a un webhook, el atacante obtiene un JWT que solo funciona desde la red interna y expira con el run
- One executeAgent function maneja UI clicks, scheduled runs y API calls — billing, logs y observability idénticos sin importar el trigger; agregar un nuevo trigger es un cambio de routing, no de arquitectura

## Open Questions
- ¿El patrón de hot-swap de runner se aplica a otros componentes? ¿Model weights, MCP servers, o skills pueden actualizarse sin romper el snapshot congelado?
- ¿Cómo escalar el API bridge cuando cada usuario tiene credenciales diferentes para decenas de servicios? ¿Rate limiting, caching, o token rotation?
- ¿Existe un tradeoff entre la seguridad del API bridge y la latencia de cada llamada auth? ¿300ms para hot-swap vs overhead de bridge en cada API call?

## Source
- **Raw note:** [[raw-notes/building-cloud-agent-infrastructure-whats-different-and-what-we-]]
- **Original URL:** https://x.com/intuitiveml/status/2062699747224568212
