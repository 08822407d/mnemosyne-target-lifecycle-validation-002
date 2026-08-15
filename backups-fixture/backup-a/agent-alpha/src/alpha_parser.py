from common_lib import parse_record

LEGACY_CONFIG = {"legacy_mode": True}


def parse_alpha(text: str):
    result = parse_record(text, strict=False)
    if result is None:
        return {"ok": False, "value": None}
    return {"ok": True, "value": result}
