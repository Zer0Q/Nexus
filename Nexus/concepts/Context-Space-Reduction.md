# Context Space Reduction

## Definition
Using structured analysis output (program analysis, knowledge graphs, algorithms) to reduce the context space an LLM needs to process. Instead of dumping entire codebases, IT landscapes, or document corpora into context, the agent retrieves focused, pre-computed representations.

## Why It Matters
Context costs dominate production LLM bills. Reducing context space by orders of magnitude while maintaining or improving accuracy is the most direct path to cost-effective enterprise AI. Agent logic primitives are the mechanism for this reduction.

## Key Ideas
- Pre-indexed representations: query structured data instead of raw text
- Graph-guided reasoning: traverse relevant subgraph instead of full landscape
- Algorithmic decomposition: break complex tasks into focused sub-tasks with minimal context each
- IBM results: 30x lower token consumption for legacy code, 77% lower for asset maintenance
- The key insight: LLMs don't need all the data; they need the right data in the right structure

## Tradeoffs
- Preprocessing cost vs per-query savings
- Representation fidelity -- how much information is lost in compression
- Coverage -- does the reduced context still contain everything the LLM might need?

## Related
- [[concepts/Agent-Logic]]
- [[concepts/Program-Analysis-for-Agents]]
- [[concepts/Context-Efficiency-Frontier]]

## Source
[[summaries/NicholasFuller-Agent-Logic-Enterprise-AI]]
