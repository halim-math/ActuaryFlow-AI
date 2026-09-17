from __future__ import annotations

from typing import Any


SYSTEM = """You are ActuaryFlow-AI. Provide insurance and actuarial decision support only.
Ground factual policy statements in supplied evidence. Clearly mark assumptions and uncertainty.
Never fabricate policy clauses or calculator outputs. Consequential decisions remain with authorized humans.
"""


def build_grounded_prompt(
    *,
    message: str,
    evidence: list[dict[str, Any]],
    calculations: list[dict[str, Any]] | None = None,
) -> str:
    passages = "\n".join(
        f"- {item.get('chunk_id', 'unknown')}: {item.get('text', '')}" for item in evidence
    ) or "- none"
    tools = "\n".join(str(item) for item in calculations or []) or "- none"
    return (
        f"REQUEST\n{message}\n\nEVIDENCE\n{passages}\n\n"
        f"CALCULATIONS\n{tools}\n\n"
        "Answer with: evidence summary, calculation summary, uncertainty, and recommended next human action."
    )
