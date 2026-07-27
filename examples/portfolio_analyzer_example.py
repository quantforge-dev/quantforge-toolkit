from models.portfolio_analyzer import (
    PortfolioAnalyzer,
)

analyzer = PortfolioAnalyzer(

    returns={

        "BTC":12,

        "Gold":5,

    },

    weights={

        "BTC":50,

        "Gold":50,

    },

    volatilities={

        "BTC":0.25,

        "Gold":0.10,

    },

    risk_free_rate=2,

)

print(
    analyzer.analyze()
)
