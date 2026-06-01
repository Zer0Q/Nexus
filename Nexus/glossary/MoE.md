# MoE (Mixture of Experts)

Model architecture where different "expert" subnetworks handle different inputs, activating only a subset of parameters per token.

- Requires expert parallelism and all-to-all interconnect traffic
- Stresses engine routing more than dense models
- Supported by ExLlamaV3, SGLang, vLLM, TensorRT-LLM

See also: [[frameworks/Inference-Engine-Families]], [[concepts/Interconnect-Bottleneck]]
