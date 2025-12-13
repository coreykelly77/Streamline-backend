from fastapi import FastAPI, UploadFile, File
from typing import List

from app.schemas import (
    WindowAnalysisResponse,
    ElevationResult,
    WindowGroup,
)

# -------------------------------------------------
# App setup
# -------------------------------------------------
app = FastAPI(
    title="Streamline Windows AI",
    description="Micro backend for window quantity takeoff from elevation drawings",
    version="0.1.0",
)

# -------------------------------------------------
# Health check
# -------------------------------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}


# -------------------------------------------------
# Windows analysis (NO FILE UPLOAD – mock)
# -------------------------------------------------
@app.post(
    "/windows/analyse",
    response_model=WindowAnalysisResponse,
)
async def analyse_windows(project_id: str):
    """
    Mock endpoint.
    Returns window quantities grouped by floor, elevation, and size.
    """

    return WindowAnalysisResponse(
        project_id=project_id,
        results=[
            ElevationResult(
                floor="First Floor",
                elevation="Front",
                windows=[
                    WindowGroup(size_mm="1200x1500", quantity=4),
                ],
            ),
            ElevationResult(
                floor="First Floor",
                elevation="Rear",
                windows=[
                    WindowGroup(size_mm="1200x1500", quantity=2),
                    WindowGroup(size_mm="900x1200", quantity=1),
                ],
            ),
        ],
        notes=[
            "Visual count from elevation drawings",
            "Sizes estimated from scale",
        ],
    )


# -------------------------------------------------
# Windows analysis (WITH FILE UPLOAD – mock)
# -------------------------------------------------
@app.post(
    "/windows/analyse/upload",
    response_model=WindowAnalysisResponse,
)
async def analyse_windows_with_upload(
    project_id: str,
    floors: List[str],
    elevations: List[str],
    drawings: List[UploadFile] = File(...),
):
    """
    Mock upload endpoint.
    Accepts elevation drawings and returns placeholder window quantities.
    """

    return WindowAnalysisResponse(
        project_id=project_id,
        results=[
            ElevationResult(
                floor=floors[0] if floors else "Unknown Floor",
                elevation=elevations[0] if elevations else "Unknown Elevation",
                windows=[
                    WindowGroup(size_mm="1200x1500", quantity=4),
                ],
            )
        ],
        notes=[
            f"{len(drawings)} drawing(s) received",
            "Visual count from elevation drawings",
            "Sizes estimated from scale",
        ],
    )
