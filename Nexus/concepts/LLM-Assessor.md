# LLM Assessor

## Definition
Modelo LLM procedimentalmente independiente que aplica una rúbrica estandarizada para evaluar contribución de texto, usado en métodos como SLICE para estimar contribution humana vs. IA.

## Why It Matters
Permite evaluación objetiva (o al menos estandarizada) de contribución sin requerir expertise técnica. Los assessors son procedimentalmente independientes — no compiten por el mismo input — lo que reduce bias.

## Key Ideas
- Procedimentalmente independiente de otros assessors (no comparten contexto)
- Aplica rúbrica estandarizada a production transcript
- Produce estimación porcentual de contribution por etapa
- Qualitative text-based analysis, no quantitative metrics
- Output: rough percentage attribution + per-stage justifications
- Los authors revisan y pueden aceptar o registrar desacuerdo

## Tradeoffs
- Los LLMs pueden tener bias inherente en evaluación de contribución
- Depende de la calidad de la rúbrica aplicada
- No reemplaza juicio humano final — es heurístico
- Costo computacional de múltiples assessors independientes

## Related
- [[concepts/SLICE]]
- [[concepts/Production-Transcript]]
- [[concepts/Contribution-Attribution]]
- [[concepts/Maker-Checker-Split]]

## Source
[[summaries/Earp-Porsdam-Slice-AI-Contribution-Estimation]]
