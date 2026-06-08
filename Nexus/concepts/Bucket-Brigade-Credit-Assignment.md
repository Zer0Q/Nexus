# Bucket Brigade Credit Assignment

## Definition
Payment rule in multi-agent systems where each auction winner pays their bid to the previous winner, creating a backward flow of value through the trajectory that solves long-horizon credit assignment without central attribution.

## Why It Matters
Solves the credit assignment problem in sparse-reward environments: if your action enables valuable future actions, later agents "buy" the continuation from you via bids, rewarding you even without direct environment rewards.

## Key Ideas
- New winner pays bid to previous winner + collects environment reward
- Creates backward credit flow: agents profit by moving the system into states where downstream agents are willing to pay
- Decentralized — no central credit tracker needed
- Combined with periodic rent (wealth degrades over time) to penalize passive agents
- Bankruptcy threshold removes agents that consistently fail to contribute

## Tradeoffs
- Requires agents to have frozen bids (not strategic bidding)
- Only works in environments where episodes have clear termination
- Credit signal quality depends on bid calibration during initialization

## Related
- [[concepts/Economy-of-Minds]]
- [[concepts/Decentralized-Credit-Assignment]]
- [[concepts/RLVR]]

## Source
[[summaries/neuralavb-Economy-of-Minds-Multi-Agent-Prompt-Optimization]]
