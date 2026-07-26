import unittest

from calculators.maximum_drawdown import (
    calculate_maximum_drawdown,
)


class TestMaximumDrawdown(unittest.TestCase):

    def test_valid(self):

        curve = [
            100,
            120,
            110,
            90,
            130,
        ]

        self.assertEqual(
            calculate_maximum_drawdown(
                curve
            ),
            25.0,
        )


if __name__ == "__main__":
    unittest.main()
