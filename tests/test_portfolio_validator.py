import unittest

from models.portfolio import Portfolio

from validation.portfolio_validator import (
    validate_portfolio,
)


class TestPortfolioValidator(
    unittest.TestCase
):

    def test_valid(self):

        portfolio = Portfolio(

            returns={
                "BTC": 12,
                "Gold": 5,
            },

            weights={
                "BTC": 50,
                "Gold": 50,
            },

            volatilities={
                "BTC": 0.25,
                "Gold": 0.10,
            },
        )

        self.assertTrue(
            validate_portfolio(
                portfolio
            )
        )


if __name__ == "__main__":
    unittest.main()
