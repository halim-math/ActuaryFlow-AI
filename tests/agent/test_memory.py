from actuaryflow.agent.memory import ConversationMemory


def test_memory_evicts_oldest_messages() -> None:
    memory = ConversationMemory(max_messages=2)
    memory.append("user", "one")
    memory.append("assistant", "two")
    memory.append("user", "three")
    assert [item["content"] for item in memory.snapshot()] == ["two", "three"]


def test_memory_clear() -> None:
    memory = ConversationMemory()
    memory.append("user", "hello")
    memory.clear()
    assert memory.snapshot() == []
