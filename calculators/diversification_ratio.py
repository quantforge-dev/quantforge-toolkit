"""
Diversification Ratio Calculator.
"""


def calculate_diversification_ratio(
    weighted_asset_volatility: float,
    portfolio_volatility: float,
) -> float:
    """
    Calculate diversification ratio.
    """

    if weighted_asset_volatility <= 0:
        raise ValueError(
            "Weighted asset volatility must be positive."
        )

    if portfolio_volatility <= 0:
        raise ValueError(
            "Portfolio volatility must be positive."
        )

    return round(
        weighted_asset_volatility
        / portfolio_volatility,
        4,
    )
