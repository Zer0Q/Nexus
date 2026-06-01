# Context Explosion

## Definition
The degradation of AI agent quality as the context window fills with specifications, architecture docs, conversation history, and code. Large specs and accumulated artifacts consume tokens that could be used for reasoning, leading to hallucination, missed constraints, and lower-quality output.

## Why It Matters
The fundamental scalability bottleneck of AI-assisted development frameworks. Tools like BMAD generate substantial artifacts (PRD, architecture, stories), which must all fit in the agent's context — creating a hard limit on project complexity.

## Key Ideas
- Context window is a finite resource shared between input and reasoning
- Large specs -> less room for agent reasoning -> lower quality output
- Mitigation: fresh chats per workflow, focused context injection, artifact summarization
- The weakest link in BMAD and similar frameworks

## Related
- [[concepts/LLM-Harness]]
- [[frameworks/BMAD-Method]], [[frameworks/Spec-Driven-Development]], [[concepts/Multi-Agent-Development]], [[concepts/KV-Cache-Growth]]

## Source
[[source-notes/SDD-vs-BMAD-Frameworks-Comparison]]
