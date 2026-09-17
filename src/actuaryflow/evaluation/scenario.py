from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class Scenario:
    scenario_id: str
    prompt: str
    expected_review: bool
    expected_evidence_ids: tuple[str, ...] = ()
    expected_tools: tuple[str, ...] = ()
    tags: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class ScenarioResult:
    scenario_id: str
    review_required: bool
    evidence_ids: tuple[str, ...]
    tools: tuple[str, ...]
    response: str
    metadata: dict[str, Any] = field(default_factory=dict)
