"""
Portfolio Volatility Calculator.

Calculate weighted portfolio volatility.
"""

from math import sqrt


def portfolio_volatility(weights: dict, volatilities: dict) -> float:
    """
    Calculate approximate portfolio volatility.

    Parameters
    ----------
    weights
        Asset weights (0-100).

    volatilities
        Asset annual volatility values.

    Returns
    -------
    float
        Portfolio volatility.
    """

    if not weights:
        raise ValueError("Weights cannot be empty.")

    if set(weights.keys()) != set(volatilities.keys()):
        raise ValueError(
            "Assets must match in both dictionaries."
        )

    total_weight = sum(weights.values())

    if round(total_weight, 2) != 100:
        raise ValueError(
            "Weights must total 100."
        )

    variance = 0

    for asset in weights:
        weight = weights[asset] / 100
        variance += (
            weight ** 2
        ) * (
            volatilities[asset] ** 2
        )

    return round(sqrt(variance), 4)
