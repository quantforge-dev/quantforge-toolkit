import unittest

from calculators.portfolio_summary import portfolio_summary


class TestPortfolioSummary(unittest.TestCase):

    def test_valid_portfolio(self):
        portfolio = {
            "Bitcoin": 5000,
            "Ethereum": 3000,
            "Gold": 2000,
        }

        result = portfolio_summary(portfolio)

        self.assertEqual(result["total_value"], 10000)
        self.assertEqual(result["number_of_assets"], 3)
        self.assertEqual(result["allocations"]["Bitcoin"], 50.0)
        self.assertEqual(result["allocations"]["Ethereum"], 30.0)
        self.assertEqual(result["allocations"]["Gold"], 20.0)

    def test_empty_portfolio(self):
        with self.assertRaises(ValueError):
            portfolio_summary({})

    def test_negative_asset_value(self):
        portfolio = {
            "Bitcoin": -100,
        }

        with self.assertRaises(ValueError):
            portfolio_summary(portfolio)

    def test_zero_value_portfolio(self):
        portfolio = {
            "Asset A": 0,
            "Asset B": 0,
        }

        result = portfolio_summary(portfolio)

        self.assertEqual(result["total_value"], 0)
        self.assertEqual(result["number_of_assets"], 2)
        self.assertEqual(result["allocations"]["Asset A"], 0.0)
        self.assertEqual(result["allocations"]["Asset B"], 0.0)


if __name__ == "__main__":
    unittest.main()
