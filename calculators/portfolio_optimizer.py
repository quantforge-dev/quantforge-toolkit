"""
Simple Portfolio Optimizer
"""

from validation.validators import validate_positive


def equal_weight_portfolio(number_of_assets):
    """
    Allocate equal weights.
    """

    validate_positive(
        number_of_assets,
        "Number of assets",
    )

    weight = round(
        1 / number_of_assets,
        4,
    )

    return [weight] * number_of_assets
