"""
Random Portfolio Generator
"""

import random

from validation.validators import validate_positive


def generate_random_weights(number_of_assets):
    """
    Generate random portfolio weights
    that sum to 1.
    """

    validate_positive(
        number_of_assets,
        "Number of assets",
    )

    values = [
        random.random()
        for _ in range(number_of_assets)
    ]

    total = sum(values)

    weights = [
        round(value / total, 4)
        for value in values
    ]

    difference = round(
        1 - sum(weights),
        4,
    )

    weights[-1] = round(
        weights[-1] + difference,
        4,
    )

    return weights
