---
type: Concept
title: Gaussian Splats
description: Representación 3D para exploración visual, output junto con collision
  meshes en systems como World Labs Marble.
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Gaussian Splats

## Definition
Representación 3D para exploración visual, output junto con collision meshes en systems como World Labs Marble.

## Why It Matters
Permite generar entornos 3D explorables desde prompts multimodales (text, image, video, spatial sketch). Gaussian splats manejan la parte visual mientras collision meshes manejan la parte física — disolviendo la frontera entre renderer y simulator.

## Key Ideas
- Output de World Labs Marble junto con collision meshes
- Representación 3D optimizada para visual exploration
- Permite renderizar vistas desde cualquier ángulo
- No contiene información física — necesita collision meshes complementarias para interacción

## Related
- [[concepts/World-Model-Simulator]]
- [[concepts/World-Model-Renderer]]
- [[concepts/World-Models]]

## Source
[[summaries/DrFeifei-A-Functional-Taxonomy-of-World-Models]]
