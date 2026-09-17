from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(frozen=True, slots=True)
class ProvenanceRecord:
    source_id: str
    source_type: str
    version: str
    content_hash: str
    retrieved_at: str

    @classmethod
    def now(cls, *, source_id: str, source_type: str, version: str, content_hash: str) -> "ProvenanceRecord":
        return cls(
            source_id=source_id,
            source_type=source_type,
            version=version,
            content_hash=content_hash,
            retrieved_at=datetime.now(UTC).isoformat(),
        )
