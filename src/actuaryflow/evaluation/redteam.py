from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RedTeamCase:
    case_id: str
    attack: str
    expected_control: str


def score_control_activation(cases: list[RedTeamCase], activated: dict[str, set[str]]) -> dict[str, float]:
    if not cases:
        return {"cases": 0.0, "activation_rate": 0.0}
    hits = 0
    for case in cases:
        hits += int(case.expected_control in activated.get(case.case_id, set()))
    return {"cases": float(len(cases)), "activation_rate": hits / len(cases)}
