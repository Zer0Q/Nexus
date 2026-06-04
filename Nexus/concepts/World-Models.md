# World Models

## Definition
Generative models that learn the dynamics of an environment -- given current observations and actions, they predict future states. In physical AI, world models generate physics-aware video and scenarios for rare edge cases, prediction, and policy learning.

## Why It Matters
World models enable agents to simulate outcomes before acting, reducing the need for expensive real-world trial-and-error. They're the foundation for safe exploration in robotics, autonomous driving, and industrial automation.

## Key Ideas
- Action-conditioned: generate future observations given current state + planned actions
- Can generate synthetic data for rare edge cases (e.g., warehouse safety incidents, traffic anomalies)
- Used for both prediction (what will happen?) and policy learning (what should I do?)
- Cosmos 3 uses a diffusion-based generator tower conditioned on a reasoner tower's physical understanding
- Evaluation shifting from subjective grading to atomic binary fact verification (HUE benchmark)

## Tradeoffs
- Visual realism vs physical accuracy -- a model can look right but violate physics
- Generation speed vs fidelity -- real-time robotics needs fast inference
- Domain generalization vs specialization -- one world model vs domain-specific ones

## Related
- [[concepts/Physical-AI]]
- [[concepts/Action-Conditioned-World-Model]]
- [[concepts/Synthetic-Data-Generation]]

## Source
[[summaries/NVIDIA-Cosmos-3-Physical-AI]]
