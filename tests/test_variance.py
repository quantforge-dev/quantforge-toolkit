import unittest

from calculators.variance import calculate_variance


class TestVariance(unittest.TestCase):

    def test_valid_variance(self):

        values = [10, 12, 14]

        result = calculate_variance(values)

        self.assertAlmostEqual(
            result,
            2.66666667,
            places=6,
        )

    def test_empty(self):

        with self.assertRaises(ValueError):

            calculate_variance([])


if __name__ == "__main__":
    unittest.main()
