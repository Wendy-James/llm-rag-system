# Data Schema

This root-level file mirrors the interview-facing schema in `docs/data_schema.md` so reviewers can find the evidence quickly.

## Corpus Fields

| Field | Type | Notes |
|---|---|---|
| `doc_id` | string | Stable document id before chunking. |
| `chunk_id` | string | Unique chunk id used for retrieval labels. |
| `source_type` | enum | `job_description`, `project_note`, `interview_review`, or `resume_note`. |
| `title` | string | Desensitized document title. |
| `section` | string | Logical section after parsing. |
| `text` | string | Cleaned chunk body. |
| `tokens` | integer | Approximate token count after cleaning. |
| `tags` | list | Retrieval and interview topic tags. |

## Query Fields

| Field | Type | Notes |
|---|---|---|
| `query_id` | string | Stable query id. |
| `query` | string | Interview-style or evidence-lookup query. |
| `intent` | enum | Query category for badcase analysis. |
| `positive_chunk_ids` | list | Accepted evidence chunks. |
| `answer_hint` | string | Short reference for manual checking. |
| `difficulty` | enum | `easy`, `medium`, or `hard`. |
| `tags` | list | Query topic tags. |

## Resume-Scale Protocol

- Documents: 300 anonymized JD, project-note, and interview-review documents.
- Chunks: about 6000 after cleaning and overlap chunking.
- Queries: 180 query-evidence pairs.
- Chunk settings compared: 300/500/800 with overlaps 60/100/120.
- Final working setting: chunk size 500, overlap 100.

## Boundary

This repository contains pseudo/anonymized samples only. It does not publish private company documents, personal interview notes, or original resume drafts.
