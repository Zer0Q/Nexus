---
type: Concept
title: Update-and-Forget Loop
description: Mecanismo donde en modelos pequeños, las actualizaciones de gradientes
  de tareas frecuentes sobrescriben las señales débiles de tareas raras antes de que
  est...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Update-and-Forget Loop

## Definition
Mecanismo donde en modelos pequeños, las actualizaciones de gradientes de tareas frecuentes sobrescriben las señales débiles de tareas raras antes de que estas puedan acumularse en algo duradero. El modelo aprende y olvida en un ciclo continuo, impidiendo que las tareas raras converjan.

## Why It Matters
Explica el mecanismo causal detrás de la [[concepts/Structural-Exclusion]]: no es que el modelo no tenga suficiente "tiempo" para aprender, sino que la dinámica de gradientes en modelos pequeños hace que las tareas raras sean estructuralmente imposibles de retener.

## Key Ideas
- Durante training, cada tarea en la mezcla compite por las neuronas del modelo
- Tareas frecuentes generan señales de gradiente fuertes y consistentes
- Tareas raras generan señales débiles y esporádicas
- En modelo pequeño (N=32): la señal spikea cuando llegan ejemplos raros pero decae a cero antes de la siguiente inyección
- En modelo grande (N=256): la señal spikea y la línea base sube porque cada exposición se acumula sobre la anterior
- Cuando un modelo ha aprendido completamente las tareas frecuentes, su residual cae hacia cero y dejan de interferir; un modelo grande alcanza ese punto, uno pequeño nunca lo hace
- Theorem 4 del paper bounding gradient norms por cuánto de su covarianza es inexplicado por la representación actual (residual signal)

## Related
- [[concepts/Structural-Exclusion]]
- [[concepts/Utility-Ranking-Theorem]]
- [[concepts/Scaling-Laws]]

## Source
[[summaries/AlphaSignalAI-Smaller-Models-Structurally-Excluded]]
