# ARROWHEAD

## Definition
Adversarial model spiral methodology: a technique for improving AI output quality by pitting multiple models against each other in successive rounds of review and refinement. Named by @javilopen during a month-long AI-assisted medical research project for a metastatic cancer case.

## Why It Matters
Represents a process-level improvement to AI output quality that does not require better models -- just multiple model access and iterative adversarial review. Claimed to be domain-agnostic, applicable to medicine, programming, mathematics, and any analytical field.

## Key Ideas
- Acronym: Adversarial ReReview Of Work Hitting An Elevated Definitive point
- Process: Model A reviews Model B's output, generates improved version; feed back to Model B; repeat 7+ rounds
- Stopping criterion: both models agree the work cannot be improved
- Automation: can be orchestrated with AutoGen, LangGraph, or CrewAI
- The "spiral" metaphor: each iteration sharpens the output like sharpening a stake

## Related
- [[concepts/Adversarial-Model-Spiral]] -- the full concept note
- [[concepts/Multi-Model-Convergence]] -- the starting point
- [[concepts/Iterative-Model-Refinement]] -- the iterative mechanism

## Source
[[source-notes/JaviLopen-AI-Medical-Research-ARROWHEAD]]
