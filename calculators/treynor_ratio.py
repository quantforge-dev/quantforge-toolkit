"""
Treynor Ratio Calculator.
"""

from validation.validators import validate_positive


def calculate_treynor_ratio(
    portfolio_return: float,
    risk_free_rate: float,
    beta: float,
) -> float:
    """
    Calculate Treynor Ratio.
    """

    validate_positive(
        beta,
        "Beta",
    )

    ratio = (
        portfolio_return - risk_free_rate
    ) / beta

    return round(ratio, 4)
