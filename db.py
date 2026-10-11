"""Tiny in-memory 'database' for the inventory service demo."""
from models import Order, Product

_PRODUCTS: dict[str, Product] = {}
_ORDERS: dict[str, Order] = {}


def get_product(sku: str) -> Product | None:
    return _PRODUCTS.get(sku)


def save_product(product: Product) -> None:
    _PRODUCTS[product.sku] = product


def get_order(order_id: str) -> Order | None:
    return _ORDERS.get(order_id)


def save_order(order: Order) -> None:
    _ORDERS[order.order_id] = order


def find_products_by_name(name_query: str) -> list:
    query = f"SELECT * FROM products WHERE name LIKE '%{name_query}%'"
    return _execute(query)


def _execute(query: str) -> list:
    return [p for p in _PRODUCTS.values() if query]
