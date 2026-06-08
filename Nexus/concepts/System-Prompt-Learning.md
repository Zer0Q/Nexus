# System Prompt Learning

## Definition
Proposed learning paradigm where the system prompt carries a richer signal than scalar rewards, and RL training leverages that signal directly rather than relying solely on hand-crafted reward functions.

## Why It Matters
Identified by Karpathy as a missing major learning paradigm for LLMs. The system prompt already defines what the agent should do — encoding those instructions as an implicit reward function eliminates the engineering overhead of writing custom scoring code.

## Key Ideas
- System prompt as implicit reward function: the instructions already define faithfulness, completeness, conciseness criteria
- RULER is a practical implementation: judge LLM reads the system prompt and applies its criteria without Python implementation
- Tighter system prompts produce tighter evaluations — the judge adapts automatically without changing scoring code
- Replaces days of reward function calibration with a single document of rules (similar to Anthropic's Constitutional AI approach)

## Tradeoffs
- Still requires an LLM judge call per training step
- Quality depends on how well the system prompt articulates desired behavior
- May not replace verifiers for purely deterministic tasks where binary checks are cleaner

## Related
- [[concepts/RULER]]
- [[concepts/RLAIF]]
- [[concepts/RLVR]]

## Source
[[summaries/avichawla-RL-Agents-2026-System-Prompt-Learning]]
