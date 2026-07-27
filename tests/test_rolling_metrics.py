import unittest

from calculators.rolling_metrics import (
    rolling_mean,
    rolling_return,
)


class TestRollingMetrics(unittest.TestCase):

    def test_rolling_mean(self):
        result = rolling_mean(
            [1, 2, 3, 4, 5],
            3,
        )

        self.assertEqual(
            result,
            [2.0, 3.0, 4.0],
        )

    def test_rolling_return(self):
        result = rolling_return(
            [100, 105, 110, 120],
            1,
        )

        self.assertEqual(
            result,
            [0.05, 0.0476, 0.0909],
        )


if __name__ == "__main__":
    unittest.main()
