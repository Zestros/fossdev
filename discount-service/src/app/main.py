from fastapi import FastAPI
from pydantic import BaseModel


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


@app.post(
    "/discounts/calculate",
    response_model=DiscountResponse,
)
async def calculate_discount(request: DiscountRequest) -> DiscountResponse:

    if request.promo_code == "STUDENT10":
        return DiscountResponse(
            discount_percent=10,
            reason="Student promo code",
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