---
type: Concept
title: Utility Ranking Theorem
description: 'Teorema (Theorem 3 del paper Stanford/Harvard/MIT/Anthropic 2026) que
  establece que un modelo de ancho N aprende features en orden de su score de utilidad:
  u...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Utility Ranking Theorem

## Definition
Teorema (Theorem 3 del paper Stanford/Harvard/MIT/Anthropic 2026) que establece que un modelo de ancho N aprende features en orden de su score de utilidad: utility(k,j) = task_frequency(k) × feature_complexity(k,j). Features con mayor utilidad se aprenden primero; features con menor utilidad requieren modelos más grandes.

## Why It Matters
Convierte el sizing de modelos de una pregunta empírica ("run ablations until something works") en un problema de razonamiento: si conoces la frecuencia de una tarea en tu distribución de training y su complejidad aproximada, puedes razonar sobre el tamaño mínimo de modelo necesario para aprenderla.

## Key Ideas
- utility(k,j) = task_frequency(k) × feature_complexity(k,j)
- Una tarea rara con muchas features complejas tiene scores de utilidad bajos en general
- Necesita un modelo lo suficientemente grande como para satisfacer todas las features de alta utilidad primero, dejando capacidad residual disponible para las raras
- Las predicciones analíticas del teorema coinciden casi exactamente con los límites empíricos del phase diagram experimental
- No es curve-fitting a posteriori: los límites se predijeron desde la teoría antes de correr los experimentos
- Implicación: aumentar frecuencia de tareas raras en fine-tuning ayuda (sube el score de utilidad) pero por debajo de cierto tamaño de modelo, los gradientes de tareas frecuentes siguen dominando

## Related
- [[concepts/Structural-Exclusion]]
- [[concepts/Update-and-Forget-Loop]]
- [[concepts/Scaling-Laws]]

## Source
[[summaries/AlphaSignalAI-Smaller-Models-Structurally-Excluded]]
