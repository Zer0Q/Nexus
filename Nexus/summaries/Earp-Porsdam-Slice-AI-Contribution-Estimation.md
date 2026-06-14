---
title: "(PDF) Mapping Human and AI Contributions Across Stages of Academic Writing Using SLICE"
source: "https://www.researchgate.net/publication/406991607_Mapping_Human_and_AI_Contributions_Across_Stages_of_Academic_Writing_Using_SLICE-A_Preliminary_LLM-Based_Method"
author: "Brian D. Earp, Sebastian Porsdam Mann"
published: "2026-06-12"
type: article
---

# SLICE: AI Contribution Estimation Method

## Summary

Earp y Porsdam Mann proponen SLICE (Stage-Level LLM-Inferred Contribution Estimation), un método ligero para estimar la contribución relativa de humanos vs. IA en escritura académica. El método descompone el proceso de escritura en 8 etapas y usa assessors LLM independientes para producir una atribución porcentual de contribución en cada etapa, generando una figura heurística auditable que complementa las prácticas actuales de disclosure.

## Core Concepts

- [[concepts/SLICE]] -- Stage-Level LLM-Inferred Contribution Estimation: método heurístico para cuantificar contribución humana vs. IA por etapa del proceso de escritura académica
- [[concepts/AI-Authorship]] -- criterios de autoría en era de IA generativa: qué constituye contribución intelectual suficiente para ser considerado autor
- [[concepts/Production-Transcript]] -- registro estructurado del proceso de escritura (drafts, edit logs, prompts) usado como input para análisis de contribución
- [[concepts/LLM-Assessor]] -- modelo LLM procedimentalmente independiente que aplica rúbrica estandarizada para evaluar contribución de texto
- [[concepts/Contribution-Attribution]] -- estimación porcentual de la contribución relativa de cada parte (humana/IA) en un documento

## Key Insights

- SLICE descompone la escritura en 8 etapas: brainstorming, outlining, drafting, directive revision, implementation revision, checking, vetting/vouching, guaranteeing
- El método requiere un "production transcript" (transcript de producción) que documenta todas las interacciones con IA
- Los assessors LLM son procedimentalmente independientes — no tienen acceso al transcript del otro assessor
- La figura de contribución es heurística (aproximación visual), no una medición exacta
- El método es voluntario e informal, depende de la honestidad de los contributors en loggear todas las interacciones con IA
- Los autores pueden aceptar la figura o registrar desacuerdo con justificaciones específicas
- Complementa las checklist-based reporting guidelines actuales que solo indican en qué etapas se usó IA, no cuánto contribuyó

## Open Questions

- ¿Cómo se escala SLICE a documentos con cientos de interacciones con IA?
- ¿Qué pasa cuando múltiples LLMs son usados en diferentes etapas? ¿Se necesita un assessor por LLM?
- ¿Cómo se maneja la subjetividad inherente a las estimaciones LLM de contribución?

## Source
- **Raw note:** [[raw-notes/pdf-mapping-human-and-ai-contributions-across-stages-of-academic]]
- **Original URL:** https://www.researchgate.net/publication/406991607_Mapping_Human_and_AI_Contributions_Across_Stages_of_Academic_Writing_Using_SLICE-A_Preliminary_LLM-Based_Method
