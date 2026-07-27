import unittest

from calculators.markowitz_optimizer import (
    markowitz_optimizer,
)


class TestMarkowitzOptimizer(unittest.TestCase):

    def test_best_portfolio(self):

        portfolios = [

            {
                "return": 12,
                "volatility": 6,
                "weights": {
                    "BTC": 60,
                    "Gold": 40,
                },
            },

            {
                "return": 15,
                "volatility": 10,
                "weights": {
                    "BTC": 80,
                    "Gold": 20,
                },
            },

            {
                "return": 9,
                "volatility": 4,
                "weights": {
                    "BTC": 30,
                    "Gold": 70,
                },
            },
        ]

        result = markowitz_optimizer(
            portfolios
        )

        self.assertEqual(
            result["return"],
            9,
        )

        self.assertEqual(
            result["volatility"],
            4,
        )

    def test_empty(self):

        with self.assertRaises(
            ValueError
        ):
            markowitz_optimizer([])


if __name__ == "__main__":
    unittest.main()
