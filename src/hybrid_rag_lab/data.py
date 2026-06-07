from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Document:
    id: str
    title: str
    text: str

    @property
    def content(self) -> str:
        return f"{self.title}. {self.text}"


@dataclass(frozen=True)
class Query:
    id: str
    query: str
    relevant_ids: list[str]


def default_data_dir() -> Path:
    return Path(__file__).resolve().parents[2] / "data"


def load_corpus(path: Path | None = None) -> list[Document]:
    corpus_path = path or default_data_dir() / "corpus.jsonl"
    docs: list[Document] = []
    with corpus_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            docs.append(Document(id=row["id"], title=row["title"], text=row["text"]))
    return docs


def load_queries(path: Path | None = None) -> list[Query]:
    query_path = path or default_data_dir() / "queries.jsonl"
    queries: list[Query] = []
    with query_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            queries.append(Query(id=row["id"], query=row["query"], relevant_ids=row["relevant_ids"]))
    return queries
