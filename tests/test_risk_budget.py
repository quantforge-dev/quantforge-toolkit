import unittest

from calculators.risk_budget import (
    risk_budget,
)


class TestRiskBudget(unittest.TestCase):

    def test_budget(self):

        result = risk_budget(
            [
                20,
                30,
                50,
            ]
        )

        self.assertEqual(
            result,
            [
                0.2,
                0.3,
                0.5,
            ],
        )

    def test_empty_weights(self):

        with self.assertRaises(
            ValueError
        ):
            risk_budget([])

    def test_zero_total(self):

        with self.assertRaises(
            ValueError
        ):
            risk_budget(
                [
                    0,
                    0,
                    0,
                ]
            )


if __name__ == "__main__":
    unittest.main()
