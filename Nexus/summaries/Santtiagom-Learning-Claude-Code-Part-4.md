---
title: "Post by @santtiagom_ on X"
source: "https://x.com/santtiagom_/status/2047837076922437817"
author: "@santtiagom_"
published: "2026-04-23"
type: article
---

# Prompt Engineering Elements

## Summary
@santtiagom_ resume un workshop de Anthropic sobre prompt engineering, mostrando cómo agregar contexto a un prompt básico mejora drásticamente los resultados del modelo. Los 6 elementos clave: contexto, datos, instrucciones, reglas, output y ejemplos.

## Core Concepts
- [[concepts/Prompt-Engineering]] -- Arte de escribir prompts efectivos con 6 elementos clave para mejores resultados con LLMs y agentes
- [[concepts/System-Prompt]] -- Parte del prompt que no cambia entre interacciones, para reglas fijas del modelo
-  -- Ejemplos concretos que se agregan al prompt para casos difíciles
-  -- Especificar el formato de salida para estandarizar resultados del modelo

## Key Insights
- Prompt básico sin contexto: Claude no entiende qué está viendo y responde mal
- Agregar contexto (rol, situación): la respuesta cambia completamente, empieza a leer bien el formulario
- Los 6 elementos del prompt efectivo: contexto (qué está pasando y rol), datos (qué analizar), instrucciones (cómo hacerlo paso a paso), reglas (no inventar, decir "no sé"), output (formato de salida)
- Regla práctica: si algo no cambia entre interacciones, ponerlo en system prompt
- Para casos difíciles: agregar ejemplos concretos (few-shot)
- El workshop de Anthropic es de 24 minutos y es gratuito, hecho por el equipo que construyó Claude

## Open Questions
- ¿Cómo se integra el system prompt de Claude Code con CLAUDE.md?
- ¿Los few-shot examples de Anthropic se pueden usar directamente en Skills de Claude Code?
- ¿Hay diferencias entre el prompt engineering de Claude y otros modelos?

## Source
- **Raw note:** [[summaries/Santtiagom-Learning-Claude-Code-Part-4]]
- **Original URL:** https://x.com/santtiagom_/status/2047837076922437817
