import unittest

from calculators.position_size import calculate_position_size


class TestPositionSize(unittest.TestCase):

    def test_valid_position_size(self):
        result = calculate_position_size(
            account_balance=10000,
            risk_percent=1,
            entry_price=100,
            stop_loss_price=95,
        )

        self.assertEqual(result, 20.0)

    def test_zero_stop_distance(self):
        with self.assertRaises(ValueError):
            calculate_position_size(
                account_balance=10000,
                risk_percent=1,
                entry_price=100,
                stop_loss_price=100,
            )

    def test_negative_account_balance(self):
        with self.assertRaises(ValueError):
            calculate_position_size(
                account_balance=-10000,
                risk_percent=1,
                entry_price=100,
                stop_loss_price=95,
            )

    def test_invalid_risk_percentage(self):
        with self.assertRaises(ValueError):
            calculate_position_size(
                account_balance=10000,
                risk_percent=120,
                entry_price=100,
                stop_loss_price=95,
            )


if __name__ == "__main__":
    unittest.main()
