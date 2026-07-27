import unittest

from calculators.alpha import calculate_alpha


class TestAlpha(unittest.TestCase):

    def test_positive_alpha(self):
        result = calculate_alpha(
            portfolio_return=0.15,
            expected_return=0.10,
        )

        self.assertEqual(result, 0.05)

    def test_negative_alpha(self):
        result = calculate_alpha(
            portfolio_return=0.08,
            expected_return=0.10,
        )

        self.assertEqual(result, -0.02)


if __name__ == "__main__":
    unittest.main()
