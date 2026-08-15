from dataclasses import dataclass


@dataclass(frozen=True)
class ParseIssue:
    message: str


@dataclass(frozen=True)
class ParseResult:
    value: dict | None
    errors: list[ParseIssue]


def parse_record(text: str, mode: str = "strict") -> ParseResult:
    if mode not in {"strict", "lenient"}:
        raise ValueError("mode must be strict or lenient")
    if not text or text.startswith("!"):
        return ParseResult(value=None, errors=[ParseIssue("invalid record")])
    return ParseResult(value={"text": text}, errors=[])
