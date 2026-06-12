# Local Inference Server

## Definition
Self-hosted GPU infrastructure serving open-weight models via OpenAI-compatible API, eliminating token limits, vendor lock-in, and data retention concerns. Typically uses a four-layer architecture: models, model serving (vLLM), API gateway (LiteLLM), and reverse proxy with monitoring.

## Why It Matters
Private model providers impose ever-lower and ever-more-expensive token limits. A community-run inference server gives builders unlimited token access, zero data retention, and full operational sovereignty. It turns frontier AI from a rented API into a manufacturable toolchain.

## Key Ideas
- Four-layer architecture: Models (GPU for LLM, CPU/RAM for others) → Model Serving (vLLM) → API Gateway (LiteLLM) → Reverse Proxy
- NaN community: members burn 300M+ tokens daily without hitting limits
- Hardware: Blackwell GPUs with nvidia-driver-570-open and cuda-toolkit; only LLM loads in vRAM
- Rate limiting without token caps: 100 RPM, 5 parallel requests max per API key
- Security: Cloudflare (SSL + tunnels), VPN for admin panels, only inference endpoint exposed to internet
- Models rotated every 3 months via community voting

## Tradeoffs
- Capital expenditure for GPUs vs recurring API costs — payback depends on token volume
- Requires operational expertise: driver management, vLLM tuning, monitoring, security hardening
- Horizontal scaling needed for peak concurrent load
- Debugging errors across the four layers requires systems knowledge

## Related
- [[concepts/Local-LLM]]
- [[concepts/Local-AI-Privacy]]
- [[concepts/LiteLLM-API-Gateway]]
- [[concepts/Model-Serving]]
- [[concepts/Speculative-Decoding]]

## Source
[[summaries/Barckcode-Como-Montar-un-Server-de-Inferencia]]
