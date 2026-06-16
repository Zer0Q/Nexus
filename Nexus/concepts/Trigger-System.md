---
type: Concept
title: Trigger System
description: 'Mecanismo que señala que un loop de agente debe iniciarse. Es el primer
  paso de cualquier loop: algo externo o interno activa el loop cuando se cumple una
  co...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Trigger System

## Definition
Mecanismo que señala que un loop de agente debe iniciarse. Es el primer paso de cualquier loop: algo externo o interno activa el loop cuando se cumple una condición específica (deal quiet, form filled, role opened, etc.).

## Why It Matters
Sin trigger, el loop no sabe cuándo empezar. El trigger es lo que convierte un agente pasivo en uno reactivo — puede actuar por sí mismo cuando las condiciones lo requieren.

## Key Ideas
- Algo que señala que se necesita trabajo (deal quiet 14 días, form filled, role opened)
- Puede ser basado en tiempo (cada X horas), evento (algo sucede), o dato (umbral alcanzado)
- Primer paso del loop: trigger → signal + context → action → eval gate → stop condition
- Sin trigger, vuelves a hacer trabajo manual para iniciar cada tarea
- El trigger define la frecuencia y oportunidad del loop

## Tradeoffs
- Triggers muy frecuentes = loops innecesarios y tokens desperdiciados
- Triggers muy raros = oportunidades perdidas
- El balance depende del costo de error vs. costo de ejecución

## Related
- [[concepts/Agent-Loop]]
- [[concepts/Revenue-Engineering]]
- [[concepts/Eval-Gate]]
- [[concepts/Stop-Condition]]

## Source
[[summaries/Ericosiu-Revenue-Engineering-Loops]]
[[summaries/Revenue-Engineering]]
