# ODKE+

## Definition
Apple's Ontology-Guided Open-Domain Knowledge Extraction system. Five-module pipeline for massive automated extraction of high-precision factual facts from web sources, reducing knowledge graph update lag from months to days.

## Why It Matters
Traditional manual KG updates take ~50 days. ODKE+ processed 9M Wikipedia pages, integrating 19M new high-confidence facts at 98.8% extraction precision -- demonstrating industrial-scale, ontology-constrained extraction is viable.

## Key Ideas
- **Five sequential modules:**
  1. Extraction Initiator -- Detects missing critical facts or obsolete temporal data; triggers on-demand updates
  2. Evidence Retriever -- Locates and stores structured supporting documents from authoritative web sources
  3. Hybrid Knowledge Extractors -- Combines traditional lexical-rule engines with ontology-guided LLMs; generates dynamic ontology fragments adapted to entity type (195 structured predicates without saturating attention windows)
  4. Grounder (Anchor Validator) -- Secondary optimized LLM validates that proposed entities/predicates match original text evidence
  5. Corroborator -- Logical normalization, confidence scoring, atomic integration of verified facts into central KG
- **Dynamic ontology fragments** -- Instead of loading the full corporate ontology, generates type-specific fragments, preventing attention window saturation
- **195 structured predicates** catalog with enforced type consistency

## Tradeoffs
- Requires pre-existing corporate ontology with well-defined predicates
- Five-module pipeline adds latency vs single-pass extraction
- Authority-based source selection may exclude valid but less-established sources

## Related
- [[concepts/Ontology-Enforcement]]
- [[concepts/Entity-Resolution]]
- [[tools/OntoGPT]]
- [[tools/KGGen]]

## Source
[[source-notes/DeepResearch-Semantic-Models-and-Agentic-Architectures]]
