from __future__ import annotations

import argparse

from .data import load_corpus, load_queries
from .evaluate import evaluate
from .pipeline import HybridRAGPipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Hybrid RAG retrieval lab")
    subparsers = parser.add_subparsers(dest="command", required=True)

    search = subparsers.add_parser("search", help="Run hybrid retrieval for one query")
    search.add_argument("--query", required=True)
    search.add_argument("--k", type=int, default=5)
    search.add_argument("--no-rerank", action="store_true")

    evaluate_cmd = subparsers.add_parser("evaluate", help="Evaluate retrieval modes")
    evaluate_cmd.add_argument("--k", type=int, default=3)
    return parser


def run_search(args: argparse.Namespace) -> None:
    pipeline = HybridRAGPipeline(load_corpus())
    results = pipeline.search_hybrid(args.query, top_k=args.k, rerank=not args.no_rerank)
    for rank, result in enumerate(results, start=1):
        print(f"{rank}. {result.doc.id} | {result.score:.4f} | {result.doc.title}")
        print(f"   {result.doc.text}")


def run_evaluate(args: argparse.Namespace) -> None:
    pipeline = HybridRAGPipeline(load_corpus())
    queries = load_queries()
    print(f"mode,recall@{args.k},mrr@{args.k},ndcg@{args.k}")
    for mode in ["bm25", "dense", "hybrid", "hybrid_rerank"]:
        metrics = evaluate(pipeline, queries, mode=mode, k=args.k)
        print(
            f"{mode},{metrics.recall_at_k:.4f},"
            f"{metrics.mrr_at_k:.4f},{metrics.ndcg_at_k:.4f}"
        )


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "search":
        run_search(args)
    elif args.command == "evaluate":
        run_evaluate(args)


if __name__ == "__main__":
    main()

