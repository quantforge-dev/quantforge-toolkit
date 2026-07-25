"""
Tests for Risk / Reward Calculator.
"""

import unittest

from calculators.risk_reward import calculate_risk_reward


class TestRiskRewardCalculator(unittest.TestCase):

    def test_valid_trade(self):
        result = calculate_risk_reward(
            entry_price=100,
            stop_loss_price=95,
            take_profit_price=115,
        )

        self.assertEqual(result["risk"], 5)
        self.assertEqual(result["reward"], 15)
        self.assertEqual(result["ratio"], 3.0)

    def test_zero_risk(self):
        with self.assertRaises(ValueError):
            calculate_risk_reward(
                entry_price=100,
                stop_loss_price=100,
                take_profit_price=120,
            )

    def test_invalid_entry(self):
        with self.assertRaises(ValueError):
            calculate_risk_reward(
                entry_price=0,
                stop_loss_price=95,
                take_profit_price=110,
            )


if __name__ == "__main__":
    unittest.main()
