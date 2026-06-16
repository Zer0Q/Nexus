---
title: "Post by @alexxubyte on X"
source: "https://x.com/alexxubyte/status/2054957919469461547"
author: "@alexxubyte"
published: "2026-05-14"
type: article
---

# AI Agent Anatomy: The Loop

## Summary
@alexxubyte descompone un agente AI en un bucle While simple: el LLM selecciona una acción, la ejecuta, evalúa el resultado y repite. Desglosa las 5 componentes esenciales — Brain, Planning, Tools, Memory y Loop — más los Guardrails como capa de seguridad.

## Core Concepts
- [[concepts/Agent-Loop]] -- Bucle fundamental de un agente: observar estado → decidir acción → ejecutar → evaluar → repetir hasta completado
- [[concepts/Chain-of-Thought]] -- Método de planificación donde el modelo piensa paso a paso antes de actuar
- [[concepts/Tree-of-Thoughts]] -- Método de planificación que explora múltiples opciones y elige la mejor
- [[concepts/Reflexion]] -- Patrón donde el agente aprende de errores y retry con mejora iterativa
- [[concepts/Context-Window]] -- Límite de información que el modelo puede ver simultáneamente
-  -- Almacén de memoria a largo plazo para agentes cuando el context window se llena
- [[concepts/Agent-Guardrails]] -- Sandboxing, validación de output, límites de tokens y scope para controlar la autonomía

## Key Insights
- El cambio fundamental de chatbot a agente: el modelo deja de escribir texto y empieza a tomar decisiones
- Planning para tareas difíciles usa Chain of Thought, Tree of Thoughts o Reflexion (aprender de errores)
- "Un LLM sin tools es un cerebro en un frasco" — las tools son funciones que el modelo puede llamar (web search, code execution, APIs, files, browsers)
- Short-term memory = context window; long-term memory = vector stores, files, knowledge bases
- Cuando el window se llena, los agentes resumen turns viejos y avanzan con el resumen
- Guardrails: sandboxing, human checks, token limits, output validation, scope limits — más autonomía requiere más guardrails

## Open Questions
- ¿Qué método de planning (CoT, ToT, Reflexion) es más adecuado para diferentes tipos de tareas?
- ¿Cómo se maneja la degradación acumulativa del resumen cuando se itera muchas veces en el loop?
- ¿Los guardrails de Claude Code cubren las mismas categorías que las de @alexxubyte?

## Source
- **Raw note:** [[raw-notes/alexxubyte-what-is-an-agent-part-4-loop]]
- **Original URL:** https://x.com/alexxubyte/status/2054957919469461547
