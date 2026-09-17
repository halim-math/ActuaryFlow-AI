from __future__ import annotations


def mean_absolute_error(actual: list[float], predicted: list[float]) -> float:
    if len(actual) != len(predicted) or not actual:
        raise ValueError("actual and predicted must be non-empty and equal length")
    return sum(abs(a - p) for a, p in zip(actual, predicted, strict=True)) / len(actual)


def mean_bias(actual: list[float], predicted: list[float]) -> float:
    if len(actual) != len(predicted) or not actual:
        raise ValueError("actual and predicted must be non-empty and equal length")
    return sum(p - a for a, p in zip(actual, predicted, strict=True)) / len(actual)


def calibration_ratio(actual: list[float], predicted: list[float]) -> float:
    denominator = sum(predicted)
    if denominator == 0:
        raise ValueError("predicted aggregate cannot be zero")
    return sum(actual) / denominator
