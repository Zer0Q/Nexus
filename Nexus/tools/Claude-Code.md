---
type: Tool
title: Claude Code
description: 'IDE de agente de código de Anthropic que envuelve un LLM con una arquitectura
  de 5 capas: memoria persistente (CLAUDE.md), conocimiento modular (Skills), gua...'
tags:
- tools
timestamp: '2026-06-16T13:58:58Z'
---

# Claude Code

## Definition
IDE de agente de código de Anthropic que envuelve un LLM con una arquitectura de 5 capas: memoria persistente (CLAUDE.md), conocimiento modular (Skills), guardrails deterministas (Hooks), delegación con contexto aislado (Subagents) y distribución en equipo (Plugins).

## Why It Matters
La diferencia entre usuarios 10x y 100x no es el modelo sino la arquitectura. Claude Code implementa el principio "thin harness, fat skills" de forma nativa.

## Key Ideas
- CLAUDE.md tiene dos scopes: global (~/.claude/) y por proyecto (.claude/)
- Skills se activan on-demand, no están siempre activas
- Hooks son comandos shell deterministas (PreToolUse, PostToolUse, SessionStart, Stop)
- Subagents no pueden spawnear subagents — límites duros por diseño
- Plugins empaquetan skills + agents + hooks + commands para distribución en equipo

## Related
- [[concepts/Agent-Architecture]]
- [[concepts/Skill-Files]]
- [[concepts/Hook-Mechanism]]
- [[concepts/Subagent-Delegation]]
- [[tools/Hermes-Agent]]

## Source
[[summaries/LearnWithBrij-Learning-Claude-Code-Part-3]]
[[summaries/Santtiagom-Learning-Claude-Code-Part-1]]
[[summaries/GarryTan-Thin-Harness-Fat-Skills]]
