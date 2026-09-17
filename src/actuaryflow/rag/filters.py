from __future__ import annotations

from .document import PolicyChunk


def filter_chunks(
    chunks: list[PolicyChunk],
    *,
    jurisdiction: str | None = None,
    product_line: str | None = None,
) -> list[PolicyChunk]:
    result: list[PolicyChunk] = []
    for chunk in chunks:
        if jurisdiction is not None and chunk.metadata.get("jurisdiction") != jurisdiction:
            continue
        if product_line is not None and chunk.metadata.get("product_line") != product_line:
            continue
        result.append(chunk)
    return result
