from __future__ import annotations

import math

from .data import Document
from .text import cosine, stable_hash, tokenize


class HashingDenseRetriever:
    """A deterministic dense-style retriever for local experiments.

    This is not a replacement for sentence embeddings. It lets the retrieval
    pipeline run without external services, then can be swapped for FAISS plus
    embedding models in later experiments.
    """

    def __init__(self, documents: list[Document], dimensions: int = 128) -> None:
        self.documents = documents
        self.dimensions = dimensions
        self.doc_vectors = [self.encode(doc.content) for doc in documents]

    def encode(self, text: str) -> list[float]:
        vector = [0.0] * self.dimensions
        tokens = tokenize(text)
        for token in tokens:
            bucket = stable_hash(token, self.dimensions)
            sign = 1.0 if stable_hash(f"sign:{token}", 2) == 0 else -1.0
            vector[bucket] += sign
        norm = math.sqrt(sum(value * value for value in vector))
        if norm == 0:
            return vector
        return [value / norm for value in vector]

    def search(self, query: str, top_k: int = 5) -> list[tuple[Document, float]]:
        query_vector = self.encode(query)
        scored = [
            (doc, cosine(query_vector, doc_vector))
            for doc, doc_vector in zip(self.documents, self.doc_vectors)
        ]
        scored.sort(key=lambda item: item[1], reverse=True)
        return scored[:top_k]

