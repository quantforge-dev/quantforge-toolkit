"""
Portfolio Summary Calculator.

This module provides functionality to generate a summary of a portfolio,
including the total portfolio value, number of assets, and allocation
percentage for each asset.
"""

from typing import Dict


def portfolio_summary(portfolio: Dict[str, float]) -> Dict[str, object]:
    """
    Generate a summary of a portfolio.

    Args:
        portfolio: A dictionary where the key is the asset name
            and the value is its monetary value.

    Returns:
        A dictionary containing:
            - total_value
            - number_of_assets
            - allocations

    Raises:
        ValueError:
            If the portfolio is empty.
            If any asset value is negative.
    """

    if not portfolio:
        raise ValueError("Portfolio cannot be empty.")

    if any(value < 0 for value in portfolio.values()):
        raise ValueError("Asset values cannot be negative.")

    total_value = sum(portfolio.values())

    allocations = {}

    if total_value > 0:
        for asset, value in portfolio.items():
            allocations[asset] = round((value / total_value) * 100, 2)
    else:
        for asset in portfolio:
            allocations[asset] = 0.0

    return {
        "total_value": total_value,
        "number_of_assets": len(portfolio),
        "allocations": allocations,
    }
