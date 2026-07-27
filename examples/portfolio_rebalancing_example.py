from calculators.portfolio_rebalancing import (
    rebalance_portfolio,
)

result = rebalance_portfolio(

    {
        "BTC": 70,
        "Gold": 30,
    },

    {
        "BTC": 60,
        "Gold": 40,
    },
)

print(result)
