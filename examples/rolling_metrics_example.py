from calculators.rolling_metrics import (
    rolling_mean,
    rolling_return,
)

prices = [
    100,
    102,
    105,
    110,
    108,
    115,
]

print(rolling_mean(prices, 3))
print(rolling_return(prices, 1))
