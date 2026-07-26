"""
Validation helpers for QuantForge Toolkit.

These functions validate user inputs before any financial
calculation is performed.
"""


def validate_positive(value: float, name: str) -> None:
    """
    Ensure that a numeric value is greater than zero.
    """

    if value <= 0:
        raise ValueError(
            f"{name} must be greater than zero."
        )


def validate_non_negative(
    value: float,
    name: str,
) -> None:
    """
    Ensure that a numeric value is zero or greater.
    """

    if value < 0:
        raise ValueError(
            f"{name} cannot be negative."
        )


def validate_percentage(
    value: float,
    name: str,
) -> None:
    """
    Ensure that a percentage is within (0, 100].
    """

    if value <= 0 or value > 100:
        raise ValueError(
            f"{name} must be between 0 and 100."
        )


def validate_not_empty(
    collection,
    name: str,
) -> None:
    """
    Ensure that a collection is not empty.
    """

    if not collection:
        raise ValueError(
            f"{name} cannot be empty."
        )
