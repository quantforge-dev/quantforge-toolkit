"""
Variance Calculator.
"""

from validation.validators import validate_positive


def calculate_variance(values: list[float]) -> float:
    """
    Calculate population variance.
    """

    if not values:
        raise ValueError("Values cannot be empty.")

    for value in values:
        validate_positive(value, "Value")

    mean = sum(values) / len(values)

    variance = sum(
        (value - mean) ** 2
        for value in values
    ) / len(values)

    return round(variance, 8)
