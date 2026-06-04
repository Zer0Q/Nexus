# KnoBuilder

## Definition
Agentic framework for autonomous, personalized knowledge graph construction from large-scale unstructured text corpora. Formalizes graph construction as iterative decision optimization where an intelligent agent continuously interacts with an evolving knowledge base.

## Why It Matters
Conventional extraction treats LLMs as passive text processors, producing fragmented and inconsistent graphs. KnoBuilder's agentic approach achieves 85% F1 on semantic extraction quality, 46% improvement in structured data acquisition efficiency, and 91% precision on complex entity disambiguation -- significantly outperforming REBEL and traditional GraphRAG.

## Key Ideas
- **Decision optimization objective:** Maximize expected utility of the generated graph over planning horizon T, balancing information relevance against compute cost
- **Four operational modules in closed loop:**
  1. Strategic Planning -- Analyzes current graph state and user profile to proactively identify information gaps; generates optimized search queries
  2. Filtering and Selection -- Evaluates retrieved document relevance; discards redundant/noisy information
  3. Self-Refining Extraction -- Multi-step validation: LLM extracts entities/relationships then immediately evaluates fidelity against source text for self-correction
  4. Dynamic Consolidation -- Integrates validated triples into global graph; resolves entity equivalence conflicts using advanced metrics
- **Termination conditions:** Budget exhaustion or no significant utility improvement detected
- **Utility function (U):** Three complementary qualitative variables -- Coverage (key concepts captured), Coherence (logical consistency), Personalization (alignment with user profile)

## Tradeoffs
- High compute cost per graph (iterative agent loops with multiple LLM calls)
- Personalization requires well-defined user profiles
- May over-optimize for stated preferences at expense of unexpected but valuable connections

## Related
- [[concepts/Zero-Shot-Ontology]]
- [[concepts/Entity-Resolution]]
- [[concepts/Agentic-GraphRAG]]
- [[tools/KGGen]]

## Source
[[summaries/DeepResearch-Semantic-Models-and-Agentic-Architectures]]
