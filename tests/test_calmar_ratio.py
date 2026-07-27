import unittest

from calculators.calmar_ratio import (
    calculate_calmar_ratio,
)


class TestCalmarRatio(unittest.TestCase):

    def test_valid_ratio(self):
        result = calculate_calmar_ratio(
            annual_return=0.20,
            maximum_drawdown=0.10,
        )

        self.assertEqual(result, 2.0)

    def test_invalid_drawdown(self):
        with self.assertRaises(ValueError):
            calculate_calmar_ratio(
                0.20,
                0,
            )


if __name__ == "__main__":
    unittest.main()
