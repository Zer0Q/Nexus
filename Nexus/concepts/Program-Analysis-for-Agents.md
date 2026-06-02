# Program Analysis for Agents

## Definition
Using static and dynamic program analysis output to focus LLM context for code-related tasks. Pre-indexed representations of codebases (hundreds of interrelated tables with complex semantics) allow agents to retrieve precise, structured information rather than dumping entire source trees into context.

## Why It Matters
Program analysis reduces LLM context by orders of magnitude while improving accuracy. Instead of feeding millions of lines of code to an LLM, the agent queries pre-computed analysis results -- call graphs, dependency trees, data flows -- and uses those to guide targeted LLM calls.

## Key Ideas
- IBM WCA4Z: ~30x lower token consumption for legacy code understanding (up to 1M LOC, 1K programs)
- IBM Aster: +20-45% improvement in test coverage with 15x lower token consumption
- Program analysis output prompts and "focuses" the LLM on relevant code sections
- Sub-agents augment coverage and remediate runtime/compilation errors
- Works across languages: Cobol, PL/I, Java, and more

## Tradeoffs
- Analysis infrastructure overhead vs per-query savings
- Analysis freshness -- how often to re-index after code changes
- Depth of analysis -- shallow analysis is fast but less useful; deep analysis is thorough but expensive

## Related
- [[concepts/Agent-Logic]]
- [[concepts/Knowledge-Graph-for-IT-Ops]]
- [[concepts/Context-Space-Reduction]]

## Source
[[source-notes/NicholasFuller-Agent-Logic-Enterprise-AI]]
