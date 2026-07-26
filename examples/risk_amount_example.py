"""
Example: Risk Amount Calculator
"""

from calculators.risk_amount import calculate_risk_amount


risk = calculate_risk_amount(
    account_balance=10000,
    risk_percent=2,
)

print(f"Risk Amount: {risk}")
