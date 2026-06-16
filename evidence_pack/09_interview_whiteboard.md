# Interview Whiteboard

```text
Documents / JD / project notes
  |
  v
Chunking
chunk size + overlap + metadata
  |
  v
Retrieval candidates
BM25                  Dense retrieval
  |                         |
  v                         v
keyword evidence       semantic evidence
          \             /
           RRF fusion
              |
              v
Reranker
              |
              v
TopK evidence chunks
              |
              v
Recall@5 / MRR / citation hit rate / no-answer control
              |
              v
Badcases: chunk too large, chunk too small, dense drift, unsupported answer
```

## How to narrate it

Frame it as retrieval evaluation first. The main question is whether the system can retrieve grounded evidence and refuse weak-evidence queries, not whether the generated answer sounds fluent.
