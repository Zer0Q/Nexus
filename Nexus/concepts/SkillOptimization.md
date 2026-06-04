# Skill Optimization

## Definition
Treating a compact natural-language skill document as the trainable state of a frozen agent, then optimizing that document through rollouts, reflection, and bounded edits gated by held-out validation. The skill file becomes an external parameter of a model whose weights never change.

## Why It Matters
Most engineers handwrite agent skill docs and hope they generalize. SkillOpt shows the doc itself should be optimized like a parameter -- a cheap, model-agnostic lever most teams are leaving on the table. The bottleneck shifts from base-model capability to how well you can train the natural-language state around a frozen agent.

## Key Ideas
- Optimizer model proposes validation-gated edits: adding, deleting, or replacing instructions
- Textual learning rate controls how aggressively each round rewrites the document
- Batch and momentum reported in text space rather than gradient space
- Every edit must pass a held-out check before being kept
- SkillOpt beats Trace2Skill, TextGrad, GEPA, EvoSkill, human-written skills, and one-shot skills (52/52 wins)
- +23.5 points on GPT-5.5, +24.8 in Codex loop, +19.1 in Claude Code from no-skill baseline

## Tradeoffs
- Optimization aggressiveness (textual learning rate) vs stability
- Validation set quality determines optimization direction
- Skill doc length -- compact docs optimize faster but may lack nuance

## Related
- [[concepts/Self-Evolving-Skills]]
- [[concepts/Skill-Curation-System]]
- [[concepts/Harness-Engineering]]

## Source
[[summaries/DAIR-Top-AI-Papers-of-the-Week]]
