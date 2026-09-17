from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class PolicyDocument:
    document_id: str
    title: str
    text: str
    source_uri: str | None = None
    effective_date: str | None = None
    jurisdiction: str | None = None
    product_line: str | None = None
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class PolicyChunk:
    document_id: str
    chunk_id: str
    title: str
    text: str
    start_char: int
    end_char: int
    metadata: dict[str, str] = field(default_factory=dict)
