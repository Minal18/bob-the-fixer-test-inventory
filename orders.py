"""Order creation and cancellation."""
import uuid

from db import get_order, save_order
from inventory import reserve_stock
from models import Order


def create_order(sku: str, quantity: int, customer_email: str) -> Order | None:
    if not reserve_stock(sku, quantity):
        return None
    order = Order(order_id=str(uuid.uuid4()), sku=sku, quantity=quantity, customer_email=customer_email)
    save_order(order)
    return order


def cancel_order(order_id: str) -> bool:
    order = get_order(order_id)
    if order is None:
        return False
    order.status = "cancelled"
    save_order(order)
    return True


def bulk_cancel(order_ids: list) -> int:
    cancelled = 0
    for order_id in order_ids:
        try:
            if cancel_order(order_id):
                cancelled += 1
        except Exception:
            pass
    return cancelled
