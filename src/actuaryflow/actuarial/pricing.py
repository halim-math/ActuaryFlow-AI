from __future__ import annotations


def expected_loss_cost(*, frequency: float, severity: float) -> float:
    if frequency < 0 or severity < 0:
        raise ValueError("frequency and severity must be non-negative")
    return frequency * severity


def indicated_premium(
    *,
    expected_loss: float,
    fixed_expense: float = 0.0,
    variable_expense_ratio: float = 0.0,
    profit_contingency_ratio: float = 0.0,
) -> float:
    if expected_loss < 0 or fixed_expense < 0:
        raise ValueError("loss and fixed expense must be non-negative")
    denominator = 1.0 - variable_expense_ratio - profit_contingency_ratio
    if denominator <= 0:
        raise ValueError("expense and profit ratios must sum to less than 1")
    return (expected_loss + fixed_expense) / denominator
