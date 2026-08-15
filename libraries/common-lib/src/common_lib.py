class ParseError(Exception):
    pass


def parse_record(text: str, strict: bool = False):
    if not text or text.startswith("!"):
        if strict:
            raise ParseError("invalid record")
        return None
    return {"text": text}
