from __future__ import annotations


def loss_ratio(*, incurred_losses: float, earned_premium: float) -> float:
    if earned_premium <= 0:
        raise ValueError("earned_premium must be positive")
    return incurred_losses / earned_premium


def pure_premium(*, aggregate_losses: float, exposure_units: float) -> float:
    if exposure_units <= 0:
        raise ValueError("exposure_units must be positive")
    return aggregate_losses / exposure_units


def combined_ratio(*, loss_ratio_value: float, expense_ratio: float) -> float:
    if loss_ratio_value < 0 or expense_ratio < 0:
        raise ValueError("ratios must be non-negative")
    return loss_ratio_value + expense_ratio
