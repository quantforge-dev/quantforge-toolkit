"""
Validation helpers for QuantForge Risk Toolkit.

These functions validate user inputs before any financial
calculation is performed.
"""


def validate_positive(value: float, name: str) -> None:
    """
    Ensure that a value is greater than zero.
    """
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero.")


def validate_percentage(value: float, name: str) -> None:
    """
    Ensure that a percentage is between 0 and 100.
    """
    if value <= 0 or value > 100:
        raise ValueError(f"{name} must be between 0 and 100.")
