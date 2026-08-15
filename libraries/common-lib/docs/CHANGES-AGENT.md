# CommonLib 2.0 — downstream Agent migration guide

## Compatibility

**Breaking change** from 1.0.0.

## Old contract

```text
parse_record(text: str, strict: bool = false) -> Record | None
Configuration: legacy_mode: bool
```

When `strict=false`, parse failure returned `None`; `strict=true` raised `ParseError`.

## New contract

```text
parse_record(text: str, mode: "strict" | "lenient" = "strict") -> ParseResult
```

`ParseResult.value` is `Record | null`; `ParseResult.errors` is `list[ParseIssue]`. Parse failure is represented in `errors`; `parse_record` no longer returns `None`. The `legacy_mode` configuration key is removed.

## Required migration actions

1. Replace `strict=false` with `mode="lenient"` where lenient behavior is required.
2. Remove `legacy_mode` configuration.
3. Replace `result is None` checks with handling of `result.errors` and `result.value`.
4. Add or update project-local tests for both strict and lenient modes.
5. Verify the old `legacy_mode` key no longer remains in the consuming project.

## Verification

Inspect the consuming project's real dependency declaration and actual parser call sites. Do not assume every consumer needs the same project-specific changes. Run or mechanically inspect target-local tests and record project-specific acceptance separately.
