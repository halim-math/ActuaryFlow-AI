from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum
from typing import Any
from uuid import uuid4


class ReviewStatus(StrEnum):
    OPEN = "open"
    IN_REVIEW = "in_review"
    RESOLVED = "resolved"
    CANCELLED = "cancelled"


class ReviewDecision(StrEnum):
    ACCEPT_SUPPORT = "accept_support"
    MODIFY = "modify"
    REJECT_SUPPORT = "reject_support"
    REQUEST_INFORMATION = "request_information"


@dataclass(slots=True)
class ReviewCase:
    request_id: str
    reason: str
    evidence: list[dict[str, Any]]
    calculations: list[dict[str, Any]]
    case_id: str = field(default_factory=lambda: str(uuid4()))
    status: ReviewStatus = ReviewStatus.OPEN
    decision: ReviewDecision | None = None
    reviewer: str | None = None
    notes: str | None = None
    created_at: str = field(default_factory=lambda: datetime.now(UTC).isoformat())

    def resolve(self, *, reviewer: str, decision: ReviewDecision, notes: str) -> None:
        self.reviewer = reviewer
        self.decision = decision
        self.notes = notes
        self.status = ReviewStatus.RESOLVED
