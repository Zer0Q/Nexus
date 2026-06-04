# Agent Reflection and Self-Correction

## Definition
Mechanism where agents review their own output, detect errors or validation failures, and retry with corrections. Enables iterative improvement without human intervention.

## Why It Matters
LLM output is imperfect. Reflection allows agents to catch and fix their own mistakes, improving output quality through self-evaluation and retry loops.

## Key Ideas
- Agent generates output, then evaluates it against criteria
- If validation fails, agent retries with feedback
- Common in structured output: schema validation triggers retry
- Can be explicit (dedicated reflection step) or implicit (framework retry on validation error)
- Risk of infinite loops if agent can't converge

## Tradeoffs
- Each retry adds latency and cost
- May not fix fundamental misunderstandings
- Requires clear validation criteria

## Related
- [[concepts/Agent-Structured-Output]]
- [[concepts/Evaluator-Optimizer-Workflow]]

## Source
[[summaries/Pydantic-Team-Pydantic-AI-Overview]]
