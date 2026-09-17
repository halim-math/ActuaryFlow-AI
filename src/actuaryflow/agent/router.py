from __future__ import annotations

from dataclasses import dataclass

from .state import AgentState


@dataclass(frozen=True, slots=True)
class RouteDecision:
    action: str
    review_required: bool
    reason: str


class DecisionRouter:
    """Routes work without making autonomous consequential insurance decisions."""

    REVIEW_FLAGS = {
        "coverage_ambiguity",
        "low_retrieval_confidence",
        "material_financial_impact",
        "missing_evidence",
        "sensitive_attribute_detected",
        "tool_failure",
    }

    def route(self, state: AgentState) -> RouteDecision:
        matched = sorted(state.risk_flags & self.REVIEW_FLAGS)
        if matched:
            return RouteDecision(
                action="human_review",
                review_required=True,
                reason=f"Escalated because: {', '.join(matched)}",
            )
        return RouteDecision(
            action="respond_with_decision_support",
            review_required=False,
            reason="No configured escalation rule fired.",
        )
