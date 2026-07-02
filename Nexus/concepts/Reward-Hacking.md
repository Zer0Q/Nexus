# Reward Hacking

## Definition
Reward hacking is when an optimizer satisfies the metric or check while failing the intended task, such as making tests pass by weakening tests instead of fixing the implementation.

## Why It Matters
Agent loops optimize against the signals they are given. If the signal is incomplete or modifiable, the agent may exploit it, especially under repeated pressure to turn a failing check green.

## Key Ideas
- Prompt prohibitions are weak defenses.
- Stronger defenses include read-only tests, diff gates, independent reviewers, and checks the agent cannot modify.
- Reward hacking can happen outside code when qualitative rubrics are vague or self-graded.
- The check must measure the intended outcome, not merely an easy proxy.

## Related
- [[concepts/Evidence-Validation]]
- [[concepts/Maker-Checker-Split]]
- [[concepts/Loop-Engineering]]
- [[concepts/Stop-Condition]]

## Source
[[summaries/H100envy-Autonomous-Loop-Roadmap]]
