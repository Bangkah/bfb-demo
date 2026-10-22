def flatten(data: dict, prefix: str = "") -> dict:
    out = {}
    for key, value in data.items():
        if isinstance(value, dict):
            out.update(flatten(value, prefix))
        else:
            out[f"{prefix}{key}"] = value
    return out
