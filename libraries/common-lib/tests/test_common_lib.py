from common_lib import parse_record


def test_v2_lenient_failure_returns_structured_errors():
    result = parse_record("!bad", mode="lenient")
    assert result.value is None
    assert result.errors


def test_v2_strict_success_is_structured_result():
    result = parse_record("ok", mode="strict")
    assert result.value == {"text": "ok"}
    assert result.errors == []


def test_v2_never_returns_none():
    assert parse_record("!bad", mode="lenient") is not None
