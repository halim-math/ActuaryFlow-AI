class ActuaryFlowError(Exception):
    """Base exception for controlled workflow failures."""


class RetrievalError(ActuaryFlowError):
    pass


class ToolExecutionError(ActuaryFlowError):
    pass


class PolicyViolationError(ActuaryFlowError):
    pass


class HumanReviewRequired(ActuaryFlowError):
    pass
