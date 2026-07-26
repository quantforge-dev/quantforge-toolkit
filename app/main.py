"""
QuantForge Toolkit

Main entry point.
"""

from calculators.portfolio_summary import portfolio_summary
from calculators.risk_amount import calculate_risk_amount
from calculators.risk_reward import calculate_risk_reward


def main() -> None:
    """
    Run a simple demonstration of the toolkit.
    """

    print("=" * 50)
    print("QuantForge Toolkit")
    print("=" * 50)

    risk = calculate_risk_amount(
        account_balance=10000,
        risk_percent=2,
    )

    print(f"Risk Amount: {risk}")

    rr = calculate_risk_reward(
        entry_price=100,
        stop_loss_price=95,
        take_profit_price=115,
    )

    print(f"Risk/Reward Ratio: {rr['ratio']}")

    portfolio = {
        "Bitcoin": 5000,
        "Gold": 3000,
        "Cash": 2000,
    }

    summary = portfolio_summary(portfolio)

    print("\nPortfolio Summary")
    print(summary)


if __name__ == "__main__":
    main()
