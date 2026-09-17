import pytest

from actuaryflow.governance.fairness import disparity_report


def test_disparity_report_is_descriptive() -> None:
    report = disparity_report([("A", True), ("A", False), ("B", True), ("B", True)])
    assert report["rates"]["A"] == pytest.approx(0.5)
    assert report["rates"]["B"] == pytest.approx(1.0)
    assert report["max_rate_gap"] == pytest.approx(0.5)
    assert report["descriptive_only"] is True
