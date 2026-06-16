# SKILL-MD

## Definition
Archivo markdown obligatorio de una Skill en Claude Code. Contiene dos partes: una descripción (qué hace la skill) y el contexto (instrucciones detalladas que el modelo lee como contexto al activar la skill).

## Why It Matters
Es el formato estándar para codificar conocimiento procedural en Claude Code. Una SKILL.md bien escrita permite que Claude trabaje exactamente como quieres, sin repetir instrucciones.

## Key Ideas
- SKILL.md tiene 2 partes: descripción y contexto
- La descripción es lo que Claude usa para matching runtime
- El contexto son las instrucciones detalladas que se cargan como prompt
- Funciona como una "method call": misma skill, diferentes parámetros = diferentes resultados
- Se puede versionar, compartir y reutilizar

## Tradeoffs
- Escribir buena SKILL.md requiere iteración y testing
- Demasiado contexto en la SKILL puede inflar el prompt
- La skill solo es efectiva si el modelo la activa correctamente

## Related
- [[concepts/Skill-Files]]
- [[concepts/Agent-Architecture]]
- [[concepts/Hook-Mechanism]]
- [[tools/Claude-Code]]

## Source
[[summaries/Santtiagom-SKILL-MD-Guide]]
[[summaries/Skill-Files]]
