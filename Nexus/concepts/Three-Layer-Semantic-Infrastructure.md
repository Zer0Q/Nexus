---
type: Concept
title: Three-Layer Semantic Infrastructure
description: 'A three-tier architecture for enterprise semantic data infrastructure:
  Semantic Model (Layer 1) → Domain Ontologies (Layer 2) → Knowledge Graph (Layer
  3). Pr...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Three-Layer Semantic Infrastructure

## Definition
A three-tier architecture for enterprise semantic data infrastructure: Semantic Model (Layer 1) → Domain Ontologies (Layer 2) → Knowledge Graph (Layer 3). Provides autonomous agents with clear operational constraints beyond narrative prompts.

## Why It Matters
Replaces custom point-to-point integrations between every system pair with a single shared semantic backbone. For 10 systems: 90 integrations → 10. For 50 systems: 2450 → 50. This linear scaling is essential for regulatory compliance (EU AI Act requires full data traceability and inference auditability).

## Key Ideas
- **Layer 1 -- Semantic Model:** Shared vocabulary, persistent identifiers, base concepts. The foundational level defining what the business operates on.
- **Layer 2 -- Domain Ontologies:** Logical rules, structural constraints, business rules (e.g., mandatory certifications). The enforcement layer.
- **Layer 3 -- Knowledge Graph:** Real data instances, interconnected with real-time traceability and provenance. The operational layer.
- **Hybrid execution flow:** Vector recall → topological validation on graph → ontological filtering → deterministic API execution
- **Three-tier agent memory:** Factual (entity states), Procedural (standardized sequences), Temporal (transaction history)

## Tradeoffs
- Higher upfront design cost vs prompt-only approaches
- Requires ongoing ontology maintenance as business rules evolve
- Layer 2 constraints may reject valid edge-case inferences

## Related
- [[concepts/Semantic-Model]]
- [[concepts/Ontology-Enforcement]]
- [[concepts/Agentic-GraphRAG]]
- [[concepts/Entity-Resolution]]

## Source
[[summaries/DeepResearch-Semantic-Models-and-Agentic-Architectures]]
