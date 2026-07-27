"""
Sortino Ratio Calculator.

Measures risk-adjusted return using downside deviation.
"""

from validation.validators import validate_positive


def calculate_sortino_ratio(
    expected_return: float,
    risk_free_rate: float,
    downside_deviation: float,
) -> float:
    """
    Calculate the Sortino Ratio.
    """

    validate_positive(
        downside_deviation,
        "Downside deviation",
    )

    ratio = (
        expected_return - risk_free_rate
    ) / downside_deviation

    return round(ratio, 4)
