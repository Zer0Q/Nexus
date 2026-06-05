# Temperature Parameter

Control de aleatoriedad en la generación de tokens de un LLM. Temperatura baja (0.1-0.2): predecible, seguro — ideal para código. Temperatura alta (0.8-1.0+): creativo, variado — ideal para brainstorming.

- Cada token generado tiene probabilidades para todas las opciones posibles
- Temperatura determina qué tan estrictamente se sigue la distribución de probabilidad
- Error común: usar temperatura por defecto (0.7-1.0) para todo

See also: [[concepts/LLM-Hallucination]], [[concepts/Context-Window]], [[concepts/Tokenization]]
