import unittest

from calculators.sortino_ratio import (
    calculate_sortino_ratio,
)


class TestSortinoRatio(unittest.TestCase):

    def test_valid_ratio(self):
        result = calculate_sortino_ratio(
            expected_return=0.14,
            risk_free_rate=0.04,
            downside_deviation=0.05,
        )

        self.assertEqual(result, 2.0)

    def test_invalid_deviation(self):
        with self.assertRaises(ValueError):
            calculate_sortino_ratio(
                0.14,
                0.04,
                0,
            )


if __name__ == "__main__":
    unittest.main()
