# Iterative Model Refinement

## Definition
Successive rounds of cross-model review where each model critiques and improves the other's output. Unlike single-pass multi-model comparison, iterative refinement feeds the improved output back into the opposing model, creating a sharpening spiral of increasingly rigorous analysis.

## Why It Matters
A single round of model comparison shows agreement/disagreement. Multiple rounds force each model to defend its conclusions against increasingly sophisticated counterarguments, producing outputs that are more thoroughly vetted than any single pass could achieve.

## Key Ideas
- Minimum 7 iterations recommended for medical research
- Each round: Model A reviews Model B's output, generates improved version; feed back to Model B
- With extended thinking models (~40 min per call), this takes hours
- Stopping criterion: both models agree the work cannot be improved
- Analogy: sharpening a stake until it gets a gleaming point
- Can be automated with orchestration frameworks

## Tradeoffs
- Exponential token cost with iterations
- Risk of over-refinement: models may polish style without improving substance
- Diminishing returns after a certain number of iterations
- May never converge on genuinely novel or controversial topics

## Related
- [[Adversarial-Model-Spiral]] -- the broader methodology
- [[Multi-Model-Convergence]] -- the starting point for iteration
- [[Expert-Committee-Simulation]] -- the metaphor for this process

## Source
[[JaviLopen-AI-Medical-Research-ARROWHEAD]]
