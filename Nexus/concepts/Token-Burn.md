# Token Burn

## Definition
The economic constraint on autonomous AI agents: loops consume tokens rapidly, with costs scaling from 50K-200K tokens per single-agent loop to 500K-2M tokens per fleet loop. At standard API pricing, a week of serious loop engineering exceeds most people's monthly AI budget.

## Why It Matters
Token burn is the hidden blocker nobody talks about. Every retry costs. Every self-correction costs. Every subagent costs. Every verification pass costs. The open loop that explores freely burns tokens at a rate that makes your eyes water. Cheap models like DeepSeek V4 (1.7B tokens for $20) make agent loops economically viable.

## Key Ideas
- Single agent loop on medium coding task: 50,000–200,000 tokens
- Fleet loop with orchestrator + 3 specialists: 500,000–2,000,000 tokens
- Scheduled daily loop: millions of tokens per week
- DeepSeek V4 changes the equation: extremely low pricing, 1M context window, 384K max output, tool calls + JSON output
- The biggest problem with autonomous agents is not intelligence — it is token burn

## Tradeoffs
- Cheap models may have lower quality on complex reasoning tasks
- Token-conscious design forces tighter loops (closed over open), which limits exploration
- Long context windows (1M tokens) are essential for loops that need to maintain state across many iterations

## Related
- [[concepts/Open-vs-Closed-Loop]]
- [[concepts/Loop-Engineering]]
- [[concepts/Single-vs-Fleet-Loop]]

## Source
[[summaries/Sairahul1-Loops-What-Every-AI-Engineer-Needs-to-Know]]
