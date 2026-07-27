import unittest

from calculators.portfolio_optimizer import (
    equal_weight_portfolio,
)


class TestPortfolioOptimizer(unittest.TestCase):

    def test_equal_weights(self):
        result = equal_weight_portfolio(4)

        self.assertEqual(
            result,
            [0.25, 0.25, 0.25, 0.25],
        )


if __name__ == "__main__":
    unittest.main()
