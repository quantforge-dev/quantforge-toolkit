from calculators.portfolio_statistics import (
    portfolio_statistics,
)

returns = [
    0.02,
    -0.01,
    0.03,
    0.01,
]

print(
    portfolio_statistics(
        returns
    )
)
