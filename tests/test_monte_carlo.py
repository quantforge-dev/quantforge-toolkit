import unittest

from calculators.monte_carlo import monte_carlo_simulation


class TestMonteCarlo(unittest.TestCase):

    def test_valid_simulation(self):
        result = monte_carlo_simulation(
            initial_value=10000,
            expected_return=0.01,
            volatility=0.02,
            simulations=500,
        )

        self.assertIn("mean", result)
        self.assertIn("minimum", result)
        self.assertIn("maximum", result)
        self.assertIn("median", result)

    def test_invalid_initial_value(self):
        with self.assertRaises(ValueError):
            monte_carlo_simulation(
                initial_value=-100,
                expected_return=0.01,
                volatility=0.02,
            )


if __name__ == "__main__":
    unittest.main()
