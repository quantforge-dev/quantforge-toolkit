"""
Portfolio Allocation Calculator

Utilities for validating and analyzing portfolio allocations.
"""

from validation.validators import validate_percentage


def calculate_portfolio_allocation(
    allocations: dict,
) -> dict:
    """
    Validate portfolio allocation percentages.

    Parameters
    ----------
    allocations : dict

        Example:

        {
            "Bitcoin": 30,
            "Gold": 20,
            "Oil": 10,
            "Silver": 10,
            "Cash": 30,
        }

    Returns
    -------
    dict
        {
            "assets": int,
            "total_allocation": float,
            "remaining": float,
            "is_valid": bool
        }
    """

    if not allocations:
        raise ValueError(
            "Portfolio cannot be empty."
        )

    total = 0.0

    for asset, percentage in allocations.items():

        validate_percentage(
            percentage,
            f"Allocation for {asset}",
        )

        total += percentage

    total = round(total, 2)

    remaining = round(
        100 - total,
        2,
    )

    return {
        "assets": len(allocations),
        "total_allocation": total,
        "remaining": remaining,
        "is_valid": total == 100,
    }
