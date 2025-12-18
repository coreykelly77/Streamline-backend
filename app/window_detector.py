# app/window_detector.py

import cv2
import numpy as np
from typing import List, Tuple


class DetectedWindow:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def to_mm(self, scale_px_per_mm: float):
        return {
            "width_mm": round(self.width / scale_px_per_mm),
            "height_mm": round(self.height / scale_px_per_mm),
        }


def detect_rectangular_windows(image_bytes: bytes) -> List[DetectedWindow]:
    """
    Detect rectangular window shapes from elevation drawings.
    Assumes black-line architectural drawings.
    """

    # Convert bytes → image
    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_GRAYSCALE)

    # Edge detection
    edges = cv2.Canny(img, threshold1=50, threshold2=150)

    # Find contours
    contours, _ = cv2.findContours(
        edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    windows = []

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)

        # Rectangles only
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)

            # Filter out noise (tune later)
            if w > 50 and h > 50:
                windows.append(DetectedWindow(x, y, w, h))

    return windows
