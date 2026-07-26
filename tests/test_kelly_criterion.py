import unittest

from calculators.kelly_criterion import (
    calculate_kelly,
)


class TestKellyCriterion(unittest.TestCase):

    def test_valid(self):

        result = calculate_kelly(
            60,
            2,
        )

        self.assertEqual(
            result,
            40.0,
        )

    def test_invalid_ratio(self):

        with self.assertRaises(ValueError):

            calculate_kelly(
                60,
                0,
            )


if __name__ == "__main__":
    unittest.main()
