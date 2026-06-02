# Software Factory Ladder

## Definition
Five-level maturity model (0-4) for AI-powered software engineering organizations. Measures how much of the development pipeline runs without human intervention, from artisan craft to autonomous factory.

## Why It Matters
Most companies overestimate their AI maturity. The ladder provides concrete, observable criteria for where an org actually sits, not where they think they are. Key metric: % of PRs shipping without human review.

## Key Ideas
- Level 0 (Artisan): Everything human. Engineer writes, reviews, tests, deploys by hand.
- Level 1 (Assisted): AI copilot helps engineer type faster. Human gates every step. MOST companies here.
- Level 2 (Delegated): Agent writes code and opens PR. Human still reviews. MOST "AI-forward" companies stuck here.
- Level 3 (Supervised Factory): Agent monitors, catches bugs, writes fixes, second agent reviews, auto-merges low-risk. Humans set guardrails. Very few orgs here.
- Level 4 (Autonomous): Full agent loop. Humans decide product direction, not implementation. Almost nobody here.
- Climb by removing human from one more step, backed by safety net (tests, version control, internal platform)
- Level 2->3 hardest: requires automated tests you'd bet on + internal platform agents plug into

## Tradeoffs
- Higher levels require more infrastructure investment
- Safety net quality determines how far up you can safely climb
- Not all functions are equally ready (verifiability matters)

## Related
- [[concepts/Verifiable-Automation]]
- [[frameworks/Industrialized-Software-Development]]

## Source
[[source-notes/BusinessBarista-Software-Factory]]
