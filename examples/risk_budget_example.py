from calculators.risk_budget import (
    risk_budget,
)

weights = [
    20,
    30,
    50,
]

budget = risk_budget(weights)

print(budget)
