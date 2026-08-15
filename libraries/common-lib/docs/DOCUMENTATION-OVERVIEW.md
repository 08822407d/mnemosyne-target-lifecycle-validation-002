# CommonLib Documentation Overview — 2.0

- `API.md` — current public interface and behavior contract; read before integration and when checking exact current signatures.
- `docs/CHANGES-HUMAN.md` — concise human-facing release explanation; read for release overview.
- `docs/CHANGES-AGENT.md` — downstream Agent migration/reconstruction information; read before rebuilding or upgrading a consuming project.
- `docs/SOURCE-REQUIREMENTS.md` — exact synthetic source requirements used for the 2.0 design.
- `tests/test_common_lib.py` — executable-style contract examples for strict/lenient and structured-result behavior.

The library documents its own change. Consuming projects decide and perform their own migrations after an explicit project trigger.
