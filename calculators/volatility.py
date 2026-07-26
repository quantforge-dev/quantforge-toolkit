"""
Volatility Calculator.
"""

from math import sqrt

from calculators.variance import (
    calculate_variance,
)


def calculate_volatility(
    returns: list[float],
) -> float:
    """
    Calculate volatility using variance.
    """

    variance = calculate_variance(
        returns,
    )

    return round(
        sqrt(variance),
        8,
    )
