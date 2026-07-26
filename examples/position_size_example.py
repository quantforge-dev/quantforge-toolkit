"""
Example: Position Size Calculator
"""

from calculators.position_size import calculate_position_size

result = calculate_position_size(
    account_balance=10000,
    risk_percent=2,
    entry_price=100,
    stop_loss_price=95,
)

print(result)
