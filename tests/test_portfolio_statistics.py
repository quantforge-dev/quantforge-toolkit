import unittest

from calculators.portfolio_statistics import (
    portfolio_statistics,
)


class TestPortfolioStatistics(unittest.TestCase):

    def test_statistics(self):
        result = portfolio_statistics(
            [0.01, 0.02, -0.01, 0.03]
        )

        self.assertEqual(
            result["observations"],
            4,
        )

        self.assertEqual(
            result["minimum_return"],
            -0.01,
        )

        self.assertEqual(
            result["maximum_return"],
            0.03,
        )

    def test_empty(self):
        with self.assertRaises(ValueError):
            portfolio_statistics([])
            

if __name__ == "__main__":
    unittest.main()
