import pytest

from actuaryflow.actuarial.reinsurance import apply_treaty, excess_of_loss


def test_excess_of_loss_layer() -> None:
    result = excess_of_loss(loss=900_000, retention=250_000, limit=500_000)
    assert result["ceded"] == pytest.approx(500_000)
    assert result["retained"] == pytest.approx(400_000)


def test_treaty_aggregates() -> None:
    result = apply_treaty([100_000, 400_000], retention=200_000, limit=150_000)
    assert result["gross"] == pytest.approx(500_000)
    assert result["ceded"] == pytest.approx(150_000)
