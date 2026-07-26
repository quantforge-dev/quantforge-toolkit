"""
Break-even Price Calculator.
"""

from validation.validators import validate_positive


def calculate_break_even(
    total_cost: float,
    quantity: float,
) -> float:
    """
    Calculate break-even price per unit.
    """

    validate_positive(total_cost, "Total cost")
    validate_positive(quantity, "Quantity")

    return round(
        total_cost / quantity,
        8,
    )
