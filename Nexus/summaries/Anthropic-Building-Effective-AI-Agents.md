---
title: "Building Effective AI Agents"
source: "https://www.anthropic.com/engineering/building-effective-agents"
author: "Anthropic (Erik S. y Barry Zhang)"
published: "2026"
type: article
---

# Building Effective AI Agents

## Summary
Guía práctica de Anthropic para construir agentes con LLMs basada en experiencia con docenas de equipos en producción. Distingue entre workflows (códigos predefinidos) y agentes (LLM dirige dinámicamente). Presenta patrones compositables: Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer. Recomienda empezar con APIs directas antes que frameworks, y seguir tres principios: simplicidad, transparencia y diseño cuidadoso de la interfaz agente-computador (ACI).

## Core Concepts
- [[concepts/Augmented-LLM]] -- LLM mejorado con retrieval, tools y memory como building block fundamental de sistemas agenticos
- [[concepts/Prompt-Chaining-Workflow]] -- descomposición de tarea en pasos secuenciales donde cada LLM call procesa el output del anterior, con checks programáticos
- [[concepts/Routing-Workflow]] -- clasificación de input hacia tareas especializadas, permitiendo prompts optimizados por categoría
- [[concepts/Parallelization-Workflow]] -- ejecución simultánea con Sectioning (subtasks independientes) o Voting (múltiples intentos para confianza)
- [[concepts/Orchestrator-Workers-Workflow]] -- LLM central descompone tareas dinámicamente, delega a workers, sintetiza resultados
- [[concepts/Evaluator-Optimizer-Workflow]] -- un LLM genera respuesta, otro evalúa y da feedback en loop iterativo
- [[concepts/Agent-Computer-Interface]] -- diseño de herramientas para agentes con documentación clara, poka-yoke y formatos cercanos al texto natural
- [[concepts/Tool-Use]] -- capacidad del LLM de interactuar con servicios externos especificando estructura y definición exacta

## Key Insights
- Los implementations más exitosos no usaban frameworks complejos — usaban patrones simples y compositables
- Los frameworks (Claude Agent SDK, Strands, Rivet, Vellum) simplifican tareas low-level pero crean capas de abstracción que dificultan debugging
- Para Routing: dirigir queries fáciles a modelos pequeños/cost-efficient (Claude Haiku 4.5) y queries difíciles a modelos más capaces (Claude Sonnet 4.5)
- Para Parallelization Sectioning: un modelo procesa queries del usuario mientras otro screena contenido inapropiado — funciona mejor que un solo LLM call
- Para Orchestrator-Workers: ideal para coding donde el número de archivos a cambiar y la naturaleza del cambio dependen de la tarea
- Para Evaluator-Optimizer: efectivo cuando LLM responses mejoran demostrablemente con feedback humano articulado
- Los agentes son típicamente solo LLMs usando tools basado en feedback ambiental en un loop — la implementación es straightforward
- Anthropic pasó más tiempo optimizando tools que el overall prompt en su agente SWE-bench — cambiar a absolute filepaths eliminó errores con relative paths
- Regla de oro para ACI: invertir tanto esfuerzo en Agent-Computer Interface como en Human-Computer Interface
- Los dos dominios más prometedores para agentes: customer support (conversación + acción + tools + métricas claras) y coding agents (verificable con tests automatizados)

## Open Questions
- ¿Cómo determinar el threshold donde la complejidad de un agente justifica el costo adicional de latencia y tokens?
- ¿Qué patrones de failure son más comunes en agentes autónomos en producción y cómo mitigarlos sistemáticamente?

## Source
- **Raw note:** [[raw-notes/building-effective-ai-agents]]
- **Original URL:** https://www.anthropic.com/engineering/building-effective-agents
