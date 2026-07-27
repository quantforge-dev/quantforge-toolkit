"""
Efficient Frontier Utilities.
"""

from calculators.portfolio_return import (
    calculate_portfolio_return,
)

from calculators.portfolio_volatility import (
    portfolio_volatility,
)


def calculate_portfolio_point(
    asset_returns: dict,
    asset_weights: dict,
    asset_volatilities: dict,
) -> dict:
    """
    Calculate one portfolio point for the efficient frontier.

    Parameters
    ----------
    asset_returns
        Dictionary of asset returns.

    asset_weights
        Dictionary of portfolio weights.

    asset_volatilities
        Dictionary of asset volatilities.

    Returns
    -------
    dict
        Portfolio return and volatility.
    """

    expected_return = calculate_portfolio_return(
        asset_returns,
    )

    volatility = portfolio_volatility(
        asset_weights,
        asset_volatilities,
    )

    return {
        "return": expected_return,
        "volatility": volatility,
    }
