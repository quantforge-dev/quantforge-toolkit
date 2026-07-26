"""
Example: Risk / Reward Calculator
"""

from calculators.risk_reward import calculate_risk_reward

result = calculate_risk_reward(
    entry_price=100,
    stop_loss_price=95,
    take_profit_price=115,
)

print(result)
