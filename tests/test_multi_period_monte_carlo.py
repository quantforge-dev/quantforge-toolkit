import unittest

from calculators.multi_period_monte_carlo import (
    multi_period_monte_carlo,
)


class TestMultiPeriodMonteCarlo(
    unittest.TestCase
):

    def test_length(self):

        result = multi_period_monte_carlo(
            initial_value=10000,
            expected_return=0.01,
            volatility=0.02,
            periods=12,
        )

        self.assertEqual(
            len(result),
            13,
        )

    def test_negative_initial(self):

        with self.assertRaises(
            ValueError
        ):

            multi_period_monte_carlo(
                -100,
                0.01,
                0.02,
                12,
            )

    def test_negative_volatility(self):

        with self.assertRaises(
            ValueError
        ):

            multi_period_monte_carlo(
                100,
                0.01,
                -0.02,
                12,
            )

    def test_zero_periods(self):

        with self.assertRaises(
            ValueError
        ):

            multi_period_monte_carlo(
                100,
                0.01,
                0.02,
                0,
            )


if __name__ == "__main__":
    unittest.main()
