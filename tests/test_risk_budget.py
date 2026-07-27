import unittest

from calculators.risk_budget import (
    risk_budget,
)


class TestRiskBudget(unittest.TestCase):

    def test_budget(self):

        budget = risk_budget(
            [
                20,
                30,
                50,
            ]
        )

        self.assertEqual(
            budget,
            [
                0.2,
                0.3,
                0.5,
            ],
        )


if __name__ == "__main__":
    unittest.main()
