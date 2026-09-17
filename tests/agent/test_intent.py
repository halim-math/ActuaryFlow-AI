from actuaryflow.agent.intent import Intent, classify_intent


def test_reserving_intent() -> None:
    assert classify_intent("Estimate IBNR using development factors") is Intent.RESERVING_SUPPORT


def test_policy_intent() -> None:
    assert classify_intent("Is fire covered under this policy?") is Intent.POLICY_QUESTION


def test_unknown_intent() -> None:
    assert classify_intent("hello there") is Intent.UNKNOWN
