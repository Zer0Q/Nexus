# Agent Architecture Index

## Overview
Mapa de conceptos y recursos sobre la arquitectura de agentes AI: patrones de diseño, componentes fundamentales, y frameworks principales (Claude Code, Hermes Agent).

## Core Concepts
- [[concepts/Agent-Architecture]] -- Estructura de capas que envuelve al LLM: thin harness, fat skills
- [[concepts/Agent-Loop]] -- Bucle fundamental: ejecutar → observar → validar → corregir → repetir
- [[concepts/Skill-Files]] -- Documentos markdown reutilizables que enseñan al modelo CÓMO hacer algo
- [[concepts/Memory-Persistence]] -- Guardar información entre sesiones para no empezar desde cero
- [[concepts/Hook-Mechanism]] -- Comandos shell deterministas para guardrails a nivel infraestructura
- [[concepts/Subagent-Delegation]] -- Delegar sub-tareas a agentes con contexto y permisos aislados
- [[concepts/Context-Engineering]] -- Diseñar el contexto que se pasa al modelo para compensar statelessness
- [[concepts/Agent-Guardrails]] -- Mecanismos de seguridad: sandboxing, validación, límites, human-in-the-loop
- [[concepts/Revenue-Engineering]] -- Aplicar loops de mejora continua al revenue del negocio

## Tools
- [[tools/Claude-Code]] -- IDE de agente de Anthropic con arquitectura de 5 capas
- [[tools/Hermes-Agent]] -- Framework de agente con memoria persistente, learning loop y multi-profile

## Summaries
- [[summaries/LearnWithBrij-Learning-Claude-Code-Part-3]] -- 5 capas de Claude Code
- [[summaries/GarryTan-Thin-Harness-Fat-Skills]] -- Principio thin harness, fat skills
- [[summaries/Santtiagom-Learning-Claude-Code-Part-1]] -- Ruta de aprendizaje Claude Code
- [[summaries/Santtiagom-Learning-Claude-Code-Part-2]] -- Arquitectura 5 capas resumen
- [[summaries/Santtiagom-Learning-Claude-Code-Part-3]] -- Prompt vs Skill vs Subagent
- [[summaries/Santtiagom-Learning-Claude-Code-Part-4]] -- Elementos de prompt engineering
- [[summaries/Santtiagom-Learning-Hermes-Part-1]] -- Conceptos fundamentales de Hermes
- [[summaries/Santtiagom-Learning-Hermes-Part-2]] -- Learning loop de Hermes
- [[summaries/Santtiagom-What-Is-Agent-Part-1]] -- Qué es un agente: componentes
- [[summaries/Santtiagom-What-Is-Agent-Part-2]] -- Stateless LLMs y context engineering
- [[summaries/Santtiagom-What-Is-Agent-Part-3]] -- Métodos de planning: CoT, ToT, Reflexion
- [[summaries/Santtiagom-What-Is-Agent-Part-5]] -- Guardrails y seguridad
- [[summaries/Santtiagom-What-Is-Agent-Part-6-Harness]] -- Patrones del harness
- [[summaries/Santtiagom-What-Is-Agent-Part-7]] -- Sistema de agente completo
- [[summaries/Santtiagom-SKILL-MD-Guide]] -- Anatomía de SKILL.md
- [[summaries/Alexxubyte-Agent-Anatomy-Loop]] -- Anatomía del agente: el loop
- [[summaries/Ericosiu-Revenue-Engineering-Loops]] -- Revenue engineering con loops
- [[summaries/Frontier-Ecosystem-Stability]] -- Ecosistema AI y estabilidad
