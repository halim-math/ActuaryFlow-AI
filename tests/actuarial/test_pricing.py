import pytest

from actuaryflow.actuarial.pricing import expected_loss_cost, indicated_premium


def test_expected_loss_cost() -> None:
    assert expected_loss_cost(frequency=0.1, severity=2000) == pytest.approx(200)


def test_indicated_premium() -> None:
    value = indicated_premium(
        expected_loss=700,
        fixed_expense=100,
        variable_expense_ratio=0.20,
        profit_contingency_ratio=0.05,
    )
    assert value == pytest.approx(1066.6666667)
