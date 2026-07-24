"""
Position Size Calculator

Calculate position size based on account balance,
risk percentage and stop-loss distance.
"""

from validation.validators import (
    validate_positive,
    validate_percentage,
)


def calculate_position_size(
    account_balance: float,
    risk_percent: float,
    entry_price: float,
    stop_loss_price: float,
) -> float:
    """
    Calculate position size.

    Returns the number of units that can be traded
    while respecting the defined risk.
    """

    validate_positive(account_balance, "Account balance")
    validate_percentage(risk_percent, "Risk percentage")
    validate_positive(entry_price, "Entry price")
    validate_positive(stop_loss_price, "Stop-loss price")

    stop_distance = abs(entry_price - stop_loss_price)

    if stop_distance == 0:
        raise ValueError(
            "Entry price and stop-loss price cannot be equal."
        )

    risk_amount = account_balance * (risk_percent / 100)

    position_size = risk_amount / stop_distance

    return round(position_size, 8)
