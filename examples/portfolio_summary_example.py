"""
Example: Portfolio Summary
"""

from calculators.portfolio_summary import (
    portfolio_summary,
)

portfolio = {
    "Bitcoin": 5000,
    "Gold": 3000,
    "Cash": 2000,
}

summary = portfolio_summary(portfolio)

print(summary)
