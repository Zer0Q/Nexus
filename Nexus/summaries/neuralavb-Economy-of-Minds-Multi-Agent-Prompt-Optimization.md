---
title: 'Economy of Minds: Multi-Agent Prompt Optimization explained'
author: '@neural_avb'
published: '2026-06-04'
type: article
resource: https://x.com/neural_avb/status/2062930609861976454
timestamp: '2026-06-04T00:00:00Z'
description: Harvard's Economy of Minds (EOM) paper replaces hand-designed orchestration
  with a market simulation where agents bid for the right to act via auctions, accu...
tags:
- summaries
---


# Economy of Minds: Market-Based Multi-Agent Optimization

## Summary
Harvard's Economy of Minds (EOM) paper replaces hand-designed orchestration with a market simulation where agents bid for the right to act via auctions, accumulate wealth through bucket-brigade payments, and evolve their prompts through economic selection. The wealthiest agents — those whose actions enable valuable downstream steps — survive and reproduce, while bankrupt agents are pruned. At inference time, the trained population acts as a frozen society with role-specialized agents coordinating through wake-up policies and bids, with no central orchestrator needed.

## Core Concepts
- [[concepts/Economy-of-Minds]] -- decentralized multi-agent system where market mechanisms (auctions, wealth, bankruptcy) drive prompt optimization and emergent coordination
- [[concepts/Bucket-Brigade-Credit-Assignment]] -- payment rule where each auction winner pays their bid to the previous winner, enabling decentralized credit assignment across trajectory steps
- [[concepts/Prompt-Evolution]] -- evolutionary mechanism where wealthy agents spawn mutated descendants (exploitation) and weak agents spawn amended variants (exploration)
- Agent-Population-Evolution -- the unit of learning is not a single agent but an evolving family tree of prompts under wealth selection pressure
- [[concepts/Decentralized-Credit-Assignment]] -- solving the long-horizon credit assignment problem through market signals rather than engineered attribution
- Agent-Wake-Up-Policy -- local "when to act" logic that determines which agents participate in auctions at each environment step
- [[concepts/Emergent-Multi-Agent-Coordination]] -- coordination that arises from simple economic incentives rather than explicit orchestration protocols

## Key Insights
- EOM does NOT train agents for financial tasks — the market simulation is purely a training mechanism for optimizing agents on verifiable environments (Math, accelerator design, CloudCast, Finance-Agent-Bench)
- The bucket-brigade rule solves credit assignment: if your action enables valuable future actions, later agents "buy" the continuation from you via bids, rewarding you even without direct environment rewards
- At inference time, the market mechanics (wallets, wealth transfer) disappear — only the trained population and bid-based selection remain
- Non-monotonic learning curves: EOM dips early as exploration tests alternative specialists, then recovers and surpasses initial performance — similar to grokking in neural nets
- Emergent behaviors include: discovering output-stationary tiling motifs without templates, agents evolving into self-auditing procedural modules, and resource-aware workflow shapes (cautious vs. aggressive) depending on workspace state
- The paper was published on arXiv: 2606.02859, presented at ICLR 2026

## Open Questions
- How does EOM scale beyond the test environments (Math, accelerator design) to open-ended agentic workflows where rewards are sparse or subjective?
- Can [[concepts/Bucket-Brigade-Credit-Assignment]] be combined with [[concepts/RLVR]] or [[concepts/GRPO]] to create a hybrid training signal?
- What happens when the population size grows beyond the tested scales — does specialization lead to diminishing returns or continued improvement?

## Source
- **Raw note:** [[raw-notes/economy-of-minds-multi-agent-prompt-optimization-explained]]
- **Original URL:** https://x.com/neural_avb/status/2062930609861976454
