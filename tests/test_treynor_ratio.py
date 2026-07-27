import unittest

from calculators.treynor_ratio import (
    calculate_treynor_ratio,
)


class TestTreynorRatio(unittest.TestCase):

    def test_valid_ratio(self):
        result = calculate_treynor_ratio(
            0.18,
            0.05,
            1.3,
        )

        self.assertEqual(result, 0.1)

    def test_invalid_beta(self):
        with self.assertRaises(ValueError):
            calculate_treynor_ratio(
                0.18,
                0.05,
                0,
            )


if __name__ == "__main__":
    unittest.main()
