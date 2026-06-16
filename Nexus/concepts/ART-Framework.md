---
type: Concept
title: ART Framework
description: OpenPipe's open-source training framework (9k+ stars on GitHub) implementing
  GRPO + RULER for agent fine-tuning, with Trajectory and TrajectoryGroup objects
  ...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# ART Framework

## Definition
OpenPipe's open-source training framework (9k+ stars on GitHub) implementing GRPO + RULER for agent fine-tuning, with Trajectory and TrajectoryGroup objects that carry reward fields for training loops.

## Why It Matters
Provides a complete, production-ready implementation of the GRPO + RULER pipeline, including Colab notebooks that walk through the training loop end to end.

## Key Ideas
- Trajectory: single complete agent interaction (messages + choices + reward)
- TrajectoryGroup: multiple trajectories for the same scenario, the unit RULER scores and GRPO trains on
- gather_trajectory_groups: orchestrates generating groups, scoring with RULER, collecting results for GRPO
- Uses OpenAI SDK types (Choice, ChatCompletionMessage) for compatibility
- RULER caches judge responses to disk; deduplicates common prefixes to cut token usage
- model.train() accepts scored TrajectoryGroups and updates LoRA weights via GRPO

## Tradeoffs
- Requires a judge LLM API key (OpenAI, Anthropic, or local via LiteLLM)
- Training cost scales with number of trajectories per group and number of training steps

## Related
- [[concepts/RULER]]
- [[concepts/GRPO]]
- [[concepts/LoRA]]

## Source
[[summaries/avichawla-RL-Agents-2026-System-Prompt-Learning]]
