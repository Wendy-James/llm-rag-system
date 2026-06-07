# Source Reading Notes

## Reading Goal

This project is organized around a retrieval-first RAG pipeline. The source code is intentionally small enough to explain in an interview while still covering the key production ideas: sparse retrieval, dense-style retrieval, query rewrite, rank fusion, reranking, and retrieval metrics.

## Entry Points

| File | Responsibility |
|---|---|
| `src/hybrid_rag_lab/cli.py` | CLI entry for search and evaluation commands |
| `scripts/run_experiment.py` | Reproducible baseline experiment runner |
| `src/hybrid_rag_lab/pipeline.py` | End-to-end retrieval pipeline orchestration |

## Core Algorithm Files

| File | What To Explain In Interviews |
|---|---|
| `bm25.py` | Token frequency, document frequency, inverse document frequency, and why sparse retrieval is strong for keyword matching |
| `dense.py` | Dense-style hashing baseline and why semantic retrieval complements BM25 |
| `rewrite.py` | Query expansion and rewrite logic before retrieval |
| `fusion.py` | Reciprocal Rank Fusion for combining multiple ranked lists |
| `rerank.py` | Second-stage reranking and the tradeoff between quality and latency |
| `evaluate.py` | Recall@K, MRR@K, and nDCG@K as retrieval quality metrics |

## Data Flow

```text
query
  -> query rewrite
  -> BM25 retrieval + dense-style retrieval
  -> RRF fusion
  -> reranking
  -> top-k documents
  -> retrieval metrics
```

## Interview Takeaways

- The project avoids relying on generation quality as a proxy for retrieval quality.
- Hybrid retrieval is useful because sparse and dense retrievers fail in different ways.
- Reranking improves the final ordering, but it should be evaluated against latency and cost.
- Metrics are separated from the CLI so experiments can be reproduced and extended.
