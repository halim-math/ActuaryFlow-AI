from __future__ import annotations

import math


def severity_summary(losses: list[float]) -> dict[str, float]:
    if not losses:
        raise ValueError("losses cannot be empty")
    if any(x < 0 for x in losses):
        raise ValueError("losses must be non-negative")
    ordered = sorted(losses)
    n = len(ordered)
    mean = sum(ordered) / n
    variance = sum((x - mean) ** 2 for x in ordered) / max(n - 1, 1)
    p95 = ordered[min(n - 1, math.ceil(0.95 * n) - 1)]
    return {"count": float(n), "mean": mean, "std": math.sqrt(variance), "p95": p95}
