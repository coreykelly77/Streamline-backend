from typing import List
from pydantic import BaseModel


class WindowGroup(BaseModel):
    size_mm: str          # e.g. "1200x1500"
    quantity: int         # e.g. 4


class ElevationResult(BaseModel):
    floor: str            # e.g. "First Floor"
    elevation: str        # e.g. "Front"
    windows: List[WindowGroup]


class WindowAnalysisResponse(BaseModel):
    project_id: str
    results: List[ElevationResult]
    notes: List[str]
