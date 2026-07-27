import unittest

from calculators.efficient_frontier_generator import (
    generate_frontier,
)


class TestEfficientFrontierGenerator(
    unittest.TestCase
):

    def test_generator(self):

        portfolios = [

            {

                "returns": {

                    "BTC": 12,

                    "Gold": 5,

                },

                "weights": {

                    "BTC": 50,

                    "Gold": 50,

                },

                "volatility": {

                    "BTC": 0.25,

                    "Gold": 0.10,

                },

            }

        ]

        result = generate_frontier(
            portfolios
        )

        self.assertEqual(
            len(result),
            1,
        )


if __name__ == "__main__":
    unittest.main()
