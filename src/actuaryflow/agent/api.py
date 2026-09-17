from __future__ import annotations

from fastapi import FastAPI

from .llm import DeterministicLLMClient
from .memory import ConversationMemory
from .router import DecisionRouter
from .schemas import AgentRequest, AgentResponse
from .service import AgentService


class EmptyRetriever:
    def search(self, query: str, *, k: int = 5) -> list[dict[str, object]]:
        del query, k
        return []


app = FastAPI(
    title="ActuaryFlow-AI",
    version="0.1.0",
    description="Human-governed actuarial and insurance decision-support API",
)

service = AgentService(
    llm=DeterministicLLMClient(),
    retriever=EmptyRetriever(),
    memory=ConversationMemory(),
    router=DecisionRouter(),
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/agent/run", response_model=AgentResponse)
def run_agent(request: AgentRequest) -> AgentResponse:
    return service.handle(request)
