# Development Log

## Public Evidence Boundary

This repository is a public evidence repo organized in **June 2026** for resume and interview review. It should be described as a retrieval-evaluation evidence repo, not as a production RAG service or a large-model training project.

The public version contains:

- anonymized and pseudo job/project/interview-review samples
- schema and metric definitions
- BM25, dense-style retrieval, RRF, reranking, and evaluation code
- retrieval metrics, chunk-size ablation, and badcase CSV files
- pytest checks and one-command execution

The public version does not contain:

- private company documents
- original JD/resume/interview notes that should not be public
- production service code
- online quality or business-impact claims

## Why The Repo Was Organized This Way

The resume mentions a RAG job knowledge-base retrieval project. To make the claim inspectable, this repo exposes:

1. corpus/query schema
2. runnable retrieval pipeline
3. Recall@K/MRR/nDCG calculation
4. retrieval metrics and chunk-size ablation
5. badcase records
6. tests and one-command execution

## Reproducible Commands

```bash
make all
```

or:

```bash
./run.sh
```

## Interview Wording

Safe wording:

> I organized a public evidence version in June 2026. It uses anonymized/pseudo documents to make the retrieval evaluation method, metric definitions, chunking ablation, and badcase analysis inspectable.

Avoid:

> This repo is a production RAG system, uses private company data, or proves large-model training experience.
