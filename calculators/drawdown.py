"""
Drawdown Calculator

Utilities for calculating account drawdown.
"""

from validation.validators import validate_positive


def calculate_drawdown(
    initial_balance: float,
    current_balance: float,
) -> dict:
    """
    Calculate account drawdown.

    Parameters
    ----------
    initial_balance : float
        Starting account balance.

    current_balance : float
        Current account balance.

    Returns
    -------
    dict
        Dictionary containing:

        loss
            Monetary loss.

        drawdown_percent
            Drawdown percentage.
    """

    validate_positive(
        initial_balance,
        "Initial balance",
    )

    validate_positive(
        current_balance,
        "Current balance",
    )

    if current_balance > initial_balance:
        raise ValueError(
            "Current balance cannot exceed initial balance."
        )

    loss = initial_balance - current_balance

    drawdown_percent = (
        loss / initial_balance
    ) * 100

    return {
        "loss": round(loss, 2),
        "drawdown_percent": round(
            drawdown_percent,
            2,
        ),
    }
