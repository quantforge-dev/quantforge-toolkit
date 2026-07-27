import unittest

from calculators.portfolio_constraints import (
    validate_weights,
)


class TestPortfolioConstraints(
    unittest.TestCase
):

    def test_valid(self):

        self.assertTrue(

            validate_weights(

                {
                    "BTC": 50,
                    "Gold": 50,
                }

            )

        )

    def test_invalid(self):

        with self.assertRaises(
            ValueError
        ):

            validate_weights(

                {
                    "BTC": 60,
                    "Gold": 60,
                }

            )


if __name__ == "__main__":
    unittest.main()
