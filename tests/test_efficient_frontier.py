import unittest

from calculators.efficient_frontier import (
    calculate_portfolio_point,
)


class TestEfficientFrontier(unittest.TestCase):

    def test_valid_portfolio_point(self):

        returns = {
            "BTC": 12,
            "ETH": 8,
        }

        weights = {
            "BTC": 60,
            "ETH": 40,
        }

        volatilities = {
            "BTC": 0.40,
            "ETH": 0.35,
        }

        result = calculate_portfolio_point(
            returns,
            weights,
            volatilities,
        )

        self.assertIn("return", result)
        self.assertIn("volatility", result)

        self.assertEqual(result["return"], 20)

    def test_empty_returns(self):

        with self.assertRaises(ValueError):

            calculate_portfolio_point(
                {},
                {
                    "BTC": 100,
                },
                {
                    "BTC": 0.40,
                },
            )


if __name__ == "__main__":
    unittest.main()
