"""
Portfolio Summary Calculator.

Generate summary statistics for a portfolio.
"""

from validation.validators import (
    validate_not_empty,
    validate_non_negative,
)


def portfolio_summary(
    portfolio: dict[str, float],
) -> dict[str, object]:
    """
    Generate a portfolio summary.
    """

    validate_not_empty(
        portfolio,
        "Portfolio",
    )

    for asset, value in portfolio.items():
        validate_non_negative(
            value,
            f"{asset} value",
        )

    total_value = sum(
        portfolio.values()
    )

    allocations = {}

    if total_value > 0:

        for asset, value in portfolio.items():

            allocations[asset] = round(
                (value / total_value) * 100,
                2,
            )

    else:

        for asset in portfolio:

            allocations[asset] = 0.0

    return {
        "total_value": round(
            total_value,
            2,
        ),
        "number_of_assets": len(
            portfolio,
        ),
        "allocations": allocations,
    }
