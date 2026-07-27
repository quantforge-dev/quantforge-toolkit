import unittest

from calculators.diversification_ratio import (
    calculate_diversification_ratio,
)


class TestDiversificationRatio(unittest.TestCase):

    def test_valid_ratio(self):
        result = calculate_diversification_ratio(
            0.25,
            0.20,
        )

        self.assertEqual(result, 1.25)

    def test_invalid_portfolio_volatility(self):
        with self.assertRaises(ValueError):
            calculate_diversification_ratio(
                0.25,
                0,
            )


if __name__ == "__main__":
    unittest.main()
