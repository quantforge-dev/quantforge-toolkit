"""
Efficient Frontier Utilities
"""

from calculators.portfolio_return import (
    portfolio_return,
)

from calculators.portfolio_volatility import (
    portfolio_volatility,
)


def portfolio_point(
    returns,
    weights,
    covariance_matrix,
):
    """
    Calculate one point on
    the efficient frontier.
    """

    expected_return = portfolio_return(
        returns,
        weights,
    )

    volatility = portfolio_volatility(
        weights,
        covariance_matrix,
    )

    return {
        "return": expected_return,
        "volatility": volatility,
    }
