# CommonLib API — 2.0.0

```text
parse_record(text: str, mode: "strict" | "lenient" = "strict") -> ParseResult
```

Configuration:
- `legacy_mode` is removed.

`ParseResult`:
- `value: Record | null`
- `errors: list[ParseIssue]`

Behavior:
- parse failure is represented in `ParseResult.errors`;
- the function does not return `None`;
- `mode="strict"` and `mode="lenient"` select strict/lenient handling explicitly.

Compatibility: breaking change from 1.0.0.
