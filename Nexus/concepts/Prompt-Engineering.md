---
type: Concept
title: Prompt Engineering
description: 'Arte de escribir prompts efectivos para LLMs y agentes. Incluye 6 elementos
  clave: contexto (rol/situación), datos (qué analizar), instrucciones (cómo hacerl...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Prompt Engineering

## Definition
Arte de escribir prompts efectivos para LLMs y agentes. Incluye 6 elementos clave: contexto (rol/situación), datos (qué analizar), instrucciones (cómo hacerlo), reglas (qué no hacer), output (formato de salida) y ejemplos (casos difíciles).

## Why It Matters
El prompt es la palanca más barata para mejorar outputs. Antes de buscar retrieval o fine-tuning, un bien estructurado prompt puede hacer una diferencia enorme. Tratar prompts como código versionado, testeado y reproducible.

## Key Ideas
- 6 elementos: contexto, datos, instrucciones, reglas, output, ejemplos
- Tratar prompts como código: versionado, testeado, reproducible
- System prompt para lo que no cambia entre interacciones
- Few-shot examples para casos difíciles
- La diferencia entre un prompt básico y uno con contexto puede ser abismal
- Anthropic ofrece workshop gratuito de 24 minutos sobre prompt engineering

## Tradeoffs
- Prompts muy largos consumen más tokens y son más difíciles de mantener
- Demasiada especificidad puede limitar la flexibilidad del modelo
- El balance entre estructura y naturalidad

## Related
- [[concepts/Skill-Files]]
- 
- 
- 
- [[concepts/System-Prompt]]

## Source
[[summaries/Santtiagom-Learning-Claude-Code-Part-1]]
[[summaries/Santtiagom-Learning-Claude-Code-Part-4]]
[[summaries/Avichawla-LLM-Engineering-Roadmap]]
