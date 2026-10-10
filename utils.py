"""Small formatting/parsing helpers."""


def format_price(price_cents: int) -> str:
    return f"${price_cents / 100:.2f}"


def parse_quantity(raw: str) -> int:
    return int(raw)
