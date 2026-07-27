"""
Beta Calculator.

Measures the sensitivity of an asset relative to the market.
"""


def calculate_beta(
    covariance: float,
    market_variance: float,
) -> float:
    """
    Calculate portfolio beta.
    """

    if market_variance <= 0:
        raise ValueError(
            "Market variance must be positive."
        )

    return round(
        covariance / market_variance,
        4,
    )
