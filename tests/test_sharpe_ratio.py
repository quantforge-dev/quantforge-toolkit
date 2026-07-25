import unittest

from calculators.sharpe_ratio import sharpe_ratio


class TestSharpeRatio(unittest.TestCase):

    def test_valid_sharpe_ratio(self):
        result = sharpe_ratio(
            expected_return=0.15,
            risk_free_rate=0.05,
            standard_deviation=0.10,
        )

        self.assertEqual(result, 1.0)

    def test_zero_standard_deviation(self):
        with self.assertRaises(ValueError):
            sharpe_ratio(
                expected_return=0.15,
                risk_free_rate=0.05,
                standard_deviation=0,
            )

    def test_negative_standard_deviation(self):
        with self.assertRaises(ValueError):
            sharpe_ratio(
                expected_return=0.15,
                risk_free_rate=0.05,
                standard_deviation=-0.10,
            )

    def test_negative_sharpe_ratio(self):
        result = sharpe_ratio(
            expected_return=0.02,
            risk_free_rate=0.05,
            standard_deviation=0.10,
        )

        self.assertEqual(result, -0.3)


if __name__ == "__main__":
    unittest.main()
