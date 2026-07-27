"""
Example:
Multi-period Monte Carlo
"""

from calculators.multi_period_monte_carlo import (
    multi_period_monte_carlo,
)

result = multi_period_monte_carlo(
    initial_value=10000,
    expected_return=0.01,
    volatility=0.02,
    periods=12,
)

print(result)
