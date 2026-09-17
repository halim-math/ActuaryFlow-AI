from __future__ import annotations

import random


def simulate_compound_poisson(
    *,
    frequency: float,
    mean_severity: float,
    simulations: int = 10000,
    seed: int = 11711,
) -> list[float]:
    if frequency < 0 or mean_severity < 0 or simulations <= 0:
        raise ValueError("invalid simulation inputs")
    rng = random.Random(seed)
    totals: list[float] = []
    for _ in range(simulations):
        # Knuth Poisson sampler keeps this module dependency-free for research baselines.
        threshold = pow(2.718281828459045, -frequency)
        product = 1.0
        count = 0
        while product > threshold:
            count += 1
            product *= rng.random()
        claim_count = max(0, count - 1)
        aggregate = sum(rng.expovariate(1.0 / mean_severity) for _ in range(claim_count)) if mean_severity > 0 else 0.0
        totals.append(aggregate)
    return totals


def empirical_var(samples: list[float], quantile: float = 0.995) -> float:
    if not samples or not 0 < quantile < 1:
        raise ValueError("samples required and quantile must lie in (0,1)")
    ordered = sorted(samples)
    index = min(len(ordered) - 1, int(quantile * len(ordered)))
    return ordered[index]
