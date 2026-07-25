"""
Tests for Portfolio Allocation Calculator.
"""

import unittest

from calculators.portfolio_allocation import (
    calculate_portfolio_allocation,
)


class TestPortfolioAllocation(unittest.TestCase):

    def test_valid_portfolio(self):
        portfolio = {
            "Bitcoin": 30,
            "Gold": 20,
            "Oil": 15,
            "Silver": 15,
            "Cash": 20,
        }

        result = calculate_portfolio_allocation(
            portfolio
        )

        self.assertTrue(result["is_valid"])
        self.assertEqual(result["assets"], 5)
        self.assertEqual(
            result["total_allocation"],
            100,
        )

    def test_invalid_portfolio(self):
        portfolio = {
            "Bitcoin": 40,
            "Gold": 30,
            "Cash": 20,
        }

        result = calculate_portfolio_allocation(
            portfolio
        )

        self.assertFalse(result["is_valid"])

    def test_empty_portfolio(self):
        with self.assertRaises(ValueError):
            calculate_portfolio_allocation({})
            

if __name__ == "__main__":
    unittest.main()
