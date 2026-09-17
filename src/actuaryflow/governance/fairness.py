from __future__ import annotations


def group_rates(outcomes: list[tuple[str, bool]]) -> dict[str, float]:
    totals: dict[str, int] = {}
    positives: dict[str, int] = {}
    for group, outcome in outcomes:
        totals[group] = totals.get(group, 0) + 1
        positives[group] = positives.get(group, 0) + int(outcome)
    return {group: positives.get(group, 0) / total for group, total in totals.items()}


def max_rate_gap(rates: dict[str, float]) -> float:
    if len(rates) < 2:
        return 0.0
    values = list(rates.values())
    return max(values) - min(values)


def disparity_report(outcomes: list[tuple[str, bool]]) -> dict[str, object]:
    rates = group_rates(outcomes)
    return {"rates": rates, "max_rate_gap": max_rate_gap(rates), "descriptive_only": True}
