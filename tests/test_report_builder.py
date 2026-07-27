import unittest

from models.report_builder import (
    ReportBuilder,
)


class TestReportBuilder(
    unittest.TestCase
):

    def test_builder(self):

        report = ReportBuilder(

            {

                "return":12,

                "risk":8,

            }

        )

        result = report.build()

        self.assertTrue(

            "return"

            in result

        )


if __name__ == "__main__":
    unittest.main()
