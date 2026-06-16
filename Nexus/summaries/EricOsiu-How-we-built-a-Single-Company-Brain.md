---
title: How we built a Single Company Brain (and how you can too)
author: '@ericosiu'
published: '2026-05-29'
type: article
resource: https://x.com/ericosiu/status/2060415100603781497
timestamp: '2026-05-29T00:00:00Z'
description: Arquitectura de 5 capas para construir un "company brain" que convierta
  conocimiento disperso en inteligencia operativa. Basado en experiencia real en Single...
tags:
- summaries
---


# Single Company Brain Architecture

## Summary
Arquitectura de 5 capas para construir un "company brain" que convierta conocimiento disperso en inteligencia operativa. Basado en experiencia real en Single Grain: 500K+ tokens de memoria persistente, 90+ crons diarios, 2,862 transcripciones Gong convertidas en playbooks. La clave no es almacenar más información sino construir una capa de inteligencia entre el contexto y el trabajo: capture → retrieval → source truth → permissions → feedback loops.

## Core Concepts
- [[concepts/Company-Brain-Architecture]] -- sistema de 5 capas que convierte conocimiento disperso (calls, CRM, SOPs, Slack) en inteligencia operativa reutilizable
- [[concepts/Retrieval-First-Organization]] -- la capa de retrieval es el operating layer, no la memoria — el agente necesita los 6 contextos relevantes, no toda la historia
- [[concepts/Source-Truth-Hierarchy]] -- diseño operativo que define qué fuente gana cuando hay conflictos (sales call vs CRM vs Slack vs SOP)
- [[concepts/Workflow-Level-Permissions]] -- control de acceso por workflow: marketing agent no necesita HR, sales no necesita leadership notes
- [[concepts/Feedback-Loop-Knowledge-System]] -- cada corrección humana se convierte en regla futura, transformando inteligencia en aprendizaje continuo
- [[Capture-Surface-Workflow]] -- needs research: workflow de captura de datos en company brain -- superficie de captura que incluye calls, CRM, content decisions, SOPs, agent outputs, daily logs y human corrections

## Key Insights
- En Single Grain, la memoria persistente consumía ~40% del context window — más info no siempre es más útil si no se recupera correctamente
- Una ingestión diaria de ejemplo: 15 calls → 390 insights, 470 facts, 125 frameworks
- 2,862 transcripciones Gong convertidas en playbooks operacionales
- Un call deja de ser solo un call y se convierte en: objection library, sales training input, positioning signal, content idea source, CRM risk flag, future agent instruction
- El audit de 6 preguntas antes de automatizar un workflow: ¿qué sources depende? ¿cuál es la truth cuando conflictúan? ¿qué contexto necesita siempre? ¿qué contexto nunca debe ver? ¿qué correcciones son repetitivas? ¿cómo una corrección se convierte en regla?
- El ejemplo de reporting: de 25 min de data pulling + horas de follow-up a respuestas en <60 segundos
- El beneficio principal no es el ahorro de tiempo sino la reducción de decision latency — líderes no esperan dashboards, operadores no empiezan desde cero
- "The companies that win with AI won't be the ones with the biggest prompt library. They'll be the ones with the cleanest intelligence layer."

## Open Questions
- ¿Cómo escalar el sistema de permissions cuando hay 50+ workflows cruzando múltiples clientes en un entorno de agencia?
- ¿Qué mecanismos de detección de drift existen para identificar cuando una source truth se ha vuelto stale?

## Source
- **Raw note:** [[raw-notes/how-we-built-a-single-company-brain-and-how-you-can-too]]
- **Original URL:** https://x.com/ericosiu/status/2060415100603781497
