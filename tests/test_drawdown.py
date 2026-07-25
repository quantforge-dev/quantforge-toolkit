import unittest

from calculators.drawdown import calculate_drawdown


class TestDrawdown(unittest.TestCase):

    def test_valid_drawdown(self):
        result = calculate_drawdown(
            initial_balance=10000,
            current_balance=8000,
        )

        self.assertEqual(result["loss"], 2000)
        self.assertEqual(result["drawdown_percent"], 20.0)

    def test_zero_drawdown(self):
        result = calculate_drawdown(
            initial_balance=10000,
            current_balance=10000,
        )

        self.assertEqual(result["loss"], 0)
        self.assertEqual(result["drawdown_percent"], 0.0)

    def test_current_balance_greater_than_initial(self):
        with self.assertRaises(ValueError):
            calculate_drawdown(
                initial_balance=10000,
                current_balance=11000,
            )

    def test_negative_initial_balance(self):
        with self.assertRaises(ValueError):
            calculate_drawdown(
                initial_balance=-10000,
                current_balance=9000,
            )

    def test_negative_current_balance(self):
        with self.assertRaises(ValueError):
            calculate_drawdown(
                initial_balance=10000,
                current_balance=-500,
            )


if __name__ == "__main__":
    unittest.main()
