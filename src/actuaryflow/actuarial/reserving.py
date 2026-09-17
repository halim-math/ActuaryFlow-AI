from __future__ import annotations


def development_factors(cumulative_triangle: list[list[float | None]]) -> list[float]:
    if not cumulative_triangle:
        return []
    width = max(len(row) for row in cumulative_triangle)
    factors: list[float] = []
    for age in range(width - 1):
        numerator = 0.0
        denominator = 0.0
        for row in cumulative_triangle:
            if age + 1 >= len(row):
                continue
            current, nxt = row[age], row[age + 1]
            if current is None or nxt is None:
                continue
            denominator += current
            numerator += nxt
        if denominator <= 0:
            raise ValueError(f"Cannot estimate factor at development age {age}")
        factors.append(numerator / denominator)
    return factors


def chain_ladder(cumulative_triangle: list[list[float | None]]) -> list[dict[str, float]]:
    factors = development_factors(cumulative_triangle)
    results: list[dict[str, float]] = []
    for accident_year, row in enumerate(cumulative_triangle):
        observed = [(i, value) for i, value in enumerate(row) if value is not None]
        if not observed:
            continue
        latest_age, latest = observed[-1]
        assert latest is not None
        cdf = 1.0
        for factor in factors[latest_age:]:
            cdf *= factor
        ultimate = latest * cdf
        results.append({
            "accident_year_index": float(accident_year),
            "latest": float(latest),
            "cdf": cdf,
            "ultimate": ultimate,
            "ibnr": ultimate - latest,
        })
    return results
