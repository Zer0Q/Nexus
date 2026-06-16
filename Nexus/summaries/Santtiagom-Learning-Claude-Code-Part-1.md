---
title: Post by @santtiagom_ on X
author: '@santtiagom_'
published: '2026-03-22'
type: article
resource: https://x.com/santtiagom_/status/2053851364787134536
timestamp: '2026-03-22T00:00:00Z'
description: '@santtiagom_ comparte su ruta de aprendizaje para Claude Code: empezar
  por el agente loop, permisos, memoria, MCP, skills, subagents, hooks y planning
  antes ...'
tags:
- summaries
---


# Learning Claude Code: The Roadmap

## Summary
@santtiagom_ comparte su ruta de aprendizaje para Claude Code: empezar por el agente loop, permisos, memoria, MCP, skills, subagents, hooks y planning antes de avanzar a conceptos avanzados como context engineering, harness y multi-agent workflows.

## Core Concepts
- [[concepts/Agent-Loop]] -- Entender cómo el agente piensa, ejecuta acciones, verifica resultados y corrige errores
-  -- Sistema de approvals y auto mode que determina qué Claude puede ejecutar automáticamente
- [[concepts/Memory-Persistence]] -- Guardar reglas, comandos y contexto en CLAUDE.md para no repetir en cada sesión
- [[concepts/MCP]] -- Protocolo para conectar Claude Code con GitHub, Slack, databases y herramientas externas
- [[concepts/Skill-Files]] -- Crear workflows reutilizables para tareas repetitivas o específicas del proyecto
- [[concepts/Subagent-Delegation]] -- Dividir tareas grandes en agentes separados para mantener el contexto limpio
- [[concepts/Prompt-Engineering]] -- Escribir prompts efectivos con contexto, datos, instrucciones, reglas y formato de output
-  -- Usar /compact, /clear, --resume y --continue para manejar sesiones largas
- [[concepts/Context-Engineering]] -- Concepto avanzado: diseñar el contexto que se pasa al modelo

## Key Insights
- La ruta de aprendizaje prioriza fundamentos sobre features avanzadas: primero el agente loop, luego todo lo demás
- Permissions & Auto Mode: entender qué Claude puede ejecutar automáticamente vs. qué necesita approval
- Rewind & checkpoints: volver atrás cuando Claude rompe algo o toma un mal camino
- Effort levels: cuándo usar think, ultrathink o distintos niveles de razonamiento según la tarea
- Conceptos avanzados solo después de dominar los fundamentos: context engineering, harness, context rot, multi-agent workflows

## Open Questions
- ¿Cómo se comparan los effort levels (think, ultrathink) con los modelos de razonamiento de otros agentes?
- ¿Qué patrón de session management funciona mejor para proyectos grandes con múltiples archivos?
- ¿El context rot de Claude Code es equivalente a la memory management de Hermes?

## Source
- **Raw note:** [[summaries/Santtiagom-Learning-Claude-Code-Part-1]]
- **Original URL:** https://x.com/santtiagom_/status/2053851364787134536
