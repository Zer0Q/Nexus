# Agentic Engineering Maturity

## Definition
Assessment of how much of the software development pipeline runs without human intervention. Measured by % of PRs shipping without human review, agent autonomy level, and safety net quality.

## Why It Matters
Most companies overestimate their AI maturity. Concrete metrics (PR auto-merge rate, agent-initiated tickets, test coverage) reveal actual vs perceived maturity.

## Key Ideas
- Level 0: Everything human
- Level 1: AI copilot assists engineer (most companies)
- Level 2: Agent writes code, human reviews (most "AI-forward" companies)
- Level 3: Agent monitors, fixes, reviews, auto-merges low-risk (very few)
- Level 4: Full agent loop, humans direct product (almost none)
- Key metric: % of PRs shipping without human review
- Safety net quality determines how far up you can climb

## Tradeoffs
- Higher levels require more infrastructure investment
- Not all functions are equally ready (verifiability matters)

## Related
- [[concepts/Software-Factory-Ladder]]
- [[concepts/Verifiable-Automation]]

## Source
[[summaries/BusinessBarista-Software-Factory]]
