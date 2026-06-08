# Latent Prediction Learning

## Definition
Self-supervised learning paradigm where models predict their own internal representations (latents) rather than surface tokens, as in JEPA and data2vec. Provides exponential data efficiency advantages over token-based prediction for compositional structures.

## Why It Matters
Predicting latents requires samples constant in tree depth L, while token-based learning needs samples exponential in L. Latent targets expose compositional, hierarchical structure directly, so the learner does not have to reconstruct it from surface tokens. Provides theoretical foundation for why world-model training could beat brute-force next-token prediction.

## Key Ideas
- Exponential gap in data efficiency: latent prediction is constant in depth, token prediction is exponential
- Mechanism: latent targets expose hierarchical structure directly, bypassing surface-level reconstruction
- Hierarchy may be implicit: explicit stacking (H-JEPA) can be redundant since data2vec learns hierarchy implicitly
- Principled argument for self-supervised objectives that predict abstractions as scaling laws press against data limits

## Tradeoffs
- Requires designing the latent space architecture (JEPA, data2vec) rather than standard token prediction
- May not match token prediction on tasks where surface-level patterns are the primary signal
- Theoretical results derived from probabilistic context-free grammars; real-world gap may differ

## Related
- [[concepts/World-Models]]
- [[concepts/Scaling-Laws]]
- [[concepts/Attention-Mechanism]]

## Source
[[summaries/DAIR-Top-AI-Papers-of-the-Week-June-7]]
