---
type: Concept
title: Stop Condition
description: 'Condición que determina cuándo un loop de agente debe detenerse y entregar
  un resultado final. Es el complemento del eval gate: el eval gate decide si contin...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Stop Condition

## Definition
Condición que determina cuándo un loop de agente debe detenerse y entregar un resultado final. Es el complemento del eval gate: el eval gate decide si continuar, el stop condition define cuándo NO se puede continuar más.

## Why It Matters
Sin stop condition, los loops pueden entrar en ciclos infinitos o desperdiciar tokens en iteraciones que no mejoran el resultado. Es un guardrail crítico para la autonomía del agente.

## Key Ideas
- Define cuándo el loop debe parar (no solo cuándo continuar)
- Puede ser basado en: éxito del objetivo, máximo de iteraciones, umbral de confianza, o timeout
- Trabaja junto al eval gate para controlar la autonomía
- Más autonomía = más necesidad de stop conditions robustas
- Un stop condition mal definido causa loops infinitos o resultados incompletos

## Tradeoffs
- Stop conditions muy estrictas = resultados incompletos
- Stop conditions muy laxas = tokens desperdiciados
- El balance depende del costo de errores vs. costo de tokens

## Related
- [[concepts/Agent-Loop]]
- [[concepts/Eval-Gate]]
- [[concepts/Agent-Guardrails]]
- 

## Source
[[summaries/Alexxubyte-Agent-Anatomy-Loop]]
[[summaries/Santtiagom-What-Is-Agent-Part-5]]
[[summaries/Revenue-Engineering]]
[[summaries/Agent-Loop]]
