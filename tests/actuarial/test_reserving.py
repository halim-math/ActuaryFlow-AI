import pytest

from actuaryflow.actuarial.reserving import chain_ladder, development_factors


def test_development_factors() -> None:
    triangle = [[100.0, 150.0, 180.0], [120.0, 180.0, None], [140.0, None, None]]
    factors = development_factors(triangle)
    assert factors[0] == pytest.approx(1.5)
    assert factors[1] == pytest.approx(1.2)


def test_chain_ladder_produces_ibnr() -> None:
    triangle = [[100.0, 150.0, 180.0], [120.0, 180.0, None], [140.0, None, None]]
    results = chain_ladder(triangle)
    assert results[-1]["ultimate"] == pytest.approx(252.0)
    assert results[-1]["ibnr"] == pytest.approx(112.0)
