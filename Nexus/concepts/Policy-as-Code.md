# Policy as Code

## Definition
Runtime-enforced governance for AI agents implemented as code, independent of model prompts and without fine-tuning. Policy-as-code enforces structured workflows, safe intent handling, reliable tool usage, and controlled output formatting through least-privilege disclosure, explicit compliance rules, and human escalation paths.

## Why It Matters
In regulated environments, reasoning can be autonomous but decision rights must be constrained. Policy-as-code closes large gaps in task correctness (15-26% accuracy improvements) across all model families by enforcing authority at runtime rather than hoping the model follows instructions.

## Key Ideas
- Reasoning is autonomous; decision rights are constrained
- Authority exercised by policy and oversight mechanisms, not by the model
- Enforced at runtime independent of model prompts -- works across Claude, GPT, and open models
- Least-privilege disclosure: agent only sees what it needs, not everything
- Human escalation paths for decisions beyond agent authority
- IBM CUGA: configurable generalist agent with policy system for healthcare domain

## Tradeoffs
- Policy granularity -- fine-grained policies are precise but complex; coarse policies are simple but leaky
- Runtime enforcement overhead vs safety guarantees
- Policy versioning -- how to update policies without disrupting running agents

## Related
- [[concepts/Agent-Logic]]
- [[tools/AI-Governance]]
- [[concepts/Enterprise-Context-Layer]]

## Source
[[summaries/NicholasFuller-Agent-Logic-Enterprise-AI]]
