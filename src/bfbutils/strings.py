def is_palindrome(text: str) -> bool:
    return text == text[::-1]


def slugify(text: str) -> str:
    text = text.lower().strip()
    out = []
    for ch in text:
        if ch.isalnum():
            out.append(ch)
        elif ch.isspace():
            out.append(ch)
        else:
            out.append("-")
    cleaned = "".join(out)
    cleaned = cleaned.strip("-")
    words = cleaned.split("-")
    return "-".join(word for word in words if word)
