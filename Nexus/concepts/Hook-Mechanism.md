---
type: Concept
title: Hook Mechanism
description: Comandos shell deterministas activados por eventos (PreToolUse, PostToolUse,
  SessionStart, Stop, SubagentStop) que enforcean calidad a nivel infraestructura,...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Hook Mechanism

## Definition
Comandos shell deterministas activados por eventos (PreToolUse, PostToolUse, SessionStart, Stop, SubagentStop) que enforcean calidad a nivel infraestructura, no a nivel prompt. Son la capa de guardrails del agente.

## Why It Matters
Los hooks son la capa que la mayoría de los equipos skippea y regrettea. Permiten auto-lint en cada Write, hard-block en comandos peligrosos (rm -rf), y notificaciones en eventos clave — calidad enforced a nivel infraestructura.

## Key Ideas
- Son comandos shell deterministas, NO IA — evento → matcher → comando
- 4 tipos de eventos: PreToolUse (antes de ejecutar), PostToolUse (después), SessionStart, Stop
- Auto-lint en cada Write, hard-block en rm -rf, Slack notification en Stop
- No dependen del prompt — son deterministas a nivel sistema
- Separan concerns: hooks manejan seguridad/qualidad, skills manejan proceso

## Tradeoffs
- Hooks requieren mantenimiento de scripts shell
- Pueden bloquear flujos legítimos si están mal configurados
- No son programables como las skills — más rígidos pero más confiables

## Related
- [[concepts/Agent-Guardrails]]
- [[concepts/Agent-Architecture]]
- [[tools/Claude-Code]]

## Source
[[summaries/LearnWithBrij-Learning-Claude-Code-Part-3]]
[[summaries/Santtiagom-Learning-Claude-Code-Part-1]]
