"""
Example:
Markowitz Optimizer
"""

from calculators.markowitz_optimizer import (
    markowitz_optimizer,
)

portfolios = [

    {
        "return": 12,
        "volatility": 6,
        "weights": {
            "BTC": 60,
            "Gold": 40,
        },
    },

    {
        "return": 15,
        "volatility": 10,
        "weights": {
            "BTC": 80,
            "Gold": 20,
        },
    },

]

best = markowitz_optimizer(
    portfolios
)

print(best)
