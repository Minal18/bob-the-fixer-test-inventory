"""Stock management for products."""
from db import get_product, save_product


def check_stock(sku: str, quantity: int) -> bool:
    product = get_product(sku)
    if product is None:
        return False
    return product.stock >= quantity


def reserve_stock(sku: str, quantity: int) -> bool:
    product = get_product(sku)
    if product is None or product.stock < quantity:
        return False
    product.stock -= quantity
    save_product(product)
    return True
