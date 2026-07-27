import unittest

from calculators.performance_metrics import (
    performance_metrics,
)


class TestPerformanceMetrics(unittest.TestCase):

    def test_active_return(self):
        result = performance_metrics(
            0.16,
            0.12,
        )

        self.assertEqual(
            result["active_return"],
            0.04,
        )


if __name__ == "__main__":
    unittest.main()
