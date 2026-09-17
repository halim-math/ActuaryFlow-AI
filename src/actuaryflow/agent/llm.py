from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class LLMClient(Protocol):
    def complete(self, *, system: str, user: str) -> str: ...


@dataclass(slots=True)
class OpenAIResponsesClient:
    model: str = "gpt-5.6"

    def complete(self, *, system: str, user: str) -> str:
        from openai import OpenAI

        client = OpenAI()
        response = client.responses.create(
            model=self.model,
            instructions=system,
            input=user,
        )
        return response.output_text


@dataclass(slots=True)
class DeterministicLLMClient:
    """Offline deterministic adapter for tests and demonstrations."""

    prefix: str = "Decision-support summary"

    def complete(self, *, system: str, user: str) -> str:
        del system
        return f"{self.prefix}: {user[:800]}"
