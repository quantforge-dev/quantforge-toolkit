"""
Value at Risk (VaR) Calculator

Historical-style parametric VaR implementation using
portfolio value, volatility and confidence level.
"""

from statistics import NormalDist

from validation.validators import validate_positive


def calculate_var(
    portfolio_value: float,
    volatility: float,
    confidence_level: float = 0.95,
) -> float:
    """
    Calculate one-period parametric Value at Risk (VaR).

    Parameters
    ----------
    portfolio_value : float
        Current portfolio value.

    volatility : float
        Portfolio volatility expressed as a decimal.
        Example: 0.02 for 2%.

    confidence_level : float
        Confidence level between 0 and 1.

    Returns
    -------
    float
        Estimated Value at Risk.
    """

    validate_positive(portfolio_value, "Portfolio value")
    validate_positive(volatility, "Volatility")

    if confidence_level <= 0 or confidence_level >= 1:
        raise ValueError(
            "Confidence level must be between 0 and 1."
        )

    z_score = NormalDist().inv_cdf(confidence_level)

    var = portfolio_value * volatility * z_score

    return round(var, 2)
