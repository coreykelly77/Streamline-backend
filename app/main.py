from fastapi import FastAPI
from app.schemas import (
    WindowAnalysisResponse,
    ElevationResult,
    WindowGroup,
)

app = FastAPI(
    title="Streamline Windows AI",
    description="Micro backend for window quantity takeoff from elevation drawings",
    version="0.1.0",
)

# -------------------------
# Health check
# -------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}


# -------------------------
# Windows analysis endpoint (MOCK for now)
# -------------------------
@app.post(
    "/windows/analyse",
    response_model=WindowAnalysisResponse,
)
async def analyse_windows(project_id: str):
    """
    Placeholder implementation.

    Returns mock window quantities grouped by:
    - floor
    - elevation
    - window size (mm)

    AI vision + scale logic will replace this later.
    """

    mock_result = WindowAnalysisResponse(
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

    return mock_result
