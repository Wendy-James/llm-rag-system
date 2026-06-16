# Data Schema

This repository uses sample or public-style documents. It does not contain private company documents or confidential interview records.

## Corpus fields

| Field | Meaning |
|---|---|
| `doc_id` | document id |
| `title` | document title |
| `source_type` | JD, project note, interview note, or learning note |
| `text` | document body |
| `metadata` | role, skill, company type, or topic tags |

## Chunk fields

| Field | Meaning |
|---|---|
| `chunk_id` | chunk id |
| `doc_id` | parent document id |
| `chunk_text` | chunk content |
| `start_offset` | start position |
| `end_offset` | end position |
| `token_count` | estimated length |

## Query-evidence fields

| Field | Meaning |
|---|---|
| `query_id` | query id |
| `query` | user question |
| `gold_doc_id` | expected evidence document |
| `gold_chunk_id` | expected evidence chunk |
| `answerable` | whether evidence exists |
