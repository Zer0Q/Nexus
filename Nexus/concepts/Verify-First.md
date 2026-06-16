---
type: Concept
title: Verify-First
description: 'Principio de que verification es el requisito mínimo para un functional
  loop: sin verificación, no tienes un loop, tienes repeated prompting. Con verificatio...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Verify-First

## Definition
Principio de que verification es el requisito mínimo para un functional loop: sin verificación, no tienes un loop, tienes repeated prompting. Con verification, el loop puede converge.

## Why It Matters
Diferencia fundamental entre loop engineering y prompting secuencial. La mayoría de "loops" que se llaman así son solo repeated prompting sin verificación real. La palabra importante no es "AI" sino "verify".

## Key Ideas
- "Without verification, you do not have a loop. You have repeated prompting."
- "With verification, the loop can converge."
- Verificador debe ser independiente (Maker-Checker-Split)
- Condición de parada debe ser medible/verificable
- Sin verification = agent deriva en vez de mejorar
- Con verification = agent mejora iterativamente hacia objetivo

## Tradeoffs
- Verification overhead vs speed de iteration
- False positives en verification (approbar work que no cumple)
- False negatives (rechazar work que sí cumple)
- Balance entre rigor de verification y agilidad del loop

## Related
- [[concepts/Loop-Driven-Development]]
- [[concepts/Maker-Checker-Split]]
- [[concepts/Loop-Engineering]]

## Source
[[summaries/bibryam-loop-driven-development]]
