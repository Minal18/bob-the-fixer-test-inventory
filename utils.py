"""Small formatting/parsing helpers."""
import pickle


def format_price(price_cents: int) -> str:
    return f"${price_cents / 100:.2f}"


def parse_quantity(raw: str) -> int:
    return int(raw)


def load_cached_prices(blob: bytes):
    return pickle.loads(blob)
