from __future__ import annotations

import re
from dataclasses import dataclass


_PROMPT_INJECTION = re.compile(
    r"(ignore|override|reveal).{0,40}(instruction|system prompt|policy|developer)",
    flags=re.IGNORECASE | re.DOTALL,
)


@dataclass(frozen=True, slots=True)
class GuardrailResult:
    allowed: bool
    flags: tuple[str, ...]


def inspect_input(text: str) -> GuardrailResult:
    flags: list[str] = []
    if len(text) > 12_000:
        flags.append("input_too_long")
    if _PROMPT_INJECTION.search(text):
        flags.append("prompt_injection_pattern")
    return GuardrailResult(allowed="input_too_long" not in flags, flags=tuple(flags))
