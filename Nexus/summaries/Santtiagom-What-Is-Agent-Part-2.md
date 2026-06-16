---
title: Post by @santtiagom_ on X
author: '@santtiagom_'
published: '2026-06-12'
type: article
resource: https://x.com/santtiagom_/status/2065898594771591653
timestamp: '2026-06-12T00:00:00Z'
description: '@santtiagom_ explica la propiedad fundamental de los LLMs: son stateless,
  no recuerdan nada entre llamadas. Esto significa que cada interacción empieza desde...'
tags:
- summaries
---


# Stateless LLMs and Context Engineering

## Summary
@santtiagom_ explica la propiedad fundamental de los LLMs: son stateless, no recuerdan nada entre llamadas. Esto significa que cada interacción empieza desde cero, y toda la "memoria" se construye artificialmente mediante el contexto que se pasa en cada request.

## Core Concepts
-  -- Propiedad fundamental: los LLMs no mantienen estado entre llamadas, cada interacción empieza desde cero
- [[concepts/Context-Engineering]] -- Diseñar el contexto que se pasa al modelo para compensar la falta de memoria nativa
- [[concepts/Context-Rot]] -- Degración del contexto cuando se acumula demasiada información irrelevante
- [[concepts/Context-Window]] -- Límite físico de tokens que el modelo puede procesar simultáneamente
- [[concepts/Agent-Harness]] -- Capa que gestiona el contexto: qué incluir, qué resumir, qué eliminar

## Key Insights
- Stateless significa: no hay "estado interno" del modelo entre llamadas — cada request es independiente
- La "memoria" de un agente es artificial: se construye pasando el contexto anterior como parte del prompt
- El context window es el límite físico: no puede ver infinita información a la vez
- Context engineering = diseñar qué información va en el contexto y cómo se organiza
- Context rot = cuando el contexto se llena de ruido y el modelo pierde capacidad de razonamiento
- El harness debe gestionar activamente el contexto: incluir lo relevante, resumir lo antiguo, eliminar lo irrelevante

## Open Questions
- ¿Cómo se mide el "costo" del context rot en términos de calidad de output?
- ¿Qué técnicas de compresión de contexto son más efectivas para agentes de producción?
- ¿Los LLMs futuros tendrán memoria nativa o seguire siendo stateless?

## Source
- **Raw note:** [[raw-notes/santtiagom-what-is-an-agent-part-2]]
- **Original URL:** https://x.com/santtiagom_/status/2065898594771591653
