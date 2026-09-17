import pytest

from actuaryflow.actuarial.credibility import credibility_blend, limited_fluctuation_weight


def test_weight_is_capped_at_one() -> None:
    assert limited_fluctuation_weight(observed_claims=100000) == 1.0


def test_credibility_blend() -> None:
    assert credibility_blend(experience=120.0, manual=100.0, weight=0.25) == pytest.approx(105.0)
