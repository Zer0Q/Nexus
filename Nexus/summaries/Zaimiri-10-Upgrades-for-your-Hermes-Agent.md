---
title: "10 Upgrades for your Hermes Agent"
source: "https://x.com/zaimiri/status/2062512177295090046"
author: "@zaimiri"
published: "2026-06-04"
type: article
---

# 10 Upgrades for your Hermes Agent

## Summary
Guía progresiva para transformar Hermes de un agente conversacional a un sistema fiable de uso diario. Propone 10 mejoras ordenadas por impacto: desde conectar un vault de Obsidian y Telegram hasta configurar webhooks, perfiles separados y Kanban para coordinación multi-agente. El enfoque clave es construir una capa a la vez en lugar de intentar implementar todo simultáneamente.

## Core Concepts
- [[concepts/Hermes-Agent-Architecture]] -- framework de agente local con skills, memory, cron, perfiles y gateways
- [[tools/Telegram-Bot-Capture]] -- gateway de Telegram como interfaz diaria para enviar voz, capturas, links y aprobar comandos sin abrir terminal
- [[concepts/Skill-Curation-System]] -- SOPs en markdown que el agente carga según el tipo de tarea, reduciendo trabajo repetitivo
- [[concepts/Persistent-AI-Helpers]] -- memoria persistente con hechos estables (preferencias, paths, quirks de herramientas) inyectada al inicio de cada sesión
- [[concepts/Scoped-Vault-Access]] -- restricción de toolsets por lane (research, code, content) para reducir ruido y errores del agente
- [[concepts/Agent-Cron-Scheduler]] -- jobs programados para checks recurrentes (brief diario, watchdogs, digest semanal)
- [[concepts/Agent-Profiles]] -- perfiles separados con config, memory y skills independientes para aislar contextos (research vs code vs client)
- [[concepts/MCP]] -- protocolo para conectar agentes a sistemas externos (GitHub, DBs, APIs) de forma estandarizada
- [[concepts/Agent-Swarm-Architecture]] -- delegación a subagents + Kanban para coordinación durable más allá de una sola sesión

## Key Insights
- El mapa de setup rápido va desde 10 minutos (Telegram) hasta 90 minutos (webhooks con GitHub/Stripe)
- Telegram privacy mode puede hacer que un bot parezca roto en grupos — verificar o hacerlo admin
- Un buen skill tiene 4 partes: cuándo usarlo, pasos exactos, puntos de fallo comunes, verificaciones
- Memory debe ser compacta: "preferred tone", "stable project paths", "tool quirks" — no PR numbers ni deadlines temporales
- Los cron jobs buenos son silenciosos: entregan algo útil o no envían nada, sin spam de "todo normal"
- MCP servers ejecutan código real — tratarlos como software a instalar, no como prompts inofensivos
- Webhooks son event-based (PR opened, Stripe event) vs cron que es time-based
- El 7-day build path recomienda una capa por día: Telegram → Obsidian+memory → primer skill → cron → perfil → webhook → cleanup

## Open Questions
- ¿Cómo escalar el sistema de perfiles cuando se necesitan 5+ agentes especializados con diferentes modelos?
- ¿Cuál es el tradeoff real entre usar MCP servers vs APIs directas en términos de latencia y fiabilidad?

## Source
- **Raw note:** [[raw-notes/10-upgrades-for-your-hermes-agent]]
- **Original URL:** https://x.com/zaimiri/status/2062512177295090046
