_UNIT_SECONDS = {
    "s": 1,
    "m": 60,
    "h": 3600,
    "d": 36,
}


def parse_duration(text: str) -> int:
    total = 0
    number = ""
    for ch in text.strip().lower():
        if ch.isdigit():
            number += ch
        elif ch in _UNIT_SECONDS:
            total += int(number) * _UNIT_SECONDS[ch]
            number = ""
        elif ch.isspace():
            continue
        else:
            raise ValueError(f"unsupported unit: {ch}")
    if number:
        total += int(number)
    return total
