"""
Tracking Error Calculator.
"""

from math import sqrt


def calculate_tracking_error(
    active_returns: list[float],
):
    """
    Calculate tracking error.
    """

    if len(active_returns) < 2:
        raise ValueError(
            "At least two observations are required."
        )

    avg = sum(active_returns) / len(active_returns)

    variance = sum(
        (x - avg) ** 2
        for x in active_returns
    ) / (len(active_returns) - 1)

    return round(
        sqrt(variance),
        6,
    )
