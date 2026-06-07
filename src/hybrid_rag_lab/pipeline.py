from __future__ import annotations

from dataclasses import dataclass

from .bm25 import BM25Retriever
from .data import Document
from .dense import HashingDenseRetriever
from .fusion import reciprocal_rank_fusion
from .rerank import LexicalReranker
from .rewrite import rewrite_query


@dataclass(frozen=True)
class SearchResult:
    doc: Document
    score: float
    source: str


class HybridRAGPipeline:
    def __init__(self, documents: list[Document]) -> None:
        self.documents = documents
        self.by_id = {doc.id: doc for doc in documents}
        self.bm25 = BM25Retriever(documents)
        self.dense = HashingDenseRetriever(documents)
        self.reranker = LexicalReranker()

    def search_bm25(self, query: str, top_k: int = 5) -> list[SearchResult]:
        return [SearchResult(doc, score, "bm25") for doc, score in self.bm25.search(query, top_k)]

    def search_dense(self, query: str, top_k: int = 5) -> list[SearchResult]:
        return [SearchResult(doc, score, "dense") for doc, score in self.dense.search(query, top_k)]

    def search_hybrid(self, query: str, top_k: int = 5, rerank: bool = True) -> list[SearchResult]:
        rewritten_queries = rewrite_query(query)
        result_sets: list[list[tuple[Document, float]]] = []
        for rewritten in rewritten_queries:
            result_sets.append(self.bm25.search(rewritten, top_k=top_k * 2))
            result_sets.append(self.dense.search(rewritten, top_k=top_k * 2))
        fused = reciprocal_rank_fusion(result_sets)
        candidates = [(self.by_id[doc_id], score) for doc_id, score in fused if doc_id in self.by_id]
        if rerank:
            candidates = self.reranker.rerank(query, candidates, top_k=top_k)
            return [SearchResult(doc, score, "hybrid+rerank") for doc, score in candidates]
        return [SearchResult(doc, score, "hybrid") for doc, score in candidates[:top_k]]

