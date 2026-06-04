# Vibe Coding

## Definition
Direct prompt-to-code development approach where developers describe what they want in natural language and AI generates code immediately, without intermediate specifications, architecture docs, or planning artifacts.

## Why It Matters
Represents the lowest-friction entry point to AI-assisted development. Useful for rapid prototyping and small tasks, but lacks traceability, quality gates, and scalability for production systems.

## Key Ideas
- Prompt -> code, no intermediate artifacts
- Best for: demos, spikes, small PoCs, quick experiments
- Does not scale: no traceability, no architecture review, no test coverage
- AI amplifies ambiguity — vague prompts produce vague code faster

## Tradeoffs
- Fastest for small tasks, slowest for debugging large codebases
- No architectural oversight leads to technical debt accumulation
- Difficult to onboard team members or maintain long-term

## Related
- [[concepts/Prompt-Validation-Over-Construction]]
- [[tools/Spec-Driven-Development]], [[tools/BMAD-Method]], [[concepts/Agentic-SDLC]]

## Source
[[summaries/SDD-vs-BMAD-Frameworks-Comparison]]
