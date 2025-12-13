import cv2
import numpy as np
from typing import List, Dict


def detect_rectangles(image: np.ndarray) -> List[Dict]:
    """
    Detect rectangular shapes in an architectural elevation image.

    Returns a list of bounding boxes:
    {x, y, w, h}
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Clean up the drawing
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blur, 50, 150)

    contours, _ = cv2.findContours(
        edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    rectangles = []

    for cnt in contours:
        epsilon = 0.02 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        # Rectangle = 4 corners
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)

            # Basic architectural sanity filters
            if w > 50 and h > 50:
                rectangles.append({
                    "x": x,
                    "y": y,
                    "w": w,
                    "h": h
                })

    return rectangles
