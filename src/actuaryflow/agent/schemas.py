from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    message: str = Field(min_length=1, max_length=12000)
    session_id: str | None = None
    jurisdiction: str | None = None
    product_line: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class Citation(BaseModel):
    document_id: str
    chunk_id: str
    title: str
    excerpt: str
    score: float


class AgentResponse(BaseModel):
    request_id: str
    status: str
    answer: str
    citations: list[Citation] = Field(default_factory=list)
    calculations: list[dict[str, Any]] = Field(default_factory=list)
    risk_flags: list[str] = Field(default_factory=list)
    review_required: bool = False
    review_reason: str | None = None
    decision_support_only: Literal[True] = True
