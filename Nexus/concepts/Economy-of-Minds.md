# Economy of Minds

## Definition
Decentralized multi-agent system where market mechanisms (auctions, wealth accumulation, bankruptcy) drive prompt optimization and emergent coordination among a population of prompted LLM agents.

## Why It Matters
Replaces hand-designed orchestration (explicit state machines, role graphs) with self-organizing agent populations that discover optimal coordination through economic incentives rather than engineered protocols.

## Key Ideas
- Each agent has a prompt (role/procedure), wake-up condition, frozen bid, and wealth variable
- Two coupled loops: Planning (auctions within episodes) and Adaptation (evolution across episodes)
- Bucket-brigade credit assignment: winners pay their bid to the previous winner, enabling decentralized credit assignment
- Wealth selection: rich agents spawn mutated descendants (exploitation), weak agents spawn amended variants (exploration)
- At inference time, the trained population acts as a frozen society — market mechanics disappear, only bid-based selection remains
- Emergent behaviors: role specialization, self-auditing checklists, resource-aware workflow shapes, discovery of reusable design heuristics

## Tradeoffs
- Non-monotonic learning curves: early exploration can temporarily hurt performance before recovery
- Requires verifiable environments for training; unclear how it scales to subjective/open-ended tasks
- Population management adds complexity vs. single-agent approaches

## Related
- [[concepts/Bucket-Brigade-Credit-Assignment]]
- [[concepts/Prompt-Evolution]]
- [[concepts/Decentralized-Credit-Assignment]]
- [[concepts/Emergent-Multi-Agent-Coordination]]

## Source
[[summaries/neuralavb-Economy-of-Minds-Multi-Agent-Prompt-Optimization]]
