import unittest

from calculators.break_even import (
    calculate_break_even,
)


class TestBreakEven(unittest.TestCase):

    def test_valid(self):

        self.assertEqual(
            calculate_break_even(
                1000,
                10,
            ),
            100,
        )

    def test_invalid_quantity(self):

        with self.assertRaises(ValueError):

            calculate_break_even(
                100,
                0,
            )


if __name__ == "__main__":
    unittest.main()
