from __future__ import annotations

from .data import Document
from .text import tokenize


class LexicalReranker:
    def score(self, query: str, doc: Document, base_score: float) -> float:
        query_terms = set(tokenize(query))
        doc_terms = set(tokenize(doc.content))
        if not query_terms:
            return base_score
        coverage = len(query_terms & doc_terms) / len(query_terms)
        title_overlap = len(query_terms & set(tokenize(doc.title))) / len(query_terms)
        return base_score + 0.35 * coverage + 0.2 * title_overlap

    def rerank(self, query: str, candidates: list[tuple[Document, float]], top_k: int = 5) -> list[tuple[Document, float]]:
        scored = [(doc, self.score(query, doc, score)) for doc, score in candidates]
        scored.sort(key=lambda item: item[1], reverse=True)
        return scored[:top_k]

