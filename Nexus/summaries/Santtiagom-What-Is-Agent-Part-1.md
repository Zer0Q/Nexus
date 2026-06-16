---
title: Post by @santtiagom_ on X
author: '@santtiagom_'
published: '2026-06-11'
type: article
resource: https://x.com/santtiagom_/status/2065230988800647419
timestamp: '2026-06-11T00:00:00Z'
description: '@santtiagom_ explica que un agente es más simple de lo que parece: un
  modelo que genera tokens + tools para actuar en el mundo + context para información
  + m...'
tags:
- summaries
---


# What is an Agent: Part 1

## Summary
@santtiagom_ explica que un agente es más simple de lo que parece: un modelo que genera tokens + tools para actuar en el mundo + context para información + memory para continuidad + harness para coordinación + loop para iteración. La combinación de estos 6 elementos produce un sistema que persigue objetivos por sí solo.

## Core Concepts
-  -- Modelo que solo genera tokens de salida a partir de una entrada (texto, imágenes, audio)
- [[concepts/Tool-Use]] -- Mecanismo que permite al modelo interactuar con el mundo: leer archivos, ejecutar código, hacer requests a APIs
-  -- Conjunto acumulado de mensajes, instrucciones, archivos y resultados de tools
- [[concepts/Context-Window]] -- Límite de información que el modelo puede ver simultáneamente
- [[concepts/Memory-Persistence]] -- Recuperar información de sesiones anteriores para no empezar de cero
- [[concepts/Agent-Harness]] -- Capa de coordinación: decide qué memory cargar, cuándo usar tools, cómo verificar resultados
- [[concepts/Agent-Loop]] -- Ejecutar → observar → validar → corregir → repetir
- [[concepts/Agent-Definition]] -- Sistema que combina modelo, contexto, memory, tools, harness y loop para perseguir objetivos autónomamente

## Key Insights
- Un modelo por sí solo solo genera tokens — no puede leer archivos, editar código ni hacer requests a APIs
- Las tools son el puente entre el modelo y el mundo real
- El contexto acumula mensajes, instrucciones, archivos y resultados de tools
- Sin memory, cada sesión empieza de cero: hay que re-explicar todo
- El harness coordina: qué memory cargar, cuándo usar tools, cómo verificar resultados
- El loop (ejecutar → observar → validar → corregir → repetir) es lo que permite perseguir objetivos
- La combinación completa de estos 6 elementos = un agente

## Open Questions
- ¿Cómo se implementa el harness en Claude Code vs Hermes Agent?
- ¿El context window tiene límites prácticos en agentes de producción?
- ¿Qué pasa cuando el harness toma decisiones incorrectas en el loop?

## Source
- **Raw note:** [[raw-notes/santtiagom-what-is-an-agent-part-1]]
- **Original URL:** https://x.com/santtiagom_/status/2065230988800647419
