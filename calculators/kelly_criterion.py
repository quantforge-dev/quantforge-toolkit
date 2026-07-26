"""
Kelly Criterion Calculator.
"""

from validation.validators import validate_percentage, validate_positive


def calculate_kelly(
    win_rate: float,
    reward_risk_ratio: float,
) -> float:
    """
    Calculate Kelly percentage.
    """

    validate_percentage(
        win_rate,
        "Win rate",
    )

    validate_positive(
        reward_risk_ratio,
        "Reward/Risk ratio",
    )

    p = win_rate / 100
    q = 1 - p
    b = reward_risk_ratio

    kelly = (b * p - q) / b

    return round(kelly * 100, 2)
