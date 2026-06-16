---
type: Concept
title: Metadata-as-Code
description: 'Repositorio donde metadata se gestiona como código: versionable, reviewable,
  shippable como tarball. Permite que agents lean y actualicen su propia library d...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Metadata-as-Code

## Definition
Repositorio donde metadata se gestiona como código: versionable, reviewable, shippable como tarball. Permite que agents lean y actualicen su propia library de markdown mientras el team curate como código.

## Why It.OKF
- OKF bundles son shippable como tarball, hostable en git repo, mountable en filesystem
- Agents pueden touch 15 files en un pass sin boredom ni forgetting
- Bookkeeping que causa que humans abandonen wikis es exactamente lo que LLMs hacen bien
- Knowledge como living wiki que crece en utilidad con el tiempo
- Pattern: metadata como código en repositorios de data teams

## Key Ideas
- Markdown como universal format para knowledge
- YAML frontmatter para campos queryable
- Git para versioning y collaboration
- Tarball para distribution entre systems
- Agents como curadores automáticos del knowledge base
- Humans como reviewers del knowledge evolution

## Tradeoffs
- Agents pueden introducir errors o drift en metadata
- Humans vs agents en curation: quién decide qué es importante
- Versioning de knowledge vs versioning de código
- Security: qué metadata es safe para agents modificar

## Related
- [[concepts/Open-Knowledge-Format]]
- [[concepts/Knowledge-Interoperability]]
- [[concepts/LLM-Wiki-Pattern]]

## Source
[[summaries/google-open-knowledge-format-okf]]
