from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class GovernancePolicy:
    mandatory_review_flags: frozenset[str] = field(
        default_factory=lambda: frozenset(
            {
                "coverage_ambiguity",
                "low_retrieval_confidence",
                "missing_evidence",
                "material_financial_impact",
                "sensitive_attribute_detected",
                "suspected_fraud",
                "tool_failure",
                "policy_conflict",
            }
        )
    )
    material_amount_threshold: float = 50_000.0

    def requires_review(self, flags: set[str], *, amount: float | None = None) -> tuple[bool, list[str]]:
        reasons = sorted(flags & self.mandatory_review_flags)
        if amount is not None and amount >= self.material_amount_threshold:
            reasons.append("material_financial_impact")
        return bool(reasons), sorted(set(reasons))
