---
title: Post by @santtiagom_ on X
author: '@santtiagom_'
published: '2026-02-24'
type: article
resource: https://x.com/santtiagom_/status/2026426248122216501
timestamp: '2026-02-24T00:00:00Z'
description: '@santtiagom_ ilustra con un ejemplo de e-commerce la diferencia entre
  prompt, MCP/tool, Skill y Subagent: el prompt es lo que pedís, MCP da acceso a datos,
  l...'
tags:
- summaries
---


# Prompt vs Skill vs Subagent

## Summary
@santtiagom_ ilustra con un ejemplo de e-commerce la diferencia entre prompt, MCP/tool, Skill y Subagent: el prompt es lo que pedís, MCP da acceso a datos, la Skill formaliza tu forma de trabajar, y el Subagent delega partes del proceso.

## Core Concepts
-  -- Instrucción puntual que se envía al modelo para una tarea específica
- [[concepts/MCP]] -- Protocolo que conecta el agente con datos y sistemas externos (databases, APIs)
- [[concepts/Skill-Files]] -- Instrucciones formales que formalizan tu forma de trabajar para consistencia
- [[concepts/Subagent-Delegation]] -- Agente invocado por otro para encargarse de una parte del proceso
- [[concepts/Agent-Loop]] -- Patrón donde el agente delega partes del trabajo a subagents y combina resultados

## Key Insights
- Ejemplo concreto: bajaron ventas → prompt pide análisis → MCP conecta a base de datos → Skill formaliza el criterio de análisis → Subagent delega campañas y cohorts
- Una Skill NO es un prompt suelto ni una función que se ejecuta sola — es tu forma de trabajar formalizada
- Skills son instrucciones y pasos definidos en archivos que el modelo lee como contexto
- El criterio de análisis (comparar contra semana pasada, separar por channel, detectar producto que cayó más) se estandariza en la Skill
- Para problemas más grandes, el agente delega: un subagent para campañas, otro para cohorts, luego combina en conclusión

## Open Questions
- ¿Cuándo conviene una Skill vs. un hook para estandarizar procesos?
- ¿Cómo se estructuran los subagents cuando hay múltiples fuentes de datos?
- ¿Se puede versionar una Skill como se versiona código?

## Source
- **Raw note:** [[summaries/Santtiagom-Learning-Claude-Code-Part-3]]
- **Original URL:** https://x.com/santtiagom_/status/2026426248122216501
