# Expert Committee Simulation

## Definition
Using multiple AI models to simulate an expert committee review process, where each model acts as a domain expert evaluating the work of others. Models critique, agree, disagree, and iteratively improve the collective output.

## Why It Matters
Real expert committees benefit from diverse perspectives and constructive disagreement. AI models trained on different data and architectures provide analogous diversity. The simulation produces more rigorous analysis than any single expert (human or AI) working alone.

## Key Ideas
- Each model acts as an "expert" reviewing the committee's work
- Prompt: "Another committee of experts says this. What do you think?"
- Models generate new reports if they find issues with the current consensus
- The process mimics peer review in academic publishing
- Can be extended to 3+ models for greater combinatorial diversity

## Tradeoffs
- AI models are not actual domain experts -- they simulate expertise through training data
- Shared training biases may limit true diversity of perspective
- The simulation cannot replace genuine human expert judgment in critical domains
- Risk of performative disagreement (models disagreeing for its own sake)

## Related
- [[concepts/Adversarial-Model-Spiral]] -- the method that implements this simulation
- [[concepts/Multi-Model-Convergence]] -- the starting configuration
- [[concepts/AI-Assisted-Medical-Research]] -- the domain where this is most impactful

## Source
[[summaries/JaviLopen-AI-Medical-Research-ARROWHEAD]]
