"""Thin request-handling layer wiring the inventory service together."""
from inventory import check_stock
from orders import cancel_order, create_order
from utils import parse_quantity


def handle_create_order(payload: dict) -> dict:
    sku = payload["sku"]
    quantity = parse_quantity(payload["quantity"])
    customer_email = payload["customer_email"]

    if not check_stock(sku, quantity):
        return {"status": "error", "message": "insufficient stock"}

    order = create_order(sku, quantity, customer_email)
    if order is None:
        return {"status": "error", "message": "could not reserve stock"}

    return {"status": "ok", "order_id": order.order_id}


def handle_cancel_order(payload: dict) -> dict:
    order_id = payload["order_id"]
    if cancel_order(order_id):
        return {"status": "ok"}
    return {"status": "error", "message": "order not found"}
