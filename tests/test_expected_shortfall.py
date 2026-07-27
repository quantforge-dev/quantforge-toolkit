import unittest

from calculators.expected_shortfall import (
    expected_shortfall,
)


class TestExpectedShortfall(unittest.TestCase):

    def test_valid_shortfall(self):
        result = expected_shortfall(
            3000,
            1.5,
        )

        self.assertEqual(
            result,
            4500,
        )

    def test_invalid_var(self):
        with self.assertRaises(ValueError):
            expected_shortfall(
                0,
                1.5,
            )

    def test_invalid_multiplier(self):
        with self.assertRaises(ValueError):
            expected_shortfall(
                1000,
                0.8,
            )


if __name__ == "__main__":
    unittest.main()
