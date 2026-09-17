from __future__ import annotations

from dataclasses import dataclass

from .intent import Intent


@dataclass(frozen=True, slots=True)
class PlanStep:
    name: str
    required: bool = True


def build_plan(intent: Intent) -> list[PlanStep]:
    base = [PlanStep("load_memory"), PlanStep("policy_retrieval")]
    if intent in {Intent.ACTUARIAL_CALCULATION, Intent.RESERVING_SUPPORT}:
        base.append(PlanStep("actuarial_tool"))
    base.extend([PlanStep("synthesize_evidence"), PlanStep("decision_router"), PlanStep("audit_log")])
    return base
