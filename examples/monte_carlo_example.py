from calculators.monte_carlo import monte_carlo_simulation

result = monte_carlo_simulation(
    initial_value=10000,
    expected_return=0.01,
    volatility=0.02,
)

print(result)
