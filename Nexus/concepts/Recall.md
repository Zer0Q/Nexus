---
type: Concept
title: Recall
description: Capacidad de un sistema de agente para recuperar conversaciones, datos
  o contexto de sesiones pasadas cuando se necesita información adicional. Es el mecanis...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Recall

## Definition
Capacidad de un sistema de agente para recuperar conversaciones, datos o contexto de sesiones pasadas cuando se necesita información adicional. Es el mecanismo de búsqueda sobre la memoria persistente.

## Why It Matters
Sin recall, la memoria persistente es solo un archivo estático. El recall permite buscar información relevante dinámicamente en el historial de interacciones, haciendo la memory efectiva en contextos variables.

## Key Ideas
- Búsqueda sobre el historial de conversaciones
- Recupera contexto relevante de sesiones anteriores
- Complementa la memory persistence (que guarda información)
- Diferente del context window (que es el límite de lo visible en una sesión)
- Implementado de forma diferente en cada framework

## Tradeoffs
- Búsqueda en grandes historiales puede ser lenta
- La calidad del recall depende de la indexación/subjetiva
- Demasiada información recuperada puede causar context rot

## Related
- [[concepts/Memory-Persistence]]
- [[concepts/Context-Engineering]]
- [[concepts/Context-Rot]]
- [[tools/Hermes-Agent]]

## Source
[[summaries/Santtiagom-Learning-Hermes-Part-1]]
[[summaries/Memory-Persistence]]
