# Spec-Driven Development

## Definition
Development methodology where the specification is the central artifact. The spec drives planning, task decomposition, architecture decisions, and implementation. Tools like Spec-Kit, OpenSpec, and BMAD operationalize this approach.

## Why It Matters
Provides traceability from requirements to code, reduces LLM drift in AI-assisted development, and forces architectural thinking before implementation begins.

## Key Ideas
- Spec is the single source of truth, not the code or the prompts
- Iterative refinement: spec evolves as understanding deepens
- Tools range from minimal (OpenSpec) to full Agile simulation (BMAD)
- Without verifiable specs, AI generates code faster AND debt faster

## Tradeoffs
- Overhead for small projects (document-driven procrastination risk)
- Spec quality directly impacts output quality — garbage in, garbage out
- Large specs cause context explosion in LLM agents

## Related
- [[concepts/Risk-by-Design]]
- [[frameworks/BMAD-Method]], [[concepts/Vibe-Coding]], [[concepts/Agentic-SDLC]], [[frameworks/Artifact-Pipeline]]

## Source
[[source-notes/SDD-vs-BMAD-Frameworks-Comparison]]
