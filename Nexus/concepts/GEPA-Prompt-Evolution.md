# GEPA Prompt Evolution

## Definition
Genetic-Pareto Prompt Evolution: an offline optimization pipeline that reads execution traces to understand why agent skills failed, then proposes targeted improvements through evolutionary search. Published as an ICLR 2026 Oral paper, MIT licensed.

## Why It Matters
The in-agent learning loop has a known weakness: agents tend toward self-congratulation and may save suboptimal skills. GEPA provides an objective evaluation mechanism that doesn't rely on the agent's own judgment of its performance.

## Key Ideas
- Not built into the Hermes runtime — lives in a companion repository
- Pipeline: read skill → generate eval dataset → run GEPA optimizer → evaluate with LLM-as-judge scoring → apply constraint gates → submit PR
- Evaluation data: synthetic test cases (via Claude Opus), real session history (SQLite), or hand-curated golden sets
- Constraint gates: test suite must pass 100%, skills stay under 15KB, caching preserved, no semantic drift
- Best variant goes out as a PR — never a direct commit
- No GPU required, runs through API calls, ~$2-10 per optimization run
- Alternative to RL/GRPO fine-tuning when you hit a wall but don't want the cost

## Tradeoffs
- Adds complexity: requires separate repo and eval dataset
- API costs per run ($2-10)
- Overkill for simple skills — best for high-value, frequently-used ones

## Related
- [[Self-Evolving-Skills]] -- creates the skills GEPA optimizes
- [[Agent-Skill-Curator]] -- maintains skill library quality
- [[LLM-Harness]] -- evaluation harnesses for structured LLM testing

## Source
[[AkshayPachaar-Hermes-Agent-Masterclass]]
