from __future__ import annotations

import math
from collections import Counter, defaultdict

from .data import Document
from .text import tokenize


class BM25Retriever:
    def __init__(self, documents: list[Document], k1: float = 1.5, b: float = 0.75) -> None:
        self.documents = documents
        self.k1 = k1
        self.b = b
        self.doc_terms = [Counter(tokenize(doc.content)) for doc in documents]
        self.doc_lengths = [sum(counts.values()) for counts in self.doc_terms]
        self.avg_doc_len = sum(self.doc_lengths) / max(len(self.doc_lengths), 1)
        self.idf = self._build_idf()

    def _build_idf(self) -> dict[str, float]:
        doc_freq: dict[str, int] = defaultdict(int)
        for counts in self.doc_terms:
            for token in counts:
                doc_freq[token] += 1
        total_docs = len(self.documents)
        return {
            token: math.log(1 + (total_docs - freq + 0.5) / (freq + 0.5))
            for token, freq in doc_freq.items()
        }

    def score(self, query: str, index: int) -> float:
        query_terms = tokenize(query)
        counts = self.doc_terms[index]
        doc_len = self.doc_lengths[index]
        score = 0.0
        for term in query_terms:
            freq = counts.get(term, 0)
            if freq == 0:
                continue
            numerator = freq * (self.k1 + 1)
            denominator = freq + self.k1 * (1 - self.b + self.b * doc_len / self.avg_doc_len)
            score += self.idf.get(term, 0.0) * numerator / denominator
        return score

    def search(self, query: str, top_k: int = 5) -> list[tuple[Document, float]]:
        scored = [(doc, self.score(query, idx)) for idx, doc in enumerate(self.documents)]
        scored.sort(key=lambda item: item[1], reverse=True)
        return scored[:top_k]

