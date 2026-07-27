import csv
import os
import unittest

from calculators.export_csv import (
    export_csv,
)


class TestExportCSV(unittest.TestCase):

    def test_export(self):

        file_name = "test.csv"

        data = [

            {
                "return": 12,
                "risk": 8,
            }

        ]

        export_csv(
            data,
            file_name,
        )

        with open(
            file_name,
            newline="",
            encoding="utf-8",
        ) as file:

            rows = list(
                csv.DictReader(file)
            )

        self.assertEqual(
            rows[0]["return"],
            "12",
        )

        os.remove(
            file_name
        )


if __name__ == "__main__":
    unittest.main()
