# qmd

## Definition
Local search engine for markdown files by @tobi. Hybrid BM25/vector search with LLM re-ranking, all on-device. Provides both CLI (for LLM shell-out) and MCP server (for native tool use).

## Why It Matters
Enables proper semantic search over growing knowledge bases. At small scale, index files suffice; as the wiki grows to hundreds/thousands of pages, qmd provides the search infrastructure without cloud dependencies.

## Key Ideas
- Hybrid BM25 + vector search + LLM re-ranking
- Fully on-device -- no cloud dependencies
- CLI interface: LLM can shell out to it for searches
- MCP server: LLM can use it as a native tool
- GitHub: github.com/tobi/qmd
- Used by @omarsar0 for indexing hundreds of research papers

## Tradeoffs
- Additional tool to maintain
- May be overkill for small vaults (<100 pages)
- Local embeddings require compute resources

## Related
- [[concepts/Write-Time-Knowledge-Systems]]
- [[concepts/Embedding-Based-Vault-Search]]
- [[concepts/Automated-Research-Curation]]

## Source
[[summaries/OmarSaridakis-Research-KB]]
