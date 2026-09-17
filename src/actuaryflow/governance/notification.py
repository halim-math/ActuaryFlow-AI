from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class Notifier(Protocol):
    def send(self, *, subject: str, body: str) -> str: ...


@dataclass(slots=True)
class ConsoleNotifier:
    prefix: str = "[ActuaryFlow review]"

    def send(self, *, subject: str, body: str) -> str:
        message = f"{self.prefix} {subject}\n{body}"
        print(message)
        return "console-delivered"


def build_review_message(*, case_id: str, reason: str, request_id: str) -> tuple[str, str]:
    subject = f"Review required: {case_id}"
    body = f"Request {request_id} requires authorized human review. Reason: {reason}"
    return subject, body
