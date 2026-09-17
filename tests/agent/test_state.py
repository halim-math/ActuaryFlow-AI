from actuaryflow.agent.state import AgentState, AgentStatus


def test_state_transition_records_trace() -> None:
    state = AgentState(user_message="hello")
    state.transition(AgentStatus.RETRIEVING, "searching")
    assert state.status is AgentStatus.RETRIEVING
    assert state.trace[-1] == "retrieving: searching"


def test_risk_flags_are_deduplicated() -> None:
    state = AgentState()
    state.add_risk_flag("missing_evidence")
    state.add_risk_flag("missing_evidence")
    assert state.risk_flags == {"missing_evidence"}
