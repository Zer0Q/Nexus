# Routing Workflow

## Definition
Classifies input and directs it to specialized downstream tasks. Enables separation of concerns and optimized prompts per input category.

## Why It Matters
One prompt optimized for one input type performs poorly on others. Routing allows specialized handling, cost optimization (easy->cheap model), and better overall accuracy.

## Key Ideas
- Classifier LLM or traditional model routes input to specialized handlers
- Separation of concerns: different prompts/tools per category
- Cost optimization: route easy/common questions to cheap models, hard to capable ones
- Classification can be LLM-based or traditional ML
- Examples: customer service (general/refund/technical), model routing (Haiku/Sonnet)

## Tradeoffs
- Classification errors route to wrong handler
- Requires maintaining multiple specialized prompts
- Overhead for simple tasks that one prompt could handle

## Related
- [[concepts/Agentic-System-Architecture]]
- [[concepts/Parallelization-Workflow]]

## Source
[[source-notes/Anthropic-Building-Effective-AI-Agents]]
