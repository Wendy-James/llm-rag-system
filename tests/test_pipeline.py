from hybrid_rag_lab.data import load_corpus, load_queries
from hybrid_rag_lab.evaluate import evaluate
from hybrid_rag_lab.pipeline import HybridRAGPipeline


def test_hybrid_search_returns_relevant_rag_document() -> None:
    pipeline = HybridRAGPipeline(load_corpus())
    results = pipeline.search_hybrid("Why use hybrid search in RAG?", top_k=3)
    ids = [result.doc.id for result in results]
    assert "doc_rag_001" in ids


def test_evaluation_metrics_are_bounded() -> None:
    pipeline = HybridRAGPipeline(load_corpus())
    metrics = evaluate(pipeline, load_queries(), mode="hybrid_rerank", k=3)
    assert 0.0 <= metrics.recall_at_k <= 1.0
    assert 0.0 <= metrics.mrr_at_k <= 1.0
    assert 0.0 <= metrics.ndcg_at_k <= 1.0

