from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class ToolPolicy:
    allowed_tools: frozenset[str]
    max_numeric_magnitude: float = 1e12

    def validate(self, name: str, arguments: dict[str, Any]) -> None:
        if name not in self.allowed_tools:
            raise PermissionError(f"Tool is not allowed: {name}")
        for key, value in arguments.items():
            if isinstance(value, (int, float)) and abs(float(value)) > self.max_numeric_magnitude:
                raise ValueError(f"Argument {key} exceeds configured magnitude bound")


DEFAULT_TOOL_POLICY = ToolPolicy(
    allowed_tools=frozenset(
        {
            "expected_loss_cost",
            "indicated_premium",
            "loss_ratio",
            "pure_premium",
            "combined_ratio",
            "chain_ladder",
            "excess_of_loss",
        }
    )
)
