import unittest

from portfolio.portfolio import Portfolio


class TestPortfolio(unittest.TestCase):

    def test_add_asset(self):
        portfolio = Portfolio()

        portfolio.add_asset(
            "BTC",
            0.6,
        )

        portfolio.add_asset(
            "ETH",
            0.4,
        )

        self.assertEqual(
            len(portfolio),
            2,
        )

        self.assertEqual(
            portfolio.total_weight(),
            1.0,
        )


if __name__ == "__main__":
    unittest.main()
