---
type: Concept
title: Synthetic Data Generation
description: Generating training data via simulation rather than real-world collection.
  For physical AI, this includes synthetic scenes for robotics, physics interactions...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Synthetic Data Generation

## Definition
Generating training data via simulation rather than real-world collection. For physical AI, this includes synthetic scenes for robotics, physics interactions, spatial reasoning, human motion, autonomous driving, and warehouse operations -- all with ground-truth annotations.

## Why It Matters
Real-world data for edge cases is expensive, dangerous, or impossible to collect at scale. Synthetic data provides diverse, annotated scenarios for training and evaluating physical AI systems without real-world risk.

## Key Ideas
- NVIDIA open-sourced 6 synthetic datasets: RobotSim, PhysxSim, Spatial Reasoning, SynHuman, DriveSim, WareHouse
- Each dataset includes ground-truth physics annotations (velocity, center-of-mass, semantic segmentation)
- Used for post-training foundation models to specific domains and embodiments
- Quality of synthetic data determines quality of physical reasoning capabilities
- Covers scenarios too rare or dangerous to capture in reality (e.g., warehouse safety incidents)

## Tradeoffs
- Simulation fidelity vs diversity -- high-fidelity sims are expensive to render
- Domain gap -- synthetic data may not capture all real-world distributions
- Annotation quality -- automated annotations may have systematic errors

## Related
- [[concepts/Physical-AI]]
- [[concepts/World-Models]]
- [[tools/NVIDIA-Cosmos]]

## Source
[[summaries/NVIDIA-Cosmos-3-Physical-AI]]
