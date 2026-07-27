"""
Example: Value at Risk Calculator
"""

from calculators.var import calculate_var

result = calculate_var(
    portfolio_value=100000,
    volatility=0.02,
    confidence_level=0.95,
)

print(f"Estimated VaR: ${result}")
