"""
Portfolio Statistics.

Provides summary statistics for portfolio returns.
"""

from statistics import mean


def portfolio_statistics(
    returns: list[float],
) -> dict:
    """
    Calculate basic portfolio statistics.
    """

    if not returns:
        raise ValueError(
            "Returns cannot be empty."
        )

    return {
        "observations": len(returns),
        "average_return": round(
            mean(returns),
            6,
        ),
        "minimum_return": min(returns),
        "maximum_return": max(returns),
    }
