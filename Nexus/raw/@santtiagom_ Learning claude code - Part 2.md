---
title: "Post by @santtiagom_ on X"
source: "https://x.com/santtiagom_/status/2051793738209669554"
author:
  - "[[@santtiagom_]]"
published: 2026-05-03
created: 2026-06-16
description: "Claude Code está armado sobre una arquitectura bastante clara. Tiene 5 capas: 1) CLAUDE.md → memoria persistente (reglas, arquitectura, co"
tags:
  - "clippings"
summary:
---
Claude Code está armado sobre una arquitectura bastante clara.

Tiene 5 capas:

1) CLAUDE.md → memoria persistente (reglas, arquitectura, contexto base)

2) Skills → conocimiento modular que se activa cuando hace falta

3) Hooks → control y calidad a nivel sistema (no depende del prompt)

4) Subagents → delegación con contexto aislado

5) Plugins → distribución de todo eso al equipo

Estas 5 capas forman el core del agente.

Alrededor de eso:

MCP → integraciones (APIs, DBs, SaaS)

Agent Teams → ejecución en paralelo y coordinación

Cómo funciona en la práctica:

definís reglas → agregás conocimiento → asegurás calidad → delegás tareas → lo compartís con el equipo

> **Brij Pandey @LearnWithBrij** · 2026-05-03
> 
> Claude Code ships with 5 architectural layers most engineers never open.
> 
> Not features. Not settings. Layers — each solving a distinct problem that LLMs alone can't solve. And four of them have nothing to do with prompting.
> 
> Here's the full Agent Development Kit:
> 
> Layer 1 —
> 
> ![Imatge](https://pbs.twimg.com/media/HHXqmmmaIAAyN5Y?format=jpg&name=large)