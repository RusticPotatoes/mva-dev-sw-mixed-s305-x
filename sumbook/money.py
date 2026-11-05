"""Formatting amounts held in cents."""


def format_cents(cents):
    """12345 -> '$123.45'; negative amounts keep their sign."""
    sign = "-" if cents < 0 else ""
    cents = abs(cents)
    return f"{sign}${cents // 100}.{cents % 100:02d}"
