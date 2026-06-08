---
title: "A Visual Guide to LLMs (Part 2): Inside the Transformer Architecture"
source: "https://x.com/_rohit_tiwari_/status/2063982924714901858"
author: "@_rohit_tiwari_"
published: "2026-06-08"
type: article
---

# Visual Guide to LLMs Part 2: Transformer Architecture

## Summary
Segunda parte de una guía visual paso a paso sobre arquitectura de LLMs. Mientras la Parte 1 cubría el input pipeline (tokenización, embeddings, positional embeddings), esta parte detalla el flujo interno del Transformer Block: cómo los vectores de entrada pasan por Masked Multi-Head Attention, Feedforward Networks, Residual Connections y Layer Normalization antes de ser proyectados al vocabulario para generar el siguiente token. Usa el ejemplo recurrente "Every moment is a beginning" con vectores numéricos de 3 dimensiones para hacer tangible cada operación matricial.

## Core Concepts
- [[concepts/Attention-Mechanism]] -- mecanismo donde cada token calcula Queries, Keys y Values para medir qué tanto debe "atender" a otros tokens en la secuencia, usando softmax(QK^T/sqrt(d_k)).V
- [[concepts/Causal-Self-Attention]] -- variante de self-attention donde cada token solo ve tokens anteriores mediante máscara triangular inferior, esencial para generación autoregresiva
- [[concepts/Masked-Multi-Head-Attention]] -- múltiples heads de causal attention en paralelo, cada uno capturando patrones diferentes (significado, gramática, estructura)
- [[concepts/Residual-Connections]] -- skip connections que suman input original al output (Output = x + Sublayer(x)), resolviendo vanishing/exploding gradients
- [[concepts/Layer-Normalization]] -- normaliza features por token (media y varianza), estabilizando activaciones; GPT usa pre-norm design
- [[concepts/Transformer-Architecture]] -- bloque que apila LayerNorm, Masked Multi-Head Attention, FFN y Residual Connections; los GPT apilan múltiples bloques idénticos
- [[concepts/Tokenization]] -- proceso de dividir texto en unidades discretas (tokens) que el modelo puede procesar, usando métodos subword como BPE
- [[concepts/Embeddings]] -- representaciones vectoriales densas de tokens que capturan similitud semántica y relaciones contextuales
- [[concepts/Positional-Embeddings]] -- vectores añadidos a los token embeddings para codificar la posición absoluta o relativa de cada token en la secuencia

## Key Insights
- Causal masking usa una matriz triangular inferior para evitar que tokens vean el futuro: se reemplazan scores bloqueados con -inf antes del softmax, resultando en probabilidad 0
- Multi-Head Attention divide los embeddings en heads paralelos donde cada head captura patrones diferentes: Head 1 conecta significado ("moment" ↔ "beginning"), Head 2 gramática ("Every" → "moment"), Head 3 estructura ("is" → "beginning")
- El FFN expande la dimensión hidden típicamente 4x con una capa lineal + GELU + segunda capa lineal, dando espacio para aprender patrones complejos no-lineales antes de comprimir de vuelta
- Residual connections resuelvan vanishing/exploding gradients: Output = x + Sublayer(x), preservando información original mientras se aprende un update residual
- Layer Normalization normaliza features por token (no por batch): calcula media y varianza, luego estandariza con epsilon para evitar división por cero; se aplica múltiples veces por bloque
- GPT usa pre-norm design: LayerNorm se aplica ANTES de attention y FFN, no después, mejorando estabilidad del training
- El output layer proyecta el último vector a logits (tamaño = vocabulario), aplica softmax para distribución de probabilidad, selecciona el token con mayor probabilidad y lo re-inyecta como input para el siguiente paso

## Open Questions
- ¿Cómo se comparan los diferentes esquemas de positional embeddings (RoPE, ALiBi, learned) en términos de extrapolación a contextos más largos que los vistos en training?
- ¿El pre-norm design de GPT tiene tradeoffs en calidad de representación vs. el post-norm design original del paper "Attention Is All You Need"?

## Source
- **Raw note:** [[raw-notes/a-visual-guide-to-llms-part-2-inside-the-transformer-architectur]]
- **Original URL:** https://x.com/_rohit_tiwari_/status/2063982924714901858
