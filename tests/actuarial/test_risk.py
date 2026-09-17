import pytest

from actuaryflow.actuarial.risk import combined_ratio, loss_ratio, pure_premium


def test_loss_ratio() -> None:
    assert loss_ratio(incurred_losses=750, earned_premium=1000) == pytest.approx(0.75)


def test_pure_premium() -> None:
    assert pure_premium(aggregate_losses=5000, exposure_units=100) == pytest.approx(50)


def test_combined_ratio() -> None:
    assert combined_ratio(loss_ratio_value=0.7, expense_ratio=0.25) == pytest.approx(0.95)
