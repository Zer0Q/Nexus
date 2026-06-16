---
type: Concept
title: Open Knowledge Format
description: 'OKF v0.1: especificación open para knowledge interoperable. Representa
  knowledge como directorio de markdown con YAML frontmatter, formalizando el patrón
  LLM...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Open Knowledge Format

## Definition
OKF v0.1: especificación open para knowledge interoperable. Representa knowledge como directorio de markdown con YAML frontmatter, formalizando el patrón LLM-wiki en formato portable sin SDKs, runtimes ni APIs complejas.

## Why It Matters
Cada vendor de knowledge tiene su propio catálogo, SDK y schema de knowledge-graph, lockeando knowledge detrás de la superficie que lo creó. OKF busca estandarizar metadata, context y knowledge curado para que wikis de distintos producers sean consumibles por distintos agents sin translation.

## Key Ideas
- OKF v0.1 = directorio markdown + YAML frontmatter + convenciones acordadas
- Campos: type, title, description, resource, tags, timestamp
- "Just markdown" — readable en cualquier editor, renderable en GitHub, indexable por cualquier search tool
- "Just files" — shippable como tarball, hostable en git repo, mountable en filesystem
- "Just YAML frontmatter" — solo campos queryable
- Formaliza patrón LLM-wiki de Karpathy en spec portable
- Vendor-neutral, agent- y human-friendly
- Similar a Obsidian/Notion/Hugo pero con schema acordado para interoperabilidad

## Tradeoffs
- v0.1 es early spec — conventions pueden cambiar
- Minimalista: solo frontmatter básico, no schema complejo
- Depende de adoption por múltiples producers para ser útil
- No resuelve discovery/search de knowledge entre bundles

## Related
- [[concepts/LLM-Wiki-Pattern]]
- [[concepts/Knowledge-Interoperability]]
- [[concepts/Knowledge-Fragmentation]]
- [[concepts/Metadata-as-Code]]

## Source
[[summaries/google-open-knowledge-format-okf]]
