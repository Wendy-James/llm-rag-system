# Roadmap

This repository is maintained as a retrieval-evaluation lab for RAG workflows. It is a supporting project for retrieval, reranking, citation quality, and refusal-boundary discussion.

## Near-term

- Add a query-type breakdown for fact lookup, comparison, constraint matching, and ambiguous queries.
- Expand chunk-size ablation with overlap and section-aware splitting.
- Add a lightweight cross-encoder reranker comparison using cached scores.

## Evaluation

- Keep Recall@5, MRR, citation hit rate, and unsupported-answer rate as the main metrics.
- Track retrieval miss, reranker inversion, stale evidence, and ambiguous-query errors separately.
- Keep evidence citation quality separate from answer fluency.

## Engineering

- Keep `make all` runnable on CPU and sample data.
- Keep schema docs and error analysis in sync with metric files.
- Prefer small, reviewable updates that improve one retriever, one metric, or one error bucket.
