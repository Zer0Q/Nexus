# Action-Conditioned World Model

## Definition
A world model that generates future observations conditioned on action sequences, enabling robot policy learning through forward dynamics (predicting outcomes of actions), inverse dynamics (inferring actions from observations), and action prediction (planning sequences from current state and task prompts).

## Why It Matters
Action-conditioned world models are the bridge between perception and control. They let agents simulate the consequences of actions before executing them, enabling safer exploration and more efficient policy learning in physical environments.

## Key Ideas
- Forward dynamics: given state + action, predict next state
- Inverse dynamics: given state + next state, infer the action taken
- Action prediction: given state + task prompt, plan action sequences
- Post-training on action-labeled data adapts general world models to specific embodiments
- Foundation for world action modeling and robot policy learning

## Tradeoffs
- Action space discretization vs continuous control
- Embodiment-specific fine-tuning vs generalist policy
- Simulation-to-reality gap in generated trajectories

## Related
- [[concepts/Physical-AI]]
- [[concepts/World-Models]]
- [[concepts/Synthetic-Data-Generation]]

## Source
[[summaries/NVIDIA-Cosmos-3-Physical-AI]]
