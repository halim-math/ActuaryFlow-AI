from __future__ import annotations

from collections.abc import Callable
from typing import Any

from .pricing import expected_loss_cost, indicated_premium
from .risk import combined_ratio, loss_ratio, pure_premium


Calculator = Callable[..., float]


CALCULATORS: dict[str, Calculator] = {
    "expected_loss_cost": expected_loss_cost,
    "indicated_premium": indicated_premium,
    "loss_ratio": loss_ratio,
    "pure_premium": pure_premium,
    "combined_ratio": combined_ratio,
}


def run_calculator(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    if name not in CALCULATORS:
        raise KeyError(f"Unsupported calculator: {name}")
    value = CALCULATORS[name](**arguments)
    return {"calculator": name, "arguments": arguments, "value": value}
