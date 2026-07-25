"""
Drawdown Calculator

This module provides utilities for calculating drawdown values
from an account balance.

Author: QuantForge
"""

from validation.validators import validate_positive_number


def calculate_drawdown(initial_balance: float, current_balance: float) -> dict:
    """
    Calculate absolute and percentage drawdown.

    Parameters
    ----------
    initial_balance : float
        Starting account balance.

    current_balance : float
        Current account balance.

    Returns
    -------
    dict
        {
            "loss": float,
            "drawdown_percent": float
        }
    """

    validate_positive_number(initial_balance, "initial_balance")
    validate_positive_number(current_balance, "current_balance")

    if current_balance > initial_balance:
        raise ValueError(
            "Current balance cannot be greater than initial balance."
        )

    loss = initial_balance - current_balance

    drawdown_percent = (loss / initial_balance) * 100

    return {
        "loss": round(loss, 2),
        "drawdown_percent": round(drawdown_percent, 2),
    }
