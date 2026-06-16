---
title: "Post by @santtiagom_ on X"
source: "https://x.com/santtiagom_/status/2068908785772089283"
author: "@santtiagom_"
published: "2026-06-16"
type: article
---

# Complete Agent System

## Summary
@santtiagom_ sintetiza los componentes de un sistema de agente completo: modelo, contexto, memory, tools, harness y loop. La combinación de estos 6 elementos produce un sistema capaz de perseguir objetivos de forma autónoma.

## Core Concepts
- [[concepts/Agent-Definition]] -- Sistema que combina modelo, contexto, memory, tools, harness y loop para perseguir objetivos
- [[concepts/Agent-Architecture]] -- Estructura de capas que envuelve al LLM para hacerlo operativo
- [[concepts/Agent-Loop]] -- Bucle fundamental: ejecutar → observar → validar → corregir → repetir
- [[concepts/Memory-Persistence]] -- Recuperar información entre sesiones
- [[concepts/Tool-Use]] -- Interactuar con el mundo externo
- [[concepts/Agent-Harness]] -- Coordinar todos los componentes

## Key Insights
- Modelo + Tools + Context + Memory + Harness + Loop = Agente completo
- Cada componente resuelve un problema específico que el modelo por sí solo no puede resolver
- El loop es lo que permite perseguir objetivos, no solo responder preguntas
- La autonomía viene del loop, no del modelo
- Los agentes más efectivos son los que mejor coordinan sus componentes, no los que tienen el mejor modelo

## Open Questions
- ¿Qué componente es el bottleneck más común en agentes de producción?
- ¿Se puede optimizar un agente cambiando solo un componente?
- ¿Cómo se mide la autonomía de un agente?

## Source
- **Raw note:** [[raw-notes/santtiagom-what-is-an-agent-part-7]]
- **Original URL:** https://x.com/santtiagom_/status/2068908785772089283
