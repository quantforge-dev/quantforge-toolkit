"""
QuantForge Risk Toolkit

Main entry point of the application.
"""

from calculators.drawdown import calculate_drawdown
from calculators.portfolio_allocation import calculate_portfolio_allocation
from calculators.portfolio_summary import portfolio_summary
from calculators.position_size import calculate_position_size
from calculators.risk_amount import calculate_risk_amount
from calculators.risk_reward import calculate_risk_reward
from calculators.sharpe_ratio import sharpe_ratio


def main() -> None:
    """
    Entry point for QuantForge Toolkit.

    This function serves as the central import location
    for all Version 1 calculators.
    """
    print("QuantForge Risk Toolkit")
    print("Version 1.0.0 (In Development)")
    print("Available calculators:")
    print("- Risk Amount")
    print("- Position Size")
    print("- Drawdown")
    print("- Risk / Reward")
    print("- Portfolio Allocation")
    print("- Portfolio Summary")
    print("- Sharpe Ratio")


if __name__ == "__main__":
    main()
