# Knowledge Fragmentation

## Definition
Problema de knowledge interno disperso en sistemas altamente incompatibles: metadata catalogs con sus propias APIs, wikis, code comments, notebook cells, y heads of senior engineers — cada uno con su formato, schema y access pattern.

## Why It Matters
Cuando un agent necesita responder "How do I compute weekly active users?" tiene que ensamblar la respuesta desde superficies mutuamente incompatibles. Cada vendor ofrece su propio catálogo, SDK y schema. Resultado: knowledge locked detrás de la superficie que lo creó.

## Key Ideas
- Metadata catalogs con sus propias APIs
- Wikis, third-party systems, shared drives
- Code comments, docstrings, notebook cells
- Heads of senior engineers (tacit knowledge)
- Cada vendor: su propio catálogo, SDK, schema de knowledge-graph
- Ningún knowledge es portable entre productos u organizaciones
- Cada agent builder resuelve mismo context-assembly problem desde scratch
- OKF busca resolver esto con estandarización

## Tradeoffs
- Fragmentación = especialización para cada caso de uso
- Centralización = rigidez y single point of failure
- Equilibrio entre autonomía de teams y estandarización global
- Costo de migración vs costo de mantener fragmentación

## Related
- [[concepts/Open-Knowledge-Format]]
- [[concepts/Knowledge-Interoperability]]
- [[concepts/Context-Assembly]]
- [[concepts/Metadata-as-Code]]

## Source
[[summaries/google-open-knowledge-format-okf]]
