from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RuntimeCounters:
    requests: int = 0
    escalations: int = 0
    retrieval_failures: int = 0
    tool_failures: int = 0
    citation_failures: int = 0

    def escalation_rate(self) -> float:
        return self.escalations / self.requests if self.requests else 0.0

    def failure_rate(self) -> float:
        failures = self.retrieval_failures + self.tool_failures + self.citation_failures
        return failures / self.requests if self.requests else 0.0

    def snapshot(self) -> dict[str, float | int]:
        return {
            "requests": self.requests,
            "escalations": self.escalations,
            "retrieval_failures": self.retrieval_failures,
            "tool_failures": self.tool_failures,
            "citation_failures": self.citation_failures,
            "escalation_rate": self.escalation_rate(),
            "failure_rate": self.failure_rate(),
        }
