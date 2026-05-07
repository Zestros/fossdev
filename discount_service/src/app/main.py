from fastapi import FastAPI
from pydantic import BaseModel
import os
import redis

redis_client = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

app = FastAPI(title="Discount Service")


class DiscountRequest(BaseModel):
    product_id: str
    quantity: int
    price_per_item: float
    promo_code: str | None = None


class DiscountResponse(BaseModel):
    discount_percent: float
    reason: str


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "discount-service",
    }

@app.on_event("startup")
def init_data():
    redis_client.set("STUDENT10", 10)

@app.post(
    "/discounts/calculate",
    response_model=DiscountResponse,
)
async def calculate_discount(request: DiscountRequest) -> DiscountResponse:

    promo_discount = redis_client.get(request.promo_code)

    if promo_discount:
        return DiscountResponse(
            discount_percent=float(promo_discount),
            reason="Promo code from Redis",
        )

    if request.quantity >= 10:
        return DiscountResponse(
            discount_percent=15,
            reason="Bulk discount",
        )

    total_price = request.quantity * request.price_per_item

    if total_price >= 100000:
        return DiscountResponse(
            discount_percent=5,
            reason="Large order discount",
        )

    return DiscountResponse(
        discount_percent=0,
        reason="No discount",
    )