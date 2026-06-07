# Interview Notes

## 60-Second Pitch

I built a Hybrid RAG retrieval lab to study how retrieval quality changes across sparse retrieval, dense retrieval, query rewrite, rank fusion, and reranking. Instead of simply calling an LLM API, the project focuses on the retrieval layer that determines whether a RAG system can find the right evidence. It includes a local corpus, labeled queries, BM25, a deterministic dense baseline, RRF fusion, reranking, and Recall/MRR/nDCG evaluation.

## STAR Version

Situation: Single-route RAG retrieval can fail when user wording differs from document wording or when exact technical terms are important.

Task: Build a measurable retrieval pipeline that can compare retrieval strategies and support later LLM generation.

Action: Implemented BM25 sparse retrieval, dense-style hashing retrieval, query rewrite, Reciprocal Rank Fusion, lexical reranking, and evaluation metrics.

Result: The repository can be run locally, tested automatically, and extended toward FAISS embeddings and cross-encoder reranking.

## Deep-Dive Questions

### Why hybrid retrieval?

Sparse retrieval is strong for exact matching, while dense retrieval is better for semantic similarity when real embeddings are used. Hybrid retrieval combines both so the system is less sensitive to query wording.

### Why RRF instead of adding scores?

BM25 and dense cosine scores are not naturally calibrated. RRF only uses ranks, so it is robust when different retrievers produce scores on different scales.

### What is the role of reranking?

First-stage retrieval focuses on recall and speed. Reranking uses richer matching signals to improve the top results. This architecture mirrors production search systems.

### What would you improve next?

I would replace the hashing baseline with sentence-transformer embeddings, index them with FAISS, add a cross-encoder reranker, build a larger evaluation set, and measure latency/quality tradeoffs.

