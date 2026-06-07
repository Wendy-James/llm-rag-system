# Experiments

## Baseline Evaluation

Run:

```bash
python -m hybrid_rag_lab.cli evaluate --k 3
```

Compared modes:

- `bm25`: sparse keyword retrieval
- `dense`: deterministic dense-style hashing retrieval
- `hybrid`: query rewrite + BM25 + dense + RRF
- `hybrid_rerank`: hybrid retrieval plus reranking

## Expected Analysis

BM25 should perform strongly on exact technical words. Dense hashing provides a local dense-style baseline but is not expected to outperform real embeddings. Hybrid retrieval should improve robustness when relevant documents appear in multiple retrieval routes. Reranking should improve ordering when candidate recall is already sufficient.

## Experiment Log Template

| Date | Change | Recall@3 | MRR@3 | nDCG@3 | Notes |
|---|---|---:|---:|---:|---|
| 2026-06-07 | BM25 baseline | 0.9000 | 1.0000 | 0.9226 | Small local corpus |
| 2026-06-07 | Dense hashing baseline | 0.9000 | 1.0000 | 0.9226 | Local deterministic dense-style baseline |
| 2026-06-07 | Query rewrite + BM25 + dense + RRF | 0.9000 | 1.0000 | 0.9226 | Hybrid first-stage retrieval |
| 2026-06-07 | Hybrid RRF + lexical reranker | 1.0000 | 1.0000 | 1.0000 | Reranking improved top-3 coverage on sample queries |

## Verification

Search command:

```bash
PYTHONPATH=src python -m hybrid_rag_lab.cli search --query "How does reranking improve RAG retrieval?" --k 3
```

Top results:

1. `doc_rag_002` - Reranking in Retrieval Pipelines
2. `doc_rag_001` - Hybrid Retrieval for RAG
3. `doc_eval_001` - Retrieval Evaluation Metrics

Evaluation command:

```bash
PYTHONPATH=src python -m hybrid_rag_lab.cli evaluate --k 3
```

Output:

```csv
mode,recall@3,mrr@3,ndcg@3
bm25,0.9000,1.0000,0.9226
dense,0.9000,1.0000,0.9226
hybrid,0.9000,1.0000,0.9226
hybrid_rerank,1.0000,1.0000,1.0000
```

## Next Experiments

1. Add a larger corpus from public technical documentation.
2. Replace hashed dense retrieval with `sentence-transformers`.
3. Add FAISS index types: FlatIP, IVF, HNSW.
4. Compare RRF with weighted score fusion.
5. Add cross-encoder reranker and measure latency-quality tradeoff.
