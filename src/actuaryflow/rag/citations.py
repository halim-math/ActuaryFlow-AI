from __future__ import annotations

from .document import PolicyChunk


def citation_payload(chunk: PolicyChunk, *, score: float) -> dict[str, object]:
    if score < 0:
        raise ValueError("score must be non-negative")
    return {
        "document_id": chunk.document_id,
        "chunk_id": chunk.chunk_id,
        "title": chunk.title,
        "excerpt": chunk.text[:500],
        "start_char": chunk.start_char,
        "end_char": chunk.end_char,
        "score": score,
    }


def validate_citation(payload: dict[str, object]) -> bool:
    required = {"document_id", "chunk_id", "title", "excerpt", "score"}
    return required.issubset(payload) and bool(payload["document_id"]) and bool(payload["chunk_id"])
