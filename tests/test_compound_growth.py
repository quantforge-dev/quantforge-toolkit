import unittest

from calculators.compound_growth import (
    compound_growth,
)


class TestCompoundGrowth(unittest.TestCase):

    def test_growth(self):

        self.assertEqual(
            compound_growth(
                1000,
                0.10,
                2,
            ),
            1210.0,
        )

    def test_invalid_principal(self):

        with self.assertRaises(ValueError):

            compound_growth(
                -100,
                0.1,
                2,
            )

    def test_invalid_years(self):

        with self.assertRaises(ValueError):

            compound_growth(
                100,
                0.1,
                0,
            )


if __name__ == "__main__":
    unittest.main()
