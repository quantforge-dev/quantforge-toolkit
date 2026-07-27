"""
Example:
Efficient Frontier
"""

from calculators.efficient_frontier import (
    calculate_portfolio_point,
)

returns = {
    "BTC": 12,
    "ETH": 8,
}

weights = {
    "BTC": 60,
    "ETH": 40,
}

volatilities = {
    "BTC": 0.40,
    "ETH": 0.35,
}

result = calculate_portfolio_point(
    returns,
    weights,
    volatilities,
)

print(result)
