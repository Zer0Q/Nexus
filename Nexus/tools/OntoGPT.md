# OntoGPT

## Definition
Schema-guided semantic knowledge extraction system developed by the Monarch Initiative for scientific domains. Implements the SPIRES methodology (Structured Prompt Interrogation and Recursive Extraction of Semantics) using LinkML schemas for mandatory grounding to public ontologies.

## Why It Matters
In scientific domains (biomedicine, environmental sciences), extracted entities MUST map to community-validated ontologies (HPO, Gene Ontology, MONDO). OntoGPT enforces this through mandatory grounding -- unregistered entities are invalidated, ensuring full interoperability of the generated graph.

## Key Ideas
- **SPIRES methodology:** Two inputs -- formal LinkML schema + unstructured text body
- **Four-step workflow:**
  1. Attribute definition and prompt generation from LinkML schema (multivalue flags, persistent IDs, semantic ranges)
  2. Zero-shot structured inference -- LLM generates pseudo-YAML response optimized for computational reading
  3. Recursive parsing (ParseCompletion) -- Line-by-line analysis splitting on first colon delimiter; recursive calls for nested attributes
  4. Mandatory semantic grounding -- All named entities mapped to persistent identifiers from public ontologies (AgroPortal, BioPortal, Gene Ontology, Human Phenotype Ontology); unregistered entities are invalidated
- **Predefined schema templates:** Biomedicine (Alzheimer's, Drugs, Mendelian Diseases, Phenotypes), Environmental Sciences (Samples, Metagenome, Biochemical Reactions), Data Management (Datasheets, Data Ontology Classes)

## Tradeoffs
- Requires domain-specific LinkML schemas (not Zero-Shot)
- Mandatory grounding rejects valid but unregistered entities
- Pseudo-YAML intermediate format adds parsing complexity

## Related
- [[concepts/Ontology-Enforcement]]
- [[concepts/Semantic-Model]]
- [[tools/ODKE-Plus]]

## Source
[[summaries/DeepResearch-Semantic-Models-and-Agentic-Architectures]]
