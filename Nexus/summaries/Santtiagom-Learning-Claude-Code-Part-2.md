---
title: "Post by @santtiagom_ on X"
source: "https://x.com/santtiagom_/status/2051793738209669554"
author: "@santtiagom_"
published: "2026-05-03"
type: article
---

# Claude Code Architecture: 5 Layers

## Summary
@santtiagom_ resume la arquitectura de Claude Code en 5 capas: memoria persistente (CLAUDE.md), conocimiento modular (Skills), control de calidad (Hooks), delegación (Subagents) y distribución (Plugins), rodeado de MCP para integraciones y Agent Teams para coordinación paralela.

## Core Concepts
- [[tools/Claude-Code]] -- IDE de agente de Anthropic con arquitectura de 5 capas
- [[concepts/Agent-Architecture]] -- Estructura de capas: reglas → conocimiento → calidad → delegación → distribución
- [[concepts/Memory-Persistence]] -- CLAUDE.md como memoria persistente para reglas, arquitectura y contexto base
- [[concepts/Skill-Files]] -- Conocimiento modular que se activa solo cuando es necesario
- [[concepts/Hook-Mechanism]] -- Control y calidad a nivel sistema, independiente del prompt
- [[concepts/Subagent-Delegation]] -- Delegación con contexto aislado para tareas específicas
- [[concepts/Plugin-Distribution]] -- Distribución del comportamiento al equipo completo
- [[concepts/MCP]] -- Integraciones con APIs, databases y servicios SaaS externos
- [[concepts/Agent-Teams]] -- Ejecución paralela y coordinación entre múltiples agentes

## Key Insights
- Las 5 capas forman el core del agente: reglas → conocimiento → calidad → delegación → compartir con equipo
- MCP y Agent Teams están "alrededor" de las 5 capas, no dentro de ellas
- Skills se activan "cuando hace falta", no están siempre activas como CLAUDE.md
- Hooks funcionan a nivel sistema, no dependen del prompt — son deterministas
- La práctica: definís reglas → agregás conocimiento → asegurás calidad → delegás → compartís

## Open Questions
- ¿Cómo se diferencian las Skills de Claude Code de las Skills de Hermes Agent?
- ¿Agent Teams de Claude Code soporta message passing entre agentes como Hermes?
- ¿Se puede exportar un Plugin de Claude Code a otro framework de agentes?

## Source
- **Raw note:** [[summaries/Santtiagom-Learning-Claude-Code-Part-2]]
- **Original URL:** https://x.com/santtiagom_/status/2051793738209669554
