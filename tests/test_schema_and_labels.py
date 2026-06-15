import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_sample_queries_have_positive_evidence_labels() -> None:
    rows = [
        json.loads(line)
        for line in (ROOT / "data" / "sample_queries.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    assert rows
    assert all(row["positive_chunk_ids"] for row in rows)
    assert {"metric_definition", "project_evidence", "ablation_reasoning"} & {row["intent"] for row in rows}


def test_retrieval_metrics_document_reranker_lift() -> None:
    csv_text = (ROOT / "experiments" / "retrieval_metrics.csv").read_text(encoding="utf-8")

    assert "bm25_dense_rrf" in csv_text
    assert "bm25_dense_reranker" in csv_text
    assert "0.71" in csv_text
    assert "0.77" in csv_text
