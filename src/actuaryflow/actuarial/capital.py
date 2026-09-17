from __future__ import annotations


def value_at_risk(samples: list[float], quantile: float = 0.995) -> float:
    if not samples or not 0 < quantile < 1:
        raise ValueError("non-empty samples and quantile in (0,1) required")
    ordered = sorted(samples)
    index = min(len(ordered) - 1, max(0, int(quantile * len(ordered))))
    return ordered[index]


def tail_value_at_risk(samples: list[float], quantile: float = 0.995) -> float:
    threshold = value_at_risk(samples, quantile)
    tail = [x for x in samples if x >= threshold]
    return sum(tail) / len(tail)


def capital_over_mean(samples: list[float], quantile: float = 0.995) -> float:
    mean = sum(samples) / len(samples)
    return max(0.0, value_at_risk(samples, quantile) - mean)
