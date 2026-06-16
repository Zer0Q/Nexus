---
type: Concept
title: Context Mining
description: The process of reverse-engineering business operations from fragmented
  reality -- connecting to systems of record, data, knowledge, work, and runtime signals...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Context Mining

## Definition
The process of reverse-engineering business operations from fragmented reality -- connecting to systems of record, data, knowledge, work, and runtime signals (query history, agent traces, human overrides) to extract semantics and skills that were never explicitly documented.

## Why It Matters
Most business context was never written down. The durable methods are system-led: extracting skills from agent sessions, building process maps from event logs, capturing context where agents fail, and running structured AI interviews to surface judgment that observation alone cannot reach.

## Key Ideas
- Mining semantics: AI reads SQL query history, notices conflicting definitions, surfaces conflicts for human resolution
- Mining skills: harder because procedural knowledge was never written down; produces candidates, not finished skills
- System-led methods: agent session extraction, event log process maps, failure-point capture, AI interviews
- AI does the heavy lifting; humans decide what becomes canonical
- None of these methods produces a finished skill alone -- they produce candidates for the next capability to test and deploy

## Tradeoffs
- Automated mining scale vs human review quality
- Mining from logs (what was done) vs mining from interviews (why it was done)
- Frequency of re-mining vs staleness of extracted context

## Related
- [[concepts/Enterprise-Context-Layer]]
- [[concepts/Skills-as-Primitives]]
- [[concepts/Context-Development-Lifecycle]]

## Source
[[summaries/Prukalpa-Enterprise-Context-Layer]]
