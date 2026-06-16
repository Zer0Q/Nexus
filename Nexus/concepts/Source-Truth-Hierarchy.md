---
type: Concept
title: Source Truth Hierarchy
description: Diseño operativo que define qué fuente de información gana cuando hay
  conflictos entre sources (sales call vs CRM field vs Slack correction vs old SOP
  vs wee...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Source Truth Hierarchy

## Definition
Diseño operativo que define qué fuente de información gana cuando hay conflictos entre sources (sales call vs CRM field vs Slack correction vs old SOP vs weekly report).

## Why It Matters
Sin source hierarchy, los agents se convierten en confident liars con mejor formatting. Algunas sources son live truth, otras son historical context, otras son inspiration, otras nunca deben usarse en contenido público. La distinción importa más a medida que el company brain crece.

## Key Ideas
- Live truth vs historical context vs inspiration vs never-quote
- Debe definirse como operating design problem, no como afterthought
- A good answer de un AI system tiene que ser accurate Y source-aware
- La jerarquía se vuelve crítica cuando el volumen de sources crece — más sources = más conflictos potenciales

## Related
- [[concepts/Company-Brain-Architecture]]
- [[concepts/Retrieval-First-Organization]]
- [[concepts/Knowledge-Source-of-Truth]]

## Source
[[summaries/EricOsiu-How-we-built-a-Single-Company-Brain]]
