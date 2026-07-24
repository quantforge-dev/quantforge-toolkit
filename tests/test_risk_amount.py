"""
Tests for Risk Amount Calculator.
"""

import unittest

from calculators.risk_amount import calculate_risk_amount


class TestRiskAmountCalculator(unittest.TestCase):

    def test_one_percent_risk(self):
        self.assertEqual(
            calculate_risk_amount(10000, 1),
            100
        )

    def test_two_percent_risk(self):
        self.assertEqual(
            calculate_risk_amount(5000, 2),
            100
        )

    def test_half_percent_risk(self):
        self.assertEqual(
            calculate_risk_amount(20000, 0.5),
            100
        )

    def test_invalid_balance(self):
        with self.assertRaises(ValueError):
            calculate_risk_amount(-1000, 1)

    def test_invalid_percentage(self):
        with self.assertRaises(ValueError):
            calculate_risk_amount(10000, 150)


if __name__ == "__main__":
    unittest.main()
