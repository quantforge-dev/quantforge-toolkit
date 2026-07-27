import unittest

from calculators.efficient_frontier import (
    portfolio_point,
)


class TestEfficientFrontier(unittest.TestCase):

    def test_frontier_point(self):

        returns = [
            0.10,
            0.20,
        ]

        weights = [
            0.4,
            0.6,
        ]

        covariance = [
            [0.01, 0.002],
            [0.002, 0.04],
        ]

        result = portfolio_point(
            returns,
            weights,
            covariance,
        )

        self.assertIn(
            "return",
            result,
        )

        self.assertIn(
            "volatility",
            result,
        )


if __name__ == "__main__":
    unittest.main()
