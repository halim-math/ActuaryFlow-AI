from actuaryflow.governance.review import ReviewCase, ReviewDecision, ReviewStatus


def test_review_case_resolves_with_reviewer_record() -> None:
    case = ReviewCase(request_id="r1", reason="ambiguity", evidence=[], calculations=[])
    case.resolve(reviewer="qualified-reviewer", decision=ReviewDecision.MODIFY, notes="Adjusted rationale")
    assert case.status is ReviewStatus.RESOLVED
    assert case.reviewer == "qualified-reviewer"
    assert case.decision is ReviewDecision.MODIFY
