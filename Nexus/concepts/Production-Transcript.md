# Production Transcript

## Definition
Registro estructurado del proceso de escritura que documenta drafts, edit logs, prompts de IA y otras interacciones, usado como input para análisis de contribución (ej. SLICE).

## Why It Matters
Sin un registro completo del proceso de creación, es imposible determinar cuánto contribuyó cada agente (humano o IA) a un documento final. El transcript es la base de datos de evidencias para attribution.

## Key Ideas
- Compilado por los autores durante el proceso de escritura
- Incluye: production transcript, draft final, edit logs anonimizados
- Donde manual editing fue substantial: extract tracked-changes records
- Input para assessors LLM independientes que aplican rúbrica estandarizada
- Debe documentar TODAS las interacciones sustanciales con IA
- Base auditable para claims de autoría humana

## Tradeoffs
- Requiere disciplina de logging que no todos los autores mantienen
- Edit logs pueden contener información sensible
- Anonymización necesaria para contribución compartida
- Depende de honestidad en logging completo

## Related
- [[concepts/SLICE]]
- [[concepts/AI-Authorship]]
- [[concepts/Contribution-Attribution]]
- [[concepts/LLM-Assessor]]

## Source
[[summaries/Earp-Porsdam-Slice-AI-Contribution-Estimation]]
