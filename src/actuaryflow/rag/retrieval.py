from __future__ import annotations

import math
import re
from dataclasses import dataclass

from .document import PolicyChunk

_TOKEN = re.compile(r"[A-Za-z0-9_]+")


def _tokens(text: str) -> set[str]:
    return {match.group(0).lower() for match in _TOKEN.finditer(text)}


@dataclass(frozen=True, slots=True)
class RetrievalResult:
    chunk: PolicyChunk
    score: float

    def as_dict(self) -> dict[str, object]:
        return {
            "document_id": self.chunk.document_id,
            "chunk_id": self.chunk.chunk_id,
            "title": self.chunk.title,
            "text": self.chunk.text,
            "score": self.score,
            "metadata": self.chunk.metadata,
        }


class PolicyRetriever:
    """Dependency-free BM25-like baseline for auditable local retrieval.

    This baseline is deliberately simple and deterministic. Production deployments can
    replace it with a vector/hybrid index while preserving the same public contract.
    """

    def __init__(self, chunks: list[PolicyChunk]) -> None:
        self._chunks = chunks
        self._tokenized = [_tokens(chunk.text) for chunk in chunks]

    def search(self, query: str, *, k: int = 5) -> list[dict[str, object]]:
        q = _tokens(query)
        if not q:
            return []
        scored: list[RetrievalResult] = []
        for chunk, tokens in zip(self._chunks, self._tokenized, strict=True):
            overlap = len(q & tokens)
            if overlap == 0:
                continue
            precision = overlap / max(len(tokens), 1)
            recall = overlap / len(q)
            score = math.sqrt(precision * recall)
            scored.append(RetrievalResult(chunk=chunk, score=score))
        scored.sort(key=lambda item: item.score, reverse=True)
        return [item.as_dict() for item in scored[:k]]
