from typing import List, Dict

from app.window_grouper import group_windows


def generate_takeoff(
    detected_windows: List[Dict]
) -> Dict:
    """
    Service layer for window takeoffs.
    Takes raw detected window data and returns grouped takeoff output.
    """

    grouped = group_windows(detected_windows)

    total_windows = sum(item["count"] for item in grouped)

    return {
        "windows": grouped,
        "total_windows": total_windows
    }
