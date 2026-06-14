# Multi-Step Reasoning

## Definition
Feature de agentes AI donde el model reasoning antes de responder: gathering evidence progressively, evaluando fuentes, y deciding qué información falta en vez de responder inmediatamente con la primera retrieval.

## Why It Matters
Separa demos de systems útiles. En vez de "retrieve → answer", el agent hace "question → reason → search → evaluate → search again → synthesize → answer". Retrieval se convierte en loop, no single action.

## Key Ideas
- Agent no responde inmediatamente — reasoning primero
- Workflow: Question → Reason → Search → Evaluate → Search Again → Synthesize → Answer
- Retrieval como loop: decide qué info falta, qué source checkear, si evidence es reliable
- "Model no longer acting like search engine. It's acting like analyst."
- Separates demos from useful systems
- MCP servers facilitan multi-source retrieval sin custom integration

## Tradeoffs
- Más reasoning = más latency en respuestas
- Reasoning puede ser overkill para preguntas simples
- Risk de reasoning loops sin convergencia
- Cost de múltiples reasoning steps vs single-shot

## Related
- [[concepts/Agentic-RAG]]
- [[concepts/MCP]]
- [[concepts/Evidence-Validation]]

## Source
[[summaries/NainsiDwiv50980-agentic-rag-mcp]]
