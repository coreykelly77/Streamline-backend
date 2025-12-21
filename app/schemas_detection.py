from pydantic import BaseModel
from typing import List, Optional


class DetectedWindow(BaseModel):
    x: float
    y: float
    width: float
    height: float
    confidence: Optional[float] = None
    type: Optional[str] = None


class DetectionResponseSchema(BaseModel):
    windows: List[DetectedWindow]
