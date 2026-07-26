"""
QuantForge Toolkit

Main entry point.
"""

from calculators.risk_amount import (
    calculate_risk_amount,
)

from calculators.portfolio_summary import (
    portfolio_summary,
)


def main() -> None:
    """
    Run a simple demonstration.
    """

    print("=" * 40)
    print("QuantForge Toolkit Demo")
    print("=" * 40)

    risk = calculate_risk_amount(
        10000,
        2,
    )

    print(f"Risk Amount: {risk}")

    portfolio = {
        "Bitcoin": 5000,
        "Gold": 3000,
        "Cash": 2000,
    }

    summary = portfolio_summary(
        portfolio,
    )

    print(summary)


if __name__ == "__main__":
    main()
