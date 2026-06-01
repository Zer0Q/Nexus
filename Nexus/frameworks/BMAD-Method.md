# BMAD Method

## Definition
Breakthrough Method for Agile AI-Driven Development. Framework that simulates an Agile team using specialized AI agents (Analyst, PM, Architect, Developer, QA) working through structured phases: Analysis, Planning, Solutioning, Implementation.

## Why It Matters
Replaces unstructured "vibe coding" with traceable workflows, PRDs, explicit architecture, and task decomposition. Scales from quick fixes to enterprise compliance projects through three planning tracks.

## Key Ideas
- Multi-agent orchestration: each agent has a defined role and responsibilities
- Four phases: Analysis (optional) -> Planning (required) -> Solutioning -> Implementation
- Three tracks: Quick Flow (1-15 stories), BMAD Method (10-50+), Enterprise (30+, compliance)
- BMad-Help: intelligent guide that inspects project state and recommends next steps
- Fresh chats per workflow prevent context contamination

## Tradeoffs
- High overhead for small PoCs — can be slower than direct prompting
- Context explosion: large specs degrade agent quality
- Risk of document-driven procrastination
- Not revolutionary — operationalizes classic Agile for LLM agents

## Related
- [[frameworks/Spec-Driven-Development]], [[concepts/Multi-Agent-Development]], [[concepts/Vibe-Coding]], [[concepts/Context-Explosion]]

## Source
[[source-notes/BMAD-Method-Getting-Started]], [[source-notes/SDD-vs-BMAD-Frameworks-Comparison]]
