import unittest

from calculators.stress_test import stress_test


class TestStressTest(unittest.TestCase):

    def test_negative_shock(self):
        result = stress_test(
            portfolio_value=10000,
            shock_percent=-20,
        )

        self.assertEqual(
            result["stressed_value"],
            8000,
        )

    def test_positive_shock(self):
        result = stress_test(
            portfolio_value=10000,
            shock_percent=10,
        )

        self.assertEqual(
            result["stressed_value"],
            11000,
        )


if __name__ == "__main__":
    unittest.main()
