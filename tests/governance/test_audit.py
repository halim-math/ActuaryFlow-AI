from actuaryflow.governance.audit import AuditEvent


def test_audit_digest_is_stable_for_event() -> None:
    event = AuditEvent("r1", "retrieval", {"chunks": ["p:1"]}, "2026-01-01T00:00:00+00:00")
    assert event.digest() == event.digest()


def test_audit_digest_changes_with_payload() -> None:
    a = AuditEvent("r1", "tool", {"value": 1}, "2026-01-01T00:00:00+00:00")
    b = AuditEvent("r1", "tool", {"value": 2}, "2026-01-01T00:00:00+00:00")
    assert a.digest() != b.digest()
