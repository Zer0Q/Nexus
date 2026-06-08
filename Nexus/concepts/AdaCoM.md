# AdaCoM

## Definition
Adaptive Context Manager — a separate external model trained with reinforcement learning to manage the context of a frozen agent through flexible modification actions (keep/compress/drop), optimized end-to-end against task outcomes.

## Why It Matters
Treats context management as a separate, trainable, transferable module rather than baking it into every agent's prompt or weights. Transfers across similar agents, improving web search and deep research by preserving task constraints and progress while pruning stale content.

## Key Ideas
- Dedicated model edits the agent's working context; the agent itself never changes
- Trained with RL against task outcomes, learning context-editing policies instead of hand-written heuristics
- Transfers across agents of similar capability, pointing toward genuinely reusable context managers
- Fixes context bloat from the outside without touching the underlying model

## Tradeoffs
- Transfer works best across agents of similar capability; cross-tier transfer is limited
- Adds a second model to the inference pipeline (context manager + agent)
- Requires RL training data for the context manager separately from the agent

## Related
- [[concepts/Context-Engineering]]
- [[concepts/Context-Window]]
- [[concepts/State-Externalizing-Harnesses]]

## Source
[[summaries/DAIR-Top-AI-Papers-of-the-Week-June-7]]
