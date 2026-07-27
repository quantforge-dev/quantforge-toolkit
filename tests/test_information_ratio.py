import unittest

from calculators.information_ratio import (
    calculate_information_ratio,
)


class TestInformationRatio(unittest.TestCase):

    def test_valid_ratio(self):
        result = calculate_information_ratio(
            0.14,
            0.10,
            0.02,
        )

        self.assertEqual(result, 2.0)

    def test_invalid_tracking_error(self):
        with self.assertRaises(ValueError):
            calculate_information_ratio(
                0.14,
                0.10,
                0,
            )


if __name__ == "__main__":
    unittest.main()
