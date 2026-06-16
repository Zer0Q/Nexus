# Concepts Needing Augmentation

Este índice lista conceptos del vault que fueron creados como placeholders vacíos o con contenido mínimo, y necesitan ser ampliados con definición sustantiva antes de integrarse al grafo de conocimiento.

## Criterio

- Creados en commits de reorganización sin contenido real
- Sin enlaces desde ningún otro archivo del vault
- Contenido actual < 50 palabras o sin sección de definición

## Lista

### Terminología industrial / OT (fuera del scope actual)

| Concepto | Creado en | Notas |
|----------|-----------|-------|
| [[concepts/Alarm-Flood]] | 2c57157 | ISA/OT terminology, no AI-native |
| [[concepts/ISA-101]] | 2c57157 | Standard industrial, no AI-native |
| [[concepts/ISA-18-2]] | 2c57157 | Standard industrial, no AI-native |
| [[concepts/MAD]] | 2c57157 | Master Alarm Database, OT-specific |
| [[concepts/PID]] | 2c57157 | P&ID diagram, OT-specific |
| [[concepts/SCADA]] | 2c57157 | Supervisory Control, OT-specific |

### Hardware / Infraestructura (fuera del scope de conceptos)

| Concepto | Creado en | Notas |
|----------|-----------|-------|
| [[concepts/FP4]] | 8418927 | Quantization format, especificación de hardware |
| [[concepts/GB10]] | 8418927 | NVIDIA GPU spec, no concepto |
| [[concepts/LPDDR5x]] | 8418927 | Memory spec, no concepto |
| [[concepts/NeMo]] | 8418927 | Herramienta NVIDIA, mover a tools/ |

### Tools (deben moverse a tools/)

| Concepto | Creado en | Notas |
|----------|-----------|-------|
| [[tools/Cursor]] | 8418927 | Editor de código, mover a tools/ |
| [[tools/N8N]] | 8418927 | Workflow automation, mover a tools/ |
| [[tools/QuickAdd]] | 4e472fe | Plugin Obsidian, mover a tools/ |
| [[tools/Readwise]] | 4e472fe | Servicio de lectura, mover a tools/ |
| [[tools/Nous-Portal]] | 8418927 | Plataforma Nous, mover a tools/ |

### Acronyms sin contenido sustantivo

| Concepto | Creado en | Notas |
|----------|-----------|-------|
| [[concepts/SDD]] | 21c33dc | Spec-Driven Development, ver [[concepts/Spec-Driven-Development]] |
| [[concepts/PRD]] | 21c33dc | Product Requirements Doc, sigla sin definición |
| [[concepts/TOC]] | 0ff6795 | Theory of Constraints, ver [[tools/Theory-of-Constraints]] |
| [[concepts/FTS5]] | 8418927 | Full-Text Search 5, especificación SQLite |
| [[concepts/VELLUM-MD]] | 4e472fe | Formato Vellum, sigla sin definición |

### Conceptos válidos pero sin enlaces (en pausa)

| Concepto | Creado en | Notas |
|----------|-----------|-------|
| [[concepts/Asset-Management]] | a51f471 | Potencialmente útil, necesita investigación |
| [[concepts/Claude-Projects]] | 8418927 | Necesita enlaces desde summaries |
| [[concepts/Context-Tree]] | 4e472fe | Necesita enlaces desde summaries |
| [[concepts/ConnectX-7]] | 8418927 | Necesita investigación |
| [[concepts/Handoff-File]] | 508fb08 | Necesita enlaces desde summaries |
| [[concepts/Memex]] | 4e472fe | Concepto histórico de PKB, potencialmente relevante |

---

## Procedimiento de limpieza

1. **Eliminar** los de "Terminología industrial" y "Acronyms sin contenido" cuando se confirme que no son relevantes
2. **Mover** los de "Tools" a `tools/`
3. **Eliminar** los de "Hardware/Infraestructura" que no son conceptos
4. **Investigar** los de "Conceptos válidos pero sin enlaces" antes de decidir
