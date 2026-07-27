import unittest

from calculators.portfolio_rebalancing import (
    rebalance_portfolio,
)


class TestPortfolioRebalancing(
    unittest.TestCase
):

    def test_rebalance(self):

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

        self.assertEqual(

            result,

            {
                "BTC": -10,
                "Gold": 10,
            },

        )

    def test_invalid_assets(self):

        with self.assertRaises(
            ValueError
        ):

            rebalance_portfolio(

                {
                    "BTC": 100,
                },

                {
                    "Gold": 100,
                },

            )


if __name__ == "__main__":
    unittest.main()
