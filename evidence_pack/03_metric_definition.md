# Metric Definition

## Recall@5

Checks whether the gold evidence chunk appears in top 5 retrieved chunks.

Use case: evidence coverage. It is the most important retrieval-stage metric in this project.

## MRR

Mean Reciprocal Rank rewards ranking the first correct evidence higher.

Use case: measures whether useful evidence appears early enough for a reranker or generator.

## NDCG

NDCG supports graded relevance when multiple chunks are partially useful.

## Citation hit rate

Checks whether the final answer cites a retrieved chunk that matches the expected evidence.

## No-answer control

For unanswerable queries, the system should avoid unsupported answers. This is tracked through no-answer / unsupported-answer analysis in badcases.
