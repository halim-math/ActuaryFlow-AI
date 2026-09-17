from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field


@dataclass(slots=True)
class ConversationMemory:
    max_messages: int = 12
    _items: deque[dict[str, str]] = field(default_factory=deque)

    def append(self, role: str, content: str) -> None:
        self._items.append({"role": role, "content": content})
        while len(self._items) > self.max_messages:
            self._items.popleft()

    def snapshot(self) -> list[dict[str, str]]:
        return list(self._items)

    def clear(self) -> None:
        self._items.clear()
