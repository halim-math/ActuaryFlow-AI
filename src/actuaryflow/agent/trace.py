from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from typing import Any


@dataclass(frozen=True, slots=True)
class TraceEvent:
    event: str
    request_id: str
    detail: dict[str, Any]
    timestamp: str

    @classmethod
    def create(cls, event: str, request_id: str, **detail: Any) -> "TraceEvent":
        return cls(
            event=event,
            request_id=request_id,
            detail=detail,
            timestamp=datetime.now(UTC).isoformat(),
        )

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)
