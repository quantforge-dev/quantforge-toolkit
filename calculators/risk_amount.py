"""
Risk Amount Calculator

Calculates the maximum amount of capital
that can be risked on a single trade.
"""

from validation.validators import (
    validate_positive,
    validate_percentage,
)


def calculate_risk_amount(account_balance: float,
                          risk_percent: float) -> float:
    """
    Calculate maximum monetary risk.

    Parameters
    ----------
    account_balance : float
        Total account balance.

    risk_percent : float
        Percentage of capital to risk.

    Returns
    -------
    float
        Risk amount.
    """

    validate_positive(account_balance, "Account balance")
    validate_percentage(risk_percent, "Risk percentage")

    risk_amount = account_balance * (risk_percent / 100)

    return round(risk_amount, 2)
