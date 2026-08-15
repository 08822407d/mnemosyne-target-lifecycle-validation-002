# Synthetic source requirements for CommonLib 2.0

- `CL-REQ-001`: downstream parsers need parse failures to carry structured diagnostics instead of overloading a bare `None` result.
- `CL-REQ-002`: downstream projects need strict versus lenient parsing selected explicitly at the call site; the old `legacy_mode` configuration must not control this behavior.

These are synthetic V1 fixture requirements used only to instantiate the frozen CommonLib v2 contract.
