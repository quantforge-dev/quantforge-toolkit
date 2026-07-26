import unittest

from calculators.covariance import (
    calculate_covariance,
)


class TestCovariance(unittest.TestCase):

    def test_valid(self):

        self.assertAlmostEqual(
            calculate_covariance(
                [2, 4, 6],
                [1, 3, 5],
            ),
            2.66666667,
            places=6,
        )


if __name__ == "__main__":
    unittest.main()
