---
type: Concept
title: Sim-to-Real Gap
description: Diferencia entre cómo las cosas se comportan en simulación vs cómo se
  comportan en la realidad. Problema abierto en robótica y world models.
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Sim-to-Real Gap

## Definition
Diferencia entre cómo las cosas se comportan en simulación vs cómo se comportan en la realidad. Problema abierto en robótica y world models.

## Why It Matters
Es uno de los hardest open problems en el campo de world models. Un simulator puede ser visualmente perfecto y físicamente preciso en su dominio, pero las diferencias con el mundo real — fricción, iluminación, materiales, ruido sensorial — hacen que políticas entrenadas en simulación fallen en producción.

## Key Ideas
- Persiste incluso con simulators de alta fidelidad
- Generative simulators introducen nuevo riesgo: geometría AI-generated con self-intersections o escala errónea produce física nonsensical
- Multi-physics simulation at scale sigue siendo órdenes de magnitud más caro que single-domain
- Los datos 3D con geometría explícita, propiedades de materiales y anotaciones físicas son órdenes de magnitud más escasos que internet video

## Related
- [[concepts/World-Model-Simulator]]
- [[concepts/World-Models]]
- [[concepts/Physical-AI]]

## Source
[[summaries/DrFeifei-A-Functional-Taxonomy-of-World-Models]]
