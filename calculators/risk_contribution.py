"""
Risk Contribution Calculator.
"""


def calculate_risk_contribution(
    asset_weight: float,
    asset_volatility: float,
    portfolio_volatility: float,
):
    """
    Calculate asset risk contribution.
    """

    if portfolio_volatility <= 0:
        raise ValueError(
            "Portfolio volatility must be positive."
        )

    contribution = (
        asset_weight
        * asset_volatility
    ) / portfolio_volatility

    return round(
        contribution,
        6,
    )
