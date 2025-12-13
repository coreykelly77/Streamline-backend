from fastapi import FastAPI, UploadFile, File
from typing import List

app = FastAPI(
    title="Streamline Windows AI",
    description="Micro backend for window quantity takeoff from elevation drawings",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/windows/analyse")
async def analyse_windows(
    project_id: str,
    floor_names: List[str],
    drawings: List[UploadFile] = File(...)
):
    """
    Receives elevation drawings and returns
    window counts grouped by size and floor.
    (AI logic added later)
    """

    return {
        "project_id": project_id,
        "floors": floor_names,
        "drawings_received": [d.filename for d in drawings],
        "message": "Window analysis placeholder – AI not wired yet"
    }
