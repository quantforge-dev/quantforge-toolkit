import unittest

from calculators.frontier_statistics import (
    frontier_statistics,
)


class TestFrontierStatistics(
    unittest.TestCase
):

    def test_statistics(self):

        frontier = [

            {

                "return": 12,

                "volatility": 6,

            },

            {

                "return": 15,

                "volatility": 8,

            },

        ]

        result = frontier_statistics(
            frontier
        )

        self.assertEqual(
            result["max_return"],
            15,
        )


if __name__ == "__main__":
    unittest.main()
