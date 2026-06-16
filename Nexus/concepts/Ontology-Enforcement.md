---
type: Concept
title: Ontology Enforcement
description: A validation mechanism where a supervisor agent audits extracted knowledge
  graphs against predefined ontological rules and business logic constraints, genera...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Ontology Enforcement

## Definition
A validation mechanism where a supervisor agent audits extracted knowledge graphs against predefined ontological rules and business logic constraints, generating self-correction instructions when violations are detected.

## Why It Matters
Raw LLM extraction produces fragmented, inconsistent graphs with spurious relationships. Ontology Enforcement acts as a quality gate, ensuring extracted entities and relationships conform to domain-specific logical rules before entering production knowledge bases.

## Key Ideas
- **Supervisor agent pattern** -- Dedicated agent validates graph against ontology rules (description logic constraints, business rules)
- **Self-correction loop** -- When violations detected (e.g., relating a control variable to a non-existent physical component), the supervisor generates correction prompts for the extraction agent
- **Real-time auditing** -- Validation happens continuously during graph construction, not as a post-processing step
- **Rule types:** Taxonomic consistency (is-a hierarchies), attribute constraints (T-Box definitions), business rules (mandatory certifications, physical dependencies)
- **Complements Zero-Shot Ontology** -- Dynamically inferred schemas can be locked and enforced for subsequent extraction cycles

## Tradeoffs
- Adds latency to extraction pipeline (additional LLM calls per validation cycle)
- Rule coverage must be comprehensive; gaps allow invalid relationships through
- Overly strict rules may reject valid but novel relationships

## Related
- [[concepts/Semantic-Model]]
- [[concepts/Zero-Shot-Ontology]]
- [[concepts/Entity-Resolution]]
- [[concepts/Three-Layer-Semantic-Infrastructure]]

## Source
[[summaries/DeepResearch-Semantic-Models-and-Agentic-Architectures]]
