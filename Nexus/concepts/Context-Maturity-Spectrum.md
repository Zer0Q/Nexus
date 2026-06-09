# Context Maturity Spectrum

## Definition
A four-level progression describing how much structure a context layer imposes on its data, from raw retrieval to formal inference. Applies independently within each tier of the [[concepts/Context-Layer-Taxonomy]].

## The Four Levels

### Level 1: Pure RAG
Extract facts, embed them, retrieve similar-looking chunks. No model of how anything connects. Cheapest to stand up; sufficient when memory is "what did the user tell me." Examples: Mem0, Hyperspell, SQLite AI, Onyx AI.

### Level 2: Hybrid Retrieval
Still file-backed or index-backed, but keeps facts and relationships alongside embeddings. A semantic layer with optional graph extraction. The sweet spot for practitioner enthusiasm. Examples: Mnemosyne Labs, Dust, Signet AI.

### Level 3: Graph-Native
An interlinked knowledge base where the graph IS the architecture. The agent compiles accumulated context into a self-maintained web of entities and relationships. Karpathy LLM-wiki / Obsidian-vault pattern is the reference. Gbrain, Glean.

### Level 4: Full Ontology
Rules over entities enable the system to INFER facts never explicitly written down. Adds temporal context ("true from / true until"). Almost nothing in conversational memory reaches this level; it's the enterprise problem. Examples: Palantir Foundry + AIP, cognee, Zep AI, Stardog.

## Why It Matters
Where you sit on the spectrum is a bet about how much accumulated context you expect. At the low end, you barely model anything; at the high end, you model everything and pay for it. The wrong level means either the agent can't do the job (too thin) or you're maintaining an ontology to answer questions vector search could handle (too heavy).

## Key Ideas
- The spectrum is independent of company size — a startup automating finance might need Level 4
- Each level builds on the one before; you don't skip levels
- Graph-native (Level 3) is where most "company brain" products actually live
- Full ontology (Level 4) adds inference — deriving facts never written down

## Related
- [[concepts/Context-Layer-Taxonomy]]
- [[concepts/Knowledge-Graph]]
- [[concepts/RAG]]
- [[concepts/LLM-Wiki-Pattern]]

## Source
[[summaries/BouBalust-Context-Layer-Landscape]]
