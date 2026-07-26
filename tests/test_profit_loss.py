import unittest

from calculators.profit_loss import (
    calculate_profit_loss,
)


class TestProfitLoss(unittest.TestCase):

    def test_profit(self):

        result = calculate_profit_loss(
            100,
            120,
            5,
        )

        self.assertEqual(
            result["profit_loss"],
            100,
        )

        self.assertEqual(
            result["percent"],
            20,
        )

    def test_loss(self):

        result = calculate_profit_loss(
            100,
            80,
            2,
        )

        self.assertEqual(
            result["profit_loss"],
            -40,
        )

        self.assertEqual(
            result["percent"],
            -20,
        )

    def test_invalid_quantity(self):

        with self.assertRaises(ValueError):

            calculate_profit_loss(
                100,
                120,
                0,
            )


if __name__ == "__main__":
    unittest.main()
