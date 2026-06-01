# Ollama Local Serving

## Definition
Ollama as a local model serving runtime on the DGX Spark. Three-command setup: install Ollama, pull a model, serve it at localhost:11434. Provides an OpenAI-compatible API endpoint for local inference with zero cloud dependency.

## Why It Matters
Ollama is the simplest path to running large models locally. The three-command setup turns the DGX Spark into a private inference engine in minutes, with the same API format as cloud providers — existing code works with a single URL change.

## Key Ideas
- Install: `curl -fsSL https://ollama.com/install.sh | sh`
- Pull model: `ollama pull llama3.3:70b` (a model no consumer card could hold)
- Serve: `ollama serve` — private 70B live at http://localhost:11434
- OpenAI-compatible API: same JSON format, same behavior, nothing bills
- Migration from cloud: change base_url from remote to localhost:11434
- Works on DGX OS out of the box

## Tradeoffs
- Ollama is optimized for ease of use, not raw throughput
- For high-concurrency serving, vLLM or TensorRT-LLM may be better choices
- Model library limited to what Ollama supports

## Related
- [[concepts/DGX-OS-Stack]] -- Ollama runs on top of the pre-built stack
- [[concepts/Open-WebUI-Local-Chat]] -- front-end that connects to Ollama
- [[glossary/Local-LLM]] -- broader concept of local model serving
- [[tools/vLLM]] -- alternative serving engine with higher throughput

## Source
[[source-notes/w1nklerr-DGX-Spark-Cost-Recovery]]
