---
title: Thin Harness, Fat Skills
author: '@garrytan'
published: '2026-04-11'
type: article
resource: https://x.com/garrytan/status/2042925773300908103
timestamp: '2026-04-11T00:00:00Z'
description: '@garrytan argumenta que la diferencia entre usuarios 100x de Claude
  Code no es el modelo, sino la arquitectura: "thin harness, fat skills". El harness
  debe s...'
tags:
- summaries
---


# Thin Harness, Fat Skills: Agent Architecture Philosophy

## Summary
@garrytan argumenta que la diferencia entre usuarios 100x de Claude Code no es el modelo, sino la arquitectura: "thin harness, fat skills". El harness debe ser mínimo y las skills deben contener el conocimiento del dominio. La accidental leak de 512K líneas de código de Claude Code confirmó su teoría.

## Core Concepts
- [[concepts/Agent-Architecture]] -- Estructura que balancea harness mínimo con skills ricos en conocimiento
- [[concepts/Skill-Files]] -- Documentos markdown que enseñan al modelo cómo hacer algo, no qué hacer
-  -- Programa mínimo que corre el LLM: loop, archivos, contexto, seguridad
-  -- Conocimiento del dominio embebido en skills, no en el harness
-  -- Problema de herramientas que comen el context window (40+ tool definitions)
-  -- Gestión de contexto entre sesiones para no perder información

## Key Insights
- "The 2x people and the 100x people are using the same models. The difference isn't intelligence. It's architecture"
- Anthropic accidentally leaked 512,000 lines of Claude Code source code — confirmed YC teachings
- El bottleneck nunca es la inteligencia del modelo — los modelos ya saben razonar y escribir código
- Los modelos fallan porque NO entienden TU data: schema, convenciones, forma particular del problema
- Una skill funciona como una "method call": toma parámetros, misma procedura produce resultados diferentes
- Ejemplo: skill /investigate con 7 pasos + 3 parámetros (TARGET, QUESTION, DATASET) — misma skill, diferentes resultados
- Anti-pattern: fat harness con 40+ tool definitions comiendo el context window
- Lo que se quiere: tooling purpose-built que sea rápido y narrow
- "Markdown is a more perfect encapsulation of capability than rigid source code"

## Open Questions
- ¿Cómo se escala el pattern "thin harness, fat skills" a equipos grandes?
- ¿Qué métricas miden la efectividad de skills vs. harness en producción?
- ¿Se puede automatizar la generación de skills a partir de datos del dominio?

## Source
- **Raw note:** [[raw-notes/thin-harness-fat-skills]]
- **Original URL:** https://x.com/garrytan/status/2042925773300908103
