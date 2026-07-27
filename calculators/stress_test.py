"""
Portfolio Stress Testing
"""

from validation.validators import validate_positive


def stress_test(
    portfolio_value: float,
    shock_percent: float,
):
    """
    Apply a market shock.

    Parameters
    ----------
    portfolio_value : float
        Current portfolio value.

    shock_percent : float
        Percentage shock.
        Example:
        -20 means minus 20%
        15 means plus 15%

    Returns
    -------
    dict
        Stress test result.
    """

    validate_positive(portfolio_value, "Portfolio value")

    stressed_value = portfolio_value * (
        1 + shock_percent / 100
    )

    return {
        "original": round(portfolio_value, 2),
        "shock_percent": shock_percent,
        "stressed_value": round(stressed_value, 2),
    }
