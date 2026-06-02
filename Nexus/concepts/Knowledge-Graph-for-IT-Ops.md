# Knowledge Graph for IT Ops

## Definition
A knowledge graph encompassing IT entities (microservices, databases, middleware, MELT) coupled with embedded tribal knowledge from domain experts. Used for observability-driven incident investigation, bounding the LLM to local reasoning for non-deterministic outcomes across the IT stack.

## Why It Matters
IT incident investigation spans the full stack -- infrastructure, middleware, applications, code. A KG provides structural context that reduces the search space for root cause analysis, enabling the LLM to reason locally rather than exploring the entire IT landscape blindly.

## Key Ideas
- Entities: microservices, databases, middleware, monitoring endpoints, logs, traces
- Embedded tribal knowledge: domain expert insights encoded as graph relationships
- Local reasoning: LLM bounded to relevant subgraph rather than full IT landscape
- IBM I3 agent: 4x improvement over ReAct with GPT-5.1 on ITBench
- Extended to source code via program dependency graphs for code analysis and bug remediation
- 3.0x better at finding culpable microservice, 1.6x better at bug repair, 3.7-5.9x fewer tokens

## Tradeoffs
- Graph completeness vs maintenance overhead
- Tribal knowledge encoding -- how to capture and update expert knowledge
- Local vs global reasoning -- when to expand beyond the local subgraph

## Related
- [[concepts/Agent-Logic]]
- [[concepts/Knowledge-Graph-as-Semantic-Layer]]
- [[concepts/Program-Analysis-for-Agents]]

## Source
[[source-notes/NicholasFuller-Agent-Logic-Enterprise-AI]]
