import unittest

from calculators.correlation import (
    calculate_correlation,
)


class TestCorrelation(unittest.TestCase):

    def test_positive(self):

        result = calculate_correlation(
            [1, 2, 3],
            [2, 4, 6],
        )

        self.assertAlmostEqual(
            result,
            1.0,
            places=6,
        )


if __name__ == "__main__":
    unittest.main()
