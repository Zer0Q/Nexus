---
title: Master 97% of Codex in 30 Minutes (Full Course)
author: 0xCodez
published: '2026-06-02'
type: article
resource: https://x.com/0xCodez/status/2061795739575963935
timestamp: '2026-06-02T00:00:00Z'
description: 'Curso intensivo de Codex Agent (OpenAI) cubriendo el 97% de funcionalidades
  usadas en el día a día: configuración de AGENTS.md como archivo de contexto del
  p...'
tags:
- summaries
---


# Codex Agent: Masterclass práctica en 30 minutos

## Summary
Curso intensivo de Codex Agent (OpenAI) cubriendo el 97% de funcionalidades usadas en el día a día: configuración de AGENTS.md como archivo de contexto del proyecto, los tres modos de thread (Local, Worktree, Cloud), Plan mode para brainstorming previo a código, Automations para prompts programados con cron, y el flujo de specification-driven development. Enfatiza que la calidad del output depende de la calidad del AGENTS.md y las especificaciones de entrada.

## Core Concepts

- [[concepts/Codex-Agent]] -- Plataforma de codificación agéntica de OpenAI (~4M usuarios semanales) con CLI, desktop, IDE y cloud
- [[concepts/AGENTS-MD]] -- Archivo de contexto del proyecto: quién eres, qué construyes, restricciones y convenciones
- [[concepts/Specification-Driven-Development]] -- Definir especificaciones claras antes de generar código con IA; garbage in, garbage out
- [[concepts/Context-Engineering]] -- Curación e inyección de contexto específico de proyecto para guiar al agente IA
- [[concepts/Code-Overload]] -- Producción excesiva de código sin verificación; Codex acelera el problema si no hay guardrails

## Key Insights

- AGENTS.md es el punto de entrada: contexto (quién eres), objetivo (estado final), restricciones (APIs, lenguajes, seguridad), convenciones (guardar lecciones, confirmar plan)
- Los tres modos de thread: Local (directo en el proyecto), Worktree (aislado en Git para experimentación), Cloud (remoto para entornos controlados)
- Plan mode: el agente brainstormea y produce un plan antes de escribir código; crítico para proyectos complejos
- Automations: prompts programados con cron para flujos end-to-end (tests, reviews, deploys)
- No escribir AGENTS.md desde cero: pedir al agente que lo bosqueje y luego editar
- Los agentes IA se atascan en razonamiento circular sin especificaciones contenidas y bien definidas
- La verificación debe ser 40% del tiempo: ~45% del código generado por IA contiene fallos de seguridad

## Open Questions

- ¿Cómo evolucionan las Automations de Codex comparado con los cron jobs de Hermes Agent?
- ¿Qué ventajas tiene Worktree mode para contribuciones a repositorios compartidos?

## Source

- **Raw note:** [[master-97-of-codex-in-30-minutes-full-course.md]]
- **Original URL:** https://x.com/0xCodez/status/2061795739575963935
