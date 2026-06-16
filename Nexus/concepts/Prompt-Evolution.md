---
type: Concept
title: Prompt Evolution
description: Evolutionary mechanism where agent prompts are treated as genotypes —
  wealthy agents spawn mutated descendants (exploitation) and weak agents spawn amended
  v...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Prompt Evolution

## Definition
Evolutionary mechanism where agent prompts are treated as genotypes — wealthy agents spawn mutated descendants (exploitation) and weak agents spawn amended variants (exploration) — with the population evolving under wealth selection pressure.

## Why It Matters
The unit of learning is not a single agent prompt but an evolving family tree of prompts. Useful lineages persist, spawn offspring, and dominate, while failed variants go bankrupt and get removed.

## Key Ideas
- Exploitation: pick wealthy "parent" agents and mutate prompts slightly to preserve useful behaviors with variation
- Exploration: replace bankrupt/weak agents with new variants that amend prompts to correct failure modes
- Prompts evolve into compact multi-step reasoning routines (self-auditing checklists, procedural modules)
- Lineage tracking reveals which behavioral strategies are valuable across episodes
- Population size is constrained; periodic rent ensures mediocre agents slowly die out

## Tradeoffs
- Mutation rate and population size are hyperparameters that affect convergence speed
- Early chaos phase can degrade performance before good lineages emerge
- Requires careful balance between exploitation (amplifying success) and exploration (testing alternatives)

## Related
- [[concepts/Economy-of-Minds]]
- [[concepts/Emergent-Multi-Agent-Coordination]]
- Agent-Population-Evolution

## Source
[[summaries/neuralavb-Economy-of-Minds-Multi-Agent-Prompt-Optimization]]
