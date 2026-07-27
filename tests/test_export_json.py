import json
import os
import unittest

from calculators.export_json import (
    export_json,
)


class TestExportJson(unittest.TestCase):

    def test_export(self):

        file_name = "test.json"

        data = {
            "return": 12,
            "risk": 8,
        }

        export_json(
            data,
            file_name,
        )

        with open(
            file_name,
            encoding="utf-8",
        ) as file:

            loaded = json.load(file)

        self.assertEqual(
            loaded,
            data,
        )

        os.remove(
            file_name
        )


if __name__ == "__main__":
    unittest.main()
