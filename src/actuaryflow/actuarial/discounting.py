from __future__ import annotations


def present_value(*, amount: float, annual_rate: float, years: float) -> float:
    if annual_rate <= -1:
        raise ValueError("annual_rate must exceed -100%")
    if years < 0:
        raise ValueError("years must be non-negative")
    return amount / ((1.0 + annual_rate) ** years)


def discounted_cashflows(cashflows: list[tuple[float, float]], *, annual_rate: float) -> float:
    return sum(present_value(amount=amount, annual_rate=annual_rate, years=years) for years, amount in cashflows)
