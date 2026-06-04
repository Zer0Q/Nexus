# OCR (Optical Character Recognition)

## Definition
Technology that converts images of text (scanned documents, photos, screenshots) into machine-readable text. In AI workflows, OCR is the bridge between visual document formats (scanned PDFs, image-based lab reports) and text-based model inputs.

## Why It Matters
AI models consume text, not images. Many documents -- especially medical records, historical archives, and handwritten notes -- exist only as scanned PDFs or images. OCR makes these accessible to AI analysis.

## Key Ideas
- Converts pixel data into character data
- Accuracy depends on source quality (resolution, contrast, handwriting)
- Modern OCR (Tesseract, AWS Textract, Google Vision) achieves 95%+ accuracy on clean documents
- Medical OCR requires verification -- errors in clinical data are dangerous
- Often combined with LLMs for post-processing and error correction

## Related
- [[concepts/OCR-Clinical-Document-Processing]] -- OCR applied to medical records
- [[concepts/Full-Clinical-History-Processing]] -- the broader pipeline
- [[concepts/RAG]] -- OCR feeds text into retrieval systems

## Source
[[summaries/JaviLopen-AI-Medical-Research-ARROWHEAD]]
