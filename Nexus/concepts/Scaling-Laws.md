# Scaling Laws

## Definition
Relaciones power-law que cuantifican cómo el loss cambia con model size, data size y compute — prediciendo el rendimiento de modelos antes de entrenarlos.

## Why It Matters
Permite planificar training runs: cuánto compute se necesita para alcanzar un target de loss. Chinchilla argumentó que muchos large models estaban undertrained — compute-optimal training debe escalar parameters y tokens together más cuidadosamente.

## Key Ideas
- Kaplan-style scaling laws: smooth power-law relationships across several orders of magnitude
- Chinchilla: muchos models estaban undertrained — scale parameters y tokens together
- Train tiny, small y medium models y fit scaling curves es el proyecto para entenderlo
- Scaling laws aplican a pretraining — post-training (SFT, DPO, RLHF) tiene dynamics diferentes

## Related
- [[concepts/Transformer-Architecture]]
- [[Fine-tuning-with-TRL]] -- needs research: framework de fine-tuning de HuggingFace

## Source
[[summaries/TheAhmadOsman-Step-By-Step-LLM-Engineering-Projects]]
