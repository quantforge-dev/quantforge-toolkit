import unittest

from models.portfolio import Portfolio


class TestPortfolio(unittest.TestCase):

    def test_create_portfolio(self):

        portfolio = Portfolio(
            name="Demo",
            assets={
                "Bitcoin": 50,
                "Gold": 50,
            },
        )

        self.assertEqual(
            portfolio.name,
            "Demo",
        )

        self.assertEqual(
            len(portfolio.assets),
            2,
        )


if __name__ == "__main__":
    unittest.main()
