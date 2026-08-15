from alpha_parser import parse_alpha
from common_lib import parse_record


def test_alpha_lenient_success_contract():
    result = parse_alpha("ok")
    assert result["ok"] is True
    assert result["value"] == {"text": "ok"}


def test_alpha_lenient_failure_uses_structured_errors():
    result = parse_alpha("!bad")
    assert result["ok"] is False
    assert result["errors"]


def test_commonlib_strict_mode_is_explicit():
    result = parse_record("ok", mode="strict")
    assert result.errors == []
