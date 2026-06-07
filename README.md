# Hybrid RAG Lab

Hybrid RAG Lab is a reproducible retrieval-augmented generation project focused on retrieval quality, not API wrapping.

It implements a full local retrieval pipeline:

- document loading and chunking
- BM25 sparse retrieval
- deterministic hashed dense retrieval
- query rewrite
- Reciprocal Rank Fusion
- lexical reranking
- Recall@K, MRR@K, and nDCG@K evaluation

The project is designed as the first core repository in an algorithm-intern GitHub portfolio. It can be explained in interviews from both algorithm and engineering perspectives.

## Why This Project

Single-route dense retrieval often fails on exact keywords, abbreviations, and rare technical terms. Pure BM25 can miss semantic matches. This project compares sparse retrieval, dense retrieval, hybrid fusion, and reranking under the same evaluation set.

## Quick Start

```bash
python -m hybrid_rag_lab.cli search --query "How does reranking improve RAG retrieval?"
python -m hybrid_rag_lab.cli evaluate --k 3
```

For editable install:

```bash
python -m pip install -e .
hybrid-rag evaluate --k 3
```

## Current Results

The default sample corpus is intentionally small so the pipeline can run anywhere. It is used to validate retrieval logic before scaling to larger datasets.

```bash
python -m hybrid_rag_lab.cli evaluate --k 3
```

Reports:

- BM25 only
- dense hashing only
- hybrid RRF
- hybrid RRF + reranker

## Project Structure

```text
hybrid-rag-lab/
  data/
    corpus.jsonl
    queries.jsonl
  docs/
    architecture.md
    algorithm.md
    experiments.md
    interview-notes.md
  src/hybrid_rag_lab/
    bm25.py
    dense.py
    evaluate.py
    pipeline.py
    rerank.py
    rewrite.py
  tests/
```

## Roadmap

- Add real benchmark datasets such as BEIR-style QA or domain documents.
- Replace hashed dense vectors with sentence-transformer embeddings.
- Add FAISS or HNSW indexing for large-scale ANN search.
- Add cross-encoder reranker experiments.
- Add answer generation and hallucination evaluation after retrieval quality is stable.

## Resume Summary

Built a production-style Hybrid RAG retrieval system with BM25+dense retrieval, query rewrite, RRF fusion, reranking, and retrieval evaluation metrics including Recall@K, MRR, and nDCG.

