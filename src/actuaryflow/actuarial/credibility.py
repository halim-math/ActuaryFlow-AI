from __future__ import annotations

import math


def full_credibility_standard(*, confidence_z: float = 1.96, relative_error: float = 0.05) -> float:
    if confidence_z <= 0 or relative_error <= 0:
        raise ValueError("confidence_z and relative_error must be positive")
    return (confidence_z / relative_error) ** 2


def limited_fluctuation_weight(
    *,
    observed_claims: float,
    confidence_z: float = 1.96,
    relative_error: float = 0.05,
) -> float:
    if observed_claims < 0:
        raise ValueError("observed_claims must be non-negative")
    standard = full_credibility_standard(
        confidence_z=confidence_z,
        relative_error=relative_error,
    )
    if standard == 0:
        return 1.0
    return min(1.0, math.sqrt(observed_claims / standard))


def credibility_blend(*, experience: float, manual: float, weight: float) -> float:
    if not 0 <= weight <= 1:
        raise ValueError("weight must be between 0 and 1")
    return weight * experience + (1.0 - weight) * manual
