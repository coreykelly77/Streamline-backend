from typing import Dict, List


def price_takeoff(
    windows: List[Dict],
    rates: Dict[str, float]
) -> Dict:
    """
    Prices a window takeoff using company-specific rates.

    windows example:
    [
        {
            "type": "single_hung",
            "width": 36,
            "height": 60,
            "count": 4
        }
    ]

    rates example:
    {
        "single_hung": 425.00,
        "double_hung": 485.00
    }
    """

    line_items = []
    total_price = 0.0

    for window in windows:
        window_type = window["type"]
        count = window["count"]

        if window_type not in rates:
            raise ValueError(f"No rate found for window type: {window_type}")

        unit_price = rates[window_type]
        line_total = unit_price * count
        total_price += line_total

        line_items.append({
            "type": window_type,
            "count": count,
            "unit_price": unit_price,
            "line_total": line_total
        })

    return {
        "line_items": line_items,
        "total_price": round(total_price, 2)
    }
