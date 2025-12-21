from pydantic import BaseModel
from typing import List, Optional


class WindowTakeoffItem(BaseModel):
    type: str
    width: Optional[float] = None
    height: Optional[float] = None
    count: int


class TakeoffResponseSchema(BaseModel):
    windows: List[WindowTakeoffItem]
    total_windows: int
