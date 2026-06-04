# Model Selection Tiers

## Definition
A three-tier model selection framework for Hermes Agent: expensive (Claude Opus/Sonnet), moderate (GPT-5.5), and affordable (Qwen 3.7 Max, Grok, Nous Portal). The right choice depends on the task, not just budget.

## Why It Matters
Choosing the wrong model wastes money or produces poor results. This framework helps match model capability to task complexity, optimizing the cost-quality tradeoff for each use case.

## Key Ideas
- **Expensive tier** (Claude Opus-4 / Sonnet-4): Complex reasoning, long /goal tasks, nuanced writing, business advisor role. Claude handles ambiguity best. Budget: hundreds/month with heavy use.
- **Moderate tier** (GPT-5.5): Coding tasks, prototyping, budget-conscious daily driver. Works with existing $20/month ChatGPT subscription. Start here if new.
- **Affordable tier** (Qwen 3.7 Max, Grok, Nous Portal): Long-horizon autonomous tasks (Qwen: 35h continuous, 1000+ tool calls), X-related research (Grok), flat-rate billing (Nous Portal at $20/month)
- Switch models anytime via `hermes model` — no code changes, different profiles can run different models simultaneously

## Tradeoffs
- Expensive models cost more but handle ambiguity and judgment calls better
- Affordable models may struggle with nuanced reasoning or complex multi-step goals
- Model switching mid-session is possible but context-dependent

## Related
- [[concepts/Goal-Command]] -- model choice affects /goal execution quality
- [[concepts/Agent-Profiles]] -- different profiles can run different models
- [[concepts/Hermes-Dashboard]] -- Models tab for instant model swapping

## Source
[[summaries/IBuzovskyi-Hermes-Agent-Complete-Guide]]
