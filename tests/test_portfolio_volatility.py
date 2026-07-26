import unittest

from calculators.portfolio_volatility import (
    portfolio_volatility,
)


class TestPortfolioVolatility(unittest.TestCase):

    def test_valid_portfolio(self):

        weights = {
            "Bitcoin": 50,
            "Gold": 50,
        }

        vol = {
            "Bitcoin": 0.60,
            "Gold": 0.15,
        }

        result = portfolio_volatility(
            weights,
            vol,
        )

        self.assertAlmostEqual(
            result,
            0.3092,
            places=4,
        )

    def test_invalid_weights(self):

        weights = {
            "Bitcoin": 70,
            "Gold": 20,
        }

        vol = {
            "Bitcoin": 0.6,
            "Gold": 0.2,
        }

        with self.assertRaises(ValueError):
            portfolio_volatility(
                weights,
                vol,
            )

    def test_asset_mismatch(self):

        weights = {
            "Bitcoin": 100,
        }

        vol = {
            "Gold": 0.2,
        }

        with self.assertRaises(ValueError):
            portfolio_volatility(
                weights,
                vol,
            )


if __name__ == "__main__":
    unittest.main()
