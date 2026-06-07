from __future__ import annotations

from collections import defaultdict

from .data import Document


def reciprocal_rank_fusion(result_sets: list[list[tuple[Document, float]]], k: int = 60) -> list[tuple[str, float]]:
    scores: dict[str, float] = defaultdict(float)
    for results in result_sets:
        for rank, (doc, _) in enumerate(results, start=1):
            scores[doc.id] += 1.0 / (k + rank)
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)

