from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from typing import Any


@dataclass(frozen=True, slots=True)
class AuditEvent:
    request_id: str
    event_type: str
    payload: dict[str, Any]
    timestamp: str
    previous_hash: str | None = None

    @classmethod
    def create(
        cls,
        *,
        request_id: str,
        event_type: str,
        payload: dict[str, Any],
        previous_hash: str | None = None,
    ) -> "AuditEvent":
        return cls(request_id, event_type, payload, datetime.now(UTC).isoformat(), previous_hash)

    def digest(self) -> str:
        raw = json.dumps(asdict(self), sort_keys=True, separators=(",", ":"), default=str)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()
