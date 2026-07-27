"""
Portfolio Analyzer.

High-level interface for
portfolio analytics.
"""

from calculators.portfolio_return import (
    calculate_portfolio_return,
)

from calculators.portfolio_volatility import (
    portfolio_volatility,
)

from calculators.sharpe_ratio import (
    calculate_sharpe_ratio,
)


class PortfolioAnalyzer:

    """
    Analyze a portfolio using
    existing toolkit modules.
    """

    def __init__(
        self,
        returns,
        weights,
        volatilities,
        risk_free_rate=0,
    ):

        self.returns = returns
        self.weights = weights
        self.volatilities = volatilities
        self.risk_free_rate = risk_free_rate

    def analyze(self):

        total_return = calculate_portfolio_return(
            self.returns
        )

        volatility = portfolio_volatility(
            self.weights,
            self.volatilities,
        )

        sharpe = calculate_sharpe_ratio(
            total_return,
            self.risk_free_rate,
            volatility,
        )

        return {

            "return": total_return,

            "volatility": volatility,

            "sharpe_ratio": sharpe,

        }
