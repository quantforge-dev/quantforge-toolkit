from calculators.stress_test import stress_test

result = stress_test(
    portfolio_value=10000,
    shock_percent=-30,
)

print(result)
