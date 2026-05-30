# Long-Document Reasoning

## Definition
The ability of an AI model to maintain argument integrity and reasoning quality across a large context window without degradation. Claude maintains coherence at token 150,000 as sharply as at token 1,000, enabling it to reason over entire research corpora, full codebases, or months of notes.

## Why It Matters
Most AI tools lose coherence as the context window fills. Long-document reasoning means you can load a complete knowledge base and get equally sharp output from the last token as the first. This is the foundation that makes Claude Projects genuinely powerful for knowledge-intensive work.

## Key Ideas
- Claude's 200K token window maintains argument integrity throughout
- Output quality at token 150,000 is as sharp as at token 1,000
- Enables loading entire research corpora, full codebases, or months of accumulated notes
- Other models degrade as context fills; Claude does not
- This is what makes the vault + Claude combination multiplicative rather than additive

## Tradeoffs
- Large context windows cost more per request
- Not all tasks need the full window -- smaller tasks can use cheaper models
- Token limits still exist; extremely large corpora may exceed even 200K

## Related
- [[Instruction-Following-Precision]] -- companion capability of Claude's reasoning layer
- [[Five-Layer-AI-Stack]] -- Claude is the reasoning layer enabled by this capability
- [[Vault-Context]] -- the context that fills the window

## Source
[[Damidefi-Five-Tool-AI-Stack-Full-Build]]
