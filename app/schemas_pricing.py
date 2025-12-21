from pydantic import BaseModel
from typing import Dict, List, Optional


class WindowTakeoffItem(BaseModel):
    type: str
    width: Optional[float] = None
    height: Optional[float] = None
    count: int


class PricingRequestSchema(BaseModel):
    windows: List[WindowTakeoffItem]
    rates: Dict[str, float]


class PricingLineItem(BaseModel):
    type: str
    count: int
    unit_price: float
    line_total: float


class PricingResponseSchema(BaseModel):
    line_items: List[PricingLineItem]
    total_price: float
