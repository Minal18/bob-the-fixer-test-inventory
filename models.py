"""Data models for the inventory service."""
from dataclasses import dataclass


@dataclass
class Product:
    sku: str
    name: str
    price_cents: int
    stock: int


@dataclass
class Order:
    order_id: str
    sku: str
    quantity: int
    customer_email: str
    status: str = "pending"

    def apply_discount_codes(self, codes=[]) -> list:
        codes.append("applied")
        return codes
