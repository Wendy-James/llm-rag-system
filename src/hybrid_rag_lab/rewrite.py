from __future__ import annotations


SYNONYMS = {
    "rag": ["retrieval augmented generation", "retrieval"],
    "reranking": ["reranker", "ranking quality", "candidate passages"],
    "rerank": ["reranker", "ranking quality"],
    "hybrid": ["sparse dense", "bm25 vector"],
    "search": ["retrieval"],
    "ctr": ["click through rate", "ranking"],
    "metrics": ["recall mrr ndcg evaluation"],
}


def rewrite_query(query: str) -> list[str]:
    lowered = query.lower()
    rewrites = [query]
    expansions: list[str] = []
    for key, values in SYNONYMS.items():
        if key in lowered:
            expansions.extend(values)
    if expansions:
        rewrites.append(f"{query} {' '.join(expansions)}")
    if "?" in query:
        rewrites.append(query.replace("?", "").strip())
    return list(dict.fromkeys(rewrites))

