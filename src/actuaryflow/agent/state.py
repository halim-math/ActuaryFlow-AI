from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any
from uuid import uuid4


class AgentStatus(StrEnum):
    RECEIVED = "received"
    CONTEXTUALIZING = "contextualizing"
    RETRIEVING = "retrieving"
    CALCULATING = "calculating"
    ROUTING = "routing"
    NEEDS_REVIEW = "needs_review"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass(slots=True)
class AgentState:
    request_id: str = field(default_factory=lambda: str(uuid4()))
    user_message: str = ""
    status: AgentStatus = AgentStatus.RECEIVED
    memory: list[dict[str, str]] = field(default_factory=list)
    evidence: list[dict[str, Any]] = field(default_factory=list)
    tool_results: list[dict[str, Any]] = field(default_factory=list)
    risk_flags: set[str] = field(default_factory=set)
    trace: list[str] = field(default_factory=list)

    def transition(self, status: AgentStatus, note: str) -> None:
        self.status = status
        self.trace.append(f"{status.value}: {note}")

    def add_risk_flag(self, flag: str) -> None:
        self.risk_flags.add(flag)
        self.trace.append(f"risk_flag: {flag}")
