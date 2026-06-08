# RLAIF

## Definition
Reinforcement Learning from AI Feedback — swaps the human labeler in RLHF for an LLM judge, achieving RLHF-level quality at a fraction of the cost.

## Why It Matters
Eliminates the expensive human labeling bottleneck from the alignment pipeline while maintaining comparable quality. Anthropic's Constitutional AI demonstrated this approach at scale.

## Key Ideas
- LLM generates preference data by evaluating outputs against written principles (constitution)
- AI judges its own outputs against rules, then uses those judgments as RL signal
- Conceptual shift: a document of rules replaces an army of human evaluators
- Cheaper and faster than human labeling, enabling larger preference datasets

## Tradeoffs
- AI judge quality depends on the constitution/principles quality
- Risk of mode collapse if the judge is too lenient or too strict
- May not capture nuanced human preferences that are hard to articulate as rules

## Related
- [[concepts/RLHF]]
- [[concepts/DPO]]
- [[concepts/System-Prompt-Learning]]
- [[concepts/RULER]]

## Source
[[summaries/avichawla-Top-15-Fine-Tuning-Techniques]]
