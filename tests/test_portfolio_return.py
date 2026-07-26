import unittest

from calculators.portfolio_return import (
    calculate_portfolio_return,
)


class TestPortfolioReturn(unittest.TestCase):

    def test_valid(self):

        portfolio = {
            "BTC": 5,
            "Gold": 2,
            "Cash": 1,
        }

        self.assertEqual(
            calculate_portfolio_return(
                portfolio
            ),
            8,
        )

    def test_empty(self):

        with self.assertRaises(ValueError):

            calculate_portfolio_return({})
            

if __name__ == "__main__":
    unittest.main()
