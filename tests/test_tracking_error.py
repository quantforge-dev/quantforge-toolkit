import unittest

from calculators.tracking_error import (
    calculate_tracking_error,
)


class TestTrackingError(unittest.TestCase):

    def test_valid(self):
        result = calculate_tracking_error(
            [0.01, -0.01, 0.02]
        )

        self.assertTrue(result > 0)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            calculate_tracking_error(
                [0.01]
            )


if __name__ == "__main__":
    unittest.main()
