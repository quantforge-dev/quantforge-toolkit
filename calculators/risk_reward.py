"""
Risk / Reward Calculator

Utilities for calculating the risk-to-reward ratio of a trade.
"""

from validation.validators import validate_positive


def calculate_risk_reward(
    entry_price: float,
    stop_loss_price: float,
    take_profit_price: float,
) -> dict:
    """
    Calculate the risk and reward distances together with
    the resulting risk-to-reward ratio.
    """

    validate_positive(entry_price, "Entry price")
    validate_positive(stop_loss_price, "Stop-loss price")
    validate_positive(take_profit_price, "Take-profit price")

    risk = abs(entry_price - stop_loss_price)
    reward = abs(take_profit_price - entry_price)

    if risk == 0:
        raise ValueError(
            "Risk cannot be zero."
        )

    ratio = reward / risk

    return {
        "risk": round(risk, 8),
        "reward": round(reward, 8),
        "ratio": round(ratio, 2),
    }
