import unittest

from calculators.expectancy import calculate_expectancy


class TestExpectancy(unittest.TestCase):

    def test_positive_expectancy(self):
        self.assertEqual(
            calculate_expectancy(
                60,
                200,
                100,
            ),
            80,
        )

    def test_invalid_win_rate(self):
        with self.assertRaises(ValueError):
            calculate_expectancy(
                120,
                100,
                50,
            )


if __name__ == "__main__":
    unittest.main()
