from typing import Any, Dict, List

from app.window_detector import detect_windows


def run_detection(
    image_bytes: bytes,
    metadata: Dict[str, Any] | None = None
) -> List[Dict]:
    """
    Service layer for window detection.
    Takes raw image bytes and returns detected window data.
    """

    detections = detect_windows(
        image_bytes=image_bytes,
        metadata=metadata
    )

    return detections
