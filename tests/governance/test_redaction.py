from actuaryflow.governance.redaction import redact_mapping, redact_text


def test_email_and_long_number_are_redacted() -> None:
    result = redact_text("mail a@example.com ref 123456789")
    assert "a@example.com" not in result
    assert "123456789" not in result


def test_secret_key_is_redacted() -> None:
    result = redact_mapping({"api_key": "secret-value", "event": "ok"})
    assert result["api_key"] == "[REDACTED_SECRET]"
