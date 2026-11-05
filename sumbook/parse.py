"""Reading amounts written as text."""


def parse_amount(text):
    """'12.5' -> 1250, '-3' -> -300, ' 7.25 ' -> 725."""
    text = text.strip()
    if not text:
        raise ValueError("empty amount")
    negative = text.startswith("-")
    dollars, _, cents = text.lstrip("-").partition(".")
    cents = (cents + "00")[:2]
    value = int(dollars or "0") * 100 + int(cents)
    return -value if negative else value
