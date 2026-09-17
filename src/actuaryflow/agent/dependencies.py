from __future__ import annotations

from .llm import DeterministicLLMClient, OpenAIResponsesClient
from .memory import ConversationMemory
from .router import DecisionRouter
from .service import AgentService, Retriever


def build_service(*, retriever: Retriever, live_llm: bool = False) -> AgentService:
    llm = OpenAIResponsesClient() if live_llm else DeterministicLLMClient()
    return AgentService(
        llm=llm,
        retriever=retriever,
        memory=ConversationMemory(max_messages=12),
        router=DecisionRouter(),
    )
