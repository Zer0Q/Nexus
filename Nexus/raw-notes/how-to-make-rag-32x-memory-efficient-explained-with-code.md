---
title: "How to make RAG 32x memory efficient (explained with code)!"
source: "https://x.com/_avichawla/status/2040326889928356122"
author:
  - "[[@_avichawla]]"
published: 2026-03-30
created: 2026-05-31
description: "How Perplexity, Azure, HubSpot, and many others use binary quantization to make RAG 32x memory efficient (explained with code)!There’s a sim..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HFCyFOmbQAEeJEv?format=jpg&name=large)

**How Perplexity, Azure, HubSpot, and many others use binary quantization to make RAG 32x memory efficient (explained with code)!**

There’s a simple technique that’s commonly used in the industry that makes RAG ~32x memory efficient!

- Perplexity uses it in its search index
- Azure uses it in its search pipeline
- HubSpot uses it in its AI assistant

To learn this, we’ll build a RAG system that queries 36M+ vectors in <30ms.

And the technique that will power it is called Binary Quantization.

Tech stack:

- Llama Index for orchestration (open-source)
- Milvus as the vector DB (open-source)
- Kimi-K2 as the LLM hosted on Groq (hosted)

![Vídeo incrustat](https://pbs.twimg.com/amplify_video_thumb/2040318073740345344/img/I1I9JtN2a48xKJIx?format=jpg&name=large)

0:13

Here's the workflow:

![Vídeo incrustat](https://pbs.twimg.com/tweet_video_thumb/HFCqp1OaoAAeKG6?format=jpg&name=large)

GIF

- Ingest documents and generate binary embeddings.
- Create a binary vector index and store embeddings in the vector DB.
- Retrieve top-k similar documents to the user's query.
- LLM generates a response based on additional context.

Let's implement this!

## 1) Load data

We ingest our documents using LlamaIndex's directory reader tool. It can read various data formats, including Markdown, PDFs, Word documents, PowerPoint decks, images, audio, and video.

```python
from llama_index.core import SimpleDirectoryReader

loader = SimpleDirectoryReader(
    input_dir=docs_dir,
    required_exts=[".pdf"],
    recursive=True
)

docs = loader.load_data()
documents = [doc.text for doc in docs]
```

We are using a simple PDF directory reader here for explainability, but in practice, your ingestion pipeline will likely pull from multiple data sources with varied formats and preprocessing steps.

## 2) Generate Binary Embeddings

Next, we generate text embeddings (in float32) and convert them to binary vectors, resulting in a 32x reduction in memory and storage.

```python
import numpy as np
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-large-en-v1.5",
    trust_remote_code=True,
    cache_folder='./hf_cache'
)

for context in batch_iterate(documents, batch_size=512):
    # Generate float32 vector embeddings
    batch_embeds = embed_model.get_text_embedding_batch(context)
    # Convert float32 vectors to binary vectors
    embeds_array = np.array(batch_embeds)
    binary_embeds = np.where(embeds_array > 0, 1, 0).astype(np.uint8)
    # Convert to bytes array
    packed_embeds = np.packbits(binary_embeds, axis=1)
    byte_embeds = [vec.tobytes() for vec in packed_embeds]

    binary_embeddings.extend(byte_embeds)
```

This is called binary quantization.

## 3) Vector indexing

After our binary quantization is done, we store and index the vectors in a Milvus vector database for efficient retrieval.

```python
from pymilvus import MilvusClient, DataType

# Initialize client and schema
client = MilvusClient("milvus_binary_quantized.db")
schema = client.create_schema(auto_id=True, enable_dynamic_fields=True)

# Add fields to schema
schema.add_field(field_name="context", datatype=DataType.VARCHAR)
schema.add_field(field_name="binary_vector", datatype=DataType.BINARY_VECTOR)

# Create index parameters for binary vectors
index_params = client.prepare_index_params()
index_params.add_index(
    field_name="binary_vector",
    index_name="binary_vector_index",
    index_type="BIN_FLAT",  # Exact search for binary vectors
    metric_type="HAMMING"   # Hamming distance for binary vectors
)

# Create collection with schema and index
client.create_collection(
    collection_name="fastest-rag",
    schema=schema,
    index_params=index_params
)

# Insert data to index
client.insert(
    collection_name="fastest-rag",
    data=[
        {"context": context, "binary_vector": binary_embedding}
        for context, binary_embedding in zip(batch_context, binary_embeddings)
    ]
)
```

Indexes are specialized data structures that help optimize the performance of data retrieval operations.

## 4) Retrieval

In the retrieval stage, we:

- Embed the user query and apply binary quantization to it.
- Use Hamming distance as the search metric to compare binary vectors.
- Retrieve the top 5 most similar chunks.
- Add the retrieved chunks to the context.

This is the implementation:

```python
# Generate float32 query embedding
query_embedding = embed_model.get_query_embedding(query)
# Apply binary quantization to query
binary_query = binary_quantize(query_embedding)

# Perform similarity search using Milvus
search_results = client.search(
    collection_name="fastest-rag",
    data=[binary_query],
    anns_field="binary_vector",
    search_params={"metric_type": "HAMMING"},
    output_fields=["context"],
    limit=5  # Retrieve top 5 similar chunks
)

# Store retrieved context
full_context = []
for res in search_results:
    context = res["payload"]["context"]
    full_context.append(context)
```

## 5) Generation

Moving on, we build a generation pipeline using the Kimi-K2 instruct model, served on the fastest AI inference by Groq.

We specify both the query and the retrieved context in a prompt template and pass it to the LLM.

```python
from llama_index.llms.groq import Groq
from llama_index.core.base.llms.types import (
    ChatMessage, MessageRole )

llm = Groq(
    model="moonshotai/kimi-k2-instruct",
    api_key=groq_api_key,
    temperature=0.5,
    max_tokens=1000
)

prompt_template = (
    "Context information is below.\n"
    "---------------------\n"
    "CONTEXT: {context}\n"
    "---------------------\n"
    "Given the context information above think step by step "
    "to answer the user's query in a crisp and concise manner. "
    "In case you don't know the answer say 'I don't know!'.\n"
    "QUERY: {query}\n"
    "ANSWER: "
)

query = "Provide concise breakdown of the document"

prompt = prompt_template.format(context=full_context, query=query)
user_msg = ChatMessage(role=MessageRole.USER, content=prompt)

# Stream response from LLM
streaming_response = llm.stream_complete(user_msg.content)
```

Finally, we wrap this up in a Streamlit interface!

To assess the scale and inference speed, we test the setup over the PubMed dataset (36M+ vectors).

Here's a demo:

![Vídeo incrustat](https://pbs.twimg.com/amplify_video_thumb/2040318809341575168/img/CGUQfALc74nvIUOy?format=jpg&name=large)

0:13

Our app:

- queried 36M+ vectors in <30ms.
- generated a response in <1s.

Done!

We just built the fastest RAG stack leveraging BQ for efficient retrieval and

using ultra-fast serverless deployment of our AI workflow.

The code is available here: [https://github.com/patchy631/ai-engineering-hub/tree/main/fastest-rag-milvus-groq](https://github.com/patchy631/ai-engineering-hub/tree/main/fastest-rag-milvus-groq)

Here's the workflow again for your reference 👇

![Vídeo incrustat](https://pbs.twimg.com/tweet_video_thumb/HFCrRRgaoAE8ZqN?format=jpg&name=large)

GIF

One thing to note here is that binary quantization makes the vector search layer incredibly efficient. But in production, retrieval is rarely just a vector lookup.

Real-world agents pull context from Slack, GitHub, Jira, databases, and docs simultaneously. That means auth, sync, query routing, permissions, and reranking all become first-class concerns alongside the embedding search itself.

So think of BQ as one powerful piece of the retrieval infrastructure, not the whole story. The faster and leaner you make your vector layer, the more room you have to invest in everything else that makes retrieval actually work at scale.

I covered what that full retrieval infrastructure looks like in a recent post, breaking down how companies like Google and Microsoft actually give context to their production agents.

Read below:

> 30 de març
> 
> RAG is a distraction! Here's how Google and Microsoft actually give context to their production agents: To understand this, think about what "give an agent context" actually means in production. In production, data lives across Slack, Gmail, Jira, Drive, Salesforce, GitHub,

That's a wrap!

If you enjoyed this tutorial:

Find me → [@\_avichawla](https://x.com/@_avichawla)

Every day, I share tutorials and insights on DS, ML, LLMs, and RAGs.