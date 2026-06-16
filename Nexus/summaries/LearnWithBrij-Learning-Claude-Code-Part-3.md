---
title: Post by @LearnWithBrij on X
author: '@LearnWithBrij'
published: '2026-05-03'
type: article
resource: https://x.com/LearnWithBrij/status/2050803172793372769
timestamp: '2026-05-03T00:00:00Z'
description: '@LearnWithBrij describe las 5 capas arquitecturales de Claude Code que
  van más allá de las funcionalidades visibles: memoria persistente (CLAUDE.md), conocim...'
tags:
- summaries
---


# Claude Code Architectural Layers

## Summary
@LearnWithBrij describe las 5 capas arquitecturales de Claude Code que van más allá de las funcionalidades visibles: memoria persistente (CLAUDE.md), conocimiento modular (Skills), guardrails deterministas (Hooks), delegación con contexto aislado (Subagents) y distribución en equipo (Plugins). Cada capa resuelve un problema que los LLMs por sí solos no pueden resolver.

## Core Concepts
- [[tools/Claude-Code]] -- IDE de agente de Anthropic con arquitectura de 5 capas para desarrollo agentic
- [[concepts/Agent-Architecture]] -- Estructura de capas que envuelve al LLM: memoria, conocimiento, guardrails, delegación y distribución
- [[concepts/Memory-Persistence]] -- Mecanismo de guardar contexto entre sesiones mediante archivos como CLAUDE.md
- [[concepts/Skill-Files]] -- Documentos markdown reutilizables que enseñan al modelo cómo realizar tareas específicas
- [[concepts/Hook-Mechanism]] -- Comandos shell deterministas activados por eventos (PreToolUse, PostToolUse, SessionStart) que enforcing calidad a nivel infraestructura
- [[concepts/Subagent-Delegation]] -- Patrón donde el agente principal delega sub-tareas a agentes con contexto y permisos aislados
- [[concepts/Plugin-Distribution]] -- Empaquetado de skills + agents + hooks + commands para distribución en equipo

## Key Insights
- Las 4 capas que no tienen que ver con prompting (Skills, Hooks, Subagents, Plugins) son las que realmente separan a los usuarios 100x de los demás
- CLAUDE.md tiene dos scopes: global (~/.claude/) y por proyecto (.claude/), funcionando como la "constitución" del agente
- Los Hooks son comandos shell deterministas, NO IA: auto-lint en cada Write, hard-block en rm -rf, notificaciones en Stop
- Subagents no pueden spawnear subagents — límites duros por diseño para mantener el contexto principal limpio
- Los Plugins son como paquetes npm pero para comportamiento del agente: "bundle your skills + agents + hooks + commands"
- La stack en una línea: CLAUDE.md → Skills → Hooks → Subagents → Plugins
- MCP servers a la izquierda (GitHub, DBs, APIs), Agent Teams a la derecha (ejecución paralela)

## Open Questions
- ¿Cómo se comparan las 5 capas de Claude Code con la arquitectura de Hermes Agent (SOUL.md, Skills, Hooks, Memory)?
- ¿Los Hooks de Claude Code son equivalentes a los event hooks de Hermes o tienen un modelo de ejecución diferente?
- ¿Se pueden combinar Skills de Claude Code con hooks de Hermes para crear workflows híbridos?

## Source
- **Raw note:** [[summaries/LearnWithBrij-Learning-Claude-Code-Part-3]]
- **Original URL:** https://x.com/LearnWithBrij/status/2050803172793372769
