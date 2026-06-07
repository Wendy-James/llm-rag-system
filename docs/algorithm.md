# Algorithm Notes

## 1. BM25 Sparse Retrieval

BM25 ranks a document by matching query terms against document terms. It improves over raw term frequency by adding:

- inverse document frequency, which gives rare terms more weight
- term-frequency saturation, which avoids over-rewarding repeated words
- document-length normalization

In this project, BM25 is useful for exact terms such as `RAG`, `FAISS`, `CTR`, `nDCG`, and `reranker`.

## 2. Dense Retrieval Baseline

The current dense retriever uses a hashing trick:

1. tokenize text
2. hash each token into a fixed vector bucket
3. assign a deterministic sign
4. L2-normalize the vector
5. rank documents with cosine similarity

This is not a semantic embedding model. It is an engineering baseline that keeps the pipeline local and testable. The next step is to replace it with sentence-transformer embeddings and FAISS ANN indexing.

## 3. Query Rewrite

Query rewrite creates multiple retrieval routes from one user question. Example:

```text
Why use hybrid search in RAG?
Why use hybrid search in RAG? retrieval augmented generation retrieval sparse dense bm25 vector
Why use hybrid search in RAG
```

This improves recall when the user query uses abbreviations or when relevant documents use different wording.

## 4. Reciprocal Rank Fusion

RRF combines ranked lists without requiring comparable raw scores.

```text
score(document) = sum(1 / (k + rank_i))
```

Where `rank_i` is the document rank in retriever `i`. A document receives a higher fused score if it appears near the top of multiple routes.

## 5. Reranking

The first-stage retrievers optimize recall. The reranker optimizes ordering.

The current reranker adds:

- query-term coverage
- title overlap
- base fused score

This is intentionally lightweight. In a later version, it can be replaced with a cross-encoder reranker.

## 6. Metrics

| Metric | Meaning | Interview Explanation |
|---|---|---|
| Recall@K | Whether relevant docs appear in top K | Measures retrieval coverage |
| MRR@K | Rank of the first relevant doc | Rewards placing a correct result early |
| nDCG@K | Ranking quality with relevance discount | Evaluates ordered result quality |

## 7. Training and Inference Flow

Current version has no neural training loop. It focuses on retrieval system evaluation.

Inference flow:

1. load corpus
2. build sparse and dense indexes
3. rewrite query
4. retrieve from BM25 and dense retriever
5. fuse candidates with RRF
6. rerank candidates
7. return top-K contexts

Future training extensions:

- train or fine-tune embedding model
- train cross-encoder reranker
- tune fusion weights and query rewrite rules on validation queries

