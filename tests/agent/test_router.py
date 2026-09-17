from actuaryflow.agent.router import DecisionRouter
from actuaryflow.agent.state import AgentState


def test_router_escalates_low_confidence() -> None:
    state = AgentState(user_message="Is this loss covered?")
    state.add_risk_flag("low_retrieval_confidence")

    decision = DecisionRouter().route(state)

    assert decision.review_required is True
    assert decision.action == "human_review"


def test_router_allows_support_response_without_flags() -> None:
    decision = DecisionRouter().route(AgentState(user_message="Explain loss ratio"))
    assert decision.review_required is False
