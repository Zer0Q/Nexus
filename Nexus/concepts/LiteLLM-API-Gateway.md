# LiteLLM API Gateway

## Definition
Unified API layer that serves multiple models under a single OpenAI-compatible endpoint, providing authentication, rate limiting, usage metrics, and hardening against DDoS and resource monopolization.

## Why It Matters
Without a gateway, each model server exposes its own API with inconsistent auth, no centralized rate limiting, and no unified metrics. LiteLLM consolidates model serving behind one endpoint while adding per-key authentication, usage tracking, and abuse prevention.

## Key Ideas
- Serves multiple models (LLM, embedding, vision) through a single API endpoint
- Per-API-key authentication and authorization for community or team access
- Rate limiting without token caps: e.g., 100 RPM, 5 parallel requests max per key
- Built-in metrics: tokens processed, requests per model, per-user usage
- Input/output tracking can be disabled for privacy — pure inference with no data retention
- Prevents single users from monopolizing GPU resources through per-key limits

## Tradeoffs
- Adds a dependency layer between users and model servers
- LiteLLM itself can become a bottleneck under very high concurrency
- Privacy mode (no logging) means less visibility for debugging issues

## Related
- [[concepts/Local-Inference-Server]]
- [[concepts/Model-Serving]]
- [[concepts/Local-AI-Privacy]]

## Source
[[summaries/Barckcode-Como-Montar-un-Server-de-Inferencia]]
