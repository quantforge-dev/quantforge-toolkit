import unittest

from calculators.beta import calculate_beta


class TestBeta(unittest.TestCase):

    def test_valid_beta(self):
        result = calculate_beta(
            covariance=0.08,
            market_variance=0.04,
        )

        self.assertEqual(result, 2.0)

    def test_invalid_variance(self):
        with self.assertRaises(ValueError):
            calculate_beta(
                0.08,
                0,
            )


if __name__ == "__main__":
    unittest.main()
