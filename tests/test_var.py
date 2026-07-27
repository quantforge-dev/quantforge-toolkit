import unittest

from calculators.var import calculate_var


class TestValueAtRisk(unittest.TestCase):

    def test_valid_var(self):
        result = calculate_var(
            portfolio_value=100000,
            volatility=0.02,
            confidence_level=0.95,
        )

        self.assertAlmostEqual(result, 3289.71, places=2)

    def test_invalid_portfolio_value(self):
        with self.assertRaises(ValueError):
            calculate_var(
                portfolio_value=-100000,
                volatility=0.02,
                confidence_level=0.95,
            )

    def test_invalid_volatility(self):
        with self.assertRaises(ValueError):
            calculate_var(
                portfolio_value=100000,
                volatility=0,
                confidence_level=0.95,
            )

    def test_invalid_confidence_level(self):
        with self.assertRaises(ValueError):
            calculate_var(
                portfolio_value=100000,
                volatility=0.02,
                confidence_level=1.5,
            )


if __name__ == "__main__":
    unittest.main()
