# TOON Format

## Definition
Token-Oriented Object Notation: formato de serialización compacta y consciente del esquema diseñado específicamente para comunicación con LLMs. Reemplaza JSON en prompts y payloads reduciendo tokens en 30-54%.

## Why It Matters
JSON consume 15-25% de tokens en sintaxis pura (comillas, llaves, espacios). TOON elimina esa "tasa de sintaxis" liberando espacio en la ventana de contexto y reduciendo costes de inferencia.

## Key Ideas
- Elimina comillas en keys, usa delimitadores token-friendly (`|`)
- Compresión de arrays con definiciones de esquema implícitas
- Alineado con cómo los tokenizadores BPE agrupan palabras
- Ejemplo: objeto JSON de ~55 tokens → TOON de ~25 tokens (54% reducción)
- Reducción de latencia: menos tokens de salida = respuesta más rápida
- Requiere capa de conversión en backend para compatibilidad
- SDK oficial (`toon-parser`) para Python y Node.js
- Siempre A/B testear: la compresión puede cambiar cómo el LLM interpreta contexto en casos raros

## Tradeoffs
- Compatibilidad: parsers y herramientas esperan JSON
- Errores de serialización: la compresión sintáctica puede ocultar bugs
- Validación con esquemas y tests unitarios obligatoria

## Related
- [[Tokenization]]
- [[Context-Window]]

## Source
[[summaries/Orli-Dun-La-ineficiencia-oculta-de-JSON-frente-a]]
