from calculators.efficient_frontier import (
    portfolio_point,
)

returns = [
    0.10,
    0.20,
]

weights = [
    0.4,
    0.6,
]

covariance = [
    [0.01, 0.002],
    [0.002, 0.04],
]

print(
    portfolio_point(
        returns,
        weights,
        covariance,
    )
)
