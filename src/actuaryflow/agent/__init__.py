"""LLM orchestration primitives for ActuaryFlow-AI.

The agent package is intentionally decision-support oriented: it can gather
context, run approved tools, explain calculations, and request human review,
but it does not autonomously approve/deny insurance applications or claims.
"""

from .service import AgentService
from .state import AgentState, AgentStatus

__all__ = ["AgentService", "AgentState", "AgentStatus"]
