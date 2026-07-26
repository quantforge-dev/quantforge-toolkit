"""
Basic application tests.
"""

import unittest

import app.main


class TestMain(unittest.TestCase):

    def test_import(self):

        self.assertTrue(
            callable(
                app.main.main
            )
        )


if __name__ == "__main__":
    unittest.main()
