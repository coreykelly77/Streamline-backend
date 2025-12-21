from typing import Dict

from app.pricing import price_takeoff
from app.schemas_pricing import (
    PricingRequestSchema,
    PricingResponseSchema,
    PricingLineItem
)


def calculate_pricing(
    request: PricingRequestSchema
) -> PricingResponseSchema:
    """
    Service layer for pricing window takeoffs.
    Converts schemas → business logic → schemas.
    """

    result = price_takeoff(
        windows=[w.dict() for w in request.windows],
        rates=request.rates
    )

    line_items = [
        PricingLineItem(**item)
        for item in result["line_items"]
    ]

    return PricingResponseSchema(
        line_items=line_items,
        total_price=result["total_price"]
    )
