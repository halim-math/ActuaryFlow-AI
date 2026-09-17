from __future__ import annotations

import json

from actuaryflow.agent.llm import DeterministicLLMClient
from actuaryflow.agent.memory import ConversationMemory
from actuaryflow.agent.router import DecisionRouter
from actuaryflow.agent.schemas import AgentRequest
from actuaryflow.agent.service import AgentService


class DemoRetriever:
    def search(self, query: str, *, k: int = 5) -> list[dict[str, object]]:
        del query, k
        return [{
            "document_id": "demo-auto",
            "chunk_id": "demo-auto:0",
            "title": "Demo Motor Policy",
            "text": "Accidental physical damage caused by fire is described as covered, subject to terms.",
            "score": 0.82,
        }]


def main() -> None:
    service = AgentService(
        llm=DeterministicLLMClient(),
        retriever=DemoRetriever(),
        memory=ConversationMemory(),
        router=DecisionRouter(),
    )
    response = service.handle(AgentRequest(message="What does the demo wording say about fire damage?"))
    print(json.dumps(response.model_dump(), indent=2))


if __name__ == "__main__":
    main()
