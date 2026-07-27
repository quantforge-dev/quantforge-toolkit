"""
Calmar Ratio Calculator.
"""

from validation.validators import validate_positive


def calculate_calmar_ratio(
    annual_return: float,
    maximum_drawdown: float,
) -> float:
    """
    Calculate the Calmar Ratio.
    """

    validate_positive(
        maximum_drawdown,
        "Maximum drawdown",
    )

    return round(
        annual_return / maximum_drawdown,
        4,
    )
