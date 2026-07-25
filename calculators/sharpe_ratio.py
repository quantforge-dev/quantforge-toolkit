"""
Sharpe Ratio Calculator.

This module provides functionality to calculate the Sharpe Ratio
for a portfolio or investment.
"""

from math import sqrt


def sharpe_ratio(
    expected_return: float,
    risk_free_rate: float,
    standard_deviation: float,
) -> float:
    """
    Calculate the Sharpe Ratio.

    Args:
        expected_return:
            Expected annual return.

        risk_free_rate:
            Risk-free annual return.

        standard_deviation:
            Standard deviation of returns.

    Returns:
        Sharpe Ratio.

    Raises:
        ValueError:
            If standard deviation is less than or equal to zero.
    """

    if standard_deviation <= 0:
        raise ValueError("Standard deviation must be greater than zero.")

    return round(
        (expected_return - risk_free_rate) / standard_deviation,
        4,
    )
