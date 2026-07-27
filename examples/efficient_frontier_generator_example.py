from calculators.efficient_frontier_generator import (
    generate_frontier,
)

portfolio = {

    "returns": {

        "BTC": 12,

        "Gold": 5,

    },

    "weights": {

        "BTC": 50,

        "Gold": 50,

    },

    "volatility": {

        "BTC": 0.25,

        "Gold": 0.10,

    },

}

print(

    generate_frontier(

        [

            portfolio

        ]

    )

)
