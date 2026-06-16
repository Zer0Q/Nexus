---
type: Concept
title: Agent Loop
description: 'Bucle fundamental de un agente: observar el estado actual → decidir
  acción con el LLM → ejecutar → evaluar resultado → repetir hasta completar el objetivo.
  E...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Agent Loop

## Definition
Bucle fundamental de un agente: observar el estado actual → decidir acción con el LLM → ejecutar → evaluar resultado → repetir hasta completar el objetivo. Es lo que diferencia un agente de un modelo que solo responde preguntas.

## Why It Matters
El loop permite perseguir objetivos autónomamente. Sin loop, el agente solo puede hacer una pregunta y recibir una respuesta. Con loop, puede iterar, corregir y mejorar hasta alcanzar el objetivo.

## Key Ideas
- Secuencia: ejecutar → observar → validar → corregir → repetir
- El LLM selecciona la acción basándose en el estado actual
- La evaluación decide si continuar o dar una respuesta final
- Más autonomía requiere más guardrails en el loop
- Las mejores empresas "dejan de promptear y empiezan a construir loops"

## Tradeoffs
- Más iteraciones = mejor resultado pero mayor costo
- El loop puede entrar en ciclos infinitos sin stop condition adecuada
- Cada iteración acumula contexto que puede degradar la calidad

## Related
- [[concepts/Agent-Architecture]]
- [[concepts/Evidence-Validation]]
- [[concepts/Agent-Guardrails]]
- 

## Source
[[summaries/Alexxubyte-Agent-Anatomy-Loop]]
[[summaries/Santtiagom-What-Is-Agent-Part-1]]
[[summaries/Santtiagom-What-Is-Agent-Part-6-Harness]]
[[summaries/Ericosiu-Revenue-Engineering-Loops]]
