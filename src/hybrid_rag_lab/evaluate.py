from __future__ import annotations

import math
from dataclasses import dataclass

from .data import Query
from .pipeline import HybridRAGPipeline, SearchResult


@dataclass(frozen=True)
class MetricResult:
    recall_at_k: float
    mrr_at_k: float
    ndcg_at_k: float


def recall_at_k(results: list[SearchResult], relevant_ids: set[str], k: int) -> float:
    if not relevant_ids:
        return 0.0
    retrieved = {result.doc.id for result in results[:k]}
    return len(retrieved & relevant_ids) / len(relevant_ids)


def mrr_at_k(results: list[SearchResult], relevant_ids: set[str], k: int) -> float:
    for rank, result in enumerate(results[:k], start=1):
        if result.doc.id in relevant_ids:
            return 1.0 / rank
    return 0.0


def ndcg_at_k(results: list[SearchResult], relevant_ids: set[str], k: int) -> float:
    dcg = 0.0
    for rank, result in enumerate(results[:k], start=1):
        relevance = 1.0 if result.doc.id in relevant_ids else 0.0
        dcg += relevance / math.log2(rank + 1)
    ideal_hits = min(len(relevant_ids), k)
    ideal_dcg = sum(1.0 / math.log2(rank + 1) for rank in range(1, ideal_hits + 1))
    return dcg / ideal_dcg if ideal_dcg else 0.0


def evaluate(
    pipeline: HybridRAGPipeline,
    queries: list[Query],
    mode: str,
    k: int,
) -> MetricResult:
    recalls: list[float] = []
    mrrs: list[float] = []
    ndcgs: list[float] = []
    for query in queries:
        if mode == "bm25":
            results = pipeline.search_bm25(query.query, top_k=k)
        elif mode == "dense":
            results = pipeline.search_dense(query.query, top_k=k)
        elif mode == "hybrid":
            results = pipeline.search_hybrid(query.query, top_k=k, rerank=False)
        elif mode == "hybrid_rerank":
            results = pipeline.search_hybrid(query.query, top_k=k, rerank=True)
        else:
            raise ValueError(f"Unknown mode: {mode}")
        relevant = set(query.relevant_ids)
        recalls.append(recall_at_k(results, relevant, k))
        mrrs.append(mrr_at_k(results, relevant, k))
        ndcgs.append(ndcg_at_k(results, relevant, k))
    total = max(len(queries), 1)
    return MetricResult(
        recall_at_k=sum(recalls) / total,
        mrr_at_k=sum(mrrs) / total,
        ndcg_at_k=sum(ndcgs) / total,
    )

