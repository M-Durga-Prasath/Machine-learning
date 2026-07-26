# 🔍 Week 5 Capstone — RAG Document Retrieval Pipeline

> **Location:** `week5_ragfoundations/day4/`
> **Main scripts:** [`embed.py`](embed.py) · [`retrival.py`](retrival.py) · [`simplerRAG.ipynb`](simplerRAG.ipynb)

---

## What This Project Does

This project builds a **Retrieval-Augmented Generation (RAG) pipeline** that lets you ask natural-language questions and retrieves the most relevant passages from a collection of PDF documents. It covers the full retrieval side of RAG — from raw PDFs to semantic search results.

### Pipeline at a Glance

```
PDF Documents
      │
      ▼
 ┌──────────┐
 │ Read PDF  │  ← pypdf extracts raw text
 └────┬─────┘
      │
      ▼
 ┌──────────┐
 │  Chunk   │  ← RecursiveCharacterTextSplitter (500 chars, 50 overlap)
 └────┬─────┘
      │
      ▼
 ┌──────────┐
 │  Embed   │  ← SentenceTransformer (all-MiniLM-L6-v2) → 384-dim vectors
 └────┬─────┘
      │
      ▼
 ┌──────────┐
 │  Index   │  ← FAISS IndexFlatL2 (exact L2 search)
 └────┬─────┘
      │
      ▼
 ┌──────────┐
 │  Query   │  ← User asks a question → embed → search → top-K chunks
 └──────────┘
```

### How It Works

1. **`embed.py`** reads all PDFs from `day3/papers/`, chunks the text using LangChain's `RecursiveCharacterTextSplitter`, generates embeddings with `all-MiniLM-L6-v2`, builds a FAISS index, and saves it to disk
2. **`retrival.py`** loads the saved FAISS index, takes a user question, embeds it, and returns the top-5 most similar chunks with source metadata
3. **`simplerRAG.ipynb`** ties it all together in an interactive notebook for experimentation

---

## Files

| File | Description |
|------|-------------|
| `embed.py` | PDF reading → chunking → embedding → FAISS index building |
| `retrival.py` | Query embedding → FAISS search → ranked results |
| `simplerRAG.ipynb` | Interactive notebook for the full RAG retrieval flow |
| `vector_store.faiss` | Pre-built FAISS index (saved binary) |
| `metadata.pkl` | Chunk metadata (source file, chunk ID, text) |
| `.env` | Environment variables |

---

## Tech Stack

- **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`) — 384-dimensional vectors
- **Vector Store:** FAISS (`IndexFlatL2` — exact L2 nearest-neighbor search)
- **PDF Parsing:** pypdf
- **Chunking:** LangChain `RecursiveCharacterTextSplitter`
- **Language:** Python

---

## How to Run

### Step 1 — Build the index

```bash
# Install dependencies
pip install sentence-transformers faiss-cpu pypdf langchain-text-splitters

# Place your PDF files in week5_ragfoundations/day3/papers/

# Build the vector index
python embed.py
```

This reads all PDFs, chunks them, generates embeddings, and saves `vector_store.faiss` + `metadata.pkl`.

### Step 2 — Query the index

```bash
python retrival.py
# You'll be prompted: "Ask a question: "
# Type your question and get the top-5 most relevant chunks
```

**Example output:**
```
Ask a question: What is attention in transformers?

Retrieved Chunks
============================================================

Rank      : 1
Source    : attention_paper.pdf
Chunk ID  : 42
Distance  : 0.8321
------------------------------------------------------------
Attention is a mechanism that allows the model to focus on
different parts of the input sequence...
```

---

## Key Concepts Applied

| Concept | Details |
|---------|---------|
| **Mean pooling** | `all-MiniLM-L6-v2` uses mean pooling over token embeddings for better semantic representation |
| **Chunking strategy** | 500-character chunks with 50-character overlap to preserve context at boundaries |
| **FAISS IndexFlatL2** | Exact L2 (Euclidean) nearest-neighbor search — no approximation, suitable for small-to-medium datasets |
| **Metadata tracking** | Each chunk stores its source PDF and chunk ID for traceability |

---

## What I Learned

- The full embed → index → retrieve pipeline that forms the "R" in RAG
- How `RecursiveCharacterTextSplitter` handles text splitting with overlap for context preservation
- Using FAISS for fast vector similarity search in Python
- Why sentence transformers (mean pooling) produce better semantic embeddings than raw BERT CLS tokens
- Structuring a retrieval system with separate indexing and querying scripts for modularity
