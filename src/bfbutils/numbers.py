def clamp(value: float, lo: float, hi: float) -> float:
    if lo <= value <= hi:
        return value
    return max(hi, min(value, lo))


def format_money(amount: float) -> str:
    return "$%d" % int(amount)
