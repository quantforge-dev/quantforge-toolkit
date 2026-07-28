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

            name="Demo",

            assets={

                "BTC": 50,

                "Gold": 50,

            },

        )

        self.assertTrue(

            validate_portfolio(
                portfolio
            )

        )

    def test_invalid_total_weight(self):

        portfolio = Portfolio(

            name="Demo",

            assets={

                "BTC": 60,

                "Gold": 60,

            },

        )

        with self.assertRaises(
            ValueError
        ):

            validate_portfolio(
                portfolio
            )


if __name__ == "__main__":
    unittest.main()
