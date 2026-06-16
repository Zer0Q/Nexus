---
type: Concept
title: Context Layer Taxonomy
description: A three-tier classification of AI context problems based on the kind
  of context being dealt with. Each tier has distinct tools, requirements, and complexity....
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Context Layer Taxonomy

## Definition
A three-tier classification of AI context problems based on the kind of context being dealt with. Each tier has distinct tools, requirements, and complexity. Tiers build on each other: bucket 1 is the agent's own context, bucket 2 adds institutional knowledge, bucket 3 adds systems of record.

## The Three Tiers

### Tier 1: Agent's Context
What you tell your agent — instruction files, conversation history, accumulated memory. Self-contained; no company stack behind it. Tools range from flat-file RAG (Mem0, SQLite AI) to full ontologies (Zep AI, cognee).

### Tier 2: Institutional Knowledge
The docs, chats, notes, and tickets scattered across apps where work happens (Slack, Notion, Drive, email). The bucket most people actually mean. Split into surface-owners (Slack, Notion, Glean) and neutral layers (Onyx AI, Hyperspell).

### Tier 3: Systems of Record
Structured sources (warehouses, databases, CRM) plus unstructured ones, across systems never built to talk to each other. The only tier where governance, access control, and auditability are mandatory, not optional. Palantir Foundry, Modern Relay, Stardog.

## Why It Matters
Misidentifying your tier is the common failure mode. Overshooting into bucket 3 when retrieval suffices wastes resources. Undershooting starves agents of context they actually need. The application layer pays for the mismatch.

## Key Ideas
- Company size is a rough proxy but not the determinant — Glean sells to enterprises but operates in bucket 2
- Each tier uses the same internal spectrum: pure RAG → hybrid → graph-native → ontology
- Governance emerges as a tax with scale, not as a separate tier
- The deepest moat is tacit context (workarounds, judgment) that was never written down

## Related
- [[concepts/Context-Maturity-Spectrum]]
- [[concepts/Surface-Owners-vs-Neutral-Layers]]
- [[concepts/Governance-Tax]]
- [[concepts/Enterprise-Context-Layer]]

## Source
[[summaries/BouBalust-Context-Layer-Landscape]]
