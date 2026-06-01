# On-Device Knowledge Base

## Definition
A knowledge management system where all processing -- search, retrieval, AI reasoning, and content generation -- happens entirely on the user's local machine. No data leaves the device at any point.

## Why It Matters
For knowledge workers handling sensitive information, on-device processing is the only way to guarantee data sovereignty. Cloud tools always involve data transfer, even if the provider promises not to train on your data.

## Key Ideas
- Three components: local knowledge base (Obsidian), local model runner (LM Studio), local bridge (plugins)
- Replicates cloud AI features without data transfer
- Requires sufficient hardware (16GB+ RAM recommended)
- Supports multiple operating systems (Mac, Windows, Linux)
- Can be combined with cloud AI in [[frameworks/Hybrid-AI-Workflow]] mode

## Tradeoffs
- Local models are less capable than frontier cloud models
- Setup is more complex than opening a browser tab
- Ongoing maintenance of models and plugins

## Related
- [[concepts/Local-AI-Privacy]]
- [[tools/LM-Studio]]
- [[frameworks/Hybrid-AI-Workflow]]

## Source
[[source-notes/KanikaBK-Offline-AI-Workflow]]
