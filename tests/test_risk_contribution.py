import unittest

from calculators.risk_contribution import (
    calculate_risk_contribution,
)


class TestRiskContribution(unittest.TestCase):

    def test_valid(self):
        result = calculate_risk_contribution(
            0.30,
            0.25,
            0.20,
        )

        self.assertEqual(
            result,
            0.375,
        )

    def test_invalid(self):
        with self.assertRaises(ValueError):
            calculate_risk_contribution(
                0.2,
                0.3,
                0,
            )


if __name__ == "__main__":
    unittest.main()
