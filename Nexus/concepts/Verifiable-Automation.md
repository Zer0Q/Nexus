# Verifiable Automation

## Definition
Principle that AI automates what you can verify, not what you can specify. Tasks with automatic success signals (tests pass/fail, schemas validate, metrics reconcile) are factory-ready; subjective tasks are not.

## Why It Matters
Karpathy's framing explains why engineering was the first domain for AI automation and predicts which functions come next. Verifiability is the dominant criterion for factory-readiness, not complexity or importance.

## Key Ideas
- Traditional software automates what you can specify (deterministic rules)
- AI automates what you can verify (outcome checkable, path flexible)
- Four factory-readiness criteria: verifiable output, digital I/O, volume/repeatability, reversibility
- Most factory-ready: engineering, QA, data pipelines, DevOps (all have ground truth)
- Increasingly ready: finance (reconciliation), customer support (CSAT), ops (conversion metrics)
- Least ready: strategy, design taste, novel architecture, executive judgment, relationship building

## Tradeoffs
- Verifiability doesn't equal importance -- critical decisions may be unverifiable
- False positives in verification can cascade (wrong test = wrong automation)

## Related
- [[concepts/Software-Factory-Ladder]]
- [[tools/Industrialized-Software-Development]]

## Source
[[summaries/BusinessBarista-Software-Factory]]
