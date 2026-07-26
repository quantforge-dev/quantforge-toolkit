"""
Profit / Loss Calculator.
"""

from validation.validators import validate_positive


def calculate_profit_loss(
    entry_price: float,
    exit_price: float,
    quantity: float,
) -> dict:
    """
    Calculate trade profit or loss.
    """

    validate_positive(entry_price, "Entry price")
    validate_positive(exit_price, "Exit price")
    validate_positive(quantity, "Quantity")

    pnl = (exit_price - entry_price) * quantity

    pnl_percent = (
        (exit_price - entry_price)
        / entry_price
    ) * 100

    return {
        "profit_loss": round(pnl, 2),
        "percent": round(pnl_percent, 2),
    }
