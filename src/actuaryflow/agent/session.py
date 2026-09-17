from __future__ import annotations

from dataclasses import dataclass, field

from .memory import ConversationMemory


@dataclass(slots=True)
class SessionStore:
    max_messages: int = 12
    _sessions: dict[str, ConversationMemory] = field(default_factory=dict)

    def get(self, session_id: str) -> ConversationMemory:
        if session_id not in self._sessions:
            self._sessions[session_id] = ConversationMemory(max_messages=self.max_messages)
        return self._sessions[session_id]

    def delete(self, session_id: str) -> bool:
        return self._sessions.pop(session_id, None) is not None
