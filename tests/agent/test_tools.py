from actuaryflow.agent.tools import ToolDefinition, ToolRegistry


def test_registry_executes_registered_tool() -> None:
    registry = ToolRegistry()
    registry.register(ToolDefinition("double", "double x", lambda payload: {"value": payload["x"] * 2}))
    result = registry.execute("double", {"x": 4})
    assert result["result"]["value"] == 8


def test_registry_rejects_duplicate_name() -> None:
    registry = ToolRegistry()
    tool = ToolDefinition("t", "test", lambda payload: payload)
    registry.register(tool)
    try:
        registry.register(tool)
    except ValueError:
        pass
    else:
        raise AssertionError("expected duplicate registration failure")
