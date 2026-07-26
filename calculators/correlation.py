"""
Correlation Calculator.
"""

from math import sqrt

from calculators.covariance import (
    calculate_covariance,
)

from calculators.variance import (
    calculate_variance,
)


def calculate_correlation(
    x: list[float],
    y: list[float],
) -> float:
    """
    Calculate Pearson correlation coefficient.
    """

    covariance = calculate_covariance(
        x,
        y,
    )

    std_x = sqrt(
        calculate_variance(x)
    )

    std_y = sqrt(
        calculate_variance(y)
    )

    if std_x == 0 or std_y == 0:
        raise ValueError(
            "Standard deviation cannot be zero."
        )

    return round(
        covariance / (std_x * std_y),
        6,
    )
