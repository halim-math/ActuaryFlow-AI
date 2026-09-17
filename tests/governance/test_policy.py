from actuaryflow.governance.policy import GovernancePolicy


def test_flag_requires_review() -> None:
    required, reasons = GovernancePolicy().requires_review({"missing_evidence"})
    assert required is True
    assert "missing_evidence" in reasons


def test_material_amount_requires_review() -> None:
    required, reasons = GovernancePolicy(material_amount_threshold=1000).requires_review(set(), amount=1500)
    assert required is True
    assert "material_financial_impact" in reasons
