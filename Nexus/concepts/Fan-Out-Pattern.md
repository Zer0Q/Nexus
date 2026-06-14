# Fan-Out Pattern

## Definition
Patrón de paralelización donde un single prompt spawn workers paralelos que procesan items independientes, y un coordinator mergea los outputs en un deliverable unificado.

## Why It Matters
Permite speed multiplier (15x) y cost multiplier (10x) vs enfoque secuencial. "A solo operator with this stack is not competing with other solo operators. They are competing with agencies."

## Key Ideas
- Un prompt entra, N workers process items en paralelo, un deliverable sale
- El prompt se mantiene same length mientras work fans out behind it
- Kimi K2.6 nativamente soporta hasta 300 sub-agents desde un prompt
- Cost math: 100 PDFs en $40-60/hora (sequential) vs $3-5/12min (parallel)
- Coordinator mergea outputs con citations
- Tasks deben ser independentes para paralelización efectiva

## Tradeoffs
- Tasks deben ser independientes — shared context complica paralelización
- Coordinator puede ser bottleneck si merge es complejo
- Error recovery más difícil con workers paralelos
- Cost vs speed tradeoff: parallel es más caro por token pero más rápido en wall time

## Related
- [[concepts/Kimi-K26]]
- [[concepts/Parallelization]]
- [[concepts/Coordinator-Pattern]]

## Source
[[summaries/Khairallah-300-AI-Agents-Parallel]]
