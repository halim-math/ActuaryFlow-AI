from __future__ import annotations


def claim_frequency(*, claim_count: float, exposure: float) -> float:
    if claim_count < 0:
        raise ValueError("claim_count must be non-negative")
    if exposure <= 0:
        raise ValueError("exposure must be positive")
    return claim_count / exposure


def exposure_weighted_frequency(observations: list[tuple[float, float]]) -> float:
    claims = sum(count for count, _ in observations)
    exposure = sum(exp for _, exp in observations)
    return claim_frequency(claim_count=claims, exposure=exposure)
