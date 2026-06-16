# RAG Retrieval Evaluation Evidence Pack

## Interview positioning

This repository supports the resume's retrieval-evaluation supplement. It is not positioned as a large-model training project. It demonstrates corpus schema design, chunking, BM25 + dense retrieval, reranking, metric evaluation, citation analysis, no-answer control, and badcase review.

## Problem

For job-description and interview-preparation documents, retrieval quality matters before generation quality. If the retriever misses evidence, the model may hallucinate or answer without support.

## What I can explain

- Why RAG evaluation starts from retrieval metrics instead of generation fluency.
- How query-evidence pairs are built.
- How chunk size affects recall and precision.
- Why BM25, dense retrieval, RRF, and reranker serve different roles.
- Why no-answer control is necessary when evidence is absent.

## Main files

- `docs/data_schema.md`: corpus and query schema.
- `scripts/run_experiment.py`: experiment runner.
- `src/hybrid_rag_lab/`: retrieval, fusion, reranking, and evaluation logic.
- `experiments/retrieval_metrics.csv`: retrieval metrics.
- `experiments/chunk_size_ablation.csv`: chunk-size ablation.
- `badcases/error_analysis.csv`: error analysis.
