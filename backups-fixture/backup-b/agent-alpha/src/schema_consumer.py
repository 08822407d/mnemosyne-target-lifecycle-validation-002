SCHEMA_VERSION = 1


def schema_label(record_id: str) -> str:
    return f"v{SCHEMA_VERSION}:{record_id}"
