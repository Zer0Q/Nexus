# Open WebUI Local Chat

## Definition
Open WebUI is a Docker-based, ChatGPT-style web interface that connects to local model serving backends like Ollama. Provides a familiar chat experience over frontier-class models running entirely on your hardware — no API key, no subscription plan, no data leaving the room.

## Why It Matters
Bridges the gap between raw local inference and a usable chat interface. Instead of interacting with models through terminal commands or raw API calls, you get a polished UI that feels like ChatGPT but runs 100% locally.

## Key Ideas
- Docker one-liner: `docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data ghcr.io/open-webui/open-webui:main`
- Connects to Ollama at localhost:11434
- ChatGPT-style interface in the browser at localhost:3000
- No API key required, no subscription, no data leaves the machine
- Works with any model Ollama is serving — including 70B+ models
- Free and open source

## Tradeoffs
- Requires Docker installation
- Adds another service to maintain
- UI features may lag behind ChatGPT's continuous updates

## Related
- [[Ollama-Local-Serving]] -- the backend Open WebUI connects to
- [[Local-AI-Privacy]] -- no data leaves your network
- [[Local-LLM]] -- broader concept of local inference
- [[LM-Studio]] -- alternative local chat interface

## Source
[[w1nklerr-DGX-Spark-Cost-Recovery]]
