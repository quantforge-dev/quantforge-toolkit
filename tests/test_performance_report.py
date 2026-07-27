import unittest

from models.backtest_result import (
    BacktestResult,
)

from models.performance_report import (
    PerformanceReport,
)


class TestPerformanceReport(
    unittest.TestCase
):

    def test_summary(self):

        result = BacktestResult(

            10000,

            12000,

            20,

            7,

            1.5,
        )

        report = PerformanceReport(
            result
        )

        summary = report.summary()

        self.assertEqual(

            summary["Final Capital"],

            12000,

        )


if __name__ == "__main__":
    unittest.main()
