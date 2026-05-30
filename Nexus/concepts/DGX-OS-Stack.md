# DGX OS Stack

## Definition
NVIDIA's pre-built Ubuntu-based operating system that ships with the DGX Spark, including the full NVIDIA AI stack: CUDA, NIM, NeMo, and the same libraries that run on data-center DGX systems. Provides day-one compatibility with the open AI ecosystem.

## Why It Matters
Eliminates the setup friction of building a local AI environment. The DGX OS comes with everything pre-installed, so Ollama, vLLM, PyTorch, Hugging Face, and llama.cpp work immediately without manual driver or library installation.

## Key Ideas
- Ubuntu-based OS preloaded on the DGX Spark
- Full NVIDIA AI stack: CUDA, NIM, NeMo
- Same libraries as data-center DGX systems — not a stripped-down version
- Open ecosystem works day one: Ollama, vLLM, PyTorch, Hugging Face, llama.cpp
- Migration from cloud to local is one line of code: change base_url from remote endpoint to localhost:11434
- Same code path, same JSON, same behavior — nothing bills, nothing leaves the building

## Tradeoffs
- Vendor-locked to NVIDIA's software stack
- Less flexibility than a clean Linux install
- Updates controlled by NVIDIA's release cycle

## Related
- [[DGX-Spark]] -- the hardware that ships with DGX OS
- [[Ollama-Local-Serving]] -- runs on top of the DGX OS stack
- [[Local-LLM]] -- the broader concept of local model serving

## Source
[[w1nklerr-DGX-Spark-Cost-Recovery]]
