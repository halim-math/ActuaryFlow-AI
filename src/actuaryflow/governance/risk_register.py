from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class Severity(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True, slots=True)
class RiskItem:
    risk_id: str
    title: str
    severity: Severity
    control: str
    owner: str
    residual_risk: str


DEFAULT_RISKS = [
    RiskItem("RAG-01", "Wrong policy version retrieved", Severity.HIGH, "version metadata filters + citation", "RAG owner", "medium"),
    RiskItem("LLM-01", "Hallucinated policy statement", Severity.HIGH, "grounding + abstention + review", "AI owner", "medium"),
    RiskItem("TOOL-01", "Incorrect tool inputs", Severity.HIGH, "schema validation + audit log", "Actuarial owner", "medium"),
    RiskItem("SEC-01", "Prompt injection in retrieved text", Severity.HIGH, "treat documents as data + red-team tests", "Security owner", "medium"),
]
