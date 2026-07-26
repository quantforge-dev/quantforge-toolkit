"""
Compound Growth Calculator.
"""

from validation.validators import (
    validate_positive,
)


def compound_growth(
    principal: float,
    annual_rate: float,
    years: float,
) -> float:
    """
    Calculate compound growth.
    """

    validate_positive(
        principal,
        "Principal",
    )

    validate_positive(
        years,
        "Years",
    )

    future_value = principal * (
        1 + annual_rate
    ) ** years

    return round(
        future_value,
        2,
    )
