---
title: How the Open Knowledge Format can improve data sharing
author: Sam McVeety, Amir Hormati
published: '2026-06-12'
type: article
resource: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/
timestamp: '2026-06-12T00:00:00Z'
description: Google Cloud presenta OKF (Open Knowledge Format) v0.1, una especificación
  open para representar metadata, contexto y conocimiento curado de forma portable
  e...
tags:
- summaries
---


# Open Knowledge Format (OKF)

## Summary

Google Cloud presenta OKF (Open Knowledge Format) v0.1, una especificación open para representar metadata, contexto y conocimiento curado de forma portable e interoperable. OKF formaliza el patrón LLM-wiki de Karpathy como un bundle de markdown con YAML frontmatter — sin SDKs, runtimes ni APIs complejas. Busca resolver la fragmentación del knowledge interno en organizaciones donde cada vendor tiene su propio catálogo, SDK y schema de knowledge-graph.

## Core Concepts

- [[concepts/Open-Knowledge-Format]] -- especificación open v0.1 para knowledge interoperable: directorio de markdown con YAML frontmatter, sin SDKs ni runtimes
- [[concepts/LLM-Wiki-Pattern]] -- patrón de knowledge base como wiki markdown que LLMs pueden leer, escribir y mantener automáticamente
- [[concepts/Knowledge-Interoperability]] -- capacidad de wikis escritas por distintos producers ser consumidas por distintos agents sin translation
- [[concepts/Knowledge-Fragmentation]] -- problema de knowledge interno disperso en sistemas incompatibles: metadata catalogs, wikis, code comments, heads of senior engineers
- [[concepts/Context-Assembly]] -- problema de ensamblar contexto desde superficies de conocimiento mutuamente incompatibles para cada agent builder
- [[concepts/Metadata-as-Code]] -- repositorio donde metadata se gestiona como código: versionable, reviewable, shippable como tarball

## Key Insights

- OKF v0.1 = directorio de markdown con YAML frontmatter + convenciones acordadas para type, title, description, resource, tags, timestamp
- "Just markdown" — readable en cualquier editor, renderable en GitHub, indexable por cualquier search tool
- "Just files" — shippable como tarball, hostable en cualquier git repo, mountable en cualquier filesystem
- "Just YAML frontmatter" — solo los campos que necesitan ser queryable
- Los vendors actuales ofrecen su propio catálogo, SDK y schema de knowledge-graph — ninguno portable
- Cada agent builder resuelve el mismo context-assembly problem desde scratch
- Karpathy: "LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass"
- El bookkeeping que causa que humans abandonen wikis personales es exactamente lo que LLMs son buenos en
- Patrones similares: Obsidian vaults wired a coding agents, AGENTS.md/CLAUDE.md, repos con index.md/log.md
- OKF permite que agents lean y actualicen su propia library de markdown mientras el team curate como código
- La arquitectura propuesta: knowledge como living wiki que crece en utilidad con el tiempo

## Open Questions
- ¿Cómo se mantiene la consistencia de schema cuando múltiples teams contribuyen a un OKF bundle?
- ¿OKF compite o complementa al LLM-wiki pattern de Karpathy?
- ¿Qué diferencia OKF de las convenciones existentes de frontmatter en Obsidian/Hugo?

## Source
- **Raw note:** [[raw-notes/how-the-open-knowledge-format-can-improve-data-sharing]]
- **Original URL:** https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/
