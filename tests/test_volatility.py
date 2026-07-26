import unittest

from calculators.volatility import (
    calculate_volatility,
)


class TestVolatility(unittest.TestCase):

    def test_valid(self):

        result = calculate_volatility(
            [10, 12, 14]
        )

        self.assertAlmostEqual(
            result,
            1.63299316,
            places=6,
        )


if __name__ == "__main__":
    unittest.main()
