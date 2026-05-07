# order_service/app/settings.py
from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    product_service_url: str
    discount_service_url: str
    database_url: str


def get_settings() -> Settings:
    return Settings(
        product_service_url=os.getenv(
            "PRODUCT_SERVICE_URL",
            "http://product-service:8000",
        ),
        discount_service_url=os.getenv(
            "DISCOUNT_SERVICE_URL",
            "http://discount-service:8000",
        ),
        database_url=os.getenv(
            "DATABASE_URL",
            "postgresql://app:app@postgres:5432/orders",
        ),
    )