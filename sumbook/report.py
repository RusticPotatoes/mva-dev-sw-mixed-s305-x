"""Summaries of a file of amounts, one per line; lines starting with # are comments."""

from sumbook.money import format_cents
from sumbook.parse import parse_amount


def amounts(lines):
    return [parse_amount(line) for line in lines
            if line.strip() and not line.lstrip().startswith("#")]


def summary(lines):
    found = amounts(lines)
    return f"{len(found)} entries, total {format_cents(sum(found))}"
