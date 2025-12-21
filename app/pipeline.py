from typing import Dict, Any

from app.services.detection_service import run_detection
from app.services.takeoff_service import generate_takeoff
from app.services.pricing_service import calculate_pricing
from app.schemas_pricing import PricingRequestSchema


def run_full_pipeline(
    image_bytes: bytes,
    rates: Dict[str, float],
    metadata: Dict[str, Any] | None = None
) -> Dict:
    """
    Runs full detection → takeoff → pricing pipeline.
    No API, no IO, pure orchestration.
    """

    # 1. Detect windows
    detections = run_detection(
        image_bytes=image_bytes,
        metadata=metadata
    )

    # 2. Generate takeoff
    takeoff = generate_takeoff(detections)

    # 3. Price takeoff
    pricing_request = PricingRequestSchema(
        windows=takeoff["windows"],
        rates=rates
    )

    pricing = calculate_pricing(pricing_request)

    return {
        "detections": detections,
        "takeoff": takeoff,
        "pricing": pricing.dict()
    }
