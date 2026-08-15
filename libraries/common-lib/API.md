# CommonLib API — 1.0.0

```text
parse_record(text: str, strict: bool = false) -> Record | None
```

Configuration:
- `legacy_mode: bool`

Behavior:
- returns `None` on parse failure when `strict=false`
- raises `ParseError` when `strict=true`
