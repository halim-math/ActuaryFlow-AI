from __future__ import annotations


def excess_of_loss(*, loss: float, retention: float, limit: float) -> dict[str, float]:
    if min(loss, retention, limit) < 0:
        raise ValueError("loss, retention and limit must be non-negative")
    ceded = min(max(loss - retention, 0.0), limit)
    retained = loss - ceded
    return {"gross": loss, "ceded": ceded, "retained": retained}


def apply_treaty(losses: list[float], *, retention: float, limit: float) -> dict[str, float]:
    transformed = [excess_of_loss(loss=x, retention=retention, limit=limit) for x in losses]
    return {
        "gross": sum(x["gross"] for x in transformed),
        "ceded": sum(x["ceded"] for x in transformed),
        "retained": sum(x["retained"] for x in transformed),
    }
