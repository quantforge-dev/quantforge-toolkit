"""
Information Ratio Calculator.

Measures active return relative to tracking error.
"""

from validation.validators import validate_positive


def calculate_information_ratio(
    portfolio_return: float,
    benchmark_return: float,
    tracking_error: float,
) -> float:
    """
    Calculate Information Ratio.
    """

    validate_positive(
        tracking_error,
        "Tracking error",
    )

    ratio = (
        portfolio_return - benchmark_return
    ) / tracking_error

    return round(ratio, 4)
