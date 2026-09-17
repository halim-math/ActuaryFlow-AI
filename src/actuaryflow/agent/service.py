from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol

from .llm import LLMClient
from .memory import ConversationMemory
from .router import DecisionRouter
from .schemas import AgentRequest, AgentResponse, Citation
from .state import AgentState, AgentStatus


class Retriever(Protocol):
    def search(self, query: str, *, k: int = 5) -> list[dict[str, Any]]: ...


SYSTEM_PROMPT = """You are ActuaryFlow-AI, an insurance and actuarial decision-support agent.
Use supplied policy evidence and calculations. Distinguish assumptions from facts. Cite evidence.
Never claim to bind coverage, approve/deny a claim, set a final premium, or replace a qualified
actuary/underwriter. Escalate ambiguity and consequential decisions for human review.
"""


@dataclass(slots=True)
class AgentService:
    llm: LLMClient
    retriever: Retriever
    memory: ConversationMemory
    router: DecisionRouter

    def handle(self, request: AgentRequest) -> AgentResponse:
        state = AgentState(user_message=request.message)
        state.transition(AgentStatus.CONTEXTUALIZING, "Loaded bounded session context")
        state.memory = self.memory.snapshot()

        state.transition(AgentStatus.RETRIEVING, "Searching policy knowledge base")
        evidence = self.retriever.search(request.message, k=5)
        state.evidence.extend(evidence)
        if not evidence or max(float(x.get("score", 0.0)) for x in evidence) < 0.35:
            state.add_risk_flag("low_retrieval_confidence")

        evidence_text = "\n\n".join(
            f"[{x.get('title', 'Policy')}] {x.get('text', '')}" for x in evidence
        )
        prompt = (
            f"User request:\n{request.message}\n\n"
            f"Policy evidence:\n{evidence_text or 'No evidence retrieved.'}\n\n"
            "Produce a concise, auditable decision-support response."
        )
        answer = self.llm.complete(system=SYSTEM_PROMPT, user=prompt)

        state.transition(AgentStatus.ROUTING, "Applying deterministic escalation policy")
        route = self.router.route(state)
        final_status = AgentStatus.NEEDS_REVIEW if route.review_required else AgentStatus.COMPLETED
        state.transition(final_status, route.reason)

        self.memory.append("user", request.message)
        self.memory.append("assistant", answer)

        citations = [
            Citation(
                document_id=str(x.get("document_id", "unknown")),
                chunk_id=str(x.get("chunk_id", "unknown")),
                title=str(x.get("title", "Policy evidence")),
                excerpt=str(x.get("text", ""))[:500],
                score=float(x.get("score", 0.0)),
            )
            for x in evidence
        ]
        return AgentResponse(
            request_id=state.request_id,
            status=state.status.value,
            answer=answer,
            citations=citations,
            calculations=state.tool_results,
            risk_flags=sorted(state.risk_flags),
            review_required=route.review_required,
            review_reason=route.reason if route.review_required else None,
        )
