from __future__ import annotations

from .document import PolicyChunk, PolicyDocument


def split_document(
    document: PolicyDocument,
    *,
    chunk_size: int = 1200,
    overlap: int = 180,
) -> list[PolicyChunk]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must satisfy 0 <= overlap < chunk_size")

    chunks: list[PolicyChunk] = []
    step = chunk_size - overlap
    for index, start in enumerate(range(0, len(document.text), step)):
        end = min(start + chunk_size, len(document.text))
        text = document.text[start:end].strip()
        if not text:
            continue
        chunks.append(
            PolicyChunk(
                document_id=document.document_id,
                chunk_id=f"{document.document_id}:{index}",
                title=document.title,
                text=text,
                start_char=start,
                end_char=end,
                metadata={**document.metadata},
            )
        )
        if end == len(document.text):
            break
    return chunks
