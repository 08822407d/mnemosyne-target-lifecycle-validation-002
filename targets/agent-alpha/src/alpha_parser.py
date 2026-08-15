from common_lib import parse_record


def parse_alpha(text: str):
    result = parse_record(text, mode="lenient")
    if result.errors:
        return {"ok": False, "value": result.value, "errors": result.errors}
    return {"ok": True, "value": result.value, "errors": []}
