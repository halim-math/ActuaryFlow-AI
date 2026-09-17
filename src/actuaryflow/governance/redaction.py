from __future__ import annotations

import re


_EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
_LONG_NUMBER = re.compile(r"\b\d{8,}\b")


def redact_text(text: str) -> str:
    value = _EMAIL.sub("[REDACTED_EMAIL]", text)
    value = _LONG_NUMBER.sub("[REDACTED_NUMBER]", value)
    return value


def redact_mapping(payload: dict[str, object]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in payload.items():
        if key.lower() in {"password", "secret", "token", "api_key"}:
            result[key] = "[REDACTED_SECRET]"
        elif isinstance(value, str):
            result[key] = redact_text(value)
        else:
            result[key] = value
    return result
